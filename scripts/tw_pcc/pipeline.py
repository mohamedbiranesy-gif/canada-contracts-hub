#!/usr/bin/env python3
"""Taiwan PCC (政府電子採購網) award notices → Canadian-supplier records.
Stage 1: scan daily award XML open-data files (award_YYYYMMDD.xml) and the GPA award JSON files for
         winning-bidder addresses that look Canadian (token 'canada'/'加拿大' or Canadian postal code / province).
Stage 2: for each candidate (org name + case no), fetch the full award notice through the openfun
         mirror API (pcc-api.openfun.app/api/tender?unit_id=&job_number=) which exposes every field of the
         notice, incl. 投標廠商N:得標廠商國別 (winner country) and 履約起迄日期 (performance period).
Stage 3: keep bidders whose 得標廠商國別 contains 加拿大/Canada AND 是否得標 = 是; emit schema records.
usage: pipeline.py --xmldir <dir> --gpadir <dir> --cache <dir> --out <jsonl> --stats <json>
"""
import sys, os, re, json, glob, argparse, time, datetime, urllib.request, urllib.parse

REF = datetime.date(2026, 10, 25)
UA = {"User-Agent": "contracts-research/1.0"}
CAN_RE = re.compile(r"canad|加拿大|\b(ontario|quebec|qu[ée]bec|british columbia|alberta|manitoba|saskatchewan|nova scotia|new brunswick|newfoundland)\b|\b[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z] ?\d[ABCEGHJ-NPRSTV-Z]\d\b", re.I)

def roc_date(s):
    """'113/12/19' (ROC year) -> date; also accepts yyyy/mm/dd"""
    m = re.match(r"\s*(\d{2,4})/(\d{1,2})/(\d{1,2})", s or "")
    if not m: return None
    y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
    if y < 1000: y += 1911
    try: return datetime.date(y, mo, d)
    except ValueError: return None

def fetch(url, cache_path):
    if os.path.exists(cache_path):
        return json.load(open(cache_path, encoding="utf-8"))
    for i in range(3):
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
            json.dump(d, open(cache_path, "w", encoding="utf-8"), ensure_ascii=False)
            return d
        except Exception as e:
            time.sleep(2 + 3 * i)
    return None

def stage1(xmldir, gpadir):
    cands = {}  # (org, caseno) -> info
    for f in sorted(glob.glob(os.path.join(xmldir, "*.xml"))):
        s = open(f, encoding="utf-8", errors="replace").read()
        for t in re.findall(r"<TENDER>.*?</TENDER>", s, re.S):
            addrs = re.findall(r"<BIDDER_SUPP_ADDR>(.*?)</BIDDER_SUPP_ADDR>", t, re.S)
            if not any(CAN_RE.search(a) for a in addrs):
                continue
            g = lambda tag: (re.search(r"<%s>(.*?)</%s>" % (tag, tag), t, re.S) or [None, None])[1]
            key = (g("TENDER_ORG_NAME"), g("TENDER_CASE_NO"))
            cands.setdefault(key, {"org": key[0], "case_no": key[1], "xml_files": [], "xml_rows": []})
            cands[key]["xml_files"].append(os.path.basename(f))
            cands[key]["xml_rows"].append({"file": os.path.basename(f), **{k: g(k) for k in ["TENDER_NAME", "PROCUREMENT_ATTR", "TENDER_CASE_NO", "TENDER_AWARD_PRICE", "AWARD_DATE", "AWARD_NOTICE_DATE", "TENDER_ORG_NAME", "PROCUREMENT_TYPE", "TENDER_TEL", "TENDER_ORG_ADDR", "CONTACT_PERSON", "TENDER_AWARD_WAY"]},
                                          "BIDDER_SUPP_NAME": re.findall(r"<BIDDER_SUPP_NAME>(.*?)</BIDDER_SUPP_NAME>", t, re.S), "BIDDER_SUPP_ADDR": addrs,
                                          "NOT_OBTAIN_SUPP_NAME": re.findall(r"<NOT_OBTAIN_SUPP_NAME>(.*?)</NOT_OBTAIN_SUPP_NAME>", t, re.S)})
    for f in sorted(glob.glob(os.path.join(gpadir, "GPAaward_*.json"))):
        try: rows = json.load(open(f, encoding="utf-8"))
        except Exception: continue
        for r in rows:
            if CAN_RE.search(r.get("得標廠商地址清單") or ""):
                key = (r.get("機關名稱"), r.get("標案案號"))
                cands.setdefault(key, {"org": key[0], "case_no": key[1], "xml_files": [], "xml_rows": []})
                cands[key].setdefault("gpa_rows", []).append({"file": os.path.basename(f), **r})
    return cands

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--xmldir", required=True); ap.add_argument("--gpadir", required=True); ap.add_argument("--cache", required=True)
    ap.add_argument("--out", required=True); ap.add_argument("--stats", required=True)
    a = ap.parse_args()
    os.makedirs(a.cache, exist_ok=True)
    cands = stage1(a.xmldir, a.gpadir)
    stats = {"candidates": len(cands), "api_found": 0, "api_missing": 0, "award_notices": 0, "canadian_winner_bidders": 0,
             "status": {}, "excluded": {}, "excluded_examples": []}
    print("candidates", len(cands), file=sys.stderr)
    retrieved = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with open(a.out, "w", encoding="utf-8") as fo:
        for (org, case_no), info in sorted(cands.items(), key=lambda kv: str(kv[0])):
            if not org or not case_no:
                continue
            # find unit_id via title search is unreliable; search by company name is also limited. Use searchbytitle on case name
            # The openfun API supports /api/tender?unit_id=&job_number= ; unit_id is unknown from the XML, so look it up by case number search.
            cp = os.path.join(a.cache, "search_%s.json" % re.sub(r"[^A-Za-z0-9_-]", "_", case_no))
            sr = fetch("https://pcc-api.openfun.app/api/searchbytitle?query=" + urllib.parse.quote(case_no), cp)
            unit_id = None
            if sr and sr.get("records"):
                for rec in sr["records"]:
                    if rec.get("job_number") == case_no and (rec.get("unit_name") == org or org in (rec.get("unit_name") or "") or (rec.get("unit_name") or "") in org):
                        unit_id = rec.get("unit_id"); break
                if unit_id is None:
                    for rec in sr["records"]:
                        if rec.get("job_number") == case_no:
                            unit_id = rec.get("unit_id"); break
            if unit_id is None:
                # fall back: search by winner company name
                names = [n for row in info.get("xml_rows", []) for n in row["BIDDER_SUPP_NAME"]] + [n for row in info.get("gpa_rows", []) for n in (row.get("得標廠商名稱清單") or "").split(",")]
                for n in names[:3]:
                    if not n.strip(): continue
                    cp2 = os.path.join(a.cache, "co_%s.json" % re.sub(r"[^A-Za-z0-9_-]", "_", n)[:60])
                    sr2 = fetch("https://pcc-api.openfun.app/api/searchbycompanyname?query=" + urllib.parse.quote(n.strip()), cp2)
                    if sr2 and sr2.get("records"):
                        for rec in sr2["records"]:
                            if rec.get("job_number") == case_no:
                                unit_id = rec.get("unit_id"); break
                    if unit_id: break
            if unit_id is None:
                stats["api_missing"] += 1
                stats["excluded_examples"].append((org, case_no, "not found in openfun API"))
                continue
            stats["api_found"] += 1
            dp = os.path.join(a.cache, "tender_%s_%s.json" % (unit_id, re.sub(r"[^A-Za-z0-9_-]", "_", case_no)))
            td = fetch("https://pcc-api.openfun.app/api/tender?unit_id=%s&job_number=%s" % (urllib.parse.quote(unit_id), urllib.parse.quote(case_no)), dp)
            if not td or not td.get("records"):
                stats["api_missing"] += 1; continue
            awards = [r for r in td["records"] if "決標公告" in (r.get("brief") or {}).get("type", "") and "無法決標" not in (r.get("brief") or {}).get("type", "")]
            if not awards:
                stats["excluded"]["no_award_notice_in_api"] = stats["excluded"].get("no_award_notice_in_api", 0) + 1; continue
            # latest award notice (by date, then by filename)
            awards.sort(key=lambda r: (str(r.get("date")), str(r.get("filename"))))
            aw = awards[-1]
            stats["award_notices"] += 1
            det = aw.get("detail") or {}
            # bidders
            nb = det.get("投標廠商:投標廠商家數")
            idx = sorted({int(m.group(1)) for k in det for m in [re.match(r"投標廠商:投標廠商(\d+):", k)] if m})
            for i in idx:
                p = "投標廠商:投標廠商%d:" % i
                won = det.get(p + "是否得標")
                country = det.get(p + "得標廠商國別") or ""
                if won != "是":
                    continue
                if not re.search(r"加拿大|canada", country, re.I):
                    continue
                stats["canadian_winner_bidders"] += 1
                per = det.get(p + "履約起迄日期") or ""
                m = re.match(r"\s*([\d/]+)\s*[－-]\s*([\d/]+)", per)
                start = roc_date(m.group(1)) if m else None
                end = roc_date(m.group(2)) if m else None
                est = "(預估)" in per
                adate = roc_date(det.get("決標資料:決標日期") or "")
                ndate = roc_date(det.get("決標資料:決標公告日期") or "")
                anchor = start or adate
                if end:
                    if end < REF:
                        stats["excluded"]["ended"] = stats["excluded"].get("ended", 0) + 1; continue
                    if anchor and anchor > REF:
                        stats["excluded"]["future_start"] = stats["excluded"].get("future_start", 0) + 1; continue
                    status = "ongoing"
                    basis = "履約起迄日期 (performance period) %s: start %s <= 2026-10-25 <= end %s%s" % (per.strip(), start, end, " (publisher flags the period as estimated 預估)" if est else "")
                else:
                    if anchor and anchor > REF:
                        stats["excluded"]["future_start"] = stats["excluded"].get("future_start", 0) + 1; continue
                    status = "end_date_unknown"
                    basis = "no 履約起迄日期 (performance period) in the award notice; award date %s" % adate
                stats["status"][status] = stats["status"].get(status, 0) + 1
                amt_s = det.get(p + "決標金額") or det.get("決標資料:總決標金額") or ""
                amt = float(re.sub(r"[^\d.]", "", amt_s)) if re.search(r"\d", amt_s) else None
                bidder = {k[len(p):]: v for k, v in det.items() if k.startswith(p)}
                addr = det.get(p + "廠商地址(英)") or det.get(p + "廠商地址")
                rec = {
                    "record_id": "tw_pcc:%s:%s:%s:bidder%d" % (unit_id, case_no, aw.get("filename"), i),
                    "source": {"key": "tw_pcc", "name": "Taiwan Government e-Procurement System (政府電子採購網) – award notices (決標公告)", "publisher": "Public Construction Commission, Executive Yuan (行政院公共工程委員會); full-notice fields via the pcc.g0v.ronny.tw / pcc-api.openfun.app open mirror",
                               "dataset_url": "https://web.pcc.gov.tw/tps/tp/OpenData/showList (daily award XML) ; https://pcc-api.openfun.app/ (notice detail API)",
                               "record_url": "https://web.pcc.gov.tw/prkms/tender/common/noticeDate/redirectPublic?ds=%s&fn=%s.xml" % (aw.get("date"), aw.get("filename")) if aw.get("filename") else None, "retrieved_at": retrieved},
                    "status": status, "status_basis": basis,
                    "contract": {"identifiers": {"unit_id": unit_id, "case_no": case_no, "notice_filename": aw.get("filename"), "contract_no": det.get("決標資料:契約編號"), "award_notice_seq": det.get("決標資料:決標公告序號"), "bidder_index": i, "supplier_code": det.get(p + "廠商代碼")},
                                 "title": det.get("已公告資料:標案名稱") or (aw.get("brief") or {}).get("title"), "description": det.get("採購資料:標的分類") or None,
                                 "instrument_type": "contract (award notice 決標公告)", "procurement_method": det.get("採購資料:招標方式") or det.get("已公告資料:招標方式"), "solicitation_procedure": det.get("採購資料:決標方式") or det.get("已公告資料:決標方式"),
                                 "commodity": {"pcc_category": det.get("採購資料:標的分類") or (aw.get("brief") or {}).get("category")},
                                 "value": amt, "currency": "TWD", "value_detail": {"bidder_award_amount_twd": amt, "total_award_amount": det.get("決標資料:總決標金額"), "reserve_price": det.get("決標資料:底價金額"), "note": det.get("決標資料:附加說明")},
                                 "dates": {"published": ndate.isoformat() if ndate else None, "signed": None, "start": start.isoformat() if start else None, "end": end.isoformat() if end else None, "award": adate.isoformat() if adate else None, "amended_last": None},
                                 "related": {"pcc_official_search": "https://web.pcc.gov.tw/prkms/tender/common/basic/indexTenderBasic", "openfun_api": "https://pcc-api.openfun.app/api/tender?unit_id=%s&job_number=%s" % (unit_id, case_no), "openfun_mirror_page": ("https://pcc.g0v.ronny.tw" + aw.get("url", "")) if aw.get("url") else None, "performance_location": det.get("已公告資料:履約地點（含地區）") or det.get("已公告資料:履約地點")}},
                    "buyer": {"name": det.get("機關資料:機關名稱") or org, "country": "TW", "type": "Taiwan government agency", "identifiers": {"unit_id": unit_id, "機關代碼": det.get("機關資料:機關代碼")}, "address": {"line1": det.get("機關資料:機關地址")}, "contact": {"name": det.get("機關資料:聯絡人"), "telephone": det.get("機關資料:聯絡電話")}},
                    "vendor": {"name": det.get(p + "廠商名稱(英)") or det.get(p + "廠商名稱"), "country": "CA", "country_basis": "award notice field 投標廠商%d:得標廠商國別 = %r (and bidder address %r)" % (i, country, addr),
                               "identifiers": {"pcc_supplier_code": det.get(p + "廠商代碼")}, "address": {"line1": addr, "city": None, "region": None, "postal_code": None, "country": country}, "contact": {"telephone": det.get(p + "廠商電話")}},
                    "raw": {"award_notice_detail": det, "award_notice_brief": aw.get("brief"), "notice_date": aw.get("date"), "all_notices_for_case": [{"date": r.get("date"), "type": (r.get("brief") or {}).get("type"), "filename": r.get("filename")} for r in td["records"]], "bulk_xml_rows": info.get("xml_rows"), "gpa_rows": info.get("gpa_rows")},
                }
                fo.write(json.dumps(rec, ensure_ascii=False) + "\n"); fo.flush()
    json.dump(stats, open(a.stats, "w"), ensure_ascii=False, indent=1)
    print(json.dumps({k: v for k, v in stats.items() if k != "excluded_examples"}, ensure_ascii=False), file=sys.stderr)

if __name__ == "__main__":
    main()

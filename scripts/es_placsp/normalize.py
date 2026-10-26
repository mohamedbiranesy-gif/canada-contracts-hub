#!/usr/bin/env python3
"""PLACSP CODICE atom entries (matches.jsonl from extract.py) -> schema records, one per (folder, Canadian winning party/lot)."""
import json, re, sys, datetime, collections, os
import xml.etree.ElementTree as ET
REF = datetime.date(2026, 10, 25)
def strip_ns(x):
    x = re.sub(r"<(/?)[A-Za-z0-9_-]+:", r"<\1", x)
    x = re.sub(r"\s[A-Za-z0-9_-]+:([A-Za-z]+=)", r" \1", x)
    return x
def todict(e):
    d = {}
    for k, v in e.attrib.items(): d["@" + k] = v
    kids = list(e)
    if not kids:
        t = (e.text or "").strip()
        if d: d["#text"] = t; return d
        return t
    for c in kids:
        v = todict(c)
        if c.tag in d:
            if not isinstance(d[c.tag], list): d[c.tag] = [d[c.tag]]
            d[c.tag].append(v)
        else: d[c.tag] = v
    return d
def txt(e, path):
    f = e.find(path) if e is not None else None
    return (f.text or "").strip() if f is not None and f.text else None
def d8(s):
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", s or "")
    return datetime.date(*map(int, m.groups())) if m else None
def add(d, n, unit):
    try: n = float(n)
    except Exception: return None
    u = (unit or "").upper()
    if u == "DAY": return d + datetime.timedelta(days=int(n))
    if u == "MON":
        m = d.month - 1 + int(n); y2, m2 = d.year + m // 12, m % 12 + 1; import calendar; return datetime.date(y2, m2, min(d.day, calendar.monthrange(y2, m2)[1]))
    if u == "ANN": return datetime.date(d.year + int(n), d.month, min(d.day, 28))
    return None
groups = collections.defaultdict(list)
for l in open(sys.argv[1], encoding="utf-8"):
    j = json.loads(l); groups[j["id"]].append(j)
out = open(sys.argv[2] + ".tmp", "w", encoding="utf-8"); st = collections.Counter(); ex = []
for eid, vers in groups.items():
    vers.sort(key=lambda j: j["updated"] or "")
    j = vers[-1]
    try: root = ET.fromstring(strip_ns(j["xml"]))
    except Exception as e:
        st["xml_error"] += 1; continue
    cfs = root.find("ContractFolderStatus")
    status_code = txt(cfs, "ContractFolderStatusCode")
    lcp = cfs.find("LocatedContractingParty/Party")
    pp = cfs.find("ProcurementProject")
    lots = {txt(l, "ID"): l for l in cfs.findall("ProcurementProjectLot")}
    for tr in cfs.findall("TenderResult"):
        wps = [w for w in tr.findall("WinningParty") if txt(w, "PhysicalLocation/Address/Country/IdentificationCode") == "CA"]
        if not wps: continue
        lot_id = txt(tr, "AwardedTenderedProject/ProcurementProjectLotID")
        for wp in wps:
            st["units"] += 1
            if status_code == "ANUL":
                st["excluded_folder_cancelled"] += 1; ex.append((eid, "ANUL")); continue
            rc = txt(tr, "ResultCode")
            if rc in ("3", "4", "5", "6", "7"):
                st["excluded_result_" + rc] += 1; ex.append((eid, "ResultCode " + rc)); continue
            per_src = lots.get(lot_id).find("ProcurementProject/PlannedPeriod") if lot_id and lots.get(lot_id) is not None and lots.get(lot_id).find("ProcurementProject/PlannedPeriod") is not None else (pp.find("PlannedPeriod") if pp is not None else None)
            p_start, p_end = d8(txt(per_src, "StartDate")), d8(txt(per_src, "EndDate"))
            dur = per_src.find("DurationMeasure") if per_src is not None else None
            dur_n, dur_u = (dur.text.strip(), dur.get("unitCode")) if dur is not None and dur.text else (None, None)
            award = d8(txt(tr, "AwardDate")); c_start = d8(txt(tr, "StartDate")); issue = d8(txt(tr, "Contract/IssueDate"))
            anchor = c_start or p_start or issue or award; aname = "TenderResult.StartDate" if c_start else ("PlannedPeriod.StartDate" if p_start else ("Contract.IssueDate (formalisation)" if issue else "AwardDate"))
            end = p_end; status = basis = None
            if end:
                if end < REF: st["excluded_ended"] += 1; ex.append((eid, "end %s" % end)); continue
                if anchor and anchor > REF: st["excluded_future"] += 1; continue
                status, basis = "ongoing", "%s %s <= 2026-10-25 <= PlannedPeriod.EndDate %s" % (aname, anchor, end)
            elif dur_n and anchor:
                end = add(anchor, dur_n, dur_u)
                if end and end < REF: st["excluded_inferred_ended"] += 1; ex.append((eid, "inferred end %s" % end)); continue
                if anchor > REF: st["excluded_future"] += 1; continue
                if end: status, basis = "ongoing_inferred", "no end date; %s %s + PlannedPeriod.DurationMeasure %s %s = %s >= 2026-10-25" % (aname, anchor, dur_n, dur_u, end)
            if status is None:
                status, basis = "end_date_unknown", "no PlannedPeriod end date or duration; %s %s" % (aname, anchor)
            st[status] += 1
            amt = txt(tr, "AwardedTenderedProject/LegalMonetaryTotal/TaxExclusiveAmount")
            pay = txt(tr, "AwardedTenderedProject/LegalMonetaryTotal/PayableAmount")
            vname = txt(wp, "PartyName/Name"); addr = wp.find("PhysicalLocation/Address")
            ids = {pi.find("ID").get("schemeName", "id"): pi.find("ID").text for pi in wp.findall("PartyIdentification") if pi.find("ID") is not None}
            bids = {pi.find("ID").get("schemeName", "id"): pi.find("ID").text for pi in (lcp.findall("PartyIdentification") if lcp is not None else []) if pi.find("ID") is not None}
            link = root.find("link"); rurl = link.get("href") if link is not None else None
            cpv = [c.text for c in (pp.findall("RequiredCommodityClassification/ItemClassificationCode") if pp is not None else [])]
            rec = {"record_id": "es_placsp:%s:%s:%s" % (eid.split("/")[-1], lot_id or "0", re.sub(r"\W+", "_", vname or "")[:30]),
              "source": {"key": "es_placsp", "name": "Plataforma de Contratación del Sector Público (PLACSP) – syndication feeds (licitaciones perfiles contratante + plataformas agregadas)", "publisher": "Ministerio de Hacienda, Spain (Dirección General del Patrimonio del Estado)",
                         "dataset_url": "https://www.hacienda.gob.es/es-ES/GobiernoAbierto/Datos%20Abiertos/Paginas/LicitacionesContratante.aspx", "record_url": rurl, "retrieved_at": "2026-10-25T19:00:00Z"},
              "status": status, "status_basis": basis,
              "contract": {"identifiers": {"placsp_entry_id": eid, "contract_folder_id": txt(cfs, "ContractFolderID"), "lot_id": lot_id, "contract_id": txt(tr, "Contract/ID")},
                "title": txt(pp, "Name") or (root.findtext("title") or "").strip(), "description": txt(tr, "Description"), "instrument_type": "contract (PLACSP adjudicación/formalización)",
                "procurement_method": txt(cfs, "TenderingProcess/ProcedureCode"), "solicitation_procedure": txt(cfs, "TenderingProcess/ProcedureCode"),
                "commodity": {"cpv": cpv[0] if cpv else None, "cpv_all": cpv, "placsp_type_code": txt(pp, "TypeCode")},
                "value": float(amt) if amt else None, "currency": "EUR", "value_detail": {"awarded_tax_exclusive": float(amt) if amt else None, "awarded_payable": float(pay) if pay else None, "budget_tax_exclusive": float(txt(pp, "BudgetAmount/TaxExclusiveAmount")) if txt(pp, "BudgetAmount/TaxExclusiveAmount") else None},
                "dates": {"published": None, "signed": issue.isoformat() if issue else None, "award": award.isoformat() if award else None, "start": (c_start or p_start).isoformat() if (c_start or p_start) else None, "end": end.isoformat() if end else None, "amended_last": (j["updated"] or "")[:10] or None},
                "related": {"folder_status_code": status_code, "result_code": rc, "planned_duration": [dur_n, dur_u], "buyer_profile": txt(cfs, "LocatedContractingParty/BuyerProfileURIID")}},
              "buyer": {"name": txt(lcp, "PartyName/Name"), "country": "ES", "type": "Spanish contracting authority (ContractingPartyTypeCode %s)" % txt(cfs, "LocatedContractingParty/ContractingPartyTypeCode"), "identifiers": bids,
                        "address": {"line1": txt(lcp, "PostalAddress/AddressLine/Line"), "city": txt(lcp, "PostalAddress/CityName"), "postal_code": txt(lcp, "PostalAddress/PostalZone"), "country": txt(lcp, "PostalAddress/Country/IdentificationCode")},
                        "contact": {"name": txt(lcp, "Contact/Name"), "telephone": txt(lcp, "Contact/Telephone"), "email": txt(lcp, "Contact/ElectronicMail")}},
              "vendor": {"name": vname, "country": "CA", "country_basis": "TenderResult/WinningParty/PhysicalLocation/Address/Country/IdentificationCode = 'CA'", "identifiers": ids,
                         "address": {"line1": txt(addr, "AddressLine/Line"), "city": txt(addr, "CityName"), "region": txt(addr, "CountrySubentity"), "postal_code": txt(addr, "PostalZone"), "country": "CA"}, "contact": {}},
              "raw": {"entry": todict(root), "xml_latest": j["xml"], "zip": j["zip"], "member": j["member"], "updated": j["updated"],
                      "rows": [{"zip": v["zip"], "member": v["member"], "updated": v["updated"]} for v in vers] if len(vers) > 1 else []}}
            out.write(json.dumps(rec, ensure_ascii=False) + "\n")
st["entries"] = len(groups); st["excluded_examples"] = ex[:30]
json.dump(st, open("downloads/es_placsp/normalize_stats.json", "w"), indent=1); print(dict(st))
out.close(); os.replace(sys.argv[2] + ".tmp", sys.argv[2])

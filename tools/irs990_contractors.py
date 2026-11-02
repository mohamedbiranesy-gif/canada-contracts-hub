#!/usr/bin/env python3
"""Private buyers that paid a contractor located in Canada, from US nonprofits' Form 990 / 990-PF e-filings. No AI.

Every Form 990 lists the five highest-paid independent contractors (over $100,000) with their address (Part VII-B),
and every 990-PF its highest-paid contractors for professional services (Part VIII). The IRS publishes all e-filed
returns as XML (https://www.irs.gov/charities-non-profits/form-990-series-downloads). A contractor whose address in the
return is a foreign address with country CA is a Canada-located vendor proven by the source itself; the filer (hospital,
university, foundation, association ...) is its buyer, named, with its website (Form 990 item J) and the fiscal year the
payment was made in. Contractors that are persons are skipped (organisations only).
For each zip of the chosen years (downloaded once into ~/cch-irs990/, one download at a time), each return is read
from the zip; only returns that mention country CA are parsed.
Output, picked up by tools/lead_scanner.py --bridge (row.period_end_date dates the record):
~/cch-leads/socrata_irs990_<year>.jsonl ; progress ~/cch-leads/socrata_irs990_<year>.jsonl.done (zip names).
Evidence page per return: ProPublica Nonprofit Explorer's full view of the same filing (EIN + object id).
  python3 tools/irs990_contractors.py [--years 2026 2025]
"""
import argparse, json, os, re, subprocess, sys, time, urllib.request, zipfile
import xml.etree.ElementTree as ET

UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
INDEX = "https://www.irs.gov/charities-non-profits/form-990-series-downloads"
CACHE = os.path.expanduser("~/cch-irs990")
LEADS = os.path.expanduser("~/cch-leads")
NS = "{http://www.irs.gov/efile}"
GROUPS = ("ContractorCompensationGrp", "CompOfHghstPdCntrctPrfSrvcGrp", "CompOfHghstPdCntrctOthSrvcGrp")
PROV = {"AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "SK", "YT"}


def text(el, *paths):
    for p in paths:
        x = find(el, p)
        if x is not None and (x.text or "").strip():
            return re.sub(r"\s+", " ", x.text).strip()
    return ""


def find(el, path):
    return el.find("/".join(".//" + NS + s if i == 0 else NS + s for i, s in enumerate(path.split("/")))) if el is not None else None


def website(raw):
    w = (raw or "").strip().lower()
    w = re.sub(r"^(https?://)?(www\.)?", "", w).split("/")[0].strip(" .")
    if not re.fullmatch(r"[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)*\.[a-z]{2,}", w) or w in ("n.a", "none.com"):
        return ""
    return w


def zips(years):
    req = urllib.request.Request(INDEX, headers={"User-Agent": UA})
    page = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
    urls = sorted(set(re.findall(r"https://apps\.irs\.gov/pub/epostcard/990/xml/(\d{4})/(\d{4}_TEOS_XML_\w+\.zip)", page)))
    return ["https://apps.irs.gov/pub/epostcard/990/xml/%s/%s" % (y, z) for y, z in urls if y in years]


def one_return(data, member, zurl):
    if b"CountryCd>CA<" not in data or not any(g.encode() in data for g in GROUPS):
        return []
    root = ET.fromstring(data)
    hdr, ret = root.find(NS + "ReturnHeader"), root.find(NS + "ReturnData")
    filer = find(hdr, "Filer")
    ein = text(filer, "EIN")
    name = " ".join(x for x in (text(filer, "BusinessName/BusinessNameLine1Txt"), text(filer, "BusinessName/BusinessNameLine2Txt")) if x)
    end = text(hdr, "TaxPeriodEndDt")
    rtype = text(hdr, "ReturnTypeCd")
    site = ""
    for tag in ("WebsiteAddressTxt", "WebSiteAddressTxt"):
        x = find(ret, tag)
        if x is not None and x.text:
            site = website(x.text)
            break
    city = text(filer, "USAddress/CityNm") or text(filer, "ForeignAddress/CityNm")
    state = text(filer, "USAddress/StateAbbreviationCd") or text(filer, "ForeignAddress/CountryCd")
    obj = os.path.basename(member).split("_")[0]
    out = []
    for g in GROUPS:
        for c in ret.iter(NS + g):
            fa = find(c, "ForeignAddress")
            if fa is None or text(fa, "CountryCd") != "CA":
                continue
            vendor = " ".join(x for x in (text(c, "BusinessNameLine1Txt"), text(c, "BusinessNameLine2Txt")) if x)
            if not vendor:  # a person, not an organisation
                continue
            addr = ", ".join(x for x in (text(fa, "AddressLine1Txt"), text(fa, "CityNm"), text(fa, "ProvinceOrStateNm"), text(fa, "ForeignPostalCd")) if x)
            out.append({"platform": "irs990", "domain": site, "dataset_id": obj,
                        "dataset": "IRS Form %s e-file: highest-paid independent contractor with an address in Canada" % rtype,
                        "dataset_url": "https://projects.propublica.org/nonprofits/organizations/%s/%s/full" % (ein, obj),
                        "publisher": name, "buyer_unit": "", "website": "https://%s/" % site if site else "",
                        "vendor": vendor, "canada_field": "contractor address country (IRS Form %s)" % rtype,
                        "canada_value": "CA - " + addr,
                        "row": {"period_end_date": end, "ein": ein, "object_id": obj, "return_type": rtype,
                                "services": text(c, "ServicesDesc", "ServiceTypeTxt"), "amount": text(c, "CompensationAmt"),
                                "contractor_address": addr, "filer_city": city, "filer_state": state,
                                "irs_zip": zurl, "irs_member": member}})
    return out


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--years", nargs="+", default=["2026", "2025"])
    a = a.parse_args()
    os.makedirs(CACHE, exist_ok=True)
    for zurl in sorted(zips(a.years), reverse=True):
        year = zurl.split("/")[-2]
        out = os.path.join(LEADS, "socrata_irs990_%s.jsonl" % year)
        done = set(open(out + ".done").read().split()) if os.path.exists(out + ".done") else set()
        zname = os.path.basename(zurl)
        if zname in done:
            continue
        path = os.path.join(CACHE, zname)
        if not os.path.exists(path):
            print(time.strftime("%H:%M"), "download", zname, flush=True)
            r = subprocess.run(["curl", "-sfL", "-A", UA, "--retry", "3", "-o", path + ".part", zurl])
            if r.returncode != 0:
                print("download failed", zname, r.returncode, flush=True)
                continue
            os.rename(path + ".part", path)
        n = hits = 0
        with zipfile.ZipFile(path) as z, open(out, "a", encoding="utf-8") as f:
            for m in z.namelist():
                if not m.endswith(".xml"):
                    continue
                n += 1
                try:
                    rows = one_return(z.read(m), m, zurl)
                except Exception:
                    continue
                for r in rows:
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")
                hits += len(rows)
        open(out + ".done", "a").write(zname + "\n")
        print(time.strftime("%H:%M"), zname, "returns", n, "contractors in Canada", hits, flush=True)
    print("finished", flush=True)


if __name__ == "__main__":
    main()

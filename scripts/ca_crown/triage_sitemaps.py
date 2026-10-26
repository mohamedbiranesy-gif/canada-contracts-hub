#!/usr/bin/env python3
"""Find contract-disclosure pages of federal Crown corporations / parliamentary bodies via robots.txt + sitemaps.
Usage: python3 -I triage_sitemaps.py <out.json>"""
import sys, re, json, gzip, time, io
import requests

UA = {"User-Agent": "contracts-research/1.0"}
ORGS = {
    "cbc": "https://cbc.radio-canada.ca", "canada_post": "https://www.canadapost-postescanada.ca", "via_rail": "https://www.viarail.ca",
    "bdc": "https://www.bdc.ca", "edc": "https://www.edc.ca", "fcc": "https://www.fcc-fac.ca", "cmhc": "https://www.cmhc-schl.gc.ca",
    "canada_lands": "https://www.clc-sic.ca", "ncc": "https://ncc-ccn.gc.ca", "destination_canada": "https://www.destinationcanada.com",
    "nac": "https://nac-cna.ca", "canada_council": "https://canadacouncil.ca", "museum_history": "https://www.historymuseum.ca",
    "museum_nature": "https://nature.ca", "ingenium": "https://ingeniumcanada.org", "cmhr": "https://humanrights.ca",
    "pier21": "https://pier21.ca", "aecl": "https://www.aecl.ca", "catsa": "https://www.catsa-acsta.gc.ca",
    "marine_atlantic": "https://www.marineatlantic.ca", "cib": "https://cib-bic.ca", "bank_of_canada": "https://www.bankofcanada.ca",
    "senate": "https://sencanada.ca", "house_of_commons": "https://www.ourcommons.ca", "cdic": "https://www.cdic.ca",
    "mint": "https://www.mint.ca", "dcc": "https://www.dcc-cdc.gc.ca", "idrc": "https://idrc-crdi.ca", "standards_council": "https://scc-ccn.ca",
    "wdba": "https://www.gordiehoweinternationalbridge.com", "jccbi": "https://jacquescartierchamplain.ca", "pspib": "https://www.investpsp.com",
    "crrf": "https://www.crrf-fcrr.ca", "pilotage_atlantic": "https://www.atlanticpilotage.com", "pilotage_pacific": "https://www.ppa.gc.ca",
    "pilotage_laurentian": "https://www.pilotagestlaurent.gc.ca", "pilotage_great_lakes": "https://www.glpa-apgl.com",
    "cdev": "https://www.cdev.gc.ca", "telefilm": "https://telefilm.ca", "parl_protective": "https://www.pps-spp.parl.ca",
    "ciec": "https://ciec-ccie.parl.gc.ca", "pbo": "https://www.pbo-dpb.ca", "cmip": "https://www.cmip.ca",
}
PAT = re.compile(r"(contract|contrat)", re.I)
PAT2 = re.compile(r"(disclos|divulg|proactive|transparen|over-10|plus-de-10|10000|10-000)", re.I)


def get(url, timeout=30):
    try:
        r = requests.get(url, headers=UA, timeout=timeout)
        return r.status_code, r.content
    except Exception as e:
        return None, str(e).encode()


res = {}
for org, home in ORGS.items():
    t0 = time.time()
    info = {"home": home, "robots_status": None, "sitemaps": [], "hits": [], "errors": []}
    code, body = get(home + "/robots.txt")
    info["robots_status"] = code
    sms = []
    if code == 200:
        txt = body.decode("utf-8", "replace")
        info["robots_disallow"] = [l.strip() for l in txt.splitlines() if l.lower().startswith("disallow")][:40]
        sms = [l.split(":", 1)[1].strip() for l in txt.splitlines() if l.lower().startswith("sitemap:")]
    if not sms:
        sms = [home + "/sitemap.xml", home + "/sitemap_index.xml"]
    queue = list(dict.fromkeys(sms)); seen = set(); n = 0
    while queue and n < 40 and time.time() - t0 < 90:
        sm = queue.pop(0)
        if sm in seen:
            continue
        seen.add(sm); n += 1
        code, body = get(sm)
        time.sleep(0.5)
        if code != 200:
            info["errors"].append(f"{sm} {code}")
            continue
        if sm.endswith(".gz"):
            try:
                body = gzip.decompress(body)
            except Exception:
                pass
        txt = body.decode("utf-8", "replace")
        info["sitemaps"].append(sm)
        locs = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", txt)
        for loc in locs:
            if loc.endswith(".xml") or loc.endswith(".xml.gz") or "sitemap" in loc.lower() and loc.lower().endswith((".xml", ".gz")):
                if len(queue) < 200:
                    queue.append(loc)
            elif PAT.search(loc) and PAT2.search(loc):
                info["hits"].append(loc)
    info["hits"] = sorted(set(info["hits"]))[:80]
    res[org] = info
    print(org, info["robots_status"], len(info["sitemaps"]), len(info["hits"]), info["hits"][:6], info["errors"][:2], flush=True)
    json.dump(res, open(sys.argv[1], "w"), indent=1)

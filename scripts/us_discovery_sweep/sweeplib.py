"""Shared helpers for W1c sweep normalizers (import with sys.path.insert(0, this dir)).
Status conventions (same as earlier US workers: us_state_virginia / us_city_la / us_state_massachusetts / us_city_nyc):
 - explicit end date: ongoing iff start(or award) <= REF <= end; ended -> excluded
 - payments / POs without term: end_date_unknown iff latest activity in [REF-12 months, REF]
 - award/contract rows without end date: end_date_unknown iff award/start within 3 years before REF (stale otherwise)
"""
import json, re, datetime, os, hashlib, collections
REF = datetime.date(2026, 10, 25); REF_S = REF.isoformat()
WIN_S = "2025-10-25"          # 12-month activity window start
STALE_S = "2023-10-25"        # 3-year award-date window start
PROV = {"ON": "ON", "ONT": "ON", "ONTARIO": "ON", "QC": "QC", "PQ": "QC", "QUE": "QC", "QUEBEC": "QC", "QUÉBEC": "QC",
        "BC": "BC", "B.C.": "BC", "BRITISH COLUMBIA": "BC", "AB": "AB", "ALTA": "AB", "ALBERTA": "AB", "MB": "MB",
        "MAN": "MB", "MANITOBA": "MB", "SK": "SK", "SASK": "SK", "SASKATCHEWAN": "SK", "NS": "NS", "N.S.": "NS",
        "NOVA SCOTIA": "NS", "NB": "NB", "N.B.": "NB", "NEW BRUNSWICK": "NB", "NL": "NL", "NF": "NL", "NFLD": "NL",
        "NEWFOUNDLAND": "NL", "NEWFOUNDLAND AND LABRADOR": "NL", "PE": "PE", "PEI": "PE", "P.E.I.": "PE",
        "PRINCE EDWARD ISLAND": "PE", "YT": "YT", "YUKON": "YT", "NT": "NT", "NWT": "NT", "NORTHWEST TERRITORIES": "NT",
        "NU": "NU", "NUNAVUT": "NU"}
PC_FULL = re.compile(r"\b([ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z])[ -]?(\d[ABCEGHJ-NPRSTV-Z]\d)\b", re.I)
PC_FSA = re.compile(r"^\s*[ABCEGHJ-NPRSTVXY]\d[A-Z]", re.I)
US_ZIP = re.compile(r"^\s*\d{5}(-?\d{4})?\s*$")
INDIVIDUAL = re.compile(r"^[A-Z'\-]+,\s*[A-Z'\-]+( [A-Z]\.?)?$")

def s(v):
    if v is None: return None
    if isinstance(v, (dict, list)): return json.dumps(v, ensure_ascii=False)
    t = str(v).strip()
    return t or None

def prov(v):
    t = (s(v) or "").upper().strip().rstrip(".")
    if t in PROV: return PROV[t]
    t2 = t.replace(".", "")
    return PROV.get(t2) or PROV.get(t + ".")

def ca_postal(v):
    m = PC_FULL.search(s(v) or "")
    return (m.group(1).upper() + " " + m.group(2).upper()) if m else None

def canadian(region=None, postal=None, country=None, text=None, region_field="state", postal_field="zip",
             country_field="country"):
    """Return (True, basis) / (False, reason). 'CA' in a state field is California and never Canada."""
    c = (s(country) or "").upper()
    r = prov(region); pc = ca_postal(postal); z = s(postal) or ""
    if c in ("CAN", "CANADA", "CDN") or "CANADA" in c:
        if z and US_ZIP.match(z) and not r: return False, f"{country_field}={c} but US ZIP {z}"
        return True, f"{country_field}='{s(country)}'" + (f"; {region_field}='{s(region)}'" if region else "") + (f"; {postal_field}='{z}'" if z else "")
    if c == "CA" and country_field:
        # ISO-2 'CA' in a COUNTRY field = Canada; require no US ZIP contradiction
        if z and US_ZIP.match(z): return False, f"{country_field}=CA but US ZIP {z}"
        return True, f"{country_field}='CA' (ISO country code)" + (f"; {postal_field}='{z}'" if z else "")
    if c and c not in ("US", "USA", "UNITED STATES", ""):
        return False, f"{country_field}={c}"
    if r:
        if z and US_ZIP.match(z): return False, f"{region_field}={s(region)} but US ZIP {z}"
        if z and not pc and not PC_FSA.match(z): return False, f"{region_field}={s(region)} but non-Canadian postal {z}"
        return True, f"{region_field}='{s(region)}' (Canadian province)" + (f"; {postal_field}='{z}'" if z else "")
    if pc and not r and (not s(region) or (s(region) or "").upper() in ("", "NA", "--", "N/A", "XX", "FC", "OT", "ZZ")):
        return True, f"{postal_field}='{z}' (Canadian postal-code pattern), {region_field} blank/foreign"
    if text:
        t = s(text).upper()
        if re.search(r"\bCANADA\b", t) and (PC_FULL.search(t) or any(re.search(r"\b" + re.escape(k) + r"\b", t) for k in PROV if len(k) > 2)):
            return True, f"address text contains 'CANADA' and a province/postal code: {s(text)[:120]}"
    return False, "no Canadian marker"

def d(v):
    """ISO date from many formats (incl. Socrata floating timestamps, epoch ms)."""
    if v is None: return None
    if isinstance(v, (int, float)) and v > 1e11:
        return datetime.datetime.fromtimestamp(v / 1000, datetime.timezone.utc).date().isoformat()
    t = str(v).strip()
    if not t: return None
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})", t)
    if m:
        try: return datetime.date(int(m[1]), int(m[2]), int(m[3])).isoformat()
        except ValueError: return None
    m = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{4})", t)
    if m:
        try: return datetime.date(int(m[3]), int(m[1]), int(m[2])).isoformat()
        except ValueError: return None
    m = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{2})\b", t)
    if m:
        try: return datetime.date(2000 + int(m[3]), int(m[1]), int(m[2])).isoformat()
        except ValueError: return None
    m = re.match(r"^(\d{4})(\d{2})(\d{2})$", t)
    if m:
        try: return datetime.date(int(m[1]), int(m[2]), int(m[3])).isoformat()
        except ValueError: return None
    for fmt in ("%d-%b-%Y", "%d-%b-%y", "%b %d, %Y", "%B %d, %Y"):
        try: return datetime.datetime.strptime(t[:12].strip(), fmt).date().isoformat()
        except ValueError: pass
    return None

def amt(v):
    if v is None: return None
    if isinstance(v, (int, float)): return float(v)
    t = str(v).strip().replace("$", "").replace(",", "")
    neg = t.startswith("(") and t.endswith(")"); t = t.strip("()")
    try:
        x = float(t); return -x if neg else x
    except ValueError: return None

def status_contract(start, end, award=None, stale_from=STALE_S):
    """For records with term fields. Returns (status, basis) or (None, reason)."""
    st = start or award
    if end:
        if end < REF_S: return None, f"ended {end}"
        if st and st > REF_S: return None, f"not started (start {st})"
        return "ongoing", f"start {st or 'n/a'} <= {REF_S} <= end {end}"
    if st and st > REF_S: return None, f"not started (start {st})"
    if st and st >= stale_from:
        return "end_date_unknown", f"no end date published; start/award {st} within 3 years before {REF_S}"
    return None, f"no end date and start/award {st or 'n/a'} older than 3 years (stale)"

def status_activity(last_activity, what="payment"):
    if last_activity and WIN_S <= last_activity <= REF_S:
        return "end_date_unknown", (f"{what} data without contract term; latest {what} date {last_activity} is within the 12 months "
                                    f"before {REF_S} (shared end_date_unknown convention for payment/PO sources)")
    return None, f"latest {what} {last_activity or 'n/a'} outside 12-month window"

def sid(*parts):
    t = ":".join(str(p) for p in parts if p not in (None, ""))
    t = re.sub(r"[^A-Za-z0-9_.:\-]+", "_", t)
    return t if len(t) <= 120 else t[:80] + "~" + hashlib.sha1(t.encode()).hexdigest()[:12]

def now_iso():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def rec(source, rid, status, basis, contract, buyer, vendor, raw):
    return {"record_id": f"{source['key']}:{rid}", "source": source, "status": status, "status_basis": basis,
            "contract": contract, "buyer": buyer, "vendor": vendor, "raw": raw}

def contract(identifiers, title=None, description=None, instrument_type=None, procurement_method=None,
             solicitation_procedure=None, commodity=None, value=None, currency="USD", value_detail=None, dates=None, related=None):
    dd = {"published": None, "signed": None, "start": None, "end": None, "amended_last": None}
    dd.update(dates or {})
    return {"identifiers": {k: v for k, v in identifiers.items() if v not in (None, "")}, "title": title,
            "description": description, "instrument_type": instrument_type, "procurement_method": procurement_method,
            "solicitation_procedure": solicitation_procedure, "commodity": commodity or {}, "value": value,
            "currency": currency, "value_detail": value_detail or {}, "dates": dd, "related": related or {}}

def buyer(name, btype, identifiers=None, address=None, contact=None):
    return {"name": name, "country": "US", "type": btype, "identifiers": identifiers or {}, "address": address or {},
            "contact": contact or {}}

def vendor(name, basis, identifiers=None, line1=None, city=None, region=None, postal=None, country=None, contact=None, line2=None):
    a = {"line1": s(line1), "city": s(city), "region": s(region), "postal_code": s(postal), "country": s(country) or "CA"}
    if line2: a["line2"] = s(line2)
    return {"name": s(name), "country": "CA", "country_basis": basis, "identifiers": {k: v for k, v in (identifiers or {}).items() if v not in (None, "")},
            "address": a, "contact": contact or {}}

class Out:
    def __init__(self, path):
        self.path = path; self.f = open(path, "w", encoding="utf-8"); self.n = 0; self.by = collections.Counter()
        self.excl = collections.Counter()
    def write(self, r):
        self.f.write(json.dumps(r, ensure_ascii=False, default=str) + "\n"); self.n += 1; self.by[r["status"]] += 1
    def exclude(self, reason):
        self.excl[reason.split(" ")[0] if reason else "?"] += 1
    def close(self):
        self.f.close()
        return {"written": self.n, "by_status": dict(self.by), "excluded": dict(self.excl)}

def read_jsonl(p):
    with open(p, encoding="utf-8") as f:
        for l in f:
            l = l.strip()
            if l: yield json.loads(l)

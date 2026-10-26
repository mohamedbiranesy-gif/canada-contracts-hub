"""Shared helpers for US state/local normalizers. Import with sys.path.insert(0, 'scripts/us_common')."""
import json, re, datetime, os

REF = datetime.date(2026, 10, 25)
REF_S = "2026-10-25"

PROV_CODES = {"ON", "QC", "BC", "AB", "MB", "SK", "NS", "NB", "NL", "PE", "NT", "YT", "NU", "PQ", "NF", "LB"}
PROV_NAMES = {
    "ONTARIO": "ON", "QUEBEC": "QC", "QUÉBEC": "QC", "BRITISH COLUMBIA": "BC", "ALBERTA": "AB", "MANITOBA": "MB",
    "SASKATCHEWAN": "SK", "NOVA SCOTIA": "NS", "NEW BRUNSWICK": "NB", "NEWFOUNDLAND": "NL", "NEWFOUNDLAND AND LABRADOR": "NL",
    "PRINCE EDWARD ISLAND": "PE", "NORTHWEST TERRITORIES": "NT", "YUKON": "YT", "NUNAVUT": "NU",
}
COUNTRY_CA = {"CA", "CAN", "CANADA"}
# Canadian postal code: A1A 1A1 (letters D,F,I,O,Q,U not allowed in first position; be lenient)
PC_RE = re.compile(r"\b([A-Za-z]\d[A-Za-z])[ -]?(\d[A-Za-z]\d)\b")


def norm_prov(s):
    if not s:
        return None
    u = s.strip().upper()
    if u in PROV_CODES:
        return "QC" if u == "PQ" else ("NL" if u in ("NF", "LB") else u)
    return PROV_NAMES.get(u)


def is_ca_postal(s):
    return bool(s and PC_RE.search(s))


def parse_date(s):
    """Return ISO date string or None. Accepts ISO timestamps, MM/DD/YYYY, YYYY-MM-DD, M/D/YY."""
    if s is None:
        return None
    s = str(s).strip()
    if not s or s in ("-", "N/A", "NA", "null", "None"):
        return None
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})", s)
    if m:
        y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
        try:
            return datetime.date(y, mo, d).isoformat()
        except ValueError:
            return None
    m = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{4})", s)
    if m:
        mo, d, y = int(m.group(1)), int(m.group(2)), int(m.group(3))
        try:
            return datetime.date(y, mo, d).isoformat()
        except ValueError:
            return None
    m = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{2})$", s)
    if m:
        mo, d, y = int(m.group(1)), int(m.group(2)), 2000 + int(m.group(3))
        try:
            return datetime.date(y, mo, d).isoformat()
        except ValueError:
            return None
    m = re.match(r"^(\d{1,2})-([A-Za-z]{3})-(\d{4})", s)
    if m:
        try:
            return datetime.datetime.strptime(m.group(0), "%d-%b-%Y").date().isoformat()
        except ValueError:
            return None
    return None


def parse_amount(s):
    if s is None:
        return None
    if isinstance(s, (int, float)):
        return float(s)
    t = str(s).strip().replace("$", "").replace(",", "")
    neg = t.startswith("(") and t.endswith(")")
    t = t.strip("()")
    if not t or t in ("-", "N/A"):
        return None
    try:
        v = float(t)
        return -v if neg else v
    except ValueError:
        return None


def status_from_dates(start, end, future_start_ok=False):
    """Return (status, basis) or (None, reason) if excluded. start/end ISO strings or None."""
    if end:
        if end < REF_S:
            return None, f"end {end} < {REF_S} (ended)"
        if start and start > REF_S and not future_start_ok:
            return None, f"start {start} > {REF_S} (not yet started)"
        return "ongoing", f"start {start or 'n/a'} <= {REF_S} <= end {end}"
    if start and start > REF_S and not future_start_ok:
        return None, f"start {start} > {REF_S} (not yet started), no end"
    return "end_date_unknown", f"no end date published; start/award {start or 'n/a'}"


def now_iso():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def file_mtime_iso(path):
    return datetime.datetime.fromtimestamp(os.path.getmtime(path), datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def record(source_key, source_name, publisher, dataset_url, record_url, retrieved_at, rid, status, basis,
           contract, buyer, vendor, raw):
    return {
        "record_id": f"{source_key}:{rid}",
        "source": {"key": source_key, "name": source_name, "publisher": publisher, "dataset_url": dataset_url,
                   "record_url": record_url, "retrieved_at": retrieved_at},
        "status": status, "status_basis": basis,
        "contract": contract, "buyer": buyer, "vendor": vendor, "raw": raw,
    }


def contract_block(identifiers, title=None, description=None, instrument_type=None, procurement_method=None,
                   solicitation_procedure=None, commodity=None, value=None, currency="USD", value_detail=None,
                   dates=None, related=None):
    d = {"published": None, "signed": None, "start": None, "end": None, "amended_last": None}
    if dates:
        d.update(dates)
    return {
        "identifiers": identifiers, "title": title, "description": description, "instrument_type": instrument_type,
        "procurement_method": procurement_method, "solicitation_procedure": solicitation_procedure,
        "commodity": commodity or {}, "value": value, "currency": currency, "value_detail": value_detail or {},
        "dates": d, "related": related or {},
    }


def buyer_block(name, btype, country="US", identifiers=None, address=None, contact=None):
    return {"name": name, "country": country, "type": btype, "identifiers": identifiers or {},
            "address": address or {}, "contact": contact or {}}


def vendor_block(name, basis, identifiers=None, address=None, contact=None):
    return {"name": name, "country": "CA", "country_basis": basis, "identifiers": identifiers or {},
            "address": address or {}, "contact": contact or {}}


class Writer:
    def __init__(self, path):
        self.path = path
        self.f = open(path, "w", encoding="utf-8")
        self.n = 0
        self.by_status = {}

    def write(self, rec):
        self.f.write(json.dumps(rec, ensure_ascii=False, default=str) + "\n")
        self.n += 1
        self.by_status[rec["status"]] = self.by_status.get(rec["status"], 0) + 1
        if self.n % 200 == 0:
            self.f.flush()

    def close(self):
        self.f.close()
        return self.n, self.by_status

"""Shared helpers for municipal award datasets: parse contract periods / terms out of free text,
Canadian address detection, status decision. Import with
    sys.path.insert(0, "scripts/_muni"); import terms
"""
import re, calendar
from datetime import date

REF = date(2026, 10, 25)
MONTHS = {m.lower(): i for i, m in enumerate(["January", "February", "March", "April", "May", "June", "July",
                                               "August", "September", "October", "November", "December"], 1)}
for _k, _v in list(MONTHS.items()):
    MONTHS[_k[:3]] = _v
MONTHS["sept"] = 9
WORDNUM = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
           "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
           "eighteen": 18, "nineteen": 19, "twenty": 20, "twenty-four": 24, "thirty": 30, "thirty-six": 36,
           "forty-eight": 48, "sixty": 60}
PROV = {"ON", "QC", "BC", "AB", "MB", "SK", "NS", "NB", "NL", "PE", "YT", "NT", "NU"}
PROV_NAMES = {"ontario": "ON", "quebec": "QC", "québec": "QC", "british columbia": "BC", "alberta": "AB", "manitoba": "MB",
              "saskatchewan": "SK", "nova scotia": "NS", "new brunswick": "NB", "newfoundland and labrador": "NL",
              "newfoundland": "NL", "prince edward island": "PE", "yukon": "YT", "northwest territories": "NT", "nunavut": "NU"}
POSTAL_RE = re.compile(r"\b([ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z])\s?(\d[ABCEGHJ-NPRSTV-Z]\d)\b", re.I)

DATE_TXT = r"(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|July?|Aug(?:ust)?|Sept?(?:ember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\.?\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})"
END_RE = re.compile(r"(?:\bto\b|\buntil\b|\bending\b|\bthrough\b|\bthru\b|\bexpir\w*\b(?:\s+on)?|-|–)\s*" + DATE_TXT, re.I)
FROM_RE = re.compile(r"(?:\bfrom\b|\bcommencing\b|\bstarting\b|\bbeginning\b|\beffective\b)\s*(?:on\s+)?" + DATE_TXT, re.I)
TERM_RE = re.compile(r"(?:period|term|duration)\s+of\s+(?:approximately\s+|up\s+to\s+)?(?:([a-z\-]+)\s*)?\(?(\d{1,3})?\)?\s*[- ]?(year|month|week)s?", re.I)
TERM2_RE = re.compile(r"\b(?:([a-z\-]+)\s*\((\d{1,3})\)|(\d{1,3})|(one|two|three|four|five|six|seven|eight|nine|ten|twelve|eighteen|twenty-four|thirty-six))[\s-]+(year|month)s?\b(?:\s+\w+){0,2}?\s+(?:contract|term|period|agreement)", re.I)


def add_months(d, n):
    y = d.year + (d.month - 1 + n) // 12
    m = (d.month - 1 + n) % 12 + 1
    return date(y, m, min(d.day, calendar.monthrange(y, m)[1]))


def _mkdate(mon, day, yr):
    try:
        return date(int(yr), MONTHS[mon.lower().rstrip(".")[:4] if mon.lower().startswith("sept") else mon.lower()[:3]], int(day))
    except Exception:
        return None


def explicit_period(text):
    """Return (start, end, matched_end_string) from text like 'from October 1, 2012 to February 28, 2014'."""
    if not text:
        return None, None, None
    ends = [(m, _mkdate(m.group(1), m.group(2), m.group(3))) for m in END_RE.finditer(text)]
    ends = [(m, d) for m, d in ends if d]
    starts = [_mkdate(m.group(1), m.group(2), m.group(3)) for m in FROM_RE.finditer(text)]
    starts = [d for d in starts if d]
    if not ends:
        return (starts[0] if starts else None), None, None
    m, e = max(ends, key=lambda x: x[1])
    return (starts[0] if starts else None), e, m.group(0)


def term_months(text):
    """Return (months, matched string) for 'for a period of three (3) years' / '24-month contract'."""
    if not text:
        return None, None
    m = TERM_RE.search(text)
    if m:
        n = int(m.group(2)) if m.group(2) else WORDNUM.get((m.group(1) or "").lower())
        if n:
            unit = m.group(3).lower()
            months = n * 12 if unit == "year" else (n if unit == "month" else max(1, round(n / 4.33)))
            return months, m.group(0)
    m = TERM2_RE.search(text)
    if m:
        n = int(m.group(2) or m.group(3) or 0) or WORDNUM.get((m.group(1) or m.group(4) or "").lower())
        if n:
            return (n * 12 if m.group(5).lower() == "year" else n), m.group(0)
    return None, None


def decide(anchor, text, anchor_label):
    """Status from free text + anchor date (award/approval). Returns (status|None, basis, start, end, end_kind)."""
    s, e, es = explicit_period(text)
    if e:
        st = s or anchor
        if e < REF:
            return None, "ended", st, e, "explicit"
        if st and st > REF:
            return None, "not_started", st, e, "explicit"
        return "ongoing", f"Description states period ending {e.isoformat()} ({es!r}); start {st.isoformat() if st else 'n/a'} <= 2026-10-25 <= end.", st, e, "explicit"
    n, ts = term_months(text)
    if n and anchor:
        st = s or anchor
        end = add_months(st, n)
        if end < REF:
            return None, "ended", st, end, "inferred"
        if st > REF:
            return None, "not_started", st, end, "inferred"
        return "ongoing_inferred", f"No end date published; description states term {ts!r} = {n} months; {('start ' + s.isoformat()) if s else anchor_label + ' ' + anchor.isoformat()} + {n} months = {end.isoformat()} >= 2026-10-25.", st, end, "inferred"
    if anchor and anchor > REF:
        return None, "not_started", anchor, None, None
    return "end_date_unknown", f"Award published ({anchor_label} {anchor.isoformat() if anchor else 'n/a'}); no end date or term published.", anchor, None, None


def canadian_address(text):
    """Return (is_ca, region, postal, basis) from a free-text address."""
    if not text:
        return False, None, None, None
    t = str(text)
    pc = POSTAL_RE.search(t)
    reg = None
    m = re.search(r"\b(ON|QC|BC|AB|MB|SK|NS|NB|NL|PE|PEI|YT|NT|NU)\b", t)
    if m:
        reg = "PE" if m.group(1) == "PEI" else m.group(1)
    else:
        for k, v in PROV_NAMES.items():
            if re.search(r"\b" + k + r"\b", t, re.I):
                reg = v
                break
    if pc and reg:
        return True, reg, (pc.group(1) + " " + pc.group(2)).upper(), "address: Canadian province + postal code"
    if re.search(r"\bcanada\b", t, re.I):
        return True, reg, (pc.group(1) + " " + pc.group(2)).upper() if pc else None, "address: country token 'Canada'"
    if pc and not re.search(r"\b(USA|United States|U\.S\.A?)\b", t, re.I):
        return True, reg, (pc.group(1) + " " + pc.group(2)).upper(), "address: Canadian postal code format"
    return False, reg, None, None

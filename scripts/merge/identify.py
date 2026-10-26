"""Shared rule: are both contract parties identifiable (named), as the user requires?"""
import re

BUYER_PLACEHOLDER = re.compile(r"undisclosed|not disclosed|identity not|confidential|withheld|redacted|anonymi[sz]ed|^not available$|^n/?a$|^unknown$|^-+$|^\W*$", re.I)
VENDOR_PLACEHOLDER = re.compile(
    r"^(undisclosed.*|not disclosed|confidential|withheld|redacted|anonymi[sz]ed|not available|n/?a|unknown|-+|\W*|canadian exporter|"
    r"individual consultants?|various( vendors| suppliers)?|multiple( vendors| suppliers)?|to be determined|tbd|"
    r"see (supplier notes|solicitation.*|attachment.*|below|above|notes|.*\.(org|ca|com)\b.*))$", re.I)


def parties_identifiable(rec):
    b = rec.get("buyer") or {}
    v = rec.get("vendor") or {}
    bn = (b.get("name") or "").strip()
    vn = (v.get("name") or "").strip()
    if not bn or BUYER_PLACEHOLDER.search(bn):
        return False, "buyer not identified in the source (%s)" % (bn[:80] or "no name")
    if not vn or v.get("name_withheld"):
        return False, "vendor name not published or withheld by the source"
    if VENDOR_PLACEHOLDER.match(vn):
        return False, "vendor name is a placeholder in the source (%s)" % vn[:60]
    return True, None

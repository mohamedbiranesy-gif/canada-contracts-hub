#!/usr/bin/env python3
"""Wrapper around scripts/ocp_registry/normalize_ocds.py for publishers whose supplier addresses carry no
country field (Public Contracts Scotland, Sell2Wales): a supplier counts as Canadian when its address has a
Canada country value OR a Canadian postal code (A9A 9A9 pattern, which cannot be a UK postcode) in
address.postalCode, OR a Canadian postal code together with a Canadian province/country token in the address text.
Same CLI as normalize_ocds.py."""
import sys, re
sys.path.insert(0, "scripts/ocp_registry")
import normalize_ocds as N
CA_PC_FULL = re.compile(r"^\s*[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][ -]?\d[ABCEGHJ-NPRSTV-Z]\d\s*$", re.I)
CA_PC = re.compile(r"\b[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][ -]?\d[ABCEGHJ-NPRSTV-Z]\d\b", re.I)
PROV = re.compile(r"\b(canada|ontario|quebec|québec|british columbia|alberta|manitoba|saskatchewan|nova scotia|new brunswick|newfoundland|prince edward island|yukon|nunavut|northwest territories|ON|QC|BC|AB|MB|SK|NS|NB|NL|PE)\b", re.I)
_orig = N.canada_basis
def canada_basis(party):
    b, v = _orig(party)
    if b: return b, v
    ad = party.get("address") or {}
    pc = str(ad.get("postalCode") or "")
    if pc and CA_PC_FULL.match(pc):
        return ("parties[].address.postalCode = %r — Canadian postal-code pattern (A9A 9A9; not a valid UK postcode); publisher gives no country field%s"
                % (pc, (", address.region = %r" % ad.get("region")) if ad.get("region") else "")), "CA"
    tail = " ".join(str(ad.get(k) or "") for k in ("streetAddress", "locality", "region"))
    m = CA_PC.search(tail)
    if m and PROV.search(tail):
        return "Canadian postal code %r with Canadian province/country token in parties[].address text (no country field published)" % m.group(0), "CA"
    return None, None
N.canada_basis = canada_basis
if __name__ == "__main__":
    N.main()

#!/usr/bin/env python3
"""The name a buyer is looked up under in the business registries (tools/registry_lookup.py, tools/bulk_registry_match.py).

A row's buyer name is the name the organisation trades under ("Pegasus Paper", "Bistro de la Gare"); the registries know the legal person
("1688150 Alberta Ltd", "9063-6341 Québec inc"). When the organisation's own site names that legal person in so many words, that is the name
to look up — the ranker (contrib/claude/rank_buyers/rank.py) marks such a name by how it was read:
    "… (stated on <page>, as the site's operator)"                       "This website is operated by X Inc.", "X Ltd. («we»)"
    "… (schema.org JSON-LD legalName on <page>, which gives this site as the organisation's own)"
    a copyright-line name that is a company's ("© 2026 8218536 Canada Inc.": the cell holds the bare name)
Otherwise the buyer name is looked up, as before 2026-11-10.
"""
import re

_SITE_SAYS = re.compile(r"\s*\((?:stated on [^()]*, as the site's operator|schema\.org JSON-LD legalName on [^()]*, which gives this site as the organisation's own)\)\s*$")
_COMPANY = re.compile(r"\b(?:inc|incorporated|incorpor[ée]e|ltd|limited|lt[ée]e|limit[ée]e|llc|llp|corp|corporation|ulc|enr|s\.?e\.?n\.?c(?:\.?r\.?l)?)\b\.?", re.I)


def lookup_name(row):
    """(name to look up, True when it is the legal person the site itself states)"""
    buyer = (row.get("buyer") or "").strip()
    cell = (row.get("buyer_legal_name_as_published") or "").strip()
    m = _SITE_SAYS.search(cell)
    if m and cell[:m.start()].strip():
        return cell[:m.start()].strip(), True
    if cell and " (" not in cell and _COMPANY.search(cell) and len(cell) <= 90:
        return cell, True
    return buyer, False

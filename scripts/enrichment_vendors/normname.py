"""Shared name / address normalisation for vendor <-> registry matching."""
import re
import unicodedata

# legal-form suffix tokens stripped for the "loose" key (kept in the "strict" key, but canonicalised)
SUFFIX_CANON = {
    'INCORPORATED': 'INC', 'INCORPORATEE': 'INC', 'INC': 'INC',
    'LIMITED': 'LTD', 'LTD': 'LTD', 'LIMITEE': 'LTEE', 'LTEE': 'LTEE',
    'CORPORATION': 'CORP', 'CORP': 'CORP',
    'COMPANY': 'CO', 'CO': 'CO', 'COMPAGNIE': 'CIE', 'CIE': 'CIE',
    'ENREGISTREE': 'ENR', 'ENR': 'ENR', 'ENRG': 'ENR',
    'SENC': 'SENC', 'SENCRL': 'SENCRL', 'SEC': 'SEC', 'SRL': 'SRL', 'LLC': 'LLC', 'LLP': 'LLP', 'LP': 'LP',
    'ULC': 'ULC', 'PLC': 'PLC', 'GMBH': 'GMBH', 'SA': 'SA', 'SAS': 'SAS', 'AG': 'AG', 'BV': 'BV', 'NV': 'NV',
    'LIMITEDPARTNERSHIP': 'LP',
}
SUFFIX_SET = set(SUFFIX_CANON.values())
LEADING_ARTICLES = {'THE', 'LES', 'LE', 'LA', 'L', 'LTD'}  # LTD not really leading; kept for safety

_ws = re.compile(r'\s+')
_nonalnum = re.compile(r'[^A-Z0-9 ]+')


def strip_accents(s: str) -> str:
    return ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))


def tokens(name: str):
    if not name:
        return []
    s = strip_accents(str(name)).upper()
    s = s.replace('&', ' AND ').replace('+', ' AND ')
    s = re.sub(r"['’`´]", '', s)           # D'ARCY -> DARCY, L'IMPRIMERIE -> LIMPRIMERIE
    s = re.sub(r'[\.\-/,;:()\[\]"«»#*_|!?]', ' ', s)
    s = _nonalnum.sub(' ', s)
    toks = s.split()
    out = []
    for t in toks:
        out.append(SUFFIX_CANON.get(t, t))
    return out


def strict_key(name: str) -> str:
    """accent/case/punctuation-insensitive, suffix canonicalised, leading article dropped"""
    t = tokens(name)
    if t and t[0] in ('THE', 'LES', 'LE', 'LA'):
        t = t[1:]
    return ' '.join(t)


def loose_key(name: str) -> str:
    """strict key with trailing legal-form suffixes removed (and 'CANADA' kept)"""
    t = tokens(name)
    if t and t[0] in ('THE', 'LES', 'LE', 'LA'):
        t = t[1:]
    while t and t[-1] in SUFFIX_SET:
        t = t[:-1]
    # also drop embedded "LTD" style tokens in the middle only if at end after article e.g. "X INC (CANADA)"
    return ' '.join(t)


PROV_MAP = {
    'ALBERTA': 'AB', 'AB': 'AB', 'BRITISH COLUMBIA': 'BC', 'BC': 'BC', 'B.C.': 'BC', 'BRITISH COLOMBIA': 'BC',
    'BRITISH-COLUMBIA': 'BC', 'COLOMBIE-BRITANNIQUE': 'BC', 'MANITOBA': 'MB', 'MB': 'MB', 'NEW BRUNSWICK': 'NB',
    'NB': 'NB', 'NOUVEAU-BRUNSWICK': 'NB', 'NEWFOUNDLAND AND LABRADOR': 'NL', 'NL': 'NL', 'NF': 'NL',
    'NEWFOUNDLAND': 'NL', 'TERRE-NEUVE-ET-LABRADOR': 'NL', 'NOVA SCOTIA': 'NS', 'NS': 'NS', 'NOUVELLE-ECOSSE': 'NS',
    'NOUVELLE-ÉCOSSE': 'NS', 'ONTARIO': 'ON', 'ON': 'ON', 'ON.': 'ON', 'PRINCE EDWARD ISLAND': 'PE', 'PE': 'PE',
    'PEI': 'PE', 'P.E.I.': 'PE', 'ILE-DU-PRINCE-EDOUARD': 'PE', 'QUEBEC': 'QC', 'QUÉBEC': 'QC', 'QC': 'QC', 'PQ': 'QC',
    '(QUÉBEC)': 'QC', '(QUEBEC)': 'QC', 'SASKATCHEWAN': 'SK', 'SK': 'SK', 'NORTHWEST TERRITORIES': 'NT', 'NT': 'NT',
    'NUNAVUT': 'NU', 'NU': 'NU', 'YUKON': 'YT', 'YT': 'YT', 'YUKON TERRITORY': 'YT', 'AB.': 'AB', 'QUE': 'QC',
    'QUE.': 'QC', 'ONT': 'ON', 'ONT.': 'ON', 'ALTA': 'AB', 'ALTA.': 'AB', 'SASK': 'SK', 'SASK.': 'SK', 'MAN': 'MB',
    'MAN.': 'MB', 'N.S.': 'NS', 'N.B.': 'NB', 'NFLD': 'NL', 'NFLD.': 'NL', 'N.L.': 'NL', 'T.N.-O.': 'NT',
}


def norm_prov(s):
    if not s:
        return None
    k = str(s).strip().upper()
    if k in PROV_MAP:
        return PROV_MAP[k]
    k2 = strip_accents(k)
    return PROV_MAP.get(k2)


def norm_city(s):
    if not s:
        return None
    k = strip_accents(str(s)).upper()
    k = re.sub(r'\(.*?\)', ' ', k)          # "Montréal (Québec)" -> "MONTREAL"
    k = re.sub(r'\b(QC|QUEBEC|ONTARIO|ON|BC|AB|ALBERTA|MB|SK|NS|NB|NL|PE)\b$', ' ', k.strip())
    k = k.replace('ST-', 'SAINT-').replace('ST.', 'SAINT').replace('STE-', 'SAINTE-').replace('STE.', 'SAINTE')
    k = re.sub(r'\bST\b', 'SAINT', k)
    k = re.sub(r'\bSTE\b', 'SAINTE', k)
    k = re.sub(r'[^A-Z0-9]+', ' ', k).strip()
    return k or None


def norm_postal(s):
    if not s:
        return None
    k = re.sub(r'[^A-Z0-9]', '', str(s).upper())
    if re.fullmatch(r'[A-Z]\d[A-Z]\d[A-Z]\d', k):
        return k
    return None


def postal_fsa(s):
    p = norm_postal(s)
    return p[:3] if p else None

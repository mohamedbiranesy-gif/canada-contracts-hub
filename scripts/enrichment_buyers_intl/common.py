import re, unicodedata, json, os, datetime

BASE = '.'
DL = BASE + '/downloads/enrichment_buyers'          # v1 downloads (read-only reuse)
DL2 = BASE + '/downloads/enrichment_buyers_intl'    # this pass: probe pages, PDFs
DL_V2 = BASE + '/downloads/enrichment_buyers_v2'    # v2 downloads (read-only reuse)
OLD_WORK = BASE + '/enrichment/work_buyers'         # v1 work files (read-only)
V2_WORK = BASE + '/enrichment/work_buyers_v2'       # v2 work files (read-only)
DEEP_WORK = BASE + '/enrichment/work_buyers_deep'   # W3 deep-pass work files (read-only)
WORK = BASE + '/enrichment/work_buyers_intl'
INPUT = BASE + '/enrichment/v2/buyers_deep_input.jsonl'
SCOPE = BASE + '/hub/claude_buyer_ap_scope.json'
PREV_ENRICHED = [BASE + '/enrichment/buyers_enriched.jsonl', BASE + '/enrichment/v2/buyers_enriched_v2.jsonl']
OUT_ENRICHED = BASE + '/enrichment/v2/buyers_intl.jsonl'
NOTE = BASE + '/notes/enrichment_buyers_intl.md'
UA = 'contracts-research/1.0 (public-procurement dataset enrichment; polite crawler)'
os.makedirs(WORK, exist_ok=True)
os.makedirs(DL2 + '/dir', exist_ok=True)
os.makedirs(DL2 + '/pages', exist_ok=True)


def now():
    return datetime.datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'


def unaccent(s):
    return ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))


def norm(s):
    s = unaccent((s or '').lower())
    s = s.replace('’', "'").replace('​', '')
    s = re.sub(r"[^a-z0-9]+", ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


def load_buyers():
    """only the buyers of this pass' scope (hub/claude_buyer_ap_scope.json)"""
    keys = set(k for g in json.load(open(SCOPE)) for k in g['buyer_keys'])
    return [b for b in (json.loads(l) for l in open(INPUT)) if b['buyer_key'] in keys]


def fixmojibake(s):
    if s and ('Ã' in s or 'Â' in s or 'â' in s):
        try:
            import ftfy
            return ftfy.fix_text(s)
        except Exception:
            pass
        try:
            return s.encode('latin1').decode('utf8')
        except Exception:
            return s
    return s

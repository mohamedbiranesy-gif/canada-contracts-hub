import re, unicodedata, json, os, datetime

BASE = '.'
DL = BASE + '/downloads/enrichment_buyers'
WORK = BASE + '/enrichment/work_buyers'
INPUT = BASE + '/enrichment/buyer_master_input.jsonl'
UA = 'contracts-research/1.0 (public-procurement dataset enrichment; polite crawler)'
os.makedirs(WORK, exist_ok=True)


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
    return [json.loads(l) for l in open(INPUT)]


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

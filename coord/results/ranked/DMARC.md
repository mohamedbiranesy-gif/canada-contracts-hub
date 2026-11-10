# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 23341 | 95 |
| v=DMARC1; p=none (monitor only) | 29532 | 404 |
| p=quarantine | 11566 | 449 |
| p=reject | 6028 | 498 |
| invalid DMARC record | 65 | 0 |
| lookup error | 31 | 0 |
| not checked | 1 | 0 |

Rows without enforcement (no record / p=none / invalid): **52938**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 179 / 207 / 214
- P01M: 1 / 3 / 4 / 7
- P01T: 9 / 38 / 52 / 37
- P02: 49 / 148 / 120 / 86
- P03: 0 / 47 / 71 / 91
- P04: 246 / 553 / 492 / 274
- P05: 54 / 126 / 115 / 83
- P06: 8 / 50 / 61 / 101
- P06M: 28 / 54 / 31 / 30
- P06T: 2927 / 3843 / 1336 / 645
- P07: 50 / 174 / 107 / 111
- P08: 2344 / 3699 / 1755 / 937
- P09: 68 / 120 / 109 / 50
- P10: 645 / 1137 / 610 / 352
- P10R: 11524 / 13524 / 4018 / 1777
- P11: 217 / 681 / 265 / 144
- P12: 2 / 4 / 0 / 2
- P13: 5144 / 5152 / 2213 / 1087

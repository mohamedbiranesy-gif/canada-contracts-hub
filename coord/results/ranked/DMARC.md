# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 132352 | 270 |
| v=DMARC1; p=none (monitor only) | 125740 | 651 |
| p=quarantine | 43701 | 636 |
| p=reject | 20996 | 623 |
| invalid DMARC record | 245 | 1 |
| lookup error | 116 | 0 |

Rows without enforcement (no record / p=none / invalid): **258337**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 196 / 208 / 224
- P01M: 56 / 100 / 110 / 111
- P01T: 36 / 74 / 60 / 40
- P02: 58 / 168 / 152 / 112
- P03: 4 / 72 / 93 / 108
- P04: 987 / 1777 / 1273 / 805
- P05: 53 / 143 / 132 / 101
- P06: 28 / 75 / 63 / 91
- P06M: 9210 / 10231 / 5853 / 3567
- P06T: 23127 / 23758 / 6295 / 2565
- P07: 218 / 284 / 163 / 123
- P08: 10107 / 11998 / 4824 / 2566
- P09: 50 / 90 / 91 / 43
- P10: 491 / 754 / 447 / 375
- P11: 569 / 711 / 308 / 221
- P12: 2 / 8 / 0 / 1
- P13: 87331 / 75301 / 23629 / 9943

# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 21269 | 90 |
| v=DMARC1; p=none (monitor only) | 26430 | 376 |
| p=quarantine | 10431 | 416 |
| p=reject | 5403 | 468 |
| invalid DMARC record | 59 | 0 |
| lookup error | 7 | 0 |

Rows without enforcement (no record / p=none / invalid): **47758**

## By package (no record / p=none / quarantine / reject)
- P01: 22 / 167 / 189 / 203
- P01M: 2 / 3 / 5 / 10
- P01T: 3 / 25 / 38 / 26
- P02: 40 / 135 / 115 / 78
- P03: 0 / 48 / 82 / 94
- P04: 258 / 568 / 503 / 286
- P05: 56 / 125 / 117 / 81
- P06: 2 / 29 / 45 / 87
- P06M: 31 / 63 / 37 / 36
- P06T: 672 / 1151 / 370 / 240
- P07: 15 / 87 / 71 / 76
- P08: 690 / 1194 / 719 / 431
- P09: 71 / 133 / 110 / 53
- P10: 628 / 1095 / 562 / 302
- P11: 41 / 242 / 128 / 87
- P12: 4 / 11 / 3 / 3
- P13: 18734 / 21354 / 7337 / 3310

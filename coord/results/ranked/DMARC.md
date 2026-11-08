# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 21266 | 90 |
| v=DMARC1; p=none (monitor only) | 26422 | 376 |
| p=quarantine | 10429 | 422 |
| p=reject | 5394 | 459 |
| invalid DMARC record | 59 | 0 |
| lookup error | 10 | 0 |

Rows without enforcement (no record / p=none / invalid): **47747**

## By package (no record / p=none / quarantine / reject)
- P01: 22 / 167 / 194 / 198
- P01M: 2 / 3 / 5 / 9
- P01T: 3 / 25 / 38 / 25
- P02: 41 / 135 / 113 / 80
- P03: 0 / 49 / 82 / 94
- P04: 257 / 568 / 500 / 286
- P05: 56 / 125 / 117 / 81
- P06: 2 / 28 / 45 / 85
- P06M: 31 / 63 / 37 / 37
- P06T: 671 / 1148 / 370 / 238
- P07: 15 / 85 / 69 / 77
- P08: 690 / 1195 / 719 / 431
- P09: 71 / 132 / 110 / 53
- P10: 628 / 1095 / 561 / 300
- P11: 41 / 242 / 129 / 87
- P12: 4 / 11 / 3 / 3
- P13: 18732 / 21351 / 7337 / 3310

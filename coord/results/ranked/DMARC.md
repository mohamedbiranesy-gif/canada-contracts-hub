# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 21266 | 90 |
| v=DMARC1; p=none (monitor only) | 26420 | 375 |
| p=quarantine | 10428 | 419 |
| p=reject | 5396 | 464 |
| invalid DMARC record | 59 | 0 |
| lookup error | 10 | 0 |
| not checked | 11 | 2 |

Rows without enforcement (no record / p=none / invalid): **47745**

## By package (no record / p=none / quarantine / reject)
- P01: 22 / 167 / 192 / 202
- P01M: 2 / 3 / 5 / 10
- P01T: 3 / 25 / 38 / 25
- P02: 41 / 135 / 114 / 78
- P03: 0 / 48 / 82 / 94
- P04: 257 / 568 / 501 / 286
- P05: 56 / 124 / 117 / 81
- P06: 2 / 28 / 45 / 85
- P06M: 31 / 63 / 37 / 36
- P06T: 671 / 1148 / 370 / 239
- P07: 15 / 85 / 69 / 76
- P08: 690 / 1194 / 719 / 431
- P09: 71 / 133 / 110 / 53
- P10: 628 / 1095 / 561 / 300
- P11: 41 / 242 / 128 / 86
- P12: 4 / 11 / 3 / 3
- P13: 18732 / 21351 / 7337 / 3311

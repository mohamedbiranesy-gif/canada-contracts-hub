# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 75031 | 185 |
| v=DMARC1; p=none (monitor only) | 74109 | 548 |
| p=quarantine | 26604 | 547 |
| p=reject | 13403 | 549 |
| invalid DMARC record | 145 | 1 |
| lookup error | 468 | 1 |
| not checked | 27622 | 49 |

Rows without enforcement (no record / p=none / invalid): **149285**

## By package (no record / p=none / quarantine / reject)
- P01: 26 / 185 / 209 / 220
- P01M: 28 / 34 / 36 / 31
- P01T: 21 / 74 / 55 / 39
- P02: 56 / 169 / 141 / 107
- P03: 2 / 67 / 90 / 113
- P04: 737 / 1416 / 929 / 609
- P05: 53 / 141 / 131 / 99
- P06: 17 / 79 / 67 / 106
- P06M: 5621 / 5261 / 2623 / 1299
- P06T: 13900 / 14966 / 4256 / 2057
- P07: 166 / 237 / 155 / 127
- P08: 7048 / 8871 / 3741 / 2055
- P09: 61 / 103 / 102 / 46
- P10: 549 / 837 / 496 / 413
- P11: 372 / 602 / 265 / 206
- P12: 4 / 9 / 2 / 1
- P13: 46370 / 41058 / 13306 / 5875

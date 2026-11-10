# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 23850 | 97 |
| v=DMARC1; p=none (monitor only) | 30874 | 414 |
| p=quarantine | 11867 | 453 |
| p=reject | 6177 | 501 |
| invalid DMARC record | 65 | 0 |
| lookup error | 20 | 0 |

Rows without enforcement (no record / p=none / invalid): **54789**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 179 / 207 / 215
- P01M: 2 / 7 / 9 / 8
- P01T: 9 / 39 / 52 / 37
- P02: 49 / 148 / 120 / 86
- P03: 0 / 47 / 71 / 91
- P04: 246 / 554 / 493 / 275
- P05: 54 / 126 / 115 / 83
- P06: 15 / 73 / 76 / 115
- P06M: 661 / 724 / 262 / 145
- P06T: 3050 / 4159 / 1423 / 687
- P07: 67 / 207 / 134 / 123
- P08: 3032 / 4868 / 2242 / 1193
- P09: 68 / 120 / 109 / 50
- P10: 619 / 1093 / 590 / 327
- P10R: 10536 / 12160 / 3549 / 1534
- P11: 626 / 1783 / 498 / 279
- P12: 2 / 4 / 0 / 2
- P13: 4789 / 4583 / 1917 / 927

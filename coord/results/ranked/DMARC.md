# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 21780 | 93 |
| v=DMARC1; p=none (monitor only) | 27342 | 390 |
| p=quarantine | 10763 | 440 |
| p=reject | 5588 | 491 |
| invalid DMARC record | 59 | 0 |
| lookup error | 223 | 0 |
| not checked | 1 | 0 |

Rows without enforcement (no record / p=none / invalid): **49181**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 178 / 207 / 214
- P01M: 1 / 3 / 5 / 9
- P01T: 4 / 26 / 37 / 26
- P02: 49 / 149 / 120 / 86
- P03: 0 / 46 / 71 / 91
- P04: 246 / 553 / 492 / 272
- P05: 56 / 127 / 119 / 82
- P06: 7 / 39 / 63 / 101
- P06M: 32 / 63 / 37 / 36
- P06T: 716 / 1225 / 385 / 252
- P07: 34 / 145 / 100 / 103
- P08: 1610 / 2857 / 1441 / 746
- P09: 72 / 135 / 115 / 57
- P10: 558 / 1005 / 533 / 287
- P11: 55 / 288 / 146 / 102
- P12: 4 / 10 / 1 / 3
- P13: 18311 / 20493 / 6891 / 3121

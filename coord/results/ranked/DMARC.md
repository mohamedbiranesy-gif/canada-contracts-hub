# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 21519 | 92 |
| v=DMARC1; p=none (monitor only) | 26807 | 390 |
| p=quarantine | 10588 | 438 |
| p=reject | 5487 | 489 |
| invalid DMARC record | 59 | 0 |
| lookup error | 76 | 0 |

Rows without enforcement (no record / p=none / invalid): **48385**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 178 / 207 / 214
- P01M: 1 / 3 / 5 / 9
- P01T: 3 / 26 / 37 / 26
- P02: 49 / 149 / 120 / 86
- P03: 0 / 46 / 71 / 91
- P04: 246 / 553 / 492 / 272
- P05: 56 / 127 / 119 / 82
- P06: 3 / 35 / 49 / 93
- P06M: 32 / 63 / 37 / 36
- P06T: 676 / 1151 / 372 / 239
- P07: 19 / 102 / 81 / 84
- P08: 1015 / 1736 / 949 / 545
- P09: 72 / 135 / 115 / 57
- P10: 625 / 1095 / 564 / 303
- P11: 51 / 240 / 125 / 89
- P12: 4 / 10 / 1 / 3
- P13: 18642 / 21158 / 7244 / 3258

# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 105192 | 215 |
| v=DMARC1; p=none (monitor only) | 101235 | 587 |
| p=quarantine | 35257 | 580 |
| p=reject | 17055 | 569 |
| invalid DMARC record | 191 | 1 |
| lookup error | 90 | 0 |

Rows without enforcement (no record / p=none / invalid): **206618**

## By package (no record / p=none / quarantine / reject)
- P01: 23 / 181 / 206 / 214
- P01M: 32 / 53 / 53 / 52
- P01T: 22 / 75 / 61 / 44
- P02: 53 / 164 / 140 / 107
- P03: 2 / 67 / 88 / 105
- P04: 706 / 1363 / 896 / 587
- P05: 52 / 139 / 130 / 98
- P06: 17 / 75 / 65 / 95
- P06M: 6617 / 6729 / 3591 / 2007
- P06T: 17994 / 18220 / 4810 / 2403
- P07: 166 / 236 / 145 / 112
- P08: 6953 / 8744 / 3648 / 1997
- P09: 51 / 90 / 92 / 43
- P10: 506 / 772 / 462 / 395
- P11: 471 / 634 / 275 / 214
- P12: 4 / 9 / 2 / 1
- P13: 71523 / 63684 / 20593 / 8581

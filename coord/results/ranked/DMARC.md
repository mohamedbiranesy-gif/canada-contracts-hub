# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 111739 | 234 |
| v=DMARC1; p=none (monitor only) | 107106 | 602 |
| p=quarantine | 37231 | 593 |
| p=reject | 17929 | 587 |
| invalid DMARC record | 210 | 1 |
| lookup error | 446 | 1 |

Rows without enforcement (no record / p=none / invalid): **219055**

## By package (no record / p=none / quarantine / reject)
- P01: 23 / 182 / 207 / 218
- P01M: 47 / 68 / 64 / 67
- P01T: 31 / 83 / 67 / 46
- P02: 54 / 163 / 141 / 106
- P03: 3 / 67 / 90 / 105
- P04: 714 / 1368 / 905 / 592
- P05: 52 / 140 / 132 / 99
- P06: 26 / 78 / 68 / 99
- P06M: 7461 / 7698 / 4306 / 2429
- P06T: 25743 / 24751 / 6434 / 2800
- P07: 206 / 283 / 167 / 126
- P08: 9781 / 11719 / 4760 / 2569
- P09: 50 / 90 / 92 / 43
- P10: 503 / 771 / 459 / 390
- P11: 554 / 710 / 312 / 221
- P12: 2 / 7 / 0 / 1
- P13: 66489 / 58928 / 19027 / 8018

# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 95511 | 201 |
| v=DMARC1; p=none (monitor only) | 87937 | 547 |
| p=quarantine | 29327 | 552 |
| p=reject | 14464 | 564 |
| invalid DMARC record | 173 | 0 |
| lookup error | 97 | 0 |

Rows without enforcement (no record / p=none / invalid): **183621**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 180 / 206 / 215
- P01M: 22 / 23 / 30 / 22
- P01T: 52 / 105 / 105 / 70
- P02: 53 / 173 / 139 / 100
- P03: 1 / 58 / 85 / 112
- P04: 631 / 1300 / 880 / 593
- P05: 53 / 143 / 134 / 97
- P06: 22 / 90 / 77 / 101
- P06M: 3734 / 3231 / 1601 / 775
- P06T: 23097 / 24994 / 7788 / 3393
- P07: 167 / 275 / 175 / 131
- P08: 7307 / 9698 / 4134 / 2197
- P09: 58 / 100 / 101 / 42
- P10: 619 / 1024 / 597 / 458
- P10R: 48593 / 35453 / 9958 / 4442
- P11: 2822 / 5049 / 962 / 587
- P12: 2 / 5 / 0 / 1
- P13: 8253 / 6036 / 2355 / 1128

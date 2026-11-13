# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 112315 | 233 |
| v=DMARC1; p=none (monitor only) | 107738 | 604 |
| p=quarantine | 37519 | 593 |
| p=reject | 18082 | 589 |
| invalid DMARC record | 212 | 1 |
| lookup error | 94 | 0 |

Rows without enforcement (no record / p=none / invalid): **220265**

## By package (no record / p=none / quarantine / reject)
- P01: 21 / 182 / 206 / 218
- P01M: 47 / 68 / 65 / 69
- P01T: 31 / 83 / 68 / 47
- P02: 55 / 165 / 142 / 106
- P03: 3 / 68 / 90 / 105
- P04: 709 / 1364 / 905 / 591
- P05: 52 / 139 / 132 / 99
- P06: 28 / 80 / 70 / 101
- P06M: 7531 / 7834 / 4396 / 2483
- P06T: 25755 / 24760 / 6443 / 2806
- P07: 222 / 301 / 175 / 131
- P08: 10428 / 12427 / 5032 / 2699
- P09: 50 / 90 / 90 / 43
- P10: 502 / 773 / 459 / 390
- P11: 558 / 714 / 312 / 226
- P12: 2 / 8 / 0 / 1
- P13: 66321 / 58682 / 18934 / 7967

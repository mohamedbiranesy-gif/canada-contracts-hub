# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 110840 | 231 |
| v=DMARC1; p=none (monitor only) | 106249 | 595 |
| p=quarantine | 36732 | 585 |
| p=reject | 17649 | 583 |
| invalid DMARC record | 207 | 1 |
| lookup error | 92 | 0 |

Rows without enforcement (no record / p=none / invalid): **217296**

## By package (no record / p=none / quarantine / reject)
- P01: 23 / 182 / 207 / 218
- P01M: 44 / 61 / 57 / 61
- P01T: 31 / 83 / 67 / 47
- P02: 54 / 163 / 141 / 106
- P03: 3 / 67 / 90 / 105
- P04: 705 / 1366 / 903 / 590
- P05: 52 / 140 / 132 / 99
- P06: 26 / 78 / 65 / 99
- P06M: 7007 / 7196 / 3944 / 2219
- P06T: 25729 / 24741 / 6431 / 2800
- P07: 195 / 275 / 159 / 126
- P08: 9067 / 11030 / 4464 / 2435
- P09: 50 / 90 / 92 / 43
- P10: 503 / 771 / 461 / 391
- P11: 551 / 696 / 308 / 218
- P12: 2 / 7 / 0 / 1
- P13: 66798 / 59303 / 19211 / 8091

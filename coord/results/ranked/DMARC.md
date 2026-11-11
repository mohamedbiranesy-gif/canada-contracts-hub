# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 102704 | 213 |
| v=DMARC1; p=none (monitor only) | 96572 | 563 |
| p=quarantine | 31980 | 583 |
| p=reject | 15906 | 586 |
| invalid DMARC record | 195 | 1 |
| lookup error | 97 | 0 |
| not checked | 1 | 0 |

Rows without enforcement (no record / p=none / invalid): **199471**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 180 / 205 / 215
- P01M: 26 / 31 / 37 / 32
- P01T: 56 / 117 / 119 / 78
- P02: 57 / 174 / 139 / 100
- P03: 2 / 59 / 84 / 112
- P04: 767 / 1482 / 939 / 627
- P05: 53 / 142 / 132 / 97
- P06: 21 / 88 / 81 / 107
- P06M: 4841 / 4534 / 2372 / 1240
- P06T: 25982 / 28332 / 8863 / 3786
- P07: 189 / 288 / 182 / 141
- P08: 8180 / 10580 / 4467 / 2391
- P09: 56 / 96 / 99 / 42
- P10: 630 / 1017 / 583 / 454
- P10R: 48824 / 35282 / 9924 / 4464
- P11: 4501 / 8141 / 1434 / 878
- P12: 2 / 4 / 0 / 1
- P13: 8492 / 6025 / 2320 / 1141

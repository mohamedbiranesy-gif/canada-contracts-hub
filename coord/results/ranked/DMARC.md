# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 113338 | 238 |
| v=DMARC1; p=none (monitor only) | 109403 | 628 |
| p=quarantine | 38328 | 619 |
| p=reject | 18557 | 604 |
| invalid DMARC record | 214 | 1 |
| lookup error | 94 | 0 |

Rows without enforcement (no record / p=none / invalid): **222955**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 192 / 210 / 223
- P01M: 49 / 88 / 90 / 86
- P01T: 31 / 82 / 68 / 47
- P02: 55 / 166 / 145 / 109
- P03: 3 / 72 / 91 / 106
- P04: 769 / 1534 / 1149 / 731
- P05: 53 / 141 / 130 / 99
- P06: 27 / 76 / 67 / 97
- P06M: 8089 / 8618 / 4955 / 2897
- P06T: 26509 / 25954 / 6594 / 2823
- P07: 221 / 293 / 170 / 128
- P08: 10416 / 12333 / 4967 / 2638
- P09: 50 / 92 / 92 / 43
- P10: 502 / 761 / 451 / 378
- P11: 566 / 722 / 316 / 223
- P12: 2 / 7 / 0 / 1
- P13: 65971 / 58272 / 18833 / 7928

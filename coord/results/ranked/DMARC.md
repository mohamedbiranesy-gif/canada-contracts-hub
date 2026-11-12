# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 71033 | 183 |
| v=DMARC1; p=none (monitor only) | 70855 | 541 |
| p=quarantine | 25626 | 541 |
| p=reject | 13030 | 543 |
| invalid DMARC record | 140 | 1 |
| lookup error | 52 | 0 |

Rows without enforcement (no record / p=none / invalid): **142028**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 180 / 206 / 215
- P01M: 28 / 34 / 36 / 31
- P01T: 21 / 74 / 55 / 39
- P02: 56 / 167 / 138 / 103
- P03: 2 / 63 / 86 / 112
- P04: 745 / 1428 / 902 / 598
- P05: 53 / 141 / 130 / 98
- P06: 17 / 80 / 67 / 106
- P06M: 5567 / 5207 / 2586 / 1290
- P06T: 14229 / 15241 / 4346 / 2081
- P07: 167 / 240 / 154 / 129
- P08: 7105 / 8936 / 3770 / 2064
- P09: 60 / 99 / 102 / 44
- P10: 559 / 852 / 505 / 416
- P11: 368 / 606 / 273 / 207
- P12: 4 / 8 / 2 / 1
- P13: 42027 / 37499 / 12268 / 5496

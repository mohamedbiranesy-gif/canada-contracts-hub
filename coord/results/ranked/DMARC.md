# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 137610 | 280 |
| v=DMARC1; p=none (monitor only) | 130274 | 672 |
| p=quarantine | 45224 | 661 |
| p=reject | 21729 | 642 |
| invalid DMARC record | 251 | 1 |
| lookup error | 124 | 0 |

Rows without enforcement (no record / p=none / invalid): **268135**

## By package (no record / p=none / quarantine / reject)
- P01: 26 / 194 / 211 / 226
- P01M: 58 / 119 / 126 / 125
- P01T: 35 / 71 / 59 / 42
- P02: 58 / 166 / 150 / 111
- P03: 4 / 72 / 92 / 106
- P04: 962 / 1749 / 1259 / 797
- P05: 53 / 143 / 132 / 100
- P06: 28 / 70 / 58 / 87
- P06M: 10055 / 11106 / 6361 / 3880
- P06T: 22799 / 23501 / 6203 / 2498
- P07: 210 / 274 / 153 / 119
- P08: 9857 / 11686 / 4640 / 2485
- P09: 8 / 24 / 24 / 15
- P10: 478 / 728 / 432 / 368
- P11: 571 / 708 / 307 / 217
- P12: 2 / 7 / 0 / 1
- P13: 92406 / 79656 / 25017 / 10552

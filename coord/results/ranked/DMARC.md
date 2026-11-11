# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 106529 | 218 |
| v=DMARC1; p=none (monitor only) | 101896 | 576 |
| p=quarantine | 33389 | 588 |
| p=reject | 16637 | 592 |
| invalid DMARC record | 202 | 1 |
| lookup error | 80 | 0 |

Rows without enforcement (no record / p=none / invalid): **208627**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 180 / 205 / 215
- P01M: 27 / 31 / 37 / 31
- P01T: 61 / 130 / 124 / 83
- P02: 57 / 174 / 139 / 101
- P03: 2 / 60 / 83 / 112
- P04: 771 / 1479 / 941 / 626
- P05: 53 / 140 / 132 / 97
- P06: 20 / 87 / 80 / 107
- P06M: 5011 / 4578 / 2381 / 1219
- P06T: 28533 / 32224 / 9888 / 4345
- P07: 188 / 283 / 181 / 140
- P08: 8112 / 10370 / 4420 / 2371
- P09: 56 / 96 / 99 / 42
- P10: 624 / 988 / 572 / 448
- P10R: 49286 / 35785 / 10207 / 4580
- P11: 5299 / 9445 / 1678 / 1011
- P12: 2 / 4 / 0 / 1
- P13: 8402 / 5842 / 2222 / 1108

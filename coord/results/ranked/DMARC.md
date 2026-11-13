# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 147713 | 288 |
| v=DMARC1; p=none (monitor only) | 136888 | 697 |
| p=quarantine | 48070 | 680 |
| p=reject | 23185 | 655 |
| invalid DMARC record | 267 | 1 |
| lookup error | 156 | 0 |

Rows without enforcement (no record / p=none / invalid): **284868**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 187 / 198 / 219
- P01M: 59 / 117 / 132 / 126
- P01T: 35 / 69 / 56 / 41
- P02: 58 / 161 / 145 / 110
- P03: 4 / 71 / 92 / 108
- P04: 965 / 1774 / 1266 / 806
- P05: 53 / 147 / 137 / 106
- P06: 27 / 71 / 58 / 86
- P06M: 10257 / 11482 / 6533 / 3999
- P06T: 22776 / 21596 / 6230 / 2502
- P07: 210 / 274 / 154 / 119
- P08: 9858 / 11695 / 4637 / 2488
- P09: 8 / 24 / 24 / 15
- P10: 479 / 731 / 429 / 363
- P11: 578 / 710 / 303 / 215
- P12: 2 / 8 / 0 / 1
- P13: 102319 / 87771 / 27676 / 11881

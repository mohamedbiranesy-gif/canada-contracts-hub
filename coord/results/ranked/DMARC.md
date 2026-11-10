# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 53568 | 143 |
| v=DMARC1; p=none (monitor only) | 55040 | 489 |
| p=quarantine | 19974 | 511 |
| p=reject | 10202 | 541 |
| invalid DMARC record | 112 | 0 |
| lookup error | 63 | 0 |
| not checked | 26293 | 52 |

Rows without enforcement (no record / p=none / invalid): **108720**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 179 / 206 / 215
- P01M: 12 / 13 / 20 / 15
- P01T: 33 / 74 / 89 / 62
- P02: 52 / 169 / 137 / 100
- P03: 1 / 58 / 85 / 111
- P04: 564 / 1182 / 835 / 550
- P05: 53 / 135 / 129 / 91
- P06: 16 / 83 / 74 / 100
- P06M: 1990 / 1551 / 787 / 377
- P06T: 11892 / 13612 / 4796 / 2112
- P07: 125 / 239 / 152 / 115
- P08: 5640 / 7797 / 3427 / 1853
- P09: 58 / 100 / 102 / 42
- P10: 578 / 956 / 554 / 411
- P10R: 25846 / 21669 / 6105 / 2757
- P11: 1229 / 2667 / 669 / 408
- P12: 2 / 5 / 0 / 1
- P13: 5452 / 4551 / 1807 / 882

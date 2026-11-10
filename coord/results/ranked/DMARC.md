# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 22876 | 94 |
| v=DMARC1; p=none (monitor only) | 28732 | 400 |
| p=quarantine | 11300 | 446 |
| p=reject | 5899 | 496 |
| invalid DMARC record | 65 | 0 |
| lookup error | 35 | 1 |

Rows without enforcement (no record / p=none / invalid): **51673**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 179 / 207 / 214
- P01M: 1 / 3 / 5 / 9
- P01T: 4 / 26 / 37 / 26
- P02: 49 / 148 / 120 / 86
- P03: 0 / 47 / 71 / 91
- P04: 246 / 554 / 493 / 274
- P05: 56 / 128 / 119 / 83
- P06: 8 / 48 / 66 / 104
- P06M: 32 / 63 / 37 / 36
- P06T: 855 / 1431 / 419 / 275
- P07: 57 / 169 / 111 / 111
- P08: 2384 / 3758 / 1801 / 949
- P09: 74 / 135 / 115 / 57
- P10: 682 / 1209 / 636 / 345
- P11: 57 / 293 / 151 / 105
- P12: 4 / 10 / 1 / 3
- P13: 18342 / 20531 / 6911 / 3131

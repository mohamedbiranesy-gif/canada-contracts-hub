# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 86543 | 180 |
| v=DMARC1; p=none (monitor only) | 79768 | 527 |
| p=quarantine | 26951 | 534 |
| p=reject | 13349 | 555 |
| invalid DMARC record | 158 | 0 |
| lookup error | 1039 | 3 |
| not checked | 12118 | 31 |

Rows without enforcement (no record / p=none / invalid): **166469**

## By package (no record / p=none / quarantine / reject)
- P01: 25 / 180 / 206 / 215
- P01M: 14 / 14 / 20 / 16
- P01T: 45 / 97 / 100 / 66
- P02: 53 / 171 / 137 / 99
- P03: 1 / 58 / 85 / 112
- P04: 598 / 1224 / 853 / 563
- P05: 53 / 137 / 131 / 94
- P06: 18 / 85 / 74 / 102
- P06M: 2531 / 1985 / 962 / 439
- P06T: 20530 / 22550 / 7077 / 3095
- P07: 136 / 252 / 161 / 122
- P08: 6195 / 8479 / 3722 / 2006
- P09: 58 / 100 / 101 / 42
- P10: 600 / 992 / 569 / 434
- P10R: 45948 / 33941 / 9621 / 4316
- P11: 1760 / 3420 / 741 / 432
- P12: 2 / 5 / 0 / 1
- P13: 7976 / 6078 / 2391 / 1195

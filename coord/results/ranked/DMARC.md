# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 91691 | 198 |
| v=DMARC1; p=none (monitor only) | 89315 | 573 |
| p=quarantine | 31418 | 564 |
| p=reject | 15456 | 568 |
| invalid DMARC record | 177 | 1 |
| lookup error | 903 | 1 |
| not checked | 30804 | 78 |

Rows without enforcement (no record / p=none / invalid): **181183**

## By package (no record / p=none / quarantine / reject)
- P01: 26 / 186 / 210 / 221
- P01M: 29 / 47 / 42 / 46
- P01T: 20 / 71 / 57 / 40
- P02: 55 / 169 / 139 / 108
- P03: 2 / 68 / 90 / 110
- P04: 716 / 1379 / 925 / 595
- P05: 53 / 139 / 132 / 100
- P06: 16 / 76 / 65 / 95
- P06M: 5956 / 5853 / 3071 / 1649
- P06T: 15339 / 16048 / 4354 / 2146
- P07: 169 / 238 / 149 / 118
- P08: 6993 / 8781 / 3676 / 2010
- P09: 61 / 103 / 102 / 46
- P10: 508 / 772 / 462 / 392
- P11: 420 / 626 / 274 / 206
- P12: 4 / 9 / 2 / 1
- P13: 61324 / 54750 / 17668 / 7573

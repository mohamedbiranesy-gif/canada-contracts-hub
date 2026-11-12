# DMARC posture of the delivered mailboxes

DNS TXT lookup at `_dmarc.<mail domain>` (organizational domain when the mailbox domain is a subdomain without its own record; negatives confirmed through 8.8.8.8). Tool: `tools/dmarc_check.py`; raw results per domain: `data/incoming/claude/claude_dmarc_check.tsv`; every row without enforcement: `dmarc_no_enforcement.csv` in this folder; the same facts sit in every package row (`email_security_posture`, `dmarc_policy`, `dmarc_record`, `spf_policy`, `mail_provider`).

| posture | delivered rows | of which invoicing/AP mailboxes |
|---|---|---|
| no DMARC record | 99926 | 207 |
| v=DMARC1; p=none (monitor only) | 96790 | 582 |
| p=quarantine | 33879 | 576 |
| p=reject | 16439 | 563 |
| invalid DMARC record | 187 | 1 |
| lookup error | 87 | 0 |
| not checked | 12313 | 30 |

Rows without enforcement (no record / p=none / invalid): **196903**

## By package (no record / p=none / quarantine / reject)
- P01: 23 / 180 / 208 / 213
- P01M: 32 / 54 / 51 / 51
- P01T: 21 / 72 / 59 / 39
- P02: 53 / 164 / 140 / 105
- P03: 2 / 67 / 87 / 104
- P04: 705 / 1362 / 896 / 585
- P05: 52 / 139 / 129 / 98
- P06: 16 / 77 / 64 / 95
- P06M: 6475 / 6519 / 3474 / 1913
- P06T: 16982 / 17343 / 4570 / 2293
- P07: 169 / 238 / 146 / 111
- P08: 6974 / 8762 / 3670 / 1999
- P09: 51 / 90 / 92 / 43
- P10: 510 / 772 / 460 / 391
- P11: 456 / 648 / 274 / 209
- P12: 4 / 9 / 2 / 1
- P13: 67401 / 60294 / 19557 / 8189

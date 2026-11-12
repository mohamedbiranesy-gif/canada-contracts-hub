# Coverage vs the downstream team's targets — 2026-11-12

Benchmarks (field × package with a numeric target): **46 of 438 met** (10.5%); 108 within 10 points; 284 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 131, P01T 193, P01_GOLD 641, P02 474, P03 274, P04 3741, P05 427, P06M 15581, P06T 39000, P06 272, P07 694, P08 22076, P09 314, P10R 0, P10 2346, P11 1514, P12 16, P13 129688

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 19.8% | 8 | vendor GST/HST number (116 rows) |
| P01T | 193 | 1.0% | 34.7% | 8 | payment terms (152 rows) |
| P01_GOLD | 641 | 24.3% | 70.8% | 9 | payment terms (224 rows) |
| P02 | 474 | 7.4% | 54.9% | 9 | PO rule (358 rows) |
| P03 | 274 | 14.6% | 57.3% | 9 | payment terms (136 rows) |
| P04 | 3741 | 1.1% | 17.4% | 6 | PO rule (3540 rows) |
| P05 | 427 | 1.2% | 17.8% | 7 | payment terms (352 rows) |
| P06M | 15581 | 0.0% | 3.0% | 7 | PO rule (15375 rows) |
| P06T | 39000 | 0.0% | 11.2% | 6 | PO rule (38756 rows) |
| P06 | 272 | 0.0% | 11.4% | 6 | reference to quote (PO / contract / vendor id) (272 rows) |
| P07 | 694 | 0.0% | 2.4% | 6 | reference to quote (PO / contract / vendor id) (694 rows) |
| P08 | 22076 | 0.0% | 0.6% | 6 | reference to quote (PO / contract / vendor id) (22076 rows) |
| P09 | 314 | 1.3% | 45.2% | 8 | payment terms (293 rows) |
| P10 | 2346 | 0.0% | 1.1% | 5 | reference to quote (PO / contract / vendor id) (2346 rows) |
| P11 | 1514 | 0.2% | 7.5% | 6 | PO rule (1446 rows) |
| P12 | 16 | 0.0% | 50.0% | 9 | PO rule (15 rows) |
| P13 | 129688 | 0.0% | 0.2% | 6 | reference to quote (PO / contract / vendor id) (129688 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 131 | 8 | 26 | 97 | 0 | 0 | 71 |
| P01T | 193 | 24 | 34 | 135 | 0 | 0 | 70 |
| P01_GOLD | 641 | 230 | 207 | 204 | 0 | 0 | 82 |
| P02 | 474 | 0 | 198 | 276 | 0 | 0 | 66 |
| P03 | 274 | 0 | 0 | 259 | 15 | 0 | 57 |
| P04 | 3741 | 0 | 0 | 3061 | 680 | 0 | 46 |
| P05 | 427 | 15 | 30 | 369 | 13 | 0 | 51 |
| P06M | 15581 | 0 | 10 | 15494 | 77 | 0 | 46 |
| P06T | 39000 | 0 | 24 | 26247 | 12729 | 0 | 38 |
| P06 | 272 | 16 | 50 | 206 | 0 | 0 | 70 |
| P07 | 694 | 0 | 21 | 649 | 24 | 0 | 54 |
| P08 | 22076 | 0 | 0 | 18862 | 3214 | 0 | 43 |
| P09 | 314 | 4 | 12 | 296 | 2 | 0 | 53 |
| P10 | 2346 | 3 | 13 | 1589 | 741 | 0 | 41 |
| P11 | 1514 | 7 | 15 | 43 | 0 | 1449 | 23 |
| P12 | 16 | 0 | 0 | 16 | 0 | 0 | 54 |
| P13 | 129688 | 8 | 61 | 129603 | 16 | 0 | 43 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 131 | 108 | 82.4% | the buyer's PO / reference rule (12) |
| P01T | 193 | 118 | 61.1% | bill-to legal name and address (59) |
| P01_GOLD | 641 | 488 | 76.1% | bill-to legal name and address (96) |
| P02 | 474 | 322 | 67.9% | the buyer's PO / reference rule (83) |
| P03 | 274 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (274) |
| P04 | 3741 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3741) |
| P05 | 427 | 47 | 11.0% | a confirmed invoicing / AP or finance channel (340) |
| P06M | 15581 | 164 | 1.1% | a confirmed invoicing / AP or finance channel (15373) |
| P06T | 39000 | 246 | 0.6% | a confirmed invoicing / AP or finance channel (38418) |
| P06 | 272 | 46 | 16.9% | the buyer's PO / reference rule (117) |
| P07 | 694 | 6 | 0.9% | the buyer's PO / reference rule (272) |
| P08 | 22076 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (22076) |
| P09 | 314 | 42 | 13.4% | a confirmed invoicing / AP or finance channel (262) |
| P10 | 2346 | 7 | 0.3% | a confirmed invoicing / AP or finance channel (2260) |
| P11 | 1514 | 14 | 0.9% | a confirmed invoicing / AP or finance channel (1449) |
| P12 | 16 | 4 | 25.0% | a confirmed invoicing / AP or finance channel (11) |
| P13 | 129688 | 39 | 0.0% | a confirmed invoicing / AP or finance channel (127698) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 131 | 6 | 4.6% | 7 | 0 | the vendor's GST/HST number (BN9) (114) |
| P01T | 193 | 70 | 36.3% | 4 | 0 | the vendor's GST/HST number (BN9) (71) |
| P01_GOLD | 641 | 405 | 63.2% | 11 | 0 | the vendor's GST/HST number (BN9) (160) |
| P02 | 474 | 213 | 44.9% | 21 | 0 | the vendor's GST/HST number (BN9) (203) |
| P03 | 274 | 17 | 6.2% | 0 | 135 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (101) |
| P04 | 3741 | 43 | 1.1% | 7 | 882 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2751) |
| P05 | 427 | 20 | 4.7% | 8 | 120 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (212) |
| P06M | 15581 | 6 | 0.0% | 11 | 402 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (14925) |
| P06T | 39000 | 232 | 0.6% | 16 | 9432 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (28924) |
| P06 | 272 | 28 | 10.3% | 51 | 0 | the vendor's GST/HST number (BN9) (117) |
| P07 | 694 | 6 | 0.9% | 111 | 35 | the vendor's GST/HST number (BN9) (306) |
| P08 | 22076 | 3 | 0.0% | 14 | 4930 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (17085) |
| P09 | 314 | 39 | 12.4% | 1 | 128 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (122) |
| P10 | 2346 | 7 | 0.3% | 15 | 294 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1940) |
| P11 | 1514 | 8 | 0.5% | 3 | 0 | a confirmed invoicing / AP or finance channel (1434) |
| P12 | 16 | 3 | 18.8% | 0 | 6 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (5) |
| P13 | 129688 | 10 | 0.0% | 633 | 33863 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (93661) |
| **all** | 217382 | 1116 | 0.5% | 913 | 50227 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 123 | 0 | 0 | 0 | 69 | 8 | 0 | 103 | 107 | 4 |
| P01T | 169 | 0 | 0 | 0 | 93 | 50 | 28 | 138 | 153 | 7 |
| P01_GOLD | 411 | 0 | 0 | 0 | 13 | 77 | 31 | 204 | 239 | 61 |
| P02 | 474 | 0 | 474 | 0 | 41 | 54 | 21 | 358 | 287 | 24 |
| P03 | 274 | 0 | 274 | 0 | 17 | 44 | 29 | 132 | 144 | 25 |
| P04 | 3741 | 0 | 3741 | 0 | 1598 | 1339 | 1032 | 3540 | 3284 | 170 |
| P05 | 412 | 0 | 360 | 0 | 79 | 88 | 43 | 343 | 354 | 53 |
| P06M | 15581 | 0 | 15581 | 0 | 10202 | 1226 | 128 | 15375 | 15254 | 218 |
| P06T | 39000 | 0 | 39000 | 0 | 34116 | 23906 | 16387 | 38756 | 38399 | 911 |
| P06 | 256 | 0 | 0 | 0 | 117 | 71 | 52 | 179 | 214 | 9 |
| P07 | 694 | 0 | 694 | 0 | 441 | 275 | 132 | 648 | 650 | 13 |
| P08 | 22076 | 0 | 22076 | 0 | 16756 | 9950 | 4706 | 21793 | 21441 | 426 |
| P09 | 310 | 0 | 289 | 0 | 13 | 73 | 3 | 283 | 296 | 48 |
| P10 | 2343 | 0 | 2309 | 0 | 1182 | 1251 | 1077 | 2276 | 2237 | 123 |
| P11 | 1507 | 1449 | 1402 | 0 | 659 | 1036 | 601 | 1446 | 1446 | 61 |
| P12 | 16 | 0 | 14 | 0 | 1 | 4 | 0 | 15 | 15 | 1 |
| P13 | 129680 | 0 | 129288 | 0 | 100590 | 76139 | 24 | 129367 | 128625 | 35 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_phone | P13 | 61.7% | 95% | 43231 |
| buyer_bn_as_published | P13 | 9.6% | 30% | 26454 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 25904 |
| buyer_logo_url | P13 | 75.1% | 95% | 25796 |
| ap_system_hint | P13 | 0.4% | 20% | 25394 |
| buyer_legal_name_as_published | P13 | 41.3% | 60% | 24264 |
| mta_sts | P13 | 82.6% | 100% | 22588 |
| tls_rpt | P13 | 82.6% | 100% | 22588 |
| bimi | P13 | 82.6% | 100% | 22588 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 19332 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 19287 |
| buyer_payment_method_preference | P13 | 0.6% | 15% | 18642 |
| vendor_registered_address | P08 | 30.3% | 70% | 8757 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 7790 |
| ap_system_hint | P06T | 0.6% | 20% | 7551 |
| buyer_phone | P08 | 68.7% | 95% | 5813 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 5778 |
| buyer_tax_exempt_status | P06T | 0.2% | 15% | 5767 |
| buyer_payment_method_preference | P06T | 0.6% | 15% | 5633 |
| invoice_reference_hint | P08 | 1.3% | 25% | 5236 |
| buyer_legal_name_as_published | P08 | 54.9% | 75% | 4431 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 4405 |
| buyer_bn_as_published | P08 | 15.2% | 35% | 4366 |
| vendor_bn9 | P08 | 30.6% | 50% | 4281 |
| ap_system_hint | P08 | 1.0% | 20% | 4192 |
| vendor_phone | P08 | 66.1% | 85% | 4178 |
| vendor_emails | P08 | 56.3% | 75% | 4127 |
| mta_sts | P06T | 90.3% | 100% | 3770 |
| tls_rpt | P06T | 90.3% | 100% | 3770 |
| bimi | P06T | 90.3% | 100% | 3770 |
| buyer_address | P08 | 78.7% | 95% | 3607 |
| buyer_esignature_preference | P08 | 0.5% | 15% | 3210 |
| buyer_tax_exempt_status | P08 | 0.5% | 15% | 3199 |
| buyer_payment_method_preference | P08 | 0.6% | 15% | 3172 |
| buyer_ap_cycle_published | P06M | 0.0% | 20% | 3111 |
| ap_system_hint | P06M | 0.8% | 20% | 2992 |
| vendor_trading_name | P08 | 36.5% | 50% | 2977 |
| average_contract_duration_days | P04 | 19.7% | 90% | 2629 |
| currency | P04 | 26.8% | 95% | 2552 |
| end_date | P04 | 24.5% | 90% | 2451 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 89.3% | 89.3% | +0.2 | 50% | ✅ met |
| P01T | 193 | 93.8% | 93.8% | +0.0 | 50% | ✅ met |
| P01_GOLD | 641 | 92.4% | 94.5% | +0.2 | 95% | 🟡 3 pts to go |
| P02 | 474 | 74.5% | 76.2% | +0.5 | 95% | ❌ 20 pts to go |
| P03 | 274 | 80.7% | 84.3% | -0.7 | 95% | ❌ 14 pts to go |
| P04 | 3741 | 31.4% | 33.0% | +1.2 | 90% | ❌ 59 pts to go |
| P05 | 427 | 38.9% | 41.7% | +0.3 | 70% | ❌ 31 pts to go |
| P06M | 15581 | 91.9% | 91.9% | +0.1 | n/a | no target |
| P06T | 39000 | 98.7% | 98.7% | +0.1 | n/a | no target |
| P06 | 272 | 34.2% | 34.2% | -0.2 | 30% | ✅ met |
| P07 | 694 | 6.6% | 6.6% | -0.3 | 30% | ❌ 23 pts to go |
| P08 | 22076 | 1.3% | 1.3% | +0.0 | 25% | ❌ 24 pts to go |
| P09 | 314 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2346 | 3.0% | 3.1% | -0.1 | 25% | ❌ 22 pts to go |
| P11 | 1514 | 48.2% | 49.0% | +1.3 | 60% | ❌ 12 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 129688 | 99.8% | 99.8% | +0.1 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 193 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 641 | 5.9% | 5.9% | -0.2 | 50% | ❌ 44 pts to go |
| P02 | 474 | 6.3% | 6.3% | +0.1 | 50% | ❌ 44 pts to go |
| P03 | 274 | 1.5% | 1.5% | +0.0 | 40% | ❌ 38 pts to go |
| P04 | 3741 | 0.5% | 0.5% | +0.0 | 30% | ❌ 30 pts to go |
| P05 | 427 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 15581 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 39000 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 694 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22076 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 0.6% | 0.6% | -0.1 | 50% | ❌ 49 pts to go |
| P10 | 2346 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1514 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 129688 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 82.4% | 82.4% | +0.2 | n/a | no target |
| P01T | 193 | 74.6% | 74.6% | +0.1 | 50% | ✅ met |
| P01_GOLD | 641 | 67.4% | 67.4% | +0.6 | 85% | ❌ 18 pts to go |
| P02 | 474 | 65.2% | 65.2% | +0.4 | 90% | ❌ 25 pts to go |
| P03 | 274 | 59.9% | 59.9% | +0.2 | 85% | ❌ 25 pts to go |
| P04 | 3741 | 28.8% | 28.8% | +1.2 | 85% | ❌ 56 pts to go |
| P05 | 427 | 29.3% | 29.3% | +0.4 | 60% | ❌ 31 pts to go |
| P06M | 15581 | 91.7% | 91.7% | +0.2 | n/a | no target |
| P06T | 39000 | 98.6% | 98.6% | +0.2 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 694 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22076 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 96.2% | 96.2% | +0.1 | 100% | 🟡 4 pts to go |
| P10 | 2346 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1514 | 44.6% | 44.6% | +1.3 | 60% | ❌ 15 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 129688 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 193 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 641 | 51.5% | 51.5% | +0.7 | 80% | ❌ 28 pts to go |
| P02 | 474 | 57.2% | 57.2% | +0.3 | 60% | 🟡 3 pts to go |
| P03 | 274 | 50.0% | 50.0% | -0.2 | 80% | ❌ 30 pts to go |
| P04 | 3741 | 24.0% | 24.0% | +1.1 | 50% | ❌ 26 pts to go |
| P05 | 427 | 11.7% | 11.7% | +0.3 | 40% | ❌ 28 pts to go |
| P06M | 15581 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 39000 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 694 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22076 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 82.8% | 82.8% | -0.6 | 50% | ✅ met |
| P10 | 2346 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1514 | 4.5% | 4.5% | -1.1 | 40% | ❌ 36 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 129688 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 193 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 61.3% | 61.3% | +0.9 | 85% | ❌ 24 pts to go |
| P02 | 474 | 56.8% | 56.8% | +0.6 | 90% | ❌ 33 pts to go |
| P03 | 274 | 58.4% | 58.4% | -0.2 | 85% | ❌ 27 pts to go |
| P04 | 3741 | 24.9% | 24.9% | +1.3 | 85% | ❌ 60 pts to go |
| P05 | 427 | 19.9% | 19.9% | +0.2 | 50% | ❌ 30 pts to go |
| P06M | 15581 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 39000 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 694 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22076 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 2346 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1514 | 5.0% | 5.0% | -1.0 | 60% | ❌ 55 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 129688 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 193 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 13.4% | 13.4% | +0.5 | 60% | ❌ 47 pts to go |
| P02 | 474 | 6.1% | 6.1% | +0.1 | 50% | ❌ 44 pts to go |
| P03 | 274 | 7.7% | 7.7% | -0.7 | 50% | ❌ 42 pts to go |
| P04 | 3741 | 1.8% | 1.8% | +0.0 | 40% | ❌ 38 pts to go |
| P05 | 427 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 15581 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 39000 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 694 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22076 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 3.5% | 3.5% | +0.2 | 50% | ❌ 46 pts to go |
| P10 | 2346 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1514 | 0.7% | 0.7% | -0.2 | n/a | no target |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 129688 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 193 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 35.6% | 35.6% | +0.8 | 80% | ❌ 44 pts to go |
| P02 | 474 | 52.1% | 52.1% | +0.2 | 90% | ❌ 38 pts to go |
| P03 | 274 | 32.8% | 32.8% | +0.1 | 80% | ❌ 47 pts to go |
| P04 | 3741 | 22.3% | 22.3% | +0.7 | 85% | ❌ 63 pts to go |
| P05 | 427 | 5.6% | 5.6% | +0.1 | 50% | ❌ 44 pts to go |
| P06M | 15581 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 39000 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 694 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22076 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 74.5% | 74.5% | +0.2 | 95% | ❌ 20 pts to go |
| P10 | 2346 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1514 | 3.5% | 3.5% | -0.8 | 50% | ❌ 46 pts to go |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 129688 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 193 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 8.4% | 8.4% | -0.1 | 50% | ❌ 42 pts to go |
| P02 | 474 | 6.3% | 6.3% | +0.1 | 50% | ❌ 44 pts to go |
| P03 | 274 | 1.8% | 1.8% | -0.1 | 30% | ❌ 28 pts to go |
| P04 | 3741 | 0.5% | 0.5% | +0.0 | 30% | ❌ 30 pts to go |
| P05 | 427 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 15581 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 39000 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 694 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22076 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10 | 2346 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1514 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 129688 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 193 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 641 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 474 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 274 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3741 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 427 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 15581 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 39000 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 272 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 694 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 22076 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 314 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2346 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1514 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 129688 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 11.5% | 11.5% | -0.1 | 70% | ❌ 58 pts to go |
| P01T | 193 | 52.3% | 52.3% | +1.8 | 60% | 🟡 8 pts to go |
| P01_GOLD | 641 | 72.7% | 72.7% | -2.1 | 90% | ❌ 17 pts to go |
| P02 | 474 | 53.6% | 53.6% | +0.0 | 85% | ❌ 31 pts to go |
| P03 | 274 | 67.2% | 67.2% | -2.4 | 90% | ❌ 23 pts to go |
| P04 | 3741 | 35.0% | 35.0% | +0.0 | 75% | ❌ 40 pts to go |
| P05 | 427 | 53.2% | 53.2% | -1.5 | 50% | ✅ met |
| P06M | 15581 | 3.1% | 3.1% | -0.1 | n/a | no target |
| P06T | 39000 | 48.8% | 48.8% | +1.5 | n/a | no target |
| P06 | 272 | 43.8% | 43.8% | -0.2 | 40% | ✅ met |
| P07 | 694 | 32.7% | 32.7% | -0.3 | 50% | ❌ 17 pts to go |
| P08 | 22076 | 30.6% | 30.6% | +0.1 | 50% | ❌ 19 pts to go |
| P09 | 314 | 57.6% | 57.6% | -0.7 | 80% | ❌ 22 pts to go |
| P10 | 2346 | 34.2% | 34.2% | -0.3 | 40% | 🟡 6 pts to go |
| P11 | 1514 | 47.4% | 47.4% | +0.5 | 60% | ❌ 13 pts to go |
| P12 | 16 | 56.2% | 56.2% | -3.8 | 85% | ❌ 29 pts to go |
| P13 | 129688 | 29.5% | 29.5% | -2.2 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 58.8% | 58.8% | -0.9 | n/a | no target |
| P01T | 193 | 53.4% | 53.4% | +2.4 | n/a | no target |
| P01_GOLD | 641 | 71.5% | 71.5% | -1.2 | 95% | ❌ 24 pts to go |
| P02 | 474 | 74.5% | 74.5% | +0.7 | 95% | ❌ 20 pts to go |
| P03 | 274 | 69.3% | 69.3% | -2.6 | 95% | ❌ 26 pts to go |
| P04 | 3741 | 49.9% | 49.9% | +0.7 | 95% | ❌ 45 pts to go |
| P05 | 427 | 57.4% | 57.4% | -0.9 | 70% | ❌ 13 pts to go |
| P06M | 15581 | 45.4% | 45.4% | -0.6 | n/a | no target |
| P06T | 39000 | 57.8% | 57.8% | +1.6 | n/a | no target |
| P06 | 272 | 41.2% | 41.2% | +0.2 | 80% | ❌ 39 pts to go |
| P07 | 694 | 32.3% | 32.3% | +0.4 | 70% | ❌ 38 pts to go |
| P08 | 22076 | 30.3% | 30.3% | +0.0 | 70% | ❌ 40 pts to go |
| P09 | 314 | 86.3% | 86.3% | -0.3 | 100% | ❌ 14 pts to go |
| P10 | 2346 | 35.6% | 35.6% | +0.1 | 70% | ❌ 34 pts to go |
| P11 | 1514 | 53.2% | 53.2% | +0.7 | 75% | ❌ 22 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 129688 | 24.9% | 24.9% | -2.0 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 16.8% | 16.8% | -0.3 | n/a | no target |
| P01T | 193 | 56.0% | 56.0% | +2.4 | n/a | no target |
| P01_GOLD | 641 | 48.4% | 48.4% | -1.4 | 60% | ❌ 12 pts to go |
| P02 | 474 | 56.5% | 56.5% | +0.3 | 60% | 🟡 4 pts to go |
| P03 | 274 | 55.1% | 55.1% | +0.0 | 60% | 🟡 5 pts to go |
| P04 | 3741 | 42.9% | 42.9% | +0.8 | 55% | ❌ 12 pts to go |
| P05 | 427 | 24.4% | 24.4% | -0.2 | 50% | ❌ 26 pts to go |
| P06M | 15581 | 6.8% | 6.8% | +0.0 | n/a | no target |
| P06T | 39000 | 51.2% | 51.2% | +0.3 | n/a | no target |
| P06 | 272 | 48.5% | 48.5% | +0.9 | n/a | no target |
| P07 | 694 | 41.8% | 41.8% | +0.9 | 55% | ❌ 13 pts to go |
| P08 | 22076 | 36.5% | 36.5% | +0.3 | 50% | ❌ 14 pts to go |
| P09 | 314 | 72.0% | 72.0% | -0.3 | 70% | ✅ met |
| P10 | 2346 | 47.7% | 47.7% | +0.9 | 55% | 🟡 7 pts to go |
| P11 | 1514 | 54.0% | 54.0% | +1.8 | 50% | ✅ met |
| P12 | 16 | 87.5% | 87.5% | +0.8 | n/a | no target |
| P13 | 129688 | 3.2% | 3.2% | -0.2 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 49.6% | 49.6% | -0.8 | n/a | no target |
| P01T | 193 | 75.6% | 75.6% | +1.1 | n/a | no target |
| P01_GOLD | 641 | 49.5% | 49.5% | -1.0 | 70% | ❌ 20 pts to go |
| P02 | 474 | 57.0% | 57.0% | -1.2 | 70% | ❌ 13 pts to go |
| P03 | 274 | 51.1% | 51.1% | -0.2 | 70% | ❌ 19 pts to go |
| P04 | 3741 | 55.7% | 55.7% | +1.6 | 65% | 🟡 9 pts to go |
| P05 | 427 | 28.6% | 28.6% | +0.2 | 60% | ❌ 31 pts to go |
| P06M | 15581 | 35.8% | 35.8% | -0.8 | n/a | no target |
| P06T | 39000 | 77.8% | 77.8% | -2.2 | n/a | no target |
| P06 | 272 | 69.1% | 69.1% | +0.2 | 40% | ✅ met |
| P07 | 694 | 65.4% | 65.4% | +0.5 | 85% | ❌ 20 pts to go |
| P08 | 22076 | 66.1% | 66.1% | +0.8 | 85% | ❌ 19 pts to go |
| P09 | 314 | 57.3% | 57.3% | -2.0 | 85% | ❌ 28 pts to go |
| P10 | 2346 | 66.2% | 66.2% | +2.7 | 85% | ❌ 19 pts to go |
| P11 | 1514 | 63.1% | 63.1% | +1.2 | 75% | ❌ 12 pts to go |
| P12 | 16 | 37.5% | 37.5% | +10.8 | n/a | no target |
| P13 | 129688 | 92.0% | 92.0% | +0.8 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 55.7% | 55.7% | -0.9 | n/a | no target |
| P01T | 193 | 97.4% | 97.4% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 78.5% | 78.5% | -1.1 | 90% | ❌ 12 pts to go |
| P02 | 474 | 82.5% | 82.5% | -1.4 | 90% | 🟡 8 pts to go |
| P03 | 274 | 86.9% | 86.9% | -0.9 | 90% | 🟡 3 pts to go |
| P04 | 3741 | 83.7% | 83.7% | -0.7 | 85% | 🟡 1 pts to go |
| P05 | 427 | 45.0% | 45.0% | +0.2 | 70% | ❌ 25 pts to go |
| P06M | 15581 | 42.3% | 42.3% | -1.3 | n/a | no target |
| P06T | 39000 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 272 | 99.3% | 99.3% | +0.0 | 50% | ✅ met |
| P07 | 694 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P08 | 22076 | 99.8% | 99.8% | +0.0 | 100% | 🟡 0 pts to go |
| P09 | 314 | 78.0% | 78.0% | -1.8 | 100% | ❌ 22 pts to go |
| P10 | 2346 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1514 | 97.5% | 97.5% | +0.2 | 100% | 🟡 2 pts to go |
| P12 | 16 | 56.2% | 56.2% | +2.9 | n/a | no target |
| P13 | 129688 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 15.3% | 15.3% | -0.2 | n/a | no target |
| P01T | 193 | 65.8% | 65.8% | +0.7 | n/a | no target |
| P01_GOLD | 641 | 42.1% | 42.1% | -1.4 | 70% | ❌ 28 pts to go |
| P02 | 474 | 48.3% | 48.3% | -0.4 | 75% | ❌ 27 pts to go |
| P03 | 274 | 43.4% | 43.4% | +0.1 | 75% | ❌ 32 pts to go |
| P04 | 3741 | 39.6% | 39.6% | +0.9 | 70% | ❌ 30 pts to go |
| P05 | 427 | 22.0% | 22.0% | +0.0 | 55% | ❌ 33 pts to go |
| P06M | 15581 | 4.7% | 4.7% | -0.1 | n/a | no target |
| P06T | 39000 | 64.1% | 64.1% | +2.0 | n/a | no target |
| P06 | 272 | 49.3% | 49.3% | +2.4 | n/a | no target |
| P07 | 694 | 51.0% | 51.0% | +1.0 | 70% | ❌ 19 pts to go |
| P08 | 22076 | 56.3% | 56.3% | +1.5 | 75% | ❌ 19 pts to go |
| P09 | 314 | 47.8% | 47.8% | -1.4 | 85% | ❌ 37 pts to go |
| P10 | 2346 | 44.6% | 44.6% | +1.0 | 80% | ❌ 35 pts to go |
| P11 | 1514 | 56.2% | 56.2% | +1.9 | 70% | ❌ 14 pts to go |
| P12 | 16 | 37.5% | 37.5% | -2.5 | n/a | no target |
| P13 | 129688 | 5.3% | 5.3% | +0.1 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 55.7% | 55.7% | -0.9 | n/a | no target |
| P01T | 193 | 95.3% | 95.3% | +0.5 | n/a | no target |
| P01_GOLD | 641 | 72.1% | 72.1% | -1.7 | 90% | ❌ 18 pts to go |
| P02 | 474 | 77.4% | 77.4% | -1.6 | 90% | ❌ 13 pts to go |
| P03 | 274 | 83.2% | 83.2% | -0.1 | 90% | 🟡 7 pts to go |
| P04 | 3741 | 78.6% | 78.6% | +2.2 | 85% | 🟡 6 pts to go |
| P05 | 427 | 43.6% | 43.6% | +0.5 | 75% | ❌ 31 pts to go |
| P06M | 15581 | 42.1% | 42.1% | -1.2 | n/a | no target |
| P06T | 39000 | 97.1% | 97.1% | +0.4 | n/a | no target |
| P06 | 272 | 92.3% | 92.3% | +1.8 | n/a | no target |
| P07 | 694 | 93.7% | 93.7% | +1.2 | 100% | 🟡 6 pts to go |
| P08 | 22076 | 92.8% | 92.8% | +2.0 | 100% | 🟡 7 pts to go |
| P09 | 314 | 66.2% | 66.2% | +0.1 | n/a | no target |
| P10 | 2346 | 89.9% | 89.9% | +3.1 | 100% | ❌ 10 pts to go |
| P11 | 1514 | 89.5% | 89.5% | +1.8 | n/a | no target |
| P12 | 16 | 56.2% | 56.2% | +9.5 | n/a | no target |
| P13 | 129688 | 67.8% | 67.8% | +2.6 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 45.8% | 45.8% | -0.7 | n/a | no target · QC vendors: 49 rows, 100.0% filled |
| P01T | 193 | 8.8% | 8.8% | -0.6 | n/a | no target · QC vendors: 4 rows, 75.0% filled |
| P01_GOLD | 641 | 42.9% | 42.9% | -0.9 | 95% | ❌ 52 pts to go · QC vendors: 51 rows, 98.0% filled |
| P02 | 474 | 56.3% | 56.3% | +0.7 | 95% | ❌ 39 pts to go · QC vendors: 113 rows, 100.0% filled |
| P03 | 274 | 46.0% | 46.0% | +0.0 | 95% | ❌ 49 pts to go · QC vendors: 22 rows, 100.0% filled |
| P04 | 3741 | 32.7% | 32.7% | +0.5 | 95% | ❌ 62 pts to go · QC vendors: 631 rows, 97.9% filled |
| P05 | 427 | 13.8% | 13.8% | -0.2 | n/a | no target · QC vendors: 35 rows, 94.3% filled |
| P06M | 15581 | 42.3% | 42.3% | -0.5 | n/a | no target · QC vendors: 5833 rows, 99.8% filled |
| P06T | 39000 | 5.1% | 5.1% | -0.2 | n/a | no target · QC vendors: 2008 rows, 76.8% filled |
| P06 | 272 | 8.5% | 8.5% | +0.1 | n/a | no target · QC vendors: 16 rows, 68.8% filled |
| P07 | 694 | 6.6% | 6.6% | +0.3 | n/a | no target · QC vendors: 40 rows, 77.5% filled |
| P08 | 22076 | 6.6% | 6.6% | +0.0 | n/a | no target · QC vendors: 1279 rows, 92.8% filled |
| P09 | 314 | 76.1% | 76.1% | -0.8 | 95% | ❌ 19 pts to go · QC vendors: 116 rows, 100.0% filled |
| P10 | 2346 | 15.7% | 15.7% | +0.1 | n/a | no target · QC vendors: 228 rows, 89.9% filled |
| P11 | 1514 | 14.1% | 14.1% | -0.7 | n/a | no target · QC vendors: 154 rows, 90.9% filled |
| P12 | 16 | 75.0% | 75.0% | +1.7 | n/a | no target · QC vendors: 3 rows, 100.0% filled |
| P13 | 129688 | 24.3% | 24.3% | -1.9 | n/a | no target · QC vendors: 31573 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 58.0% | 58.0% | -0.9 | n/a | no target · vendors with a registry record: 76 rows, 100.0% filled |
| P01T | 193 | 53.4% | 53.4% | +2.4 | n/a | no target · vendors with a registry record: 103 rows, 100.0% filled |
| P01_GOLD | 641 | 79.7% | 79.7% | -1.8 | 100% | ❌ 20 pts to go · vendors with a registry record: 511 rows, 100.0% filled |
| P02 | 474 | 77.4% | 77.4% | -0.1 | 100% | ❌ 23 pts to go · vendors with a registry record: 367 rows, 100.0% filled |
| P03 | 274 | 78.1% | 78.1% | -2.9 | 100% | ❌ 22 pts to go · vendors with a registry record: 214 rows, 100.0% filled |
| P04 | 3741 | 50.5% | 50.5% | +0.8 | 100% | ❌ 50 pts to go · vendors with a registry record: 1890 rows, 100.0% filled |
| P05 | 427 | 62.1% | 62.1% | -1.2 | n/a | no target · vendors with a registry record: 265 rows, 100.0% filled |
| P06M | 15581 | 45.2% | 45.2% | -0.7 | n/a | no target · vendors with a registry record: 7049 rows, 100.0% filled |
| P06T | 39000 | 57.9% | 57.9% | +1.7 | n/a | no target · vendors with a registry record: 22574 rows, 100.0% filled |
| P06 | 272 | 41.5% | 41.5% | +0.1 | n/a | no target · vendors with a registry record: 113 rows, 100.0% filled |
| P07 | 694 | 32.9% | 32.9% | +0.6 | n/a | no target · vendors with a registry record: 228 rows, 100.0% filled |
| P08 | 22076 | 30.5% | 30.5% | +0.1 | n/a | no target · vendors with a registry record: 6729 rows, 100.0% filled |
| P09 | 314 | 90.1% | 90.1% | -0.5 | n/a | no target · vendors with a registry record: 283 rows, 100.0% filled |
| P10 | 2346 | 36.4% | 36.4% | +0.2 | n/a | no target · vendors with a registry record: 853 rows, 100.0% filled |
| P11 | 1514 | 54.1% | 54.1% | +0.5 | n/a | no target · vendors with a registry record: 819 rows, 100.0% filled |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 16 rows, 100.0% filled |
| P13 | 129688 | 24.9% | 24.9% | -2.0 | n/a | no target · vendors with a registry record: 32237 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 93.9% | 93.9% | +0.1 | 90% | ✅ met |
| P01T | 193 | 74.1% | 74.1% | +1.7 | 90% | ❌ 16 pts to go |
| P01_GOLD | 641 | 88.0% | 88.0% | +0.3 | 95% | 🟡 7 pts to go |
| P02 | 474 | 88.6% | 88.6% | +0.8 | 95% | 🟡 6 pts to go |
| P03 | 274 | 83.9% | 83.9% | -0.5 | 85% | 🟡 1 pts to go |
| P04 | 3741 | 64.2% | 64.2% | +1.2 | 90% | ❌ 26 pts to go |
| P05 | 427 | 79.4% | 79.4% | +0.3 | 75% | ✅ met |
| P06M | 15581 | 92.1% | 92.1% | +0.5 | n/a | no target |
| P06T | 39000 | 38.7% | 38.7% | +1.4 | n/a | no target |
| P06 | 272 | 73.9% | 73.9% | +0.3 | 80% | 🟡 6 pts to go |
| P07 | 694 | 60.4% | 60.5% | +0.6 | 80% | ❌ 20 pts to go |
| P08 | 22076 | 54.9% | 54.9% | +0.5 | 75% | ❌ 20 pts to go |
| P09 | 314 | 76.8% | 76.8% | -0.1 | 95% | ❌ 18 pts to go |
| P10 | 2346 | 46.7% | 46.7% | +0.0 | 70% | ❌ 23 pts to go |
| P11 | 1514 | 31.6% | 31.6% | +0.3 | 65% | ❌ 33 pts to go |
| P12 | 16 | 75.0% | 75.0% | -5.0 | 80% | 🟡 5 pts to go |
| P13 | 129688 | 41.3% | 41.3% | -6.2 | 60% | ❌ 19 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 19.8% | 19.8% | -0.4 | 50% | ❌ 30 pts to go |
| P01T | 193 | 15.5% | 15.5% | -0.6 | n/a | no target |
| P01_GOLD | 641 | 19.0% | 19.0% | -0.5 | 40% | ❌ 21 pts to go |
| P02 | 474 | 19.0% | 19.0% | -0.1 | 40% | ❌ 21 pts to go |
| P03 | 274 | 21.5% | 21.5% | +0.2 | 40% | ❌ 18 pts to go |
| P04 | 3741 | 14.9% | 14.9% | -0.3 | 40% | ❌ 25 pts to go |
| P05 | 427 | 17.6% | 17.6% | +0.1 | 25% | 🟡 7 pts to go |
| P06M | 15581 | 10.9% | 10.9% | -0.7 | n/a | no target |
| P06T | 39000 | 6.0% | 6.0% | -0.9 | n/a | no target |
| P06 | 272 | 12.5% | 12.5% | -0.3 | 35% | ❌ 22 pts to go |
| P07 | 694 | 13.8% | 13.8% | -0.3 | 35% | ❌ 21 pts to go |
| P08 | 22076 | 15.2% | 15.2% | -0.2 | 35% | ❌ 20 pts to go |
| P09 | 314 | 16.6% | 16.6% | +0.3 | n/a | no target |
| P10 | 2346 | 6.1% | 6.1% | -0.6 | 30% | ❌ 24 pts to go |
| P11 | 1514 | 6.9% | 6.9% | -0.5 | n/a | no target |
| P12 | 16 | 6.2% | 6.2% | -0.5 | n/a | no target |
| P13 | 129688 | 9.6% | 9.6% | -2.7 | 30% | ❌ 20 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 193 | 84.5% | 84.5% | +0.1 | 100% | ❌ 16 pts to go |
| P01_GOLD | 641 | 90.8% | 90.8% | +0.1 | 100% | 🟡 9 pts to go |
| P02 | 474 | 95.1% | 95.1% | -0.4 | 100% | 🟡 5 pts to go |
| P03 | 274 | 88.3% | 88.3% | -1.1 | 100% | ❌ 12 pts to go |
| P04 | 3741 | 71.9% | 71.9% | +0.5 | 100% | ❌ 28 pts to go |
| P05 | 427 | 89.2% | 89.2% | -0.1 | 100% | ❌ 11 pts to go |
| P06M | 15581 | 99.2% | 99.2% | +0.0 | n/a | no target |
| P06T | 39000 | 58.0% | 58.0% | -1.3 | n/a | no target |
| P06 | 272 | 79.4% | 79.4% | +0.6 | 95% | ❌ 16 pts to go |
| P07 | 694 | 80.7% | 80.7% | -0.5 | 95% | ❌ 14 pts to go |
| P08 | 22076 | 78.7% | 78.7% | +0.4 | 95% | ❌ 16 pts to go |
| P09 | 314 | 95.9% | 95.9% | -0.2 | 100% | 🟡 4 pts to go |
| P10 | 2346 | 54.0% | 54.0% | -0.4 | 95% | ❌ 41 pts to go |
| P11 | 1514 | 50.3% | 50.3% | +0.9 | 80% | ❌ 30 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 129688 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 87.0% | 87.0% | +1.0 | n/a | no target |
| P01T | 193 | 74.6% | 74.6% | +6.4 | n/a | no target |
| P01_GOLD | 641 | 72.9% | 72.9% | -0.1 | 90% | ❌ 17 pts to go |
| P02 | 474 | 77.4% | 77.4% | -0.5 | 95% | ❌ 18 pts to go |
| P03 | 274 | 73.7% | 73.7% | -1.2 | 95% | ❌ 21 pts to go |
| P04 | 3741 | 69.1% | 69.1% | +0.2 | 95% | ❌ 26 pts to go |
| P05 | 427 | 72.6% | 72.6% | -0.9 | 90% | ❌ 17 pts to go |
| P06M | 15581 | 85.3% | 85.3% | -1.6 | n/a | no target |
| P06T | 39000 | 60.7% | 60.7% | +3.5 | n/a | no target |
| P06 | 272 | 69.5% | 69.5% | +1.0 | 95% | ❌ 26 pts to go |
| P07 | 694 | 66.1% | 66.1% | +1.3 | 90% | ❌ 24 pts to go |
| P08 | 22076 | 68.7% | 68.7% | +0.9 | 95% | ❌ 26 pts to go |
| P09 | 314 | 86.6% | 86.6% | -0.4 | 100% | ❌ 13 pts to go |
| P10 | 2346 | 54.4% | 54.4% | -0.9 | 95% | ❌ 41 pts to go |
| P11 | 1514 | 31.1% | 31.1% | +2.2 | 75% | ❌ 44 pts to go |
| P12 | 16 | 87.5% | 87.5% | -5.8 | n/a | no target |
| P13 | 129688 | 61.7% | 61.7% | -9.1 | 95% | ❌ 33 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 88.5% | 88.5% | +0.9 | n/a | no target |
| P01T | 193 | 90.2% | 90.2% | +6.9 | 95% | 🟡 5 pts to go |
| P01_GOLD | 641 | 84.6% | 84.6% | -0.2 | 90% | 🟡 5 pts to go |
| P02 | 474 | 90.3% | 90.3% | -0.3 | 95% | 🟡 5 pts to go |
| P03 | 274 | 83.6% | 83.6% | -2.0 | 95% | ❌ 11 pts to go |
| P04 | 3741 | 90.3% | 90.3% | +1.1 | 90% | ✅ met |
| P05 | 427 | 92.3% | 92.3% | -0.8 | 95% | 🟡 3 pts to go |
| P06M | 15581 | 90.8% | 90.8% | -2.4 | n/a | no target |
| P06T | 39000 | 82.4% | 82.4% | +7.5 | n/a | no target |
| P06 | 272 | 93.0% | 93.0% | +0.7 | 100% | 🟡 7 pts to go |
| P07 | 694 | 92.8% | 92.8% | +0.6 | 100% | 🟡 7 pts to go |
| P08 | 22076 | 94.2% | 94.2% | +1.9 | 100% | 🟡 6 pts to go |
| P09 | 314 | 73.6% | 73.6% | +0.6 | n/a | no target |
| P10 | 2346 | 93.1% | 93.1% | +1.8 | 100% | 🟡 7 pts to go |
| P11 | 1514 | 49.7% | 49.7% | +7.8 | 80% | ❌ 30 pts to go |
| P12 | 16 | 93.8% | 93.8% | -6.2 | n/a | no target |
| P13 | 129688 | 75.1% | 75.1% | -8.6 | 95% | ❌ 20 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 3.1% | 3.1% | +0.0 | n/a | no target |
| P01T | 193 | 8.8% | 8.8% | -0.6 | n/a | no target |
| P01_GOLD | 641 | 13.9% | 13.9% | -0.3 | 25% | ❌ 11 pts to go |
| P02 | 474 | 24.9% | 24.9% | -0.4 | 40% | ❌ 15 pts to go |
| P03 | 274 | 8.8% | 8.8% | -0.3 | 20% | ❌ 11 pts to go |
| P04 | 3741 | 3.5% | 3.5% | +0.0 | 20% | ❌ 16 pts to go |
| P05 | 427 | 3.3% | 3.3% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 15581 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 39000 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 272 | 5.1% | 5.1% | +0.0 | n/a | no target |
| P07 | 694 | 8.4% | 8.4% | -0.1 | n/a | no target |
| P08 | 22076 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P09 | 314 | 7.6% | 7.6% | -0.2 | n/a | no target |
| P10 | 2346 | 0.9% | 0.9% | +0.1 | n/a | no target |
| P11 | 1514 | 0.9% | 0.9% | -0.1 | n/a | no target |
| P12 | 16 | 6.2% | 6.2% | -0.5 | n/a | no target |
| P13 | 129688 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 18.3% | 18.3% | -0.3 | n/a | no target |
| P01T | 193 | 22.3% | 22.3% | -0.1 | 70% | ❌ 48 pts to go |
| P01_GOLD | 641 | 42.9% | 42.9% | -0.6 | 80% | ❌ 37 pts to go |
| P02 | 474 | 57.4% | 57.4% | +0.1 | 90% | ❌ 33 pts to go |
| P03 | 274 | 18.6% | 18.6% | +0.0 | 60% | ❌ 41 pts to go |
| P04 | 3741 | 22.2% | 22.2% | +0.6 | 85% | ❌ 63 pts to go |
| P05 | 427 | 11.9% | 11.9% | +0.3 | 50% | ❌ 38 pts to go |
| P06M | 15581 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06T | 39000 | 0.6% | 0.6% | -0.1 | n/a | no target |
| P06 | 272 | 15.4% | 15.4% | +0.0 | n/a | no target |
| P07 | 694 | 9.9% | 9.9% | -0.6 | n/a | no target |
| P08 | 22076 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P09 | 314 | 77.1% | 77.1% | -0.8 | 95% | ❌ 18 pts to go |
| P10 | 2346 | 1.5% | 1.5% | -0.2 | n/a | no target |
| P11 | 1514 | 15.7% | 15.7% | -1.0 | n/a | no target |
| P12 | 16 | 25.0% | 25.0% | -1.7 | n/a | no target |
| P13 | 129688 | 0.4% | 0.4% | -0.1 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 6.1% | 6.1% | -0.1 | n/a | no target |
| P01T | 193 | 9.8% | 9.8% | -0.6 | n/a | no target |
| P01_GOLD | 641 | 34.0% | 34.0% | +0.0 | 70% | ❌ 36 pts to go |
| P02 | 474 | 39.2% | 39.2% | +0.1 | 75% | ❌ 36 pts to go |
| P03 | 274 | 18.6% | 18.6% | +0.0 | 55% | ❌ 36 pts to go |
| P04 | 3741 | 22.2% | 22.2% | +0.6 | 75% | ❌ 53 pts to go |
| P05 | 427 | 11.0% | 11.0% | +0.3 | 50% | ❌ 39 pts to go |
| P06M | 15581 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06T | 39000 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 272 | 6.2% | 6.2% | +0.3 | n/a | no target |
| P07 | 694 | 4.9% | 4.9% | -0.3 | n/a | no target |
| P08 | 22076 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 314 | 74.5% | 74.5% | -0.7 | 95% | ❌ 20 pts to go |
| P10 | 2346 | 0.7% | 0.7% | -0.2 | n/a | no target |
| P11 | 1514 | 15.4% | 15.4% | -1.0 | n/a | no target |
| P12 | 16 | 18.8% | 18.8% | -1.2 | n/a | no target |
| P13 | 129688 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 7.6% | 7.6% | -0.2 | n/a | no target |
| P01T | 193 | 8.3% | 8.3% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 57.9% | 58.0% | -0.1 | 80% | ❌ 22 pts to go |
| P02 | 474 | 45.6% | 45.8% | -0.1 | 75% | ❌ 29 pts to go |
| P03 | 274 | 37.2% | 37.2% | -0.1 | 70% | ❌ 33 pts to go |
| P04 | 3741 | 21.7% | 22.2% | +0.6 | 70% | ❌ 48 pts to go |
| P05 | 427 | 14.8% | 14.8% | +0.6 | 50% | ❌ 35 pts to go |
| P06M | 15581 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 39000 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 272 | 15.8% | 15.8% | -0.7 | n/a | no target |
| P07 | 694 | 1.9% | 1.9% | -0.1 | n/a | no target |
| P08 | 22076 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P09 | 314 | 47.1% | 47.1% | +0.5 | 80% | ❌ 33 pts to go |
| P10 | 2346 | 1.1% | 1.1% | -0.1 | n/a | no target |
| P11 | 1514 | 6.2% | 6.3% | -0.6 | n/a | no target |
| P12 | 16 | 37.5% | 37.5% | -2.5 | n/a | no target |
| P13 | 129688 | 0.1% | 0.2% | -0.1 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 18.3% | 18.3% | -0.3 | n/a | no target |
| P01T | 193 | 20.7% | 20.7% | -0.7 | 60% | ❌ 39 pts to go |
| P01_GOLD | 641 | 62.7% | 62.7% | -0.7 | 70% | 🟡 7 pts to go |
| P02 | 474 | 39.5% | 39.5% | -0.2 | 50% | ❌ 10 pts to go |
| P03 | 274 | 47.4% | 47.4% | -0.9 | 55% | 🟡 8 pts to go |
| P04 | 3741 | 12.2% | 12.2% | +0.0 | 40% | ❌ 28 pts to go |
| P05 | 427 | 17.1% | 17.1% | +0.0 | 40% | ❌ 23 pts to go |
| P06M | 15581 | 2.1% | 2.1% | -0.1 | n/a | no target |
| P06T | 39000 | 1.5% | 1.5% | -0.2 | n/a | no target |
| P06 | 272 | 21.3% | 21.3% | -0.7 | n/a | no target |
| P07 | 694 | 6.3% | 6.3% | -0.3 | n/a | no target |
| P08 | 22076 | 2.9% | 2.9% | +0.0 | n/a | no target |
| P09 | 314 | 5.7% | 5.7% | -0.2 | n/a | no target |
| P10 | 2346 | 4.6% | 4.6% | +0.0 | n/a | no target |
| P11 | 1514 | 4.5% | 4.5% | -0.7 | n/a | no target |
| P12 | 16 | 6.2% | 6.2% | -0.5 | n/a | no target |
| P13 | 129688 | 0.8% | 0.8% | -0.2 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 21.4% | 21.4% | -0.3 | n/a | no target |
| P01T | 193 | 28.5% | 28.5% | -0.1 | 65% | ❌ 36 pts to go |
| P01_GOLD | 641 | 68.2% | 68.2% | -0.8 | 70% | 🟡 2 pts to go |
| P02 | 474 | 24.5% | 24.5% | +0.3 | 50% | ❌ 26 pts to go |
| P03 | 274 | 51.8% | 51.8% | -0.7 | 60% | 🟡 8 pts to go |
| P04 | 3741 | 5.4% | 5.4% | +0.0 | 40% | ❌ 35 pts to go |
| P05 | 427 | 19.7% | 19.7% | +0.0 | 45% | ❌ 25 pts to go |
| P06M | 15581 | 1.3% | 1.3% | -0.1 | n/a | no target |
| P06T | 39000 | 0.6% | 0.6% | -0.1 | n/a | no target |
| P06 | 272 | 34.2% | 34.2% | -0.2 | n/a | no target |
| P07 | 694 | 6.6% | 6.6% | -0.3 | n/a | no target |
| P08 | 22076 | 1.3% | 1.3% | +0.0 | n/a | no target |
| P09 | 314 | 9.9% | 9.9% | +0.1 | n/a | no target |
| P10 | 2346 | 3.0% | 3.0% | -0.1 | n/a | no target |
| P11 | 1514 | 4.5% | 4.5% | -0.6 | n/a | no target |
| P12 | 16 | 6.2% | 6.2% | -0.5 | n/a | no target |
| P13 | 129688 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 12.2% | 12.2% | -0.2 | n/a | no target |
| P01T | 193 | 13.5% | 13.5% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 49.1% | 49.1% | -0.7 | 50% | 🟡 1 pts to go |
| P02 | 474 | 37.3% | 37.3% | +0.0 | n/a | no target |
| P03 | 274 | 51.1% | 51.1% | -1.0 | 60% | 🟡 9 pts to go |
| P04 | 3741 | 11.8% | 11.8% | -0.1 | n/a | no target |
| P05 | 427 | 15.0% | 15.0% | -0.2 | n/a | no target |
| P06M | 15581 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P06T | 39000 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 272 | 25.4% | 25.4% | -0.2 | n/a | no target |
| P07 | 694 | 8.2% | 8.2% | -0.1 | n/a | no target |
| P08 | 22076 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P09 | 314 | 18.5% | 18.5% | +0.9 | n/a | no target |
| P10 | 2346 | 2.4% | 2.4% | +0.0 | n/a | no target |
| P11 | 1514 | 3.8% | 3.8% | -0.9 | n/a | no target |
| P12 | 16 | 12.5% | 12.5% | -0.8 | n/a | no target |
| P13 | 129688 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 11.5% | 11.5% | -0.1 | 15% | 🟡 4 pts to go |
| P01T | 193 | 12.4% | 12.4% | -0.1 | 15% | 🟡 3 pts to go |
| P01_GOLD | 641 | 34.8% | 34.8% | -0.5 | 40% | 🟡 5 pts to go |
| P02 | 474 | 12.7% | 12.9% | -0.2 | 25% | ❌ 12 pts to go |
| P03 | 274 | 17.2% | 17.2% | -0.3 | 25% | 🟡 8 pts to go |
| P04 | 3741 | 2.7% | 2.7% | +0.0 | 15% | ❌ 12 pts to go |
| P05 | 427 | 6.6% | 6.6% | +0.0 | 15% | 🟡 8 pts to go |
| P06M | 15581 | 0.8% | 0.8% | -0.1 | 15% | ❌ 14 pts to go |
| P06T | 39000 | 0.6% | 0.6% | +0.1 | 15% | ❌ 14 pts to go |
| P06 | 272 | 10.7% | 10.7% | +0.1 | 15% | 🟡 4 pts to go |
| P07 | 694 | 4.2% | 4.2% | -0.1 | 15% | ❌ 11 pts to go |
| P08 | 22076 | 0.6% | 0.6% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 314 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2346 | 1.2% | 1.2% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 1514 | 1.5% | 1.5% | +0.0 | 15% | ❌ 14 pts to go |
| P12 | 16 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 129688 | 0.6% | 0.6% | -0.1 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 5.3% | 5.3% | -0.1 | 15% | 🟡 10 pts to go |
| P01T | 193 | 11.4% | 11.4% | -0.1 | 25% | ❌ 14 pts to go |
| P01_GOLD | 641 | 28.5% | 28.5% | -0.7 | 25% | ✅ met |
| P02 | 474 | 25.1% | 25.1% | -0.2 | 15% | ✅ met |
| P03 | 274 | 22.3% | 22.3% | +0.2 | 15% | ✅ met |
| P04 | 3741 | 4.0% | 4.0% | +0.0 | 15% | ❌ 11 pts to go |
| P05 | 427 | 11.2% | 11.2% | +0.1 | 15% | 🟡 4 pts to go |
| P06M | 15581 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P06T | 39000 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 272 | 8.5% | 8.5% | +0.1 | 15% | 🟡 6 pts to go |
| P07 | 694 | 2.7% | 2.7% | -0.2 | 15% | ❌ 12 pts to go |
| P08 | 22076 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 314 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2346 | 1.5% | 1.5% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 1514 | 2.2% | 2.2% | -0.5 | 15% | ❌ 13 pts to go |
| P12 | 16 | 18.8% | 18.8% | -1.2 | 15% | ✅ met |
| P13 | 129688 | 0.1% | 0.1% | -0.1 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 2.3% | 2.3% | +0.0 | 20% | ❌ 18 pts to go |
| P01T | 193 | 4.1% | 4.1% | -0.1 | 20% | ❌ 16 pts to go |
| P01_GOLD | 641 | 4.4% | 4.4% | -0.1 | 20% | ❌ 16 pts to go |
| P02 | 474 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P03 | 274 | 1.8% | 1.8% | +0.3 | 20% | ❌ 18 pts to go |
| P04 | 3741 | 0.6% | 0.6% | +0.0 | 20% | ❌ 19 pts to go |
| P05 | 427 | 1.2% | 1.2% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 15581 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 39000 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 272 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P07 | 694 | 0.4% | 0.4% | +0.0 | 20% | ❌ 20 pts to go |
| P08 | 22076 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 314 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2346 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1514 | 0.1% | 0.1% | -0.2 | 20% | ❌ 20 pts to go |
| P12 | 16 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 129688 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 1.5% | 1.5% | -0.1 | 15% | ❌ 14 pts to go |
| P01T | 193 | 3.1% | 3.1% | +0.0 | 15% | ❌ 12 pts to go |
| P01_GOLD | 641 | 10.1% | 10.1% | -0.3 | 15% | 🟡 5 pts to go |
| P02 | 474 | 11.8% | 11.8% | -0.2 | 15% | 🟡 3 pts to go |
| P03 | 274 | 20.1% | 20.1% | -0.1 | 15% | ✅ met |
| P04 | 3741 | 2.3% | 2.3% | +0.0 | 15% | ❌ 13 pts to go |
| P05 | 427 | 2.8% | 2.8% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 15581 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P06T | 39000 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 272 | 5.1% | 5.1% | +0.0 | 15% | 🟡 10 pts to go |
| P07 | 694 | 1.6% | 1.6% | +0.0 | 15% | ❌ 13 pts to go |
| P08 | 22076 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 314 | 0.6% | 0.6% | -0.1 | 15% | ❌ 14 pts to go |
| P10 | 2346 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 1514 | 1.1% | 1.1% | -0.1 | 15% | ❌ 14 pts to go |
| P12 | 16 | 6.2% | 6.2% | -0.5 | 15% | 🟡 9 pts to go |
| P13 | 129688 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 13.7% | 13.7% | -0.3 | 20% | 🟡 6 pts to go |
| P01T | 193 | 14.0% | 14.0% | -0.1 | 40% | ❌ 26 pts to go |
| P01_GOLD | 641 | 45.6% | 45.6% | -0.6 | 40% | ✅ met |
| P02 | 474 | 42.8% | 42.8% | -0.1 | 20% | ✅ met |
| P03 | 274 | 48.2% | 48.2% | -0.8 | 35% | ✅ met |
| P04 | 3741 | 14.2% | 14.2% | +0.0 | 20% | 🟡 6 pts to go |
| P05 | 427 | 15.5% | 15.5% | +0.1 | 20% | 🟡 4 pts to go |
| P06M | 15581 | 0.8% | 0.8% | +0.0 | 20% | ❌ 19 pts to go |
| P06T | 39000 | 0.6% | 0.6% | -0.1 | 20% | ❌ 19 pts to go |
| P06 | 272 | 25.0% | 25.0% | -0.3 | 20% | ✅ met |
| P07 | 694 | 8.6% | 8.6% | +0.0 | 20% | ❌ 11 pts to go |
| P08 | 22076 | 1.0% | 1.0% | +0.0 | 20% | ❌ 19 pts to go |
| P09 | 314 | 18.5% | 18.5% | +0.3 | 20% | 🟡 2 pts to go |
| P10 | 2346 | 3.7% | 3.7% | +0.0 | 20% | ❌ 16 pts to go |
| P11 | 1514 | 4.0% | 4.0% | -0.8 | 20% | ❌ 16 pts to go |
| P12 | 16 | 6.2% | 6.2% | -0.5 | 20% | ❌ 14 pts to go |
| P13 | 129688 | 0.4% | 0.4% | -0.1 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 33.6% | 33.6% | +0.3 | n/a | no target |
| P01T | 193 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 71.9% | 71.9% | +2.4 | 95% | ❌ 23 pts to go |
| P02 | 474 | 64.8% | 64.8% | +1.9 | 95% | ❌ 30 pts to go |
| P03 | 274 | 56.9% | 56.9% | +3.7 | 90% | ❌ 33 pts to go |
| P04 | 3741 | 26.4% | 26.4% | +1.6 | 85% | ❌ 59 pts to go |
| P05 | 427 | 38.4% | 38.4% | +0.7 | 75% | ❌ 37 pts to go |
| P06M | 15581 | 36.1% | 36.1% | +0.0 | n/a | no target |
| P06T | 39000 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 694 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22076 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 90.1% | 90.1% | +1.8 | 100% | 🟡 10 pts to go |
| P10 | 2346 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1514 | 5.2% | 5.2% | -0.8 | 60% | ❌ 55 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 129688 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 33.6% | 33.6% | +0.3 | n/a | no target |
| P01T | 193 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 73.6% | 73.6% | +0.8 | 100% | ❌ 26 pts to go |
| P02 | 474 | 66.9% | 66.9% | +0.6 | 100% | ❌ 33 pts to go |
| P03 | 274 | 59.5% | 59.5% | +0.6 | n/a | no target |
| P04 | 3741 | 26.8% | 26.8% | +1.3 | 95% | ❌ 68 pts to go |
| P05 | 427 | 34.2% | 34.2% | +0.8 | 80% | ❌ 46 pts to go |
| P06M | 15581 | 36.1% | 36.1% | +0.0 | n/a | no target |
| P06T | 39000 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 694 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22076 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 92.0% | 92.0% | +0.5 | 100% | 🟡 8 pts to go |
| P10 | 2346 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1514 | 5.4% | 5.4% | -1.0 | n/a | no target |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 129688 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 80.2% | 80.2% | +0.4 | n/a | no target |
| P01T | 193 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 52.3% | 52.3% | +0.7 | 85% | ❌ 33 pts to go |
| P02 | 474 | 58.0% | 58.0% | +0.5 | 90% | ❌ 32 pts to go |
| P03 | 274 | 43.1% | 43.1% | +0.5 | 85% | ❌ 42 pts to go |
| P04 | 3741 | 28.8% | 28.8% | +0.9 | 90% | ❌ 61 pts to go |
| P05 | 427 | 32.3% | 32.3% | -0.4 | 75% | ❌ 43 pts to go |
| P06M | 15581 | 86.1% | 86.1% | -1.0 | n/a | no target |
| P06T | 39000 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 694 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22076 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 82.5% | 82.5% | -0.9 | 95% | ❌ 12 pts to go |
| P10 | 2346 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1514 | 4.6% | 4.6% | -0.8 | n/a | no target |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 129688 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 78.6% | 78.6% | +0.3 | n/a | no target |
| P01T | 193 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 52.6% | 52.6% | +0.8 | 85% | ❌ 32 pts to go |
| P02 | 474 | 52.7% | 52.7% | +0.1 | 90% | ❌ 37 pts to go |
| P03 | 274 | 43.1% | 43.1% | -0.6 | 85% | ❌ 42 pts to go |
| P04 | 3741 | 24.5% | 24.5% | +0.7 | 90% | ❌ 66 pts to go |
| P05 | 427 | 42.6% | 42.6% | -0.8 | 75% | ❌ 32 pts to go |
| P06M | 15581 | 76.7% | 76.7% | -1.1 | n/a | no target |
| P06T | 39000 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 694 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22076 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10 | 2346 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1514 | 3.6% | 3.6% | -0.9 | n/a | no target |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 129688 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 90.1% | 90.1% | +0.2 | n/a | no target |
| P01T | 193 | 94.3% | 94.3% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 85.5% | 85.5% | +0.2 | 100% | ❌ 14 pts to go |
| P02 | 474 | 77.0% | 77.0% | +0.6 | 100% | ❌ 23 pts to go |
| P03 | 274 | 91.6% | 91.6% | +0.3 | n/a | no target |
| P04 | 3741 | 50.1% | 50.1% | +1.3 | 95% | ❌ 45 pts to go |
| P05 | 427 | 77.5% | 77.5% | +0.0 | 95% | ❌ 18 pts to go |
| P06M | 15581 | 99.0% | 99.0% | +0.1 | n/a | no target |
| P06T | 39000 | 91.6% | 91.6% | +1.0 | n/a | no target |
| P06 | 272 | 22.8% | 22.8% | -0.3 | n/a | no target |
| P07 | 694 | 13.3% | 13.3% | -0.5 | n/a | no target |
| P08 | 22076 | 7.0% | 7.0% | -0.1 | n/a | no target |
| P09 | 314 | 98.4% | 98.4% | -0.3 | 100% | 🟡 2 pts to go |
| P10 | 2346 | 70.9% | 70.9% | -0.1 | n/a | no target |
| P11 | 1514 | 69.0% | 69.0% | +0.9 | n/a | no target |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 129688 | 99.8% | 99.8% | +0.1 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 90.1% | 90.1% | +0.2 | n/a | no target |
| P01T | 193 | 94.3% | 94.3% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 88.6% | 88.6% | +0.1 | 100% | ❌ 11 pts to go |
| P02 | 474 | 78.1% | 78.3% | +0.6 | 100% | ❌ 22 pts to go |
| P03 | 274 | 92.3% | 92.3% | +0.3 | n/a | no target |
| P04 | 3741 | 53.3% | 53.3% | +1.4 | 95% | ❌ 42 pts to go |
| P05 | 427 | 89.5% | 89.5% | -0.1 | 70% | ✅ met |
| P06M | 15581 | 99.0% | 99.0% | +0.1 | n/a | no target |
| P06T | 39000 | 91.6% | 91.6% | +1.0 | n/a | no target |
| P06 | 272 | 22.8% | 22.8% | -0.3 | n/a | no target |
| P07 | 694 | 13.3% | 13.3% | -0.5 | n/a | no target |
| P08 | 22076 | 7.0% | 7.0% | -0.1 | n/a | no target |
| P09 | 314 | 98.4% | 98.4% | -0.3 | 100% | 🟡 2 pts to go |
| P10 | 2346 | 70.9% | 70.9% | -0.1 | n/a | no target |
| P11 | 1514 | 69.1% | 69.1% | +0.9 | n/a | no target |
| P12 | 16 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 129688 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 193 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 16.7% | 16.7% | -0.1 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 376 rows, 28.5% filled |
| P02 | 474 | 11.0% | 11.0% | -0.2 | n/a | no target · rows from a source that publishes bids: 298 rows, 17.4% filled |
| P03 | 274 | 14.2% | 14.2% | +1.3 | n/a | no target · rows from a source that publishes bids: 144 rows, 27.1% filled |
| P04 | 3741 | 1.6% | 1.6% | +0.1 | n/a | no target · rows from a source that publishes bids: 920 rows, 6.3% filled |
| P05 | 427 | 2.6% | 2.6% | +0.0 | n/a | no target · rows from a source that publishes bids: 52 rows, 21.2% filled |
| P06M | 15581 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 39000 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 694 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 22076 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 314 | 4.5% | 4.5% | +0.3 | n/a | no target · rows from a source that publishes bids: 300 rows, 4.7% filled |
| P10 | 2346 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1514 | 0.7% | 0.7% | -0.2 | n/a | no target · rows from a source that publishes bids: 77 rows, 13.0% filled |
| P12 | 16 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 16 rows, 0.0% filled |
| P13 | 129688 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 193 | 0.0% | 97.9% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 53.7% | 82.4% | +0.5 | 90% | ❌ 36 pts to go |
| P02 | 474 | 52.7% | 87.3% | +0.3 | 90% | ❌ 37 pts to go |
| P03 | 274 | 44.9% | 80.3% | +0.4 | 90% | ❌ 45 pts to go |
| P04 | 3741 | 19.7% | 93.2% | +0.6 | 90% | ❌ 70 pts to go |
| P05 | 427 | 0.0% | 82.9% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 15581 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 39000 | 0.0% | 99.8% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 694 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 22076 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 314 | 2.5% | 4.1% | +0.2 | 90% | ❌ 88 pts to go |
| P10 | 2346 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1514 | 3.1% | 97.1% | -1.0 | n/a | no target |
| P12 | 16 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 129688 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 193 | 0.5% | 98.4% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 26.4% | 55.1% | +0.5 | 90% | ❌ 64 pts to go |
| P02 | 474 | 51.5% | 86.1% | +0.0 | n/a | no target |
| P03 | 274 | 24.5% | 59.9% | +0.2 | n/a | no target |
| P04 | 3741 | 21.6% | 95.1% | +0.6 | n/a | no target |
| P05 | 427 | 0.5% | 83.4% | +0.0 | n/a | no target |
| P06M | 15581 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 39000 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 694 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 22076 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 314 | 40.8% | 42.4% | -0.2 | n/a | no target |
| P10 | 2346 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1514 | 3.0% | 97.0% | -0.7 | n/a | no target |
| P12 | 16 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 129688 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 193 | 2.1% | 100.0% | +0.0 | n/a | no target |
| P01_GOLD | 641 | 52.3% | 81.0% | +0.5 | 95% | ❌ 43 pts to go |
| P02 | 474 | 57.0% | 91.6% | +0.6 | n/a | no target |
| P03 | 274 | 47.8% | 83.2% | +1.0 | n/a | no target |
| P04 | 3741 | 22.3% | 95.7% | +1.1 | n/a | no target |
| P05 | 427 | 4.7% | 87.6% | +0.2 | n/a | no target |
| P06M | 15581 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 39000 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 272 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 694 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 22076 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 314 | 61.8% | 63.4% | -0.7 | n/a | no target |
| P10 | 2346 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1514 | 3.2% | 97.2% | -0.9 | n/a | no target |
| P12 | 16 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 129688 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P01T | 193 | 97.9% | 97.9% | -2.1 | 100% | 🟡 2 pts to go |
| P01_GOLD | 641 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P02 | 474 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P03 | 274 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P04 | 3741 | 98.8% | 98.8% | -1.2 | 100% | 🟡 1 pts to go |
| P05 | 427 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P06M | 15581 | 95.2% | 95.2% | -4.8 | 100% | 🟡 5 pts to go |
| P06T | 39000 | 90.3% | 90.3% | -9.7 | 100% | 🟡 10 pts to go |
| P06 | 272 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P07 | 694 | 98.8% | 98.8% | -1.2 | 100% | 🟡 1 pts to go |
| P08 | 22076 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P09 | 314 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2346 | 98.0% | 98.0% | -2.0 | 100% | 🟡 2 pts to go |
| P11 | 1514 | 95.6% | 95.6% | -4.4 | 100% | 🟡 4 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 129688 | 82.6% | 82.6% | -17.4 | 100% | ❌ 17 pts to go |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P01T | 193 | 97.9% | 97.9% | -2.1 | 100% | 🟡 2 pts to go |
| P01_GOLD | 641 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P02 | 474 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P03 | 274 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P04 | 3741 | 98.8% | 98.8% | -1.2 | 100% | 🟡 1 pts to go |
| P05 | 427 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P06M | 15581 | 95.2% | 95.2% | -4.8 | 100% | 🟡 5 pts to go |
| P06T | 39000 | 90.3% | 90.3% | -9.7 | 100% | 🟡 10 pts to go |
| P06 | 272 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P07 | 694 | 98.8% | 98.8% | -1.2 | 100% | 🟡 1 pts to go |
| P08 | 22076 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P09 | 314 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2346 | 98.0% | 98.0% | -2.0 | 100% | 🟡 2 pts to go |
| P11 | 1514 | 95.6% | 95.6% | -4.4 | 100% | 🟡 4 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 129688 | 82.6% | 82.6% | -17.4 | 100% | ❌ 17 pts to go |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 131 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P01T | 193 | 97.9% | 97.9% | -2.1 | 100% | 🟡 2 pts to go |
| P01_GOLD | 641 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P02 | 474 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P03 | 274 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P04 | 3741 | 98.8% | 98.8% | -1.2 | 100% | 🟡 1 pts to go |
| P05 | 427 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P06M | 15581 | 95.2% | 95.2% | -4.8 | 100% | 🟡 5 pts to go |
| P06T | 39000 | 90.3% | 90.3% | -9.7 | 100% | 🟡 10 pts to go |
| P06 | 272 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P07 | 694 | 98.8% | 98.8% | -1.2 | 100% | 🟡 1 pts to go |
| P08 | 22076 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P09 | 314 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2346 | 98.0% | 98.0% | -2.0 | 100% | 🟡 2 pts to go |
| P11 | 1514 | 95.6% | 95.6% | -4.4 | 100% | 🟡 4 pts to go |
| P12 | 16 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 129688 | 82.6% | 82.6% | -17.4 | 100% | ❌ 17 pts to go |


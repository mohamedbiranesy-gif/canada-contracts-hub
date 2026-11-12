# Coverage vs the downstream team's targets — 2026-11-12

Benchmarks (field × package with a numeric target): **92 of 438 met** (21.0%); 64 within 10 points; 282 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 246, P01T 227, P01_GOLD 630, P02 464, P03 265, P04 3584, P05 423, P06M 21978, P06T 59807, P06 273, P07 787, P08 29136, P09 277, P10R 0, P10 2125, P11 1801, P12 10, P13 152628

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 246 | 0.0% | 14.6% | 7 | vendor GST/HST number (230 rows) |
| P01T | 227 | 1.3% | 37.4% | 8 | payment terms (181 rows) |
| P01_GOLD | 630 | 24.3% | 71.6% | 10 | payment terms (220 rows) |
| P02 | 464 | 7.8% | 55.4% | 9 | PO rule (354 rows) |
| P03 | 265 | 14.7% | 56.2% | 9 | PO rule (132 rows) |
| P04 | 3584 | 1.3% | 17.2% | 6 | PO rule (3384 rows) |
| P05 | 423 | 0.9% | 17.0% | 7 | payment terms (351 rows) |
| P06M | 21978 | 0.0% | 2.9% | 7 | PO rule (21599 rows) |
| P06T | 59807 | 0.1% | 13.0% | 7 | PO rule (59427 rows) |
| P06 | 273 | 0.0% | 10.3% | 6 | reference to quote (PO / contract / vendor id) (258 rows) |
| P07 | 787 | 0.0% | 2.4% | 6 | payment terms (746 rows) |
| P08 | 29136 | 0.0% | 1.0% | 6 | PO rule (28866 rows) |
| P09 | 277 | 1.4% | 41.9% | 8 | payment terms (259 rows) |
| P10 | 2125 | 0.0% | 1.3% | 5 | reference to quote (PO / contract / vendor id) (2125 rows) |
| P11 | 1801 | 0.1% | 7.9% | 6 | PO rule (1734 rows) |
| P12 | 10 | 0.0% | 40.0% | 8 | PO rule (10 rows) |
| P13 | 152628 | 0.0% | 0.3% | 7 | reference to quote (PO / contract / vendor id) (152628 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 246 | 9 | 56 | 181 | 0 | 0 | 70 |
| P01T | 227 | 27 | 37 | 163 | 0 | 0 | 67 |
| P01_GOLD | 630 | 257 | 169 | 204 | 0 | 0 | 82 |
| P02 | 464 | 0 | 189 | 275 | 0 | 0 | 66 |
| P03 | 265 | 0 | 0 | 253 | 12 | 0 | 57 |
| P04 | 3584 | 0 | 0 | 2957 | 627 | 0 | 46 |
| P05 | 423 | 15 | 28 | 367 | 13 | 0 | 51 |
| P06M | 21978 | 0 | 17 | 21906 | 55 | 0 | 46 |
| P06T | 59807 | 0 | 28 | 40237 | 19542 | 0 | 38 |
| P06 | 273 | 18 | 42 | 213 | 0 | 0 | 68 |
| P07 | 787 | 0 | 21 | 744 | 22 | 0 | 54 |
| P08 | 29136 | 0 | 0 | 25993 | 3143 | 0 | 43 |
| P09 | 277 | 5 | 10 | 261 | 1 | 0 | 53 |
| P10 | 2125 | 3 | 13 | 1445 | 664 | 0 | 41 |
| P11 | 1801 | 7 | 13 | 37 | 0 | 1744 | 23 |
| P12 | 10 | 0 | 0 | 10 | 0 | 0 | 54 |
| P13 | 152628 | 14 | 64 | 152538 | 12 | 0 | 43 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 246 | 189 | 76.8% | tax treatment (33) |
| P01T | 227 | 138 | 60.8% | bill-to legal name and address (75) |
| P01_GOLD | 630 | 477 | 75.7% | bill-to legal name and address (97) |
| P02 | 464 | 314 | 67.7% | the buyer's PO / reference rule (85) |
| P03 | 265 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (265) |
| P04 | 3584 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3584) |
| P05 | 423 | 44 | 10.4% | a confirmed invoicing / AP or finance channel (336) |
| P06M | 21978 | 235 | 1.1% | a confirmed invoicing / AP or finance channel (21680) |
| P06T | 59807 | 333 | 0.6% | a confirmed invoicing / AP or finance channel (59002) |
| P06 | 273 | 50 | 18.3% | the buyer's PO / reference rule (114) |
| P07 | 787 | 31 | 3.9% | bill-to legal name and address (311) |
| P08 | 29136 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (29136) |
| P09 | 277 | 40 | 14.4% | a confirmed invoicing / AP or finance channel (226) |
| P10 | 2125 | 7 | 0.3% | a confirmed invoicing / AP or finance channel (2047) |
| P11 | 1801 | 14 | 0.8% | a confirmed invoicing / AP or finance channel (1744) |
| P12 | 10 | 2 | 20.0% | a confirmed invoicing / AP or finance channel (8) |
| P13 | 152628 | 43 | 0.0% | a confirmed invoicing / AP or finance channel (150488) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 246 | 6 | 2.4% | 7 | 0 | the vendor's GST/HST number (BN9) (230) |
| P01T | 227 | 99 | 43.6% | 3 | 0 | the vendor's GST/HST number (BN9) (74) |
| P01_GOLD | 630 | 409 | 64.9% | 11 | 0 | the vendor's GST/HST number (BN9) (144) |
| P02 | 464 | 214 | 46.1% | 22 | 0 | the vendor's GST/HST number (BN9) (200) |
| P03 | 265 | 18 | 6.8% | 0 | 133 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (96) |
| P04 | 3584 | 42 | 1.2% | 7 | 903 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2574) |
| P05 | 423 | 20 | 4.7% | 8 | 125 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (203) |
| P06M | 21978 | 8 | 0.0% | 12 | 537 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (21050) |
| P06T | 59807 | 386 | 0.6% | 14 | 18661 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (40256) |
| P06 | 273 | 25 | 9.2% | 54 | 0 | the vendor's GST/HST number (BN9) (127) |
| P07 | 787 | 13 | 1.7% | 134 | 36 | the vendor's GST/HST number (BN9) (365) |
| P08 | 29136 | 5 | 0.0% | 13 | 6966 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (22107) |
| P09 | 277 | 37 | 13.4% | 0 | 108 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (106) |
| P10 | 2125 | 7 | 0.3% | 15 | 304 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1719) |
| P11 | 1801 | 7 | 0.4% | 3 | 0 | a confirmed invoicing / AP or finance channel (1728) |
| P12 | 10 | 1 | 10.0% | 0 | 4 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (4) |
| P13 | 152628 | 21 | 0.0% | 1054 | 60980 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (89323) |
| **all** | 274661 | 1318 | 0.5% | 1357 | 88757 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 237 | 0 | 0 | 0 | 161 | 9 | 0 | 192 | 209 | 1 |
| P01T | 200 | 0 | 0 | 0 | 122 | 67 | 31 | 165 | 183 | 4 |
| P01_GOLD | 373 | 0 | 0 | 0 | 13 | 79 | 30 | 199 | 235 | 3 |
| P02 | 464 | 0 | 464 | 0 | 37 | 55 | 14 | 354 | 283 | 2 |
| P03 | 265 | 0 | 265 | 0 | 17 | 46 | 26 | 132 | 140 | 2 |
| P04 | 3584 | 0 | 3584 | 0 | 1535 | 1277 | 959 | 3384 | 3131 | 33 |
| P05 | 408 | 0 | 356 | 0 | 83 | 94 | 39 | 339 | 353 | 7 |
| P06M | 21978 | 0 | 21978 | 0 | 16238 | 1373 | 146 | 21599 | 21352 | 19 |
| P06T | 59807 | 0 | 59807 | 0 | 53638 | 37764 | 24720 | 59427 | 58901 | 375 |
| P06 | 255 | 0 | 0 | 0 | 137 | 75 | 45 | 192 | 223 | 4 |
| P07 | 787 | 0 | 787 | 0 | 533 | 326 | 119 | 745 | 746 | 5 |
| P08 | 29136 | 0 | 29136 | 0 | 22960 | 13906 | 4688 | 28866 | 28507 | 160 |
| P09 | 272 | 0 | 253 | 0 | 12 | 69 | 1 | 247 | 261 | 7 |
| P10 | 2122 | 0 | 2089 | 0 | 1100 | 1130 | 962 | 2054 | 2016 | 16 |
| P11 | 1794 | 1744 | 1696 | 0 | 903 | 1230 | 547 | 1734 | 1727 | 20 |
| P12 | 10 | 0 | 9 | 0 | 0 | 2 | 0 | 10 | 10 | 1 |
| P13 | 152614 | 0 | 152219 | 0 | 122573 | 83019 | 18 | 152292 | 151507 | 61 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_phone | P13 | 67.9% | 95% | 41382 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 30477 |
| ap_system_hint | P13 | 0.4% | 20% | 29932 |
| buyer_bn_as_published | P13 | 12.5% | 30% | 26651 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 22754 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 22710 |
| buyer_legal_name_as_published | P13 | 45.6% | 60% | 21968 |
| buyer_payment_method_preference | P13 | 0.6% | 15% | 21923 |
| buyer_logo_url | P13 | 80.8% | 95% | 21686 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 11946 |
| ap_system_hint | P06T | 0.6% | 20% | 11615 |
| vendor_registered_address | P08 | 30.7% | 70% | 11456 |
| buyer_phone | P08 | 60.0% | 95% | 10191 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 8866 |
| buyer_tax_exempt_status | P06T | 0.2% | 15% | 8853 |
| buyer_payment_method_preference | P06T | 0.7% | 15% | 8574 |
| buyer_legal_name_as_published | P08 | 52.3% | 75% | 6622 |
| vendor_phone | P08 | 64.0% | 85% | 6124 |
| vendor_emails | P08 | 54.3% | 75% | 6039 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 5816 |
| buyer_logo_url | P08 | 80.1% | 100% | 5810 |
| ap_system_hint | P08 | 0.8% | 20% | 5597 |
| vendor_bn9 | P08 | 31.5% | 50% | 5404 |
| vendor_trading_name | P08 | 33.0% | 50% | 4967 |
| buyer_bn_as_published | P08 | 18.4% | 35% | 4850 |
| buyer_ap_cycle_published | P06M | 0.1% | 20% | 4385 |
| buyer_esignature_preference | P08 | 0.3% | 15% | 4270 |
| buyer_tax_exempt_status | P08 | 0.4% | 15% | 4269 |
| buyer_payment_method_preference | P08 | 0.5% | 15% | 4214 |
| ap_system_hint | P06M | 1.0% | 20% | 4168 |
| invoice_reference_hint | P08 | 11.3% | 25% | 3984 |
| vendor_logo_url | P08 | 87.2% | 100% | 3728 |
| buyer_address | P08 | 83.9% | 95% | 3239 |
| buyer_esignature_preference | P06M | 0.4% | 15% | 3200 |
| buyer_tax_exempt_status | P06M | 0.7% | 15% | 3154 |
| buyer_payment_method_preference | P06M | 0.8% | 15% | 3124 |
| average_contract_duration_days | P04 | 19.6% | 90% | 2522 |
| currency | P04 | 26.9% | 95% | 2441 |
| end_date | P04 | 24.6% | 90% | 2346 |
| ap_phone | P04 | 21.4% | 85% | 2279 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 93.1% | 93.1% | +4.0 | 50% | ✅ met |
| P01T | 227 | 95.6% | 95.6% | +1.8 | 50% | ✅ met |
| P01_GOLD | 630 | 92.1% | 94.4% | -0.1 | 95% | 🟡 3 pts to go |
| P02 | 464 | 75.0% | 76.5% | +1.0 | 95% | ❌ 20 pts to go |
| P03 | 265 | 81.1% | 84.5% | -0.3 | 95% | ❌ 14 pts to go |
| P04 | 3584 | 32.1% | 33.8% | +1.9 | 90% | ❌ 58 pts to go |
| P05 | 423 | 39.5% | 42.3% | +0.9 | 70% | ❌ 30 pts to go |
| P06M | 21978 | 93.2% | 93.2% | +1.4 | n/a | no target |
| P06T | 59807 | 99.3% | 99.3% | +0.7 | n/a | no target |
| P06 | 273 | 35.2% | 35.2% | +0.8 | 30% | ✅ met |
| P07 | 787 | 12.5% | 12.5% | +5.6 | 30% | ❌ 18 pts to go |
| P08 | 29136 | 11.3% | 11.3% | +10.0 | 25% | ❌ 14 pts to go |
| P09 | 277 | 98.9% | 99.6% | -0.1 | 100% | 🟡 1 pts to go |
| P10 | 2125 | 3.3% | 3.3% | +0.2 | 25% | ❌ 22 pts to go |
| P11 | 1801 | 54.6% | 55.3% | +7.7 | 60% | 🟡 5 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 152628 | 99.6% | 99.6% | -0.1 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 227 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 630 | 5.9% | 5.9% | -0.2 | 50% | ❌ 44 pts to go |
| P02 | 464 | 5.6% | 5.6% | -0.6 | 50% | ❌ 44 pts to go |
| P03 | 265 | 1.9% | 1.9% | +0.4 | 40% | ❌ 38 pts to go |
| P04 | 3584 | 0.6% | 0.6% | +0.1 | 30% | ❌ 29 pts to go |
| P05 | 423 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 21978 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59807 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 787 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29136 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 277 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10 | 2125 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1801 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 152628 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 89.4% | 89.4% | +7.2 | n/a | no target |
| P01T | 227 | 79.7% | 79.7% | +5.2 | 50% | ✅ met |
| P01_GOLD | 630 | 67.1% | 67.1% | +0.3 | 85% | ❌ 18 pts to go |
| P02 | 464 | 66.2% | 66.2% | +1.4 | 90% | ❌ 24 pts to go |
| P03 | 265 | 60.4% | 60.4% | +0.7 | 85% | ❌ 25 pts to go |
| P04 | 3584 | 29.3% | 29.3% | +1.7 | 85% | ❌ 56 pts to go |
| P05 | 423 | 29.8% | 29.8% | +0.9 | 60% | ❌ 30 pts to go |
| P06M | 21978 | 92.9% | 92.9% | +1.4 | n/a | no target |
| P06T | 59807 | 99.2% | 99.2% | +0.8 | n/a | no target |
| P06 | 273 | 5.5% | 5.5% | +5.5 | n/a | no target |
| P07 | 787 | 7.1% | 7.1% | +7.1 | n/a | no target |
| P08 | 29136 | 10.4% | 10.4% | +10.4 | n/a | no target |
| P09 | 277 | 95.7% | 95.7% | -0.4 | 100% | 🟡 4 pts to go |
| P10 | 2125 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1801 | 51.7% | 51.7% | +8.4 | 60% | 🟡 8 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152628 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 227 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 630 | 51.4% | 51.4% | +0.6 | 80% | ❌ 29 pts to go |
| P02 | 464 | 58.4% | 58.4% | +1.5 | 60% | 🟡 2 pts to go |
| P03 | 265 | 50.2% | 50.2% | +0.0 | 80% | ❌ 30 pts to go |
| P04 | 3584 | 23.9% | 23.9% | +1.0 | 50% | ❌ 26 pts to go |
| P05 | 423 | 12.5% | 12.5% | +1.1 | 40% | ❌ 28 pts to go |
| P06M | 21978 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59807 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 787 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29136 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 277 | 81.2% | 81.2% | -2.2 | 50% | ✅ met |
| P10 | 2125 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1801 | 3.3% | 3.3% | -2.3 | 40% | ❌ 37 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 152628 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 227 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P01_GOLD | 630 | 61.0% | 61.0% | +0.6 | 85% | ❌ 24 pts to go |
| P02 | 464 | 58.6% | 58.6% | +2.4 | 90% | ❌ 31 pts to go |
| P03 | 265 | 58.9% | 58.9% | +0.3 | 85% | ❌ 26 pts to go |
| P04 | 3584 | 24.8% | 24.8% | +1.2 | 85% | ❌ 60 pts to go |
| P05 | 423 | 20.3% | 20.3% | +0.6 | 50% | ❌ 30 pts to go |
| P06M | 21978 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59807 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 787 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29136 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 277 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 2125 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1801 | 3.7% | 3.7% | -2.3 | 60% | ❌ 56 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152628 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 227 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 630 | 13.0% | 13.0% | +0.1 | 60% | ❌ 47 pts to go |
| P02 | 464 | 6.9% | 6.9% | +0.9 | 50% | ❌ 43 pts to go |
| P03 | 265 | 8.7% | 8.7% | +0.3 | 50% | ❌ 41 pts to go |
| P04 | 3584 | 1.9% | 1.9% | +0.1 | 40% | ❌ 38 pts to go |
| P05 | 423 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 21978 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59807 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 787 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29136 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 277 | 3.2% | 3.2% | -0.1 | 50% | ❌ 47 pts to go |
| P10 | 2125 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1801 | 0.4% | 0.4% | -0.5 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 152628 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 227 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 630 | 35.9% | 35.9% | +1.1 | 80% | ❌ 44 pts to go |
| P02 | 464 | 52.6% | 52.6% | +0.7 | 90% | ❌ 37 pts to go |
| P03 | 265 | 34.0% | 34.0% | +1.3 | 80% | ❌ 46 pts to go |
| P04 | 3584 | 22.1% | 22.1% | +0.5 | 85% | ❌ 63 pts to go |
| P05 | 423 | 6.4% | 6.4% | +0.9 | 50% | ❌ 44 pts to go |
| P06M | 21978 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59807 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 787 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29136 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 277 | 73.6% | 73.6% | -0.7 | 95% | ❌ 21 pts to go |
| P10 | 2125 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1801 | 2.7% | 2.7% | -1.6 | 50% | ❌ 47 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 152628 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 227 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 630 | 8.3% | 8.3% | -0.2 | 50% | ❌ 42 pts to go |
| P02 | 464 | 5.6% | 5.6% | -0.6 | 50% | ❌ 44 pts to go |
| P03 | 265 | 2.6% | 2.6% | +0.7 | 30% | ❌ 27 pts to go |
| P04 | 3584 | 0.6% | 0.6% | +0.1 | 30% | ❌ 29 pts to go |
| P05 | 423 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 21978 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59807 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 787 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29136 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 277 | 0.4% | 0.4% | +0.1 | n/a | no target |
| P10 | 2125 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1801 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 152628 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 227 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 630 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 464 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 265 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3584 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 423 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 21978 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 59807 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 273 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 787 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 29136 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 277 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2125 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1801 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152628 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 6.5% | 6.5% | -5.1 | 70% | ❌ 64 pts to go |
| P01T | 227 | 59.9% | 59.9% | +9.4 | 60% | 🟡 0 pts to go |
| P01_GOLD | 630 | 74.9% | 74.9% | +0.1 | 90% | ❌ 15 pts to go |
| P02 | 464 | 54.3% | 54.3% | +0.7 | 85% | ❌ 31 pts to go |
| P03 | 265 | 66.8% | 66.8% | -2.8 | 90% | ❌ 23 pts to go |
| P04 | 3584 | 38.1% | 38.1% | +3.1 | 75% | ❌ 37 pts to go |
| P05 | 423 | 54.6% | 54.6% | -0.1 | 50% | ✅ met |
| P06M | 21978 | 2.9% | 2.9% | -0.3 | n/a | no target |
| P06T | 59807 | 64.5% | 64.5% | +17.2 | n/a | no target |
| P06 | 273 | 42.9% | 42.9% | -1.1 | 40% | ✅ met |
| P07 | 787 | 33.7% | 33.7% | +0.7 | 50% | ❌ 16 pts to go |
| P08 | 29136 | 31.5% | 31.5% | +1.0 | 50% | ❌ 18 pts to go |
| P09 | 277 | 57.0% | 57.0% | -1.3 | 80% | ❌ 23 pts to go |
| P10 | 2125 | 38.8% | 38.8% | +4.3 | 40% | 🟡 1 pts to go |
| P11 | 1801 | 55.1% | 55.1% | +8.2 | 60% | 🟡 5 pts to go |
| P12 | 10 | 50.0% | 50.0% | -10.0 | 85% | ❌ 35 pts to go |
| P13 | 152628 | 44.8% | 44.8% | +13.1 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 46.3% | 46.3% | -13.4 | n/a | no target |
| P01T | 227 | 59.5% | 59.5% | +8.5 | n/a | no target |
| P01_GOLD | 630 | 72.7% | 72.7% | +0.0 | 95% | ❌ 22 pts to go |
| P02 | 464 | 74.8% | 74.8% | +1.0 | 95% | ❌ 20 pts to go |
| P03 | 265 | 69.4% | 69.4% | -2.5 | 95% | ❌ 26 pts to go |
| P04 | 3584 | 53.0% | 53.0% | +3.8 | 95% | ❌ 42 pts to go |
| P05 | 423 | 58.2% | 58.2% | -0.1 | 70% | ❌ 12 pts to go |
| P06M | 21978 | 41.5% | 41.5% | -4.5 | n/a | no target |
| P06T | 59807 | 67.5% | 67.5% | +11.3 | n/a | no target |
| P06 | 273 | 38.8% | 38.8% | -2.2 | 80% | ❌ 41 pts to go |
| P07 | 787 | 32.7% | 32.7% | +0.8 | 70% | ❌ 37 pts to go |
| P08 | 29136 | 30.7% | 30.7% | +0.4 | 70% | ❌ 39 pts to go |
| P09 | 277 | 86.6% | 86.6% | +0.0 | 100% | ❌ 13 pts to go |
| P10 | 2125 | 39.2% | 39.2% | +3.7 | 70% | ❌ 31 pts to go |
| P11 | 1801 | 59.1% | 59.1% | +6.6 | 75% | ❌ 16 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152628 | 40.2% | 40.2% | +13.3 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 21.5% | 21.5% | +4.4 | n/a | no target |
| P01T | 227 | 65.2% | 65.2% | +11.6 | n/a | no target |
| P01_GOLD | 630 | 48.7% | 48.7% | -1.1 | 60% | ❌ 11 pts to go |
| P02 | 464 | 56.2% | 56.2% | +0.0 | 60% | 🟡 4 pts to go |
| P03 | 265 | 52.1% | 52.1% | -3.0 | 60% | 🟡 8 pts to go |
| P04 | 3584 | 42.8% | 42.8% | +0.7 | 55% | ❌ 12 pts to go |
| P05 | 423 | 22.9% | 22.9% | -1.7 | 50% | ❌ 27 pts to go |
| P06M | 21978 | 9.4% | 9.4% | +2.6 | n/a | no target |
| P06T | 59807 | 67.9% | 67.9% | +17.0 | n/a | no target |
| P06 | 273 | 48.4% | 48.4% | +0.8 | n/a | no target |
| P07 | 787 | 40.3% | 40.3% | -0.6 | 55% | ❌ 15 pts to go |
| P08 | 29136 | 33.0% | 33.0% | -3.2 | 50% | ❌ 17 pts to go |
| P09 | 277 | 72.6% | 72.6% | +0.3 | 70% | ✅ met |
| P10 | 2125 | 48.1% | 48.1% | +1.3 | 55% | 🟡 7 pts to go |
| P11 | 1801 | 59.3% | 59.3% | +7.1 | 50% | ✅ met |
| P12 | 10 | 90.0% | 90.0% | +3.3 | n/a | no target |
| P13 | 152628 | 3.2% | 3.2% | -0.2 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 32.9% | 32.9% | -17.5 | n/a | no target |
| P01T | 227 | 79.3% | 79.3% | +4.8 | n/a | no target |
| P01_GOLD | 630 | 50.3% | 50.3% | -0.2 | 70% | ❌ 20 pts to go |
| P02 | 464 | 57.1% | 57.1% | -1.1 | 70% | ❌ 13 pts to go |
| P03 | 265 | 50.2% | 50.2% | -1.1 | 70% | ❌ 20 pts to go |
| P04 | 3584 | 55.1% | 55.1% | +1.0 | 65% | 🟡 10 pts to go |
| P05 | 423 | 29.1% | 29.1% | +0.7 | 60% | ❌ 31 pts to go |
| P06M | 21978 | 27.8% | 27.8% | -8.8 | n/a | no target |
| P06T | 59807 | 82.7% | 82.7% | +2.7 | n/a | no target |
| P06 | 273 | 69.6% | 69.6% | +0.7 | 40% | ✅ met |
| P07 | 787 | 64.8% | 64.8% | -0.1 | 85% | ❌ 20 pts to go |
| P08 | 29136 | 64.0% | 64.0% | -1.3 | 85% | ❌ 21 pts to go |
| P09 | 277 | 56.7% | 56.7% | -2.6 | 85% | ❌ 28 pts to go |
| P10 | 2125 | 66.1% | 66.1% | +2.6 | 85% | ❌ 19 pts to go |
| P11 | 1801 | 68.4% | 68.4% | +6.5 | 75% | 🟡 7 pts to go |
| P12 | 10 | 40.0% | 40.0% | +13.3 | n/a | no target |
| P13 | 152628 | 91.8% | 91.8% | +0.6 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 37.4% | 37.4% | -19.2 | n/a | no target |
| P01T | 227 | 98.2% | 98.2% | +0.8 | n/a | no target |
| P01_GOLD | 630 | 78.6% | 78.6% | -1.0 | 90% | ❌ 11 pts to go |
| P02 | 464 | 82.1% | 82.1% | -1.8 | 90% | 🟡 8 pts to go |
| P03 | 265 | 85.3% | 85.3% | -2.5 | 90% | 🟡 5 pts to go |
| P04 | 3584 | 82.9% | 82.9% | -1.5 | 85% | 🟡 2 pts to go |
| P05 | 423 | 44.7% | 44.7% | -0.1 | 70% | ❌ 25 pts to go |
| P06M | 21978 | 33.5% | 33.5% | -10.1 | n/a | no target |
| P06T | 59807 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 273 | 99.3% | 99.3% | +0.0 | 50% | ✅ met |
| P07 | 787 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P08 | 29136 | 99.9% | 99.9% | +0.1 | 100% | 🟡 0 pts to go |
| P09 | 277 | 78.3% | 78.3% | -1.5 | 100% | ❌ 22 pts to go |
| P10 | 2125 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1801 | 97.9% | 97.9% | +0.6 | 100% | 🟡 2 pts to go |
| P12 | 10 | 60.0% | 60.0% | +6.7 | n/a | no target |
| P13 | 152628 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 15.4% | 15.4% | -0.1 | n/a | no target |
| P01T | 227 | 59.5% | 59.5% | -5.6 | n/a | no target |
| P01_GOLD | 630 | 43.2% | 43.2% | -0.3 | 70% | ❌ 27 pts to go |
| P02 | 464 | 47.4% | 47.4% | -1.3 | 75% | ❌ 28 pts to go |
| P03 | 265 | 44.5% | 44.5% | +1.2 | 75% | ❌ 30 pts to go |
| P04 | 3584 | 38.6% | 38.6% | -0.1 | 70% | ❌ 31 pts to go |
| P05 | 423 | 21.5% | 21.5% | -0.5 | 55% | ❌ 34 pts to go |
| P06M | 21978 | 5.9% | 5.9% | +1.1 | n/a | no target |
| P06T | 59807 | 47.4% | 47.4% | -14.7 | n/a | no target |
| P06 | 273 | 52.0% | 52.0% | +5.1 | n/a | no target |
| P07 | 787 | 51.5% | 51.5% | +1.5 | 70% | ❌ 18 pts to go |
| P08 | 29136 | 54.3% | 54.3% | -0.5 | 75% | ❌ 21 pts to go |
| P09 | 277 | 47.7% | 47.7% | -1.5 | 85% | ❌ 37 pts to go |
| P10 | 2125 | 44.4% | 44.4% | +0.8 | 80% | ❌ 36 pts to go |
| P11 | 1801 | 53.3% | 53.3% | -1.0 | 70% | ❌ 17 pts to go |
| P12 | 10 | 30.0% | 30.0% | -10.0 | n/a | no target |
| P13 | 152628 | 5.5% | 5.5% | +0.3 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 37.4% | 37.4% | -19.2 | n/a | no target |
| P01T | 227 | 96.5% | 96.5% | +1.7 | n/a | no target |
| P01_GOLD | 630 | 72.9% | 72.9% | -0.9 | 90% | ❌ 17 pts to go |
| P02 | 464 | 76.9% | 76.9% | -2.1 | 90% | ❌ 13 pts to go |
| P03 | 265 | 81.9% | 81.9% | -1.4 | 90% | 🟡 8 pts to go |
| P04 | 3584 | 77.9% | 77.9% | +1.5 | 85% | 🟡 7 pts to go |
| P05 | 423 | 43.0% | 43.0% | -0.1 | 75% | ❌ 32 pts to go |
| P06M | 21978 | 33.4% | 33.4% | -9.9 | n/a | no target |
| P06T | 59807 | 98.3% | 98.3% | +1.6 | n/a | no target |
| P06 | 273 | 90.1% | 90.1% | -0.4 | n/a | no target |
| P07 | 787 | 91.4% | 91.4% | -1.1 | 100% | 🟡 9 pts to go |
| P08 | 29136 | 87.2% | 87.2% | -3.6 | 100% | ❌ 13 pts to go |
| P09 | 277 | 66.8% | 66.8% | +0.7 | n/a | no target |
| P10 | 2125 | 90.3% | 90.3% | +3.5 | 100% | 🟡 10 pts to go |
| P11 | 1801 | 90.2% | 90.2% | +2.5 | n/a | no target |
| P12 | 10 | 60.0% | 60.0% | +13.3 | n/a | no target |
| P13 | 152628 | 69.7% | 69.7% | +4.5 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 36.6% | 36.6% | -9.9 | n/a | no target · QC vendors: 48 rows, 100.0% filled |
| P01T | 227 | 18.9% | 18.9% | +9.5 | n/a | no target · QC vendors: 33 rows, 87.9% filled |
| P01_GOLD | 630 | 43.0% | 43.0% | -0.8 | 95% | ❌ 52 pts to go · QC vendors: 49 rows, 98.0% filled |
| P02 | 464 | 56.5% | 56.5% | +0.9 | 95% | ❌ 38 pts to go · QC vendors: 111 rows, 100.0% filled |
| P03 | 265 | 42.3% | 42.3% | -3.7 | 95% | ❌ 53 pts to go · QC vendors: 18 rows, 100.0% filled |
| P04 | 3584 | 32.4% | 32.4% | +0.2 | 95% | ❌ 63 pts to go · QC vendors: 600 rows, 98.0% filled |
| P05 | 423 | 14.2% | 14.2% | +0.2 | n/a | no target · QC vendors: 36 rows, 100.0% filled |
| P06M | 21978 | 37.8% | 37.8% | -5.0 | n/a | no target · QC vendors: 6609 rows, 99.9% filled |
| P06T | 59807 | 30.6% | 30.6% | +25.3 | n/a | no target · QC vendors: 18597 rows, 95.7% filled |
| P06 | 273 | 7.3% | 7.3% | -1.1 | n/a | no target · QC vendors: 12 rows, 66.7% filled |
| P07 | 787 | 7.2% | 7.2% | +0.9 | n/a | no target · QC vendors: 47 rows, 78.7% filled |
| P08 | 29136 | 7.2% | 7.2% | +0.6 | n/a | no target · QC vendors: 1730 rows, 94.9% filled |
| P09 | 277 | 74.0% | 74.0% | -2.9 | 95% | ❌ 21 pts to go · QC vendors: 100 rows, 100.0% filled |
| P10 | 2125 | 15.7% | 15.7% | +0.1 | n/a | no target · QC vendors: 202 rows, 92.6% filled |
| P11 | 1801 | 19.7% | 19.7% | +4.9 | n/a | no target · QC vendors: 298 rows, 94.6% filled |
| P12 | 10 | 80.0% | 80.0% | +6.7 | n/a | no target · QC vendors: 2 rows, 100.0% filled |
| P13 | 152628 | 22.2% | 22.2% | -4.0 | n/a | no target · QC vendors: 33909 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 45.9% | 45.9% | -13.0 | n/a | no target · vendors with a registry record: 113 rows, 100.0% filled |
| P01T | 227 | 59.5% | 59.5% | +8.5 | n/a | no target · vendors with a registry record: 135 rows, 100.0% filled |
| P01_GOLD | 630 | 80.8% | 80.8% | -0.7 | 100% | ❌ 19 pts to go · vendors with a registry record: 509 rows, 100.0% filled |
| P02 | 464 | 78.4% | 78.4% | +0.9 | 100% | ❌ 22 pts to go · vendors with a registry record: 364 rows, 100.0% filled |
| P03 | 265 | 78.1% | 78.1% | -2.9 | 100% | ❌ 22 pts to go · vendors with a registry record: 207 rows, 100.0% filled |
| P04 | 3584 | 53.8% | 53.8% | +4.1 | 100% | ❌ 46 pts to go · vendors with a registry record: 1929 rows, 100.0% filled |
| P05 | 423 | 62.9% | 62.9% | -0.4 | n/a | no target · vendors with a registry record: 266 rows, 100.0% filled |
| P06M | 21978 | 41.5% | 41.5% | -4.4 | n/a | no target · vendors with a registry record: 9110 rows, 100.0% filled |
| P06T | 59807 | 67.6% | 67.6% | +11.4 | n/a | no target · vendors with a registry record: 40407 rows, 100.0% filled |
| P06 | 273 | 39.9% | 39.9% | -1.5 | n/a | no target · vendors with a registry record: 109 rows, 100.0% filled |
| P07 | 787 | 33.4% | 33.4% | +1.1 | n/a | no target · vendors with a registry record: 263 rows, 100.0% filled |
| P08 | 29136 | 31.0% | 31.0% | +0.6 | n/a | no target · vendors with a registry record: 9022 rows, 100.0% filled |
| P09 | 277 | 89.9% | 89.9% | -0.7 | n/a | no target · vendors with a registry record: 249 rows, 100.0% filled |
| P10 | 2125 | 40.1% | 40.1% | +3.9 | n/a | no target · vendors with a registry record: 853 rows, 100.0% filled |
| P11 | 1801 | 59.9% | 59.9% | +6.3 | n/a | no target · vendors with a registry record: 1078 rows, 100.0% filled |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 10 rows, 100.0% filled |
| P13 | 152628 | 40.2% | 40.2% | +13.3 | n/a | no target · vendors with a registry record: 61409 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 96.3% | 96.3% | +2.5 | 90% | ✅ met |
| P01T | 227 | 70.5% | 70.5% | -1.9 | 90% | ❌ 20 pts to go |
| P01_GOLD | 630 | 87.5% | 87.5% | -0.2 | 95% | 🟡 8 pts to go |
| P02 | 464 | 88.1% | 88.1% | +0.3 | 95% | 🟡 7 pts to go |
| P03 | 265 | 82.6% | 82.6% | -1.8 | 85% | 🟡 2 pts to go |
| P04 | 3584 | 64.4% | 64.4% | +1.4 | 90% | ❌ 26 pts to go |
| P05 | 423 | 77.8% | 77.8% | -1.3 | 75% | ✅ met |
| P06M | 21978 | 93.8% | 93.8% | +2.2 | n/a | no target |
| P06T | 59807 | 36.9% | 36.9% | -0.4 | n/a | no target |
| P06 | 273 | 72.5% | 72.5% | -1.1 | 80% | 🟡 8 pts to go |
| P07 | 787 | 58.6% | 58.7% | -1.2 | 80% | ❌ 21 pts to go |
| P08 | 29136 | 52.3% | 52.3% | -2.1 | 75% | ❌ 23 pts to go |
| P09 | 277 | 75.1% | 75.1% | -1.8 | 95% | ❌ 20 pts to go |
| P10 | 2125 | 46.8% | 46.9% | +0.1 | 70% | ❌ 23 pts to go |
| P11 | 1801 | 31.7% | 31.7% | +0.4 | 65% | ❌ 33 pts to go |
| P12 | 10 | 80.0% | 80.0% | +0.0 | 80% | ✅ met |
| P13 | 152628 | 45.6% | 45.6% | -1.9 | 60% | ❌ 14 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 18.7% | 18.7% | -1.5 | 50% | ❌ 31 pts to go |
| P01T | 227 | 15.9% | 15.9% | -0.2 | n/a | no target |
| P01_GOLD | 630 | 19.4% | 19.4% | -0.1 | 40% | ❌ 21 pts to go |
| P02 | 464 | 20.3% | 20.3% | +1.2 | 40% | ❌ 20 pts to go |
| P03 | 265 | 20.4% | 20.4% | -0.9 | 40% | ❌ 20 pts to go |
| P04 | 3584 | 16.2% | 16.2% | +1.0 | 40% | ❌ 24 pts to go |
| P05 | 423 | 20.8% | 20.8% | +3.3 | 25% | 🟡 4 pts to go |
| P06M | 21978 | 20.7% | 20.7% | +9.1 | n/a | no target |
| P06T | 59807 | 7.5% | 7.5% | +0.6 | n/a | no target |
| P06 | 273 | 17.9% | 17.9% | +5.1 | 35% | ❌ 17 pts to go |
| P07 | 787 | 19.7% | 19.7% | +5.6 | 35% | ❌ 15 pts to go |
| P08 | 29136 | 18.4% | 18.4% | +3.0 | 35% | ❌ 17 pts to go |
| P09 | 277 | 16.6% | 16.6% | +0.3 | n/a | no target |
| P10 | 2125 | 7.1% | 7.1% | +0.4 | 30% | ❌ 23 pts to go |
| P11 | 1801 | 6.5% | 6.5% | -0.9 | n/a | no target |
| P12 | 10 | 20.0% | 20.0% | +13.3 | n/a | no target |
| P13 | 152628 | 12.5% | 12.5% | +0.2 | 30% | ❌ 18 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 227 | 85.0% | 85.0% | +0.6 | 100% | ❌ 15 pts to go |
| P01_GOLD | 630 | 90.8% | 90.8% | +0.1 | 100% | 🟡 9 pts to go |
| P02 | 464 | 96.6% | 96.6% | +1.1 | 100% | 🟡 3 pts to go |
| P03 | 265 | 89.1% | 89.1% | -0.3 | 100% | ❌ 11 pts to go |
| P04 | 3584 | 72.7% | 72.7% | +1.3 | 100% | ❌ 27 pts to go |
| P05 | 423 | 90.1% | 90.1% | +0.8 | 100% | 🟡 10 pts to go |
| P06M | 21978 | 99.3% | 99.3% | +0.1 | n/a | no target |
| P06T | 59807 | 58.6% | 58.7% | -0.7 | n/a | no target |
| P06 | 273 | 82.1% | 82.1% | +3.3 | 95% | ❌ 13 pts to go |
| P07 | 787 | 84.6% | 84.6% | +3.4 | 95% | ❌ 10 pts to go |
| P08 | 29136 | 83.9% | 83.9% | +5.6 | 95% | ❌ 11 pts to go |
| P09 | 277 | 96.4% | 96.4% | +0.3 | 100% | 🟡 4 pts to go |
| P10 | 2125 | 54.6% | 54.7% | +0.2 | 95% | ❌ 40 pts to go |
| P11 | 1801 | 60.8% | 60.8% | +11.4 | 80% | ❌ 19 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 152628 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 72.0% | 72.0% | -14.0 | n/a | no target |
| P01T | 227 | 74.9% | 74.9% | +6.7 | n/a | no target |
| P01_GOLD | 630 | 73.2% | 73.2% | +0.2 | 90% | ❌ 17 pts to go |
| P02 | 464 | 79.1% | 79.1% | +1.2 | 95% | ❌ 16 pts to go |
| P03 | 265 | 74.0% | 74.0% | -0.9 | 95% | ❌ 21 pts to go |
| P04 | 3584 | 69.6% | 69.6% | +0.7 | 95% | ❌ 25 pts to go |
| P05 | 423 | 72.6% | 72.6% | -0.9 | 90% | ❌ 17 pts to go |
| P06M | 21978 | 77.8% | 77.8% | -9.1 | n/a | no target |
| P06T | 59807 | 58.6% | 58.6% | +1.4 | n/a | no target |
| P06 | 273 | 66.3% | 66.3% | -2.2 | 95% | ❌ 29 pts to go |
| P07 | 787 | 60.7% | 60.7% | -4.1 | 90% | ❌ 29 pts to go |
| P08 | 29136 | 60.0% | 60.0% | -7.8 | 95% | ❌ 35 pts to go |
| P09 | 277 | 85.9% | 85.9% | -1.1 | 100% | ❌ 14 pts to go |
| P10 | 2125 | 53.8% | 53.8% | -1.5 | 95% | ❌ 41 pts to go |
| P11 | 1801 | 30.8% | 30.8% | +1.9 | 75% | ❌ 44 pts to go |
| P12 | 10 | 80.0% | 80.0% | -13.3 | n/a | no target |
| P13 | 152628 | 67.9% | 67.9% | -2.9 | 95% | ❌ 27 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 84.6% | 84.6% | -3.0 | n/a | no target |
| P01T | 227 | 91.2% | 91.2% | +7.9 | 95% | 🟡 4 pts to go |
| P01_GOLD | 630 | 84.9% | 84.9% | +0.1 | 90% | 🟡 5 pts to go |
| P02 | 464 | 90.9% | 90.9% | +0.3 | 95% | 🟡 4 pts to go |
| P03 | 265 | 83.4% | 83.4% | -2.2 | 95% | ❌ 12 pts to go |
| P04 | 3584 | 91.6% | 91.6% | +2.4 | 90% | ✅ met |
| P05 | 423 | 92.4% | 92.4% | -0.7 | 95% | 🟡 3 pts to go |
| P06M | 21978 | 86.5% | 86.5% | -6.7 | n/a | no target |
| P06T | 59807 | 84.7% | 84.7% | +9.8 | n/a | no target |
| P06 | 273 | 86.8% | 86.8% | -5.5 | 100% | ❌ 13 pts to go |
| P07 | 787 | 85.6% | 85.6% | -6.6 | 100% | ❌ 14 pts to go |
| P08 | 29136 | 80.1% | 80.1% | -12.2 | 100% | ❌ 20 pts to go |
| P09 | 277 | 74.0% | 74.0% | +1.0 | n/a | no target |
| P10 | 2125 | 94.4% | 94.4% | +3.1 | 100% | 🟡 6 pts to go |
| P11 | 1801 | 51.1% | 51.1% | +9.2 | 80% | ❌ 29 pts to go |
| P12 | 10 | 90.0% | 90.0% | -10.0 | n/a | no target |
| P13 | 152628 | 80.8% | 80.8% | -2.9 | 95% | ❌ 14 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 3.3% | 3.3% | +0.2 | n/a | no target |
| P01T | 227 | 8.8% | 8.8% | -0.6 | n/a | no target |
| P01_GOLD | 630 | 13.8% | 13.8% | -0.4 | 25% | ❌ 11 pts to go |
| P02 | 464 | 25.0% | 25.0% | -0.3 | 40% | ❌ 15 pts to go |
| P03 | 265 | 8.7% | 8.7% | -0.4 | 20% | ❌ 11 pts to go |
| P04 | 3584 | 3.7% | 3.7% | +0.2 | 20% | ❌ 16 pts to go |
| P05 | 423 | 3.3% | 3.3% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 21978 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 59807 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06 | 273 | 5.5% | 5.5% | +0.4 | n/a | no target |
| P07 | 787 | 8.0% | 8.0% | -0.5 | n/a | no target |
| P08 | 29136 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P09 | 277 | 8.3% | 8.3% | +0.5 | n/a | no target |
| P10 | 2125 | 0.8% | 0.8% | +0.0 | n/a | no target |
| P11 | 1801 | 0.7% | 0.7% | -0.3 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | -6.7 | n/a | no target |
| P13 | 152628 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 16.3% | 16.3% | -2.3 | n/a | no target |
| P01T | 227 | 19.4% | 19.4% | -3.0 | 70% | ❌ 51 pts to go |
| P01_GOLD | 630 | 43.7% | 43.7% | +0.2 | 80% | ❌ 36 pts to go |
| P02 | 464 | 57.8% | 57.8% | +0.5 | 90% | ❌ 32 pts to go |
| P03 | 265 | 19.2% | 19.2% | +0.6 | 60% | ❌ 41 pts to go |
| P04 | 3584 | 21.4% | 21.4% | -0.2 | 85% | ❌ 64 pts to go |
| P05 | 423 | 11.6% | 11.6% | +0.0 | 50% | ❌ 38 pts to go |
| P06M | 21978 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06T | 59807 | 0.5% | 0.5% | -0.2 | n/a | no target |
| P06 | 273 | 13.6% | 13.6% | -1.8 | n/a | no target |
| P07 | 787 | 9.0% | 9.0% | -1.5 | n/a | no target |
| P08 | 29136 | 0.5% | 0.5% | -0.1 | n/a | no target |
| P09 | 277 | 74.7% | 74.7% | -3.2 | 95% | ❌ 20 pts to go |
| P10 | 2125 | 1.6% | 1.6% | -0.1 | n/a | no target |
| P11 | 1801 | 13.6% | 13.6% | -3.1 | n/a | no target |
| P12 | 10 | 30.0% | 30.0% | +3.3 | n/a | no target |
| P13 | 152628 | 0.3% | 0.3% | -0.2 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 5.7% | 5.7% | -0.5 | n/a | no target |
| P01T | 227 | 9.7% | 9.7% | -0.7 | n/a | no target |
| P01_GOLD | 630 | 34.6% | 34.6% | +0.6 | 70% | ❌ 35 pts to go |
| P02 | 464 | 39.4% | 39.4% | +0.3 | 75% | ❌ 36 pts to go |
| P03 | 265 | 19.6% | 19.6% | +1.0 | 55% | ❌ 35 pts to go |
| P04 | 3584 | 21.4% | 21.4% | -0.2 | 75% | ❌ 54 pts to go |
| P05 | 423 | 10.6% | 10.6% | -0.1 | 50% | ❌ 39 pts to go |
| P06M | 21978 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06T | 59807 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 273 | 5.9% | 5.9% | +0.0 | n/a | no target |
| P07 | 787 | 4.4% | 4.4% | -0.8 | n/a | no target |
| P08 | 29136 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 277 | 71.5% | 71.5% | -3.7 | 95% | ❌ 24 pts to go |
| P10 | 2125 | 0.8% | 0.8% | -0.1 | n/a | no target |
| P11 | 1801 | 13.3% | 13.3% | -3.1 | n/a | no target |
| P12 | 10 | 20.0% | 20.0% | +0.0 | n/a | no target |
| P13 | 152628 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 7.7% | 7.7% | -0.1 | n/a | no target |
| P01T | 227 | 8.4% | 8.4% | +0.1 | n/a | no target |
| P01_GOLD | 630 | 57.9% | 58.1% | -0.1 | 80% | ❌ 22 pts to go |
| P02 | 464 | 45.5% | 45.7% | -0.2 | 75% | ❌ 30 pts to go |
| P03 | 265 | 37.0% | 37.0% | -0.3 | 70% | ❌ 33 pts to go |
| P04 | 3584 | 21.3% | 21.7% | +0.2 | 70% | ❌ 49 pts to go |
| P05 | 423 | 14.4% | 14.4% | +0.2 | 50% | ❌ 36 pts to go |
| P06M | 21978 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06T | 59807 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06 | 273 | 13.6% | 13.6% | -2.9 | n/a | no target |
| P07 | 787 | 1.1% | 1.1% | -0.9 | n/a | no target |
| P08 | 29136 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P09 | 277 | 48.7% | 48.7% | +2.1 | 80% | ❌ 31 pts to go |
| P10 | 2125 | 1.1% | 1.2% | -0.1 | n/a | no target |
| P11 | 1801 | 4.7% | 4.8% | -2.1 | n/a | no target |
| P12 | 10 | 30.0% | 30.0% | -10.0 | n/a | no target |
| P13 | 152628 | 0.1% | 0.1% | -0.1 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 15.0% | 15.0% | -3.6 | n/a | no target |
| P01T | 227 | 19.4% | 19.4% | -2.0 | 60% | ❌ 41 pts to go |
| P01_GOLD | 630 | 62.7% | 62.7% | -0.7 | 70% | 🟡 7 pts to go |
| P02 | 464 | 39.0% | 39.0% | -0.7 | 50% | ❌ 11 pts to go |
| P03 | 265 | 47.2% | 47.2% | -1.1 | 55% | 🟡 8 pts to go |
| P04 | 3584 | 12.6% | 12.6% | +0.4 | 40% | ❌ 27 pts to go |
| P05 | 423 | 16.5% | 16.5% | -0.6 | 40% | ❌ 24 pts to go |
| P06M | 21978 | 2.8% | 2.8% | +0.6 | n/a | no target |
| P06T | 59807 | 1.5% | 1.5% | -0.2 | n/a | no target |
| P06 | 273 | 18.3% | 18.3% | -3.7 | n/a | no target |
| P07 | 787 | 5.2% | 5.2% | -1.4 | n/a | no target |
| P08 | 29136 | 2.2% | 2.2% | -0.7 | n/a | no target |
| P09 | 277 | 5.8% | 5.8% | -0.1 | n/a | no target |
| P10 | 2125 | 5.1% | 5.1% | +0.5 | n/a | no target |
| P11 | 1801 | 4.1% | 4.1% | -1.1 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | -6.7 | n/a | no target |
| P13 | 152628 | 0.7% | 0.7% | -0.3 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 22.0% | 22.0% | +0.3 | n/a | no target |
| P01T | 227 | 27.3% | 27.3% | -1.3 | 65% | ❌ 38 pts to go |
| P01_GOLD | 630 | 68.4% | 68.4% | -0.6 | 70% | 🟡 2 pts to go |
| P02 | 464 | 23.7% | 23.7% | -0.5 | 50% | ❌ 26 pts to go |
| P03 | 265 | 50.2% | 50.2% | -2.3 | 60% | 🟡 10 pts to go |
| P04 | 3584 | 5.6% | 5.6% | +0.2 | 40% | ❌ 34 pts to go |
| P05 | 423 | 19.9% | 19.9% | +0.2 | 45% | ❌ 25 pts to go |
| P06M | 21978 | 1.7% | 1.7% | +0.3 | n/a | no target |
| P06T | 59807 | 0.6% | 0.6% | -0.1 | n/a | no target |
| P06 | 273 | 29.7% | 29.7% | -4.7 | n/a | no target |
| P07 | 787 | 5.3% | 5.3% | -1.6 | n/a | no target |
| P08 | 29136 | 0.9% | 0.9% | -0.4 | n/a | no target |
| P09 | 277 | 10.8% | 10.8% | +1.0 | n/a | no target |
| P10 | 2125 | 3.3% | 3.3% | +0.2 | n/a | no target |
| P11 | 1801 | 3.7% | 3.7% | -1.4 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | -6.7 | n/a | no target |
| P13 | 152628 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 11.8% | 11.8% | -0.6 | n/a | no target |
| P01T | 227 | 12.3% | 12.3% | -1.2 | n/a | no target |
| P01_GOLD | 630 | 49.7% | 49.7% | -0.1 | 50% | 🟡 0 pts to go |
| P02 | 464 | 38.4% | 38.4% | +1.1 | n/a | no target |
| P03 | 265 | 51.3% | 51.3% | -0.8 | 60% | 🟡 9 pts to go |
| P04 | 3584 | 12.7% | 12.7% | +0.8 | n/a | no target |
| P05 | 423 | 15.1% | 15.1% | -0.1 | n/a | no target |
| P06M | 21978 | 0.8% | 0.8% | +0.3 | n/a | no target |
| P06T | 59807 | 0.3% | 0.3% | -0.1 | n/a | no target |
| P06 | 273 | 20.9% | 20.9% | -4.7 | n/a | no target |
| P07 | 787 | 6.1% | 6.1% | -2.2 | n/a | no target |
| P08 | 29136 | 0.4% | 0.4% | -0.2 | n/a | no target |
| P09 | 277 | 20.9% | 20.9% | +3.3 | n/a | no target |
| P10 | 2125 | 2.5% | 2.5% | +0.1 | n/a | no target |
| P11 | 1801 | 2.8% | 2.8% | -1.9 | n/a | no target |
| P12 | 10 | 20.0% | 20.0% | +6.7 | n/a | no target |
| P13 | 152628 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 8.9% | 8.9% | -2.7 | 15% | 🟡 6 pts to go |
| P01T | 227 | 12.8% | 12.8% | +0.3 | 15% | 🟡 2 pts to go |
| P01_GOLD | 630 | 35.1% | 35.1% | -0.2 | 40% | 🟡 5 pts to go |
| P02 | 464 | 12.1% | 12.3% | -0.8 | 25% | ❌ 13 pts to go |
| P03 | 265 | 15.8% | 15.8% | -1.7 | 25% | 🟡 9 pts to go |
| P04 | 3584 | 2.8% | 2.8% | +0.1 | 15% | ❌ 12 pts to go |
| P05 | 423 | 6.6% | 6.6% | +0.0 | 15% | 🟡 8 pts to go |
| P06M | 21978 | 0.8% | 0.8% | -0.1 | 15% | ❌ 14 pts to go |
| P06T | 59807 | 0.7% | 0.7% | +0.2 | 15% | ❌ 14 pts to go |
| P06 | 273 | 9.5% | 9.5% | -1.1 | 15% | 🟡 6 pts to go |
| P07 | 787 | 3.4% | 3.4% | -0.9 | 15% | ❌ 12 pts to go |
| P08 | 29136 | 0.5% | 0.5% | -0.1 | 15% | ❌ 14 pts to go |
| P09 | 277 | 1.1% | 1.1% | +0.1 | 15% | ❌ 14 pts to go |
| P10 | 2125 | 1.4% | 1.4% | +0.1 | 15% | ❌ 14 pts to go |
| P11 | 1801 | 1.3% | 1.3% | -0.2 | 15% | ❌ 14 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 152628 | 0.6% | 0.6% | -0.1 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 5.7% | 5.7% | +0.3 | 15% | 🟡 9 pts to go |
| P01T | 227 | 11.0% | 11.0% | -0.5 | 25% | ❌ 14 pts to go |
| P01_GOLD | 630 | 28.9% | 28.9% | -0.3 | 25% | ✅ met |
| P02 | 464 | 25.4% | 25.4% | +0.1 | 15% | ✅ met |
| P03 | 265 | 22.3% | 22.3% | +0.2 | 15% | ✅ met |
| P04 | 3584 | 4.0% | 4.0% | +0.0 | 15% | ❌ 11 pts to go |
| P05 | 423 | 11.3% | 11.3% | +0.2 | 15% | 🟡 4 pts to go |
| P06M | 21978 | 0.7% | 0.7% | +0.2 | 15% | ❌ 14 pts to go |
| P06T | 59807 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 273 | 7.7% | 7.7% | -0.7 | 15% | 🟡 7 pts to go |
| P07 | 787 | 1.9% | 1.9% | -1.0 | 15% | ❌ 13 pts to go |
| P08 | 29136 | 0.4% | 0.4% | -0.1 | 15% | ❌ 15 pts to go |
| P09 | 277 | 1.4% | 1.4% | +0.4 | 15% | ❌ 14 pts to go |
| P10 | 2125 | 1.6% | 1.6% | +0.0 | 15% | ❌ 13 pts to go |
| P11 | 1801 | 1.8% | 1.8% | -0.9 | 15% | ❌ 13 pts to go |
| P12 | 10 | 0.0% | 0.0% | -20.0 | 15% | ❌ 15 pts to go |
| P13 | 152628 | 0.1% | 0.1% | -0.1 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 1.6% | 1.6% | -0.7 | 20% | ❌ 18 pts to go |
| P01T | 227 | 3.1% | 3.1% | -1.1 | 20% | ❌ 17 pts to go |
| P01_GOLD | 630 | 4.3% | 4.3% | -0.2 | 20% | ❌ 16 pts to go |
| P02 | 464 | 1.7% | 1.7% | +0.2 | 20% | ❌ 18 pts to go |
| P03 | 265 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P04 | 3584 | 0.7% | 0.7% | +0.1 | 20% | ❌ 19 pts to go |
| P05 | 423 | 0.9% | 0.9% | -0.3 | 20% | ❌ 19 pts to go |
| P06M | 21978 | 0.1% | 0.1% | +0.1 | 20% | ❌ 20 pts to go |
| P06T | 59807 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 273 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P07 | 787 | 0.3% | 0.3% | -0.1 | 20% | ❌ 20 pts to go |
| P08 | 29136 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 277 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2125 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1801 | 0.1% | 0.1% | -0.2 | 20% | ❌ 20 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 152628 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 1.6% | 1.6% | +0.0 | 15% | ❌ 13 pts to go |
| P01T | 227 | 3.1% | 3.1% | +0.0 | 15% | ❌ 12 pts to go |
| P01_GOLD | 630 | 10.5% | 10.5% | +0.1 | 15% | 🟡 4 pts to go |
| P02 | 464 | 11.0% | 11.0% | -1.0 | 15% | 🟡 4 pts to go |
| P03 | 265 | 21.1% | 21.1% | +0.9 | 15% | ✅ met |
| P04 | 3584 | 2.3% | 2.3% | +0.0 | 15% | ❌ 13 pts to go |
| P05 | 423 | 2.8% | 2.8% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 21978 | 0.4% | 0.4% | +0.1 | 15% | ❌ 15 pts to go |
| P06T | 59807 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 273 | 4.0% | 4.0% | -1.1 | 15% | ❌ 11 pts to go |
| P07 | 787 | 1.3% | 1.3% | -0.3 | 15% | ❌ 14 pts to go |
| P08 | 29136 | 0.3% | 0.3% | -0.2 | 15% | ❌ 15 pts to go |
| P09 | 277 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2125 | 1.1% | 1.1% | +0.1 | 15% | ❌ 14 pts to go |
| P11 | 1801 | 0.8% | 0.8% | -0.4 | 15% | ❌ 14 pts to go |
| P12 | 10 | 0.0% | 0.0% | -6.7 | 15% | ❌ 15 pts to go |
| P13 | 152628 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 12.6% | 12.6% | -1.4 | 20% | 🟡 7 pts to go |
| P01T | 227 | 13.2% | 13.2% | -0.9 | 40% | ❌ 27 pts to go |
| P01_GOLD | 630 | 46.0% | 46.0% | -0.2 | 40% | ✅ met |
| P02 | 464 | 44.0% | 44.0% | +1.1 | 20% | ✅ met |
| P03 | 265 | 48.3% | 48.3% | -0.7 | 35% | ✅ met |
| P04 | 3584 | 14.9% | 14.9% | +0.7 | 20% | 🟡 5 pts to go |
| P05 | 423 | 15.6% | 15.6% | +0.2 | 20% | 🟡 4 pts to go |
| P06M | 21978 | 1.0% | 1.0% | +0.2 | 20% | ❌ 19 pts to go |
| P06T | 59807 | 0.6% | 0.6% | -0.1 | 20% | ❌ 19 pts to go |
| P06 | 273 | 21.6% | 21.6% | -3.7 | 20% | ✅ met |
| P07 | 787 | 6.6% | 6.6% | -2.0 | 20% | ❌ 13 pts to go |
| P08 | 29136 | 0.8% | 0.8% | -0.2 | 20% | ❌ 19 pts to go |
| P09 | 277 | 20.9% | 20.9% | +2.7 | 20% | ✅ met |
| P10 | 2125 | 3.8% | 3.8% | +0.1 | 20% | ❌ 16 pts to go |
| P11 | 1801 | 3.2% | 3.2% | -1.6 | 20% | ❌ 17 pts to go |
| P12 | 10 | 10.0% | 10.0% | +3.3 | 20% | 🟡 10 pts to go |
| P13 | 152628 | 0.4% | 0.4% | -0.1 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 18.3% | 18.3% | -15.0 | n/a | no target |
| P01T | 227 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P01_GOLD | 630 | 71.9% | 71.9% | +2.4 | 95% | ❌ 23 pts to go |
| P02 | 464 | 65.9% | 65.9% | +3.0 | 95% | ❌ 29 pts to go |
| P03 | 265 | 57.4% | 57.4% | +4.2 | 90% | ❌ 33 pts to go |
| P04 | 3584 | 26.4% | 26.4% | +1.6 | 85% | ❌ 59 pts to go |
| P05 | 423 | 38.8% | 38.8% | +1.1 | 75% | ❌ 36 pts to go |
| P06M | 21978 | 28.6% | 28.6% | -7.5 | n/a | no target |
| P06T | 59807 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 787 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29136 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 277 | 89.5% | 89.5% | +1.2 | 100% | ❌ 10 pts to go |
| P10 | 2125 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1801 | 3.9% | 3.9% | -2.1 | 60% | ❌ 56 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152628 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 18.3% | 18.3% | -15.0 | n/a | no target |
| P01T | 227 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 630 | 73.7% | 73.7% | +0.9 | 100% | ❌ 26 pts to go |
| P02 | 464 | 68.1% | 68.1% | +1.8 | 100% | ❌ 32 pts to go |
| P03 | 265 | 60.0% | 60.0% | +1.1 | n/a | no target |
| P04 | 3584 | 26.9% | 26.9% | +1.4 | 95% | ❌ 68 pts to go |
| P05 | 423 | 34.5% | 34.5% | +1.1 | 80% | ❌ 46 pts to go |
| P06M | 21978 | 28.6% | 28.6% | -7.5 | n/a | no target |
| P06T | 59807 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 787 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29136 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 277 | 92.1% | 92.1% | +0.6 | 100% | 🟡 8 pts to go |
| P10 | 2125 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1801 | 4.1% | 4.1% | -2.3 | n/a | no target |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152628 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 84.1% | 84.1% | +4.3 | n/a | no target |
| P01T | 227 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P01_GOLD | 630 | 52.2% | 52.2% | +0.6 | 85% | ❌ 33 pts to go |
| P02 | 464 | 58.6% | 58.6% | +1.1 | 90% | ❌ 31 pts to go |
| P03 | 265 | 44.2% | 44.2% | +1.6 | 85% | ❌ 41 pts to go |
| P04 | 3584 | 28.9% | 28.9% | +1.0 | 90% | ❌ 61 pts to go |
| P05 | 423 | 32.9% | 32.9% | +0.2 | 75% | ❌ 42 pts to go |
| P06M | 21978 | 84.4% | 84.4% | -2.7 | n/a | no target |
| P06T | 59807 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 787 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29136 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 277 | 82.3% | 82.3% | -1.1 | 95% | ❌ 13 pts to go |
| P10 | 2125 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1801 | 3.4% | 3.4% | -2.0 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 152628 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 65.0% | 65.0% | -13.3 | n/a | no target |
| P01T | 227 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P01_GOLD | 630 | 52.1% | 52.1% | +0.3 | 85% | ❌ 33 pts to go |
| P02 | 464 | 52.6% | 52.6% | +0.0 | 90% | ❌ 37 pts to go |
| P03 | 265 | 44.2% | 44.2% | +0.5 | 85% | ❌ 41 pts to go |
| P04 | 3584 | 24.6% | 24.6% | +0.8 | 90% | ❌ 65 pts to go |
| P05 | 423 | 42.6% | 42.6% | -0.8 | 75% | ❌ 32 pts to go |
| P06M | 21978 | 69.1% | 69.1% | -8.7 | n/a | no target |
| P06T | 59807 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 787 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29136 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 277 | 0.4% | 0.4% | +0.1 | 95% | ❌ 95 pts to go |
| P10 | 2125 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1801 | 2.6% | 2.6% | -1.9 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 152628 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 95.1% | 95.1% | +5.2 | n/a | no target |
| P01T | 227 | 96.0% | 96.0% | +1.7 | n/a | no target |
| P01_GOLD | 630 | 85.4% | 85.6% | +0.1 | 100% | ❌ 15 pts to go |
| P02 | 464 | 77.6% | 77.6% | +1.2 | 100% | ❌ 22 pts to go |
| P03 | 265 | 91.7% | 91.7% | +0.4 | n/a | no target |
| P04 | 3584 | 50.5% | 50.5% | +1.7 | 95% | ❌ 44 pts to go |
| P05 | 423 | 77.3% | 77.3% | -0.2 | 95% | ❌ 18 pts to go |
| P06M | 21978 | 99.3% | 99.3% | +0.4 | n/a | no target |
| P06T | 59807 | 94.5% | 94.5% | +3.9 | n/a | no target |
| P06 | 273 | 20.9% | 20.9% | -2.2 | n/a | no target |
| P07 | 787 | 10.8% | 10.8% | -3.0 | n/a | no target |
| P08 | 29136 | 4.7% | 4.7% | -2.4 | n/a | no target |
| P09 | 277 | 98.2% | 98.2% | -0.5 | 100% | 🟡 2 pts to go |
| P10 | 2125 | 70.6% | 70.6% | -0.4 | n/a | no target |
| P11 | 1801 | 70.3% | 70.3% | +2.2 | n/a | no target |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152628 | 99.6% | 99.6% | -0.1 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 95.1% | 95.1% | +5.2 | n/a | no target |
| P01T | 227 | 96.0% | 96.0% | +1.7 | n/a | no target |
| P01_GOLD | 630 | 88.6% | 88.7% | +0.1 | 100% | ❌ 11 pts to go |
| P02 | 464 | 78.9% | 78.9% | +1.4 | 100% | ❌ 21 pts to go |
| P03 | 265 | 92.5% | 92.5% | +0.5 | n/a | no target |
| P04 | 3584 | 53.8% | 53.8% | +1.9 | 95% | ❌ 41 pts to go |
| P05 | 423 | 89.4% | 89.4% | -0.2 | 70% | ✅ met |
| P06M | 21978 | 99.3% | 99.3% | +0.4 | n/a | no target |
| P06T | 59807 | 94.5% | 94.5% | +3.9 | n/a | no target |
| P06 | 273 | 20.9% | 20.9% | -2.2 | n/a | no target |
| P07 | 787 | 10.8% | 10.8% | -3.0 | n/a | no target |
| P08 | 29136 | 4.7% | 4.7% | -2.4 | n/a | no target |
| P09 | 277 | 98.2% | 98.2% | -0.5 | 100% | 🟡 2 pts to go |
| P10 | 2125 | 70.6% | 70.6% | -0.4 | n/a | no target |
| P11 | 1801 | 70.3% | 70.3% | +2.1 | n/a | no target |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152628 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 227 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 630 | 16.8% | 16.8% | +0.0 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 368 rows, 28.8% filled |
| P02 | 464 | 10.3% | 10.3% | -0.9 | n/a | no target · rows from a source that publishes bids: 295 rows, 16.3% filled |
| P03 | 265 | 13.6% | 13.6% | +0.7 | n/a | no target · rows from a source that publishes bids: 142 rows, 25.4% filled |
| P04 | 3584 | 1.7% | 1.7% | +0.2 | n/a | no target · rows from a source that publishes bids: 880 rows, 7.0% filled |
| P05 | 423 | 2.6% | 2.6% | +0.0 | n/a | no target · rows from a source that publishes bids: 55 rows, 20.0% filled |
| P06M | 21978 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59807 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 787 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29136 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 277 | 4.0% | 4.0% | -0.2 | n/a | no target · rows from a source that publishes bids: 264 rows, 4.2% filled |
| P10 | 2125 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1801 | 0.4% | 0.4% | -0.5 | n/a | no target · rows from a source that publishes bids: 69 rows, 11.6% filled |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 10 rows, 0.0% filled |
| P13 | 152628 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 227 | 0.0% | 97.8% | +0.0 | n/a | no target |
| P01_GOLD | 630 | 53.3% | 82.2% | +0.1 | 90% | ❌ 37 pts to go |
| P02 | 464 | 52.8% | 86.4% | +0.4 | 90% | ❌ 37 pts to go |
| P03 | 265 | 45.7% | 80.0% | +1.2 | 90% | ❌ 44 pts to go |
| P04 | 3584 | 19.6% | 93.0% | +0.5 | 90% | ❌ 70 pts to go |
| P05 | 423 | 0.0% | 82.5% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 21978 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 59807 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 787 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 29136 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 277 | 2.9% | 4.7% | +0.6 | 90% | ❌ 87 pts to go |
| P10 | 2125 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1801 | 2.2% | 97.6% | -1.9 | n/a | no target |
| P12 | 10 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152628 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 227 | 0.9% | 98.7% | +0.4 | n/a | no target |
| P01_GOLD | 630 | 26.3% | 55.2% | +0.4 | 90% | ❌ 64 pts to go |
| P02 | 464 | 51.9% | 85.6% | +0.4 | n/a | no target |
| P03 | 265 | 25.3% | 59.6% | +1.0 | n/a | no target |
| P04 | 3584 | 21.3% | 94.7% | +0.3 | n/a | no target |
| P05 | 423 | 0.5% | 83.0% | +0.0 | n/a | no target |
| P06M | 21978 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 59807 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 787 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 29136 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 277 | 40.4% | 42.2% | -0.6 | n/a | no target |
| P10 | 2125 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1801 | 2.3% | 97.7% | -1.4 | n/a | no target |
| P12 | 10 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152628 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 227 | 2.2% | 100.0% | +0.1 | n/a | no target |
| P01_GOLD | 630 | 52.2% | 81.1% | +0.4 | 95% | ❌ 43 pts to go |
| P02 | 464 | 57.8% | 91.4% | +1.4 | n/a | no target |
| P03 | 265 | 49.8% | 84.2% | +3.0 | n/a | no target |
| P04 | 3584 | 22.1% | 95.4% | +0.9 | n/a | no target |
| P05 | 423 | 5.0% | 87.5% | +0.5 | n/a | no target |
| P06M | 21978 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 59807 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 273 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 787 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 29136 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 277 | 61.0% | 62.8% | -1.5 | n/a | no target |
| P10 | 2125 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1801 | 2.4% | 97.8% | -1.7 | n/a | no target |
| P12 | 10 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 152628 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 227 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 630 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 464 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 265 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3584 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 423 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 21978 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 59807 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 273 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 787 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 29136 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 277 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2125 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1801 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 152628 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 227 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 630 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 464 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 265 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3584 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 423 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 21978 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 59807 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 273 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 787 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 29136 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 277 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2125 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1801 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 152628 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 246 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 227 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 630 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 464 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 265 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3584 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 423 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 21978 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 59807 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 273 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 787 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 29136 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 277 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2125 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1801 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 152628 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |


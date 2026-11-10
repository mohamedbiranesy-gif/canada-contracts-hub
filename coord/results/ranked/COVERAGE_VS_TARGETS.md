# Coverage vs the downstream team's targets — 2026-11-10

Benchmarks (field × package with a numeric target): **102 of 438 met** (23.3%); 69 within 10 points; 267 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 18, P01T 93, P01_GOLD 625, P02 403, P03 209, P04 1570, P05 386, P06M 168, P06T 2983, P06 227, P07 449, P08 8926, P09 383, P10 2874, P11 607, P12 18, P13 48968

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 33.3% | 8 | reference to quote (PO / contract / vendor id) (18 rows) |
| P01T | 93 | 1.1% | 46.2% | 8 | reference to quote (PO / contract / vendor id) (88 rows) |
| P01_GOLD | 625 | 24.3% | 71.2% | 10 | payment terms (214 rows) |
| P02 | 403 | 8.9% | 62.8% | 9 | PO rule (298 rows) |
| P03 | 209 | 17.7% | 69.9% | 9 | PO rule (92 rows) |
| P04 | 1570 | 2.9% | 38.4% | 8 | PO rule (1415 rows) |
| P05 | 386 | 1.3% | 18.4% | 7 | payment terms (317 rows) |
| P06M | 168 | 0.0% | 5.4% | 7 | reference to quote (PO / contract / vendor id) (168 rows) |
| P06T | 2983 | 0.0% | 4.7% | 6 | reference to quote (PO / contract / vendor id) (2979 rows) |
| P06 | 227 | 0.0% | 9.7% | 6 | reference to quote (PO / contract / vendor id) (227 rows) |
| P07 | 449 | 0.0% | 3.3% | 5 | reference to quote (PO / contract / vendor id) (449 rows) |
| P08 | 8926 | 0.0% | 0.3% | 4 | reference to quote (PO / contract / vendor id) (8926 rows) |
| P09 | 383 | 1.0% | 44.6% | 8 | payment terms (357 rows) |
| P10 | 2874 | 0.0% | 0.8% | 5 | reference to quote (PO / contract / vendor id) (2871 rows) |
| P11 | 607 | 1.0% | 9.6% | 4 | PO rule (575 rows) |
| P12 | 18 | 0.0% | 44.4% | 8 | PO rule (17 rows) |
| P13 | 48968 | 0.0% | 0.0% | 6 | reference to quote (PO / contract / vendor id) (48968 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 18 | 5 | 3 | 10 | 0 | 0 | 77 |
| P01T | 93 | 27 | 40 | 26 | 0 | 0 | 80 |
| P01_GOLD | 625 | 231 | 186 | 208 | 0 | 0 | 82 |
| P02 | 403 | 0 | 183 | 220 | 0 | 0 | 66 |
| P03 | 209 | 0 | 0 | 202 | 7 | 0 | 58 |
| P04 | 1570 | 0 | 0 | 1520 | 50 | 0 | 53 |
| P05 | 386 | 15 | 29 | 325 | 17 | 0 | 51 |
| P06M | 168 | 0 | 5 | 159 | 4 | 0 | 51 |
| P06T | 2983 | 0 | 25 | 2731 | 227 | 0 | 49 |
| P06 | 227 | 20 | 32 | 175 | 0 | 0 | 71 |
| P07 | 449 | 0 | 16 | 405 | 28 | 0 | 53 |
| P08 | 8926 | 0 | 0 | 6122 | 2804 | 0 | 38 |
| P09 | 383 | 5 | 13 | 362 | 3 | 0 | 53 |
| P10 | 2874 | 4 | 14 | 2027 | 829 | 0 | 43 |
| P11 | 607 | 0 | 0 | 0 | 0 | 607 | 26 |
| P12 | 18 | 0 | 1 | 17 | 0 | 0 | 54 |
| P13 | 48968 | 5 | 21 | 42277 | 6665 | 0 | 45 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 18 | 7 | 38.9% | the buyer's PO / reference rule (10) |
| P01T | 93 | 53 | 57.0% | the buyer's PO / reference rule (24) |
| P01_GOLD | 625 | 464 | 74.2% | bill-to legal name and address (109) |
| P02 | 403 | 305 | 75.7% | the buyer's PO / reference rule (54) |
| P03 | 209 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (209) |
| P04 | 1570 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (1570) |
| P05 | 386 | 47 | 12.2% | a confirmed invoicing / AP or finance channel (298) |
| P06M | 168 | 2 | 1.2% | a confirmed invoicing / AP or finance channel (143) |
| P06T | 2983 | 16 | 0.5% | a confirmed invoicing / AP or finance channel (2894) |
| P06 | 227 | 32 | 14.1% | bill-to legal name and address (126) |
| P07 | 449 | 9 | 2.0% | bill-to legal name and address (193) |
| P08 | 8926 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (8926) |
| P09 | 383 | 50 | 13.1% | a confirmed invoicing / AP or finance channel (324) |
| P10 | 2874 | 10 | 0.3% | a confirmed invoicing / AP or finance channel (2732) |
| P11 | 607 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (607) |
| P12 | 18 | 5 | 27.8% | a confirmed invoicing / AP or finance channel (13) |
| P13 | 48968 | 10 | 0.0% | a confirmed invoicing / AP or finance channel (47796) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 18 | 7 | 38.9% | 9 | 0 | tax treatment (1) |
| P01T | 93 | 41 | 44.1% | 15 | 0 | the vendor's GST/HST number (BN9) (18) |
| P01_GOLD | 625 | 409 | 65.4% | 20 | 0 | the vendor's GST/HST number (BN9) (124) |
| P02 | 403 | 218 | 54.1% | 35 | 0 | the vendor's GST/HST number (BN9) (130) |
| P03 | 209 | 17 | 8.1% | 1 | 131 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (49) |
| P04 | 1570 | 43 | 2.7% | 10 | 707 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (772) |
| P05 | 386 | 22 | 5.7% | 10 | 95 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (194) |
| P06M | 168 | 3 | 1.8% | 18 | 81 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (59) |
| P06T | 2983 | 17 | 0.6% | 55 | 1278 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1555) |
| P06 | 227 | 15 | 6.6% | 22 | 0 | the vendor's GST/HST number (BN9) (101) |
| P07 | 449 | 7 | 1.6% | 32 | 18 | the vendor's GST/HST number (BN9) (173) |
| P08 | 8926 | 2 | 0.0% | 3 | 790 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (8101) |
| P09 | 383 | 46 | 12.0% | 1 | 147 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (166) |
| P10 | 2874 | 6 | 0.2% | 23 | 456 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2251) |
| P11 | 607 | 6 | 1.0% | 0 | 0 | a confirmed invoicing / AP or finance channel (590) |
| P12 | 18 | 3 | 16.7% | 0 | 6 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (7) |
| P13 | 48968 | 12 | 0.0% | 898 | 32571 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (15099) |
| **all** | 68907 | 874 | 1.3% | 1152 | 36280 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 13 | 0 | 0 | 0 | 0 | 1 | 0 | 10 | 11 | 1 |
| P01T | 66 | 0 | 0 | 0 | 2 | 6 | 1 | 29 | 40 | 30 |
| P01_GOLD | 394 | 0 | 0 | 0 | 11 | 94 | 34 | 192 | 227 | 60 |
| P02 | 403 | 0 | 403 | 0 | 4 | 38 | 8 | 298 | 227 | 22 |
| P03 | 209 | 0 | 209 | 0 | 2 | 34 | 11 | 92 | 94 | 25 |
| P04 | 1570 | 0 | 1570 | 0 | 12 | 329 | 93 | 1415 | 1210 | 106 |
| P05 | 371 | 0 | 321 | 0 | 8 | 95 | 44 | 304 | 319 | 56 |
| P06M | 168 | 0 | 168 | 0 | 0 | 19 | 31 | 156 | 140 | 0 |
| P06T | 2983 | 0 | 2983 | 0 | 499 | 1377 | 380 | 2877 | 2675 | 89 |
| P06 | 207 | 0 | 0 | 0 | 31 | 114 | 53 | 141 | 173 | 8 |
| P07 | 449 | 0 | 449 | 0 | 122 | 249 | 101 | 388 | 407 | 17 |
| P08 | 8926 | 0 | 8926 | 0 | 3983 | 6677 | 3080 | 8851 | 8764 | 175 |
| P09 | 378 | 0 | 356 | 0 | 9 | 74 | 4 | 350 | 361 | 54 |
| P10 | 2870 | 0 | 2815 | 0 | 280 | 1954 | 998 | 2819 | 2773 | 124 |
| P11 | 607 | 607 | 569 | 0 | 35 | 484 | 283 | 575 | 571 | 32 |
| P12 | 18 | 0 | 16 | 0 | 0 | 4 | 0 | 17 | 16 | 1 |
| P13 | 48963 | 0 | 48685 | 0 | 614 | 23593 | 9156 | 48897 | 48848 | 61 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 9786 |
| ap_system_hint | P13 | 0.6% | 20% | 9519 |
| buyer_phone | P13 | 78.8% | 95% | 7943 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 7312 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 7310 |
| buyer_payment_method_preference | P13 | 0.5% | 15% | 7081 |
| buyer_address | P13 | 81.2% | 95% | 6752 |
| buyer_logo_url | P13 | 83.7% | 95% | 5517 |
| buyer_phone | P08 | 44.0% | 95% | 4557 |
| vendor_registered_address | P08 | 20.0% | 70% | 4461 |
| buyer_legal_name_as_published | P08 | 25.2% | 75% | 4446 |
| buyer_logo_url | P08 | 50.5% | 100% | 4421 |
| buyer_legal_name_as_published | P13 | 51.8% | 60% | 4006 |
| vendor_logo_url | P08 | 55.5% | 100% | 3968 |
| vendor_phone | P08 | 43.0% | 85% | 3750 |
| vendor_emails | P08 | 37.8% | 75% | 3322 |
| vendor_bn9 | P08 | 15.9% | 50% | 3046 |
| buyer_address | P08 | 65.4% | 95% | 2639 |
| buyer_bn_as_published | P08 | 9.9% | 35% | 2242 |
| buyer_bn_as_published | P13 | 25.5% | 30% | 2217 |
| vendor_trading_name | P08 | 25.4% | 50% | 2196 |
| invoice_reference_hint | P08 | 0.8% | 25% | 2157 |
| buyer_ap_cycle_published | P08 | 0.1% | 20% | 1780 |
| ap_system_hint | P08 | 1.0% | 20% | 1699 |
| buyer_esignature_preference | P08 | 0.3% | 15% | 1315 |
| buyer_tax_exempt_status | P08 | 0.3% | 15% | 1308 |
| buyer_payment_method_preference | P08 | 0.4% | 15% | 1307 |
| buyer_legal_name_as_published | P10 | 32.0% | 70% | 1092 |
| vendor_registered_address | P10 | 35.8% | 70% | 982 |
| vendor_emails | P10 | 47.7% | 80% | 929 |
| buyer_phone | P10 | 64.5% | 95% | 877 |
| buyer_address | P10 | 65.2% | 95% | 858 |
| average_contract_duration_days | P04 | 45.4% | 90% | 700 |
| vendor_phone | P10 | 61.8% | 85% | 667 |
| invoice_reference_hint | P10 | 2.0% | 25% | 661 |
| buyer_ap_cycle_published | P06T | 0.2% | 20% | 591 |
| buyer_bn_as_published | P10 | 9.9% | 30% | 579 |
| buyer_ap_cycle_published | P10 | 0.2% | 20% | 568 |
| buyer_vendor_id | P04 | 4.3% | 40% | 560 |
| end_date | P04 | 54.4% | 90% | 559 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 44.4% | 44.4% | +0.0 | 50% | 🟡 6 pts to go |
| P01T | 93 | 71.0% | 71.0% | -0.7 | 50% | ✅ met |
| P01_GOLD | 625 | 92.5% | 94.6% | +0.0 | 95% | 🟡 2 pts to go |
| P02 | 403 | 83.9% | 85.6% | +0.0 | 95% | ❌ 11 pts to go |
| P03 | 209 | 92.3% | 95.7% | -0.5 | 95% | 🟡 3 pts to go |
| P04 | 1570 | 68.7% | 71.3% | +0.1 | 90% | ❌ 21 pts to go |
| P05 | 386 | 40.9% | 43.8% | -0.2 | 70% | ❌ 29 pts to go |
| P06M | 168 | 7.1% | 7.1% | +0.0 | n/a | no target |
| P06T | 2983 | 3.7% | 3.7% | -0.7 | n/a | no target |
| P06 | 227 | 37.9% | 37.9% | -10.3 | 30% | ✅ met |
| P07 | 449 | 13.6% | 13.6% | -10.2 | 30% | ❌ 16 pts to go |
| P08 | 8926 | 0.8% | 0.8% | -1.6 | 25% | ❌ 24 pts to go |
| P09 | 383 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2874 | 2.0% | 2.8% | -0.2 | 25% | ❌ 23 pts to go |
| P11 | 607 | 18.8% | 21.3% | -5.3 | 60% | ❌ 41 pts to go |
| P12 | 18 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 48968 | 0.1% | 0.3% | -0.1 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 625 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 403 | 7.2% | 7.2% | +0.0 | 50% | ❌ 43 pts to go |
| P03 | 209 | 1.9% | 1.9% | +0.0 | 40% | ❌ 38 pts to go |
| P04 | 1570 | 1.1% | 1.1% | +0.0 | 30% | ❌ 29 pts to go |
| P05 | 386 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2983 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 227 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 449 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 8926 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 383 | 0.5% | 0.5% | +0.0 | 50% | ❌ 50 pts to go |
| P10 | 2874 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P11 | 607 | 0.7% | 0.7% | -0.1 | n/a | no target |
| P12 | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 48968 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 5.4% | 5.4% | +0.0 | 50% | ❌ 45 pts to go |
| P01_GOLD | 625 | 67.7% | 67.7% | +0.1 | 85% | ❌ 17 pts to go |
| P02 | 403 | 75.4% | 75.4% | -0.1 | 90% | ❌ 15 pts to go |
| P03 | 209 | 75.1% | 75.1% | -0.4 | 85% | 🟡 10 pts to go |
| P04 | 1570 | 65.6% | 65.6% | +0.1 | 85% | ❌ 19 pts to go |
| P05 | 386 | 30.8% | 30.8% | -0.2 | 60% | ❌ 29 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2983 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P06 | 227 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 449 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 8926 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 383 | 96.6% | 96.6% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 2874 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 607 | 15.7% | 15.7% | -4.3 | 60% | ❌ 44 pts to go |
| P12 | 18 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 48968 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 2.2% | 2.2% | +0.0 | 30% | ❌ 28 pts to go |
| P01_GOLD | 625 | 51.4% | 51.4% | +0.1 | 80% | ❌ 29 pts to go |
| P02 | 403 | 66.7% | 66.7% | -0.1 | 60% | ✅ met |
| P03 | 209 | 63.6% | 63.6% | -0.3 | 80% | ❌ 16 pts to go |
| P04 | 1570 | 54.6% | 54.6% | +0.1 | 50% | ✅ met |
| P05 | 386 | 13.2% | 13.2% | -0.1 | 40% | ❌ 27 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2983 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P06 | 227 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 449 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 8926 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 383 | 86.2% | 86.2% | +0.1 | 50% | ✅ met |
| P10 | 2874 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 607 | 13.7% | 13.7% | -3.8 | 40% | ❌ 26 pts to go |
| P12 | 18 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 48968 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 3.2% | 3.2% | -0.1 | n/a | no target |
| P01_GOLD | 625 | 61.1% | 61.1% | +0.0 | 85% | ❌ 24 pts to go |
| P02 | 403 | 65.8% | 65.8% | +0.0 | 90% | ❌ 24 pts to go |
| P03 | 209 | 74.2% | 74.2% | -0.3 | 85% | ❌ 11 pts to go |
| P04 | 1570 | 56.4% | 56.4% | +0.1 | 85% | ❌ 29 pts to go |
| P05 | 386 | 21.0% | 21.0% | -0.1 | 50% | ❌ 29 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2983 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P06 | 227 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 449 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 8926 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 383 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 2874 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 607 | 14.8% | 14.8% | -4.2 | 60% | ❌ 45 pts to go |
| P12 | 18 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 48968 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 2.2% | 2.2% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 13.0% | 13.0% | +0.0 | 60% | ❌ 47 pts to go |
| P02 | 403 | 7.2% | 7.2% | +0.0 | 50% | ❌ 43 pts to go |
| P03 | 209 | 10.5% | 10.5% | -0.1 | 50% | ❌ 40 pts to go |
| P04 | 1570 | 4.3% | 4.3% | +0.0 | 40% | ❌ 36 pts to go |
| P05 | 386 | 1.3% | 1.3% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2983 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P06 | 227 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 449 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 8926 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 383 | 2.6% | 2.6% | +0.0 | 50% | ❌ 47 pts to go |
| P10 | 2874 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 607 | 2.3% | 2.3% | -0.7 | n/a | no target |
| P12 | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 48968 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 35.0% | 35.0% | -0.1 | 80% | ❌ 45 pts to go |
| P02 | 403 | 60.8% | 60.8% | +0.2 | 90% | ❌ 29 pts to go |
| P03 | 209 | 41.1% | 41.1% | -0.2 | 80% | ❌ 39 pts to go |
| P04 | 1570 | 51.3% | 51.3% | +0.0 | 85% | ❌ 34 pts to go |
| P05 | 386 | 6.0% | 6.0% | +0.0 | 50% | ❌ 44 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2983 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 227 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 449 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 8926 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 383 | 75.7% | 75.7% | -0.2 | 95% | ❌ 19 pts to go |
| P10 | 2874 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 607 | 10.2% | 10.2% | -2.9 | 50% | ❌ 40 pts to go |
| P12 | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 48968 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 1.1% | 1.1% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 403 | 7.2% | 7.2% | +0.0 | 50% | ❌ 43 pts to go |
| P03 | 209 | 2.4% | 2.4% | +0.0 | 30% | ❌ 28 pts to go |
| P04 | 1570 | 1.1% | 1.1% | +0.0 | 30% | ❌ 29 pts to go |
| P05 | 386 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2983 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 227 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 449 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 8926 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 383 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10 | 2874 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 607 | 0.7% | 0.7% | -0.1 | n/a | no target |
| P12 | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 48968 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 93 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 403 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 209 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1570 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 386 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 168 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 2983 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 227 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 449 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 8926 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 383 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2874 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 607 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 18 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 48968 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P01T | 93 | 80.6% | 80.6% | +0.2 | 60% | ✅ met |
| P01_GOLD | 625 | 77.8% | 77.8% | -0.1 | 90% | ❌ 12 pts to go |
| P02 | 403 | 67.2% | 67.2% | -0.1 | 85% | ❌ 18 pts to go |
| P03 | 209 | 82.3% | 82.3% | +0.1 | 90% | 🟡 8 pts to go |
| P04 | 1570 | 55.3% | 55.3% | -0.1 | 75% | ❌ 20 pts to go |
| P05 | 386 | 52.8% | 52.8% | +0.2 | 50% | ✅ met |
| P06M | 168 | 74.4% | 74.4% | +0.0 | n/a | no target |
| P06T | 2983 | 58.6% | 58.6% | -2.1 | n/a | no target |
| P06 | 227 | 32.6% | 32.6% | -11.4 | 40% | 🟡 7 pts to go |
| P07 | 449 | 22.9% | 22.9% | -15.2 | 50% | ❌ 27 pts to go |
| P08 | 8926 | 15.9% | 15.9% | -24.3 | 50% | ❌ 34 pts to go |
| P09 | 383 | 54.6% | 54.6% | +0.3 | 80% | ❌ 25 pts to go |
| P10 | 2874 | 31.4% | 31.4% | -5.2 | 40% | 🟡 9 pts to go |
| P11 | 607 | 35.7% | 35.7% | -9.0 | 60% | ❌ 24 pts to go |
| P12 | 18 | 50.0% | 50.0% | -2.6 | 85% | ❌ 35 pts to go |
| P13 | 48968 | 91.8% | 91.8% | +0.1 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 94.4% | 94.4% | +33.3 | n/a | no target |
| P01T | 93 | 63.4% | 63.4% | +0.4 | n/a | no target |
| P01_GOLD | 625 | 74.9% | 74.9% | +0.1 | 95% | ❌ 20 pts to go |
| P02 | 403 | 84.9% | 84.9% | +0.0 | 95% | ❌ 10 pts to go |
| P03 | 209 | 78.0% | 78.0% | +0.1 | 95% | ❌ 17 pts to go |
| P04 | 1570 | 80.6% | 80.6% | -0.1 | 95% | ❌ 14 pts to go |
| P05 | 386 | 56.2% | 56.2% | +0.0 | 70% | ❌ 14 pts to go |
| P06M | 168 | 58.3% | 58.3% | +37.5 | n/a | no target |
| P06T | 2983 | 79.9% | 79.9% | +1.7 | n/a | no target |
| P06 | 227 | 40.1% | 40.1% | -15.3 | 80% | ❌ 40 pts to go |
| P07 | 449 | 30.7% | 30.7% | -21.3 | 70% | ❌ 39 pts to go |
| P08 | 8926 | 20.0% | 20.0% | -32.4 | 70% | ❌ 50 pts to go |
| P09 | 383 | 88.5% | 88.5% | +0.0 | 100% | ❌ 12 pts to go |
| P10 | 2874 | 35.8% | 35.8% | -6.6 | 70% | ❌ 34 pts to go |
| P11 | 607 | 45.1% | 45.1% | -10.2 | 75% | ❌ 30 pts to go |
| P12 | 18 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 48968 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 50.0% | 50.0% | +0.0 | n/a | no target |
| P01T | 93 | 20.4% | 20.4% | +0.8 | n/a | no target |
| P01_GOLD | 625 | 52.3% | 52.3% | -0.1 | 60% | 🟡 8 pts to go |
| P02 | 403 | 67.2% | 67.2% | -0.1 | 60% | ✅ met |
| P03 | 209 | 64.6% | 64.6% | -0.3 | 60% | ✅ met |
| P04 | 1570 | 55.5% | 55.5% | +0.0 | 55% | ✅ met |
| P05 | 386 | 25.4% | 25.4% | +0.1 | 50% | ❌ 25 pts to go |
| P06M | 168 | 17.3% | 17.3% | +0.0 | n/a | no target |
| P06T | 2983 | 53.0% | 53.0% | -0.6 | n/a | no target |
| P06 | 227 | 42.7% | 42.7% | -10.3 | n/a | no target |
| P07 | 449 | 31.6% | 31.6% | -14.4 | 55% | ❌ 23 pts to go |
| P08 | 8926 | 25.4% | 25.4% | -22.1 | 50% | ❌ 25 pts to go |
| P09 | 383 | 71.5% | 71.5% | +0.1 | 70% | ✅ met |
| P10 | 2874 | 47.0% | 47.0% | -4.9 | 55% | 🟡 8 pts to go |
| P11 | 607 | 37.7% | 37.7% | -5.3 | 50% | ❌ 12 pts to go |
| P12 | 18 | 83.3% | 83.3% | -0.9 | n/a | no target |
| P13 | 48968 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 61.1% | 61.1% | +0.0 | n/a | no target |
| P01T | 93 | 30.1% | 30.1% | -0.3 | n/a | no target |
| P01_GOLD | 625 | 51.8% | 51.8% | +0.0 | 70% | ❌ 18 pts to go |
| P02 | 403 | 57.1% | 57.1% | -0.1 | 70% | ❌ 13 pts to go |
| P03 | 209 | 57.4% | 57.4% | +0.2 | 70% | ❌ 13 pts to go |
| P04 | 1570 | 52.0% | 52.0% | +0.0 | 65% | ❌ 13 pts to go |
| P05 | 386 | 34.7% | 34.7% | +0.1 | 60% | ❌ 25 pts to go |
| P06M | 168 | 30.4% | 30.4% | +0.0 | n/a | no target |
| P06T | 2983 | 4.1% | 4.1% | +0.6 | n/a | no target |
| P06 | 227 | 51.5% | 51.5% | -8.1 | 40% | ✅ met |
| P07 | 449 | 51.7% | 51.7% | -16.2 | 85% | ❌ 33 pts to go |
| P08 | 8926 | 43.0% | 43.0% | -25.1 | 85% | ❌ 42 pts to go |
| P09 | 383 | 55.4% | 55.4% | +0.0 | 85% | ❌ 30 pts to go |
| P10 | 2874 | 61.8% | 61.8% | -4.5 | 85% | ❌ 23 pts to go |
| P11 | 607 | 51.9% | 51.9% | -3.0 | 75% | ❌ 23 pts to go |
| P12 | 18 | 11.1% | 11.1% | -4.7 | n/a | no target |
| P13 | 48968 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 94.4% | 94.4% | +0.0 | n/a | no target |
| P01T | 93 | 90.3% | 90.3% | +0.1 | n/a | no target |
| P01_GOLD | 625 | 89.4% | 89.4% | +0.0 | 90% | 🟡 1 pts to go |
| P02 | 403 | 87.8% | 87.8% | +0.2 | 90% | 🟡 2 pts to go |
| P03 | 209 | 90.0% | 90.0% | +0.1 | 90% | ✅ met |
| P04 | 1570 | 81.2% | 81.2% | -0.1 | 85% | 🟡 4 pts to go |
| P05 | 386 | 51.3% | 51.3% | +0.3 | 70% | ❌ 19 pts to go |
| P06M | 168 | 67.9% | 67.9% | +0.0 | n/a | no target |
| P06T | 2983 | 75.0% | 75.0% | -2.9 | n/a | no target |
| P06 | 227 | 97.8% | 97.8% | +0.8 | 50% | ✅ met |
| P07 | 449 | 98.2% | 98.2% | +1.4 | 100% | 🟡 2 pts to go |
| P08 | 8926 | 98.7% | 98.7% | +2.6 | 100% | 🟡 1 pts to go |
| P09 | 383 | 79.9% | 79.9% | +0.1 | 100% | ❌ 20 pts to go |
| P10 | 2874 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 607 | 94.6% | 94.6% | +1.6 | 100% | 🟡 5 pts to go |
| P12 | 18 | 38.9% | 38.9% | -3.2 | n/a | no target |
| P13 | 48968 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 50.0% | 50.0% | +0.0 | n/a | no target |
| P01T | 93 | 45.2% | 45.2% | -0.5 | n/a | no target |
| P01_GOLD | 625 | 45.8% | 45.8% | +0.1 | 70% | ❌ 24 pts to go |
| P02 | 403 | 51.6% | 51.6% | +0.1 | 75% | ❌ 23 pts to go |
| P03 | 209 | 51.7% | 51.7% | +0.3 | 75% | ❌ 23 pts to go |
| P04 | 1570 | 42.9% | 42.9% | +0.0 | 70% | ❌ 27 pts to go |
| P05 | 386 | 24.9% | 24.9% | +0.4 | 55% | ❌ 30 pts to go |
| P06M | 168 | 16.1% | 16.1% | +0.0 | n/a | no target |
| P06T | 2983 | 3.3% | 3.3% | +0.4 | n/a | no target |
| P06 | 227 | 38.3% | 38.3% | -2.7 | n/a | no target |
| P07 | 449 | 35.6% | 35.6% | -1.3 | 70% | ❌ 34 pts to go |
| P08 | 8926 | 37.8% | 37.8% | -10.9 | 75% | ❌ 37 pts to go |
| P09 | 383 | 51.7% | 51.7% | -0.3 | 85% | ❌ 33 pts to go |
| P10 | 2874 | 47.7% | 47.7% | -3.6 | 80% | ❌ 32 pts to go |
| P11 | 607 | 40.7% | 40.7% | +0.2 | 70% | ❌ 29 pts to go |
| P12 | 18 | 27.8% | 27.8% | -3.8 | n/a | no target |
| P13 | 48968 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 94.4% | 94.4% | +0.0 | n/a | no target |
| P01T | 93 | 89.2% | 89.2% | +0.1 | n/a | no target |
| P01_GOLD | 625 | 79.8% | 79.8% | +0.0 | 90% | ❌ 10 pts to go |
| P02 | 403 | 77.4% | 77.4% | +0.2 | 90% | ❌ 13 pts to go |
| P03 | 209 | 81.8% | 81.8% | +0.1 | 90% | 🟡 8 pts to go |
| P04 | 1570 | 70.8% | 70.8% | -0.1 | 85% | ❌ 14 pts to go |
| P05 | 386 | 48.7% | 48.7% | +0.3 | 75% | ❌ 26 pts to go |
| P06M | 168 | 67.9% | 67.9% | +0.0 | n/a | no target |
| P06T | 2983 | 73.4% | 73.4% | -3.7 | n/a | no target |
| P06 | 227 | 75.8% | 75.8% | -12.8 | n/a | no target |
| P07 | 449 | 68.4% | 68.4% | -22.1 | 100% | ❌ 32 pts to go |
| P08 | 8926 | 55.5% | 55.5% | -33.5 | 100% | ❌ 44 pts to go |
| P09 | 383 | 62.4% | 62.4% | -0.1 | n/a | no target |
| P10 | 2874 | 82.3% | 82.3% | -6.7 | 100% | ❌ 18 pts to go |
| P11 | 607 | 69.0% | 69.0% | -5.5 | n/a | no target |
| P12 | 18 | 33.3% | 33.3% | -3.5 | n/a | no target |
| P13 | 48968 | 82.6% | 82.6% | -0.1 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 22.6% | 22.6% | +0.9 | n/a | no target · QC vendors: 2 rows, 100.0% filled |
| P01_GOLD | 625 | 48.0% | 48.0% | +0.1 | 95% | ❌ 47 pts to go · QC vendors: 52 rows, 98.1% filled |
| P02 | 403 | 68.5% | 68.5% | -0.1 | 95% | ❌ 26 pts to go · QC vendors: 107 rows, 100.0% filled |
| P03 | 209 | 55.5% | 55.5% | -0.3 | 95% | ❌ 40 pts to go · QC vendors: 17 rows, 100.0% filled |
| P04 | 1570 | 60.1% | 60.1% | -0.1 | 95% | ❌ 35 pts to go · QC vendors: 435 rows, 98.6% filled |
| P05 | 386 | 15.0% | 15.0% | +0.2 | n/a | no target · QC vendors: 31 rows, 93.5% filled |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2983 | 56.2% | 56.2% | +0.3 | n/a | no target · QC vendors: 103 rows, 100.0% filled |
| P06 | 227 | 19.8% | 19.8% | -6.7 | n/a | no target · QC vendors: 21 rows, 100.0% filled |
| P07 | 449 | 13.1% | 13.1% | -8.3 | n/a | no target · QC vendors: 33 rows, 97.0% filled |
| P08 | 8926 | 11.4% | 11.4% | -17.5 | n/a | no target · QC vendors: 702 rows, 99.3% filled |
| P09 | 383 | 80.2% | 80.2% | +0.1 | 95% | ❌ 15 pts to go · QC vendors: 154 rows, 99.4% filled |
| P10 | 2874 | 19.9% | 19.9% | -3.5 | n/a | no target · QC vendors: 446 rows, 97.8% filled |
| P11 | 607 | 24.4% | 24.4% | -4.9 | n/a | no target · QC vendors: 90 rows, 98.9% filled |
| P12 | 18 | 72.2% | 72.2% | -1.5 | n/a | no target · QC vendors: 3 rows, 100.0% filled |
| P13 | 48968 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 61.1% | 61.1% | +0.0 | n/a | no target · vendors with a registry record: 11 rows, 100.0% filled |
| P01T | 93 | 63.4% | 63.4% | +0.4 | n/a | no target · vendors with a registry record: 59 rows, 100.0% filled |
| P01_GOLD | 625 | 83.4% | 83.4% | -0.1 | 100% | ❌ 17 pts to go · vendors with a registry record: 521 rows, 100.0% filled |
| P02 | 403 | 89.1% | 89.1% | +0.0 | 100% | ❌ 11 pts to go · vendors with a registry record: 359 rows, 100.0% filled |
| P03 | 209 | 89.0% | 89.0% | +0.1 | 100% | ❌ 11 pts to go · vendors with a registry record: 186 rows, 100.0% filled |
| P04 | 1570 | 81.3% | 81.3% | -0.1 | 100% | ❌ 19 pts to go · vendors with a registry record: 1276 rows, 100.0% filled |
| P05 | 386 | 61.7% | 61.7% | +0.0 | n/a | no target · vendors with a registry record: 238 rows, 100.0% filled |
| P06M | 168 | 20.8% | 20.8% | +0.0 | n/a | no target · vendors with a registry record: 35 rows, 100.0% filled |
| P06T | 2983 | 79.9% | 79.9% | +1.7 | n/a | no target · vendors with a registry record: 2383 rows, 100.0% filled |
| P06 | 227 | 41.9% | 41.9% | -15.9 | n/a | no target · vendors with a registry record: 95 rows, 100.0% filled |
| P07 | 449 | 31.6% | 31.6% | -22.8 | n/a | no target · vendors with a registry record: 142 rows, 100.0% filled |
| P08 | 8926 | 20.6% | 20.6% | -33.7 | n/a | no target · vendors with a registry record: 1838 rows, 100.0% filled |
| P09 | 383 | 91.6% | 91.6% | +0.0 | n/a | no target · vendors with a registry record: 351 rows, 100.0% filled |
| P10 | 2874 | 36.9% | 36.9% | -6.8 | n/a | no target · vendors with a registry record: 1061 rows, 100.0% filled |
| P11 | 607 | 47.3% | 47.3% | -10.9 | n/a | no target · vendors with a registry record: 287 rows, 100.0% filled |
| P12 | 18 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 18 rows, 100.0% filled |
| P13 | 48968 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 94.4% | 94.4% | +0.0 | 90% | ✅ met |
| P01T | 93 | 93.5% | 93.5% | -1.1 | 90% | ✅ met |
| P01_GOLD | 625 | 85.0% | 85.0% | +0.4 | 95% | 🟡 10 pts to go |
| P02 | 403 | 90.6% | 90.6% | +0.0 | 95% | 🟡 4 pts to go |
| P03 | 209 | 83.7% | 83.7% | +0.5 | 85% | 🟡 1 pts to go |
| P04 | 1570 | 79.0% | 79.0% | +0.2 | 90% | ❌ 11 pts to go |
| P05 | 386 | 75.4% | 75.4% | -0.4 | 75% | ✅ met |
| P06M | 168 | 88.7% | 88.7% | +0.0 | n/a | no target |
| P06T | 2983 | 53.8% | 53.8% | -10.6 | n/a | no target |
| P06 | 227 | 49.8% | 49.8% | -6.8 | 80% | ❌ 30 pts to go |
| P07 | 449 | 44.5% | 44.5% | -9.1 | 80% | ❌ 36 pts to go |
| P08 | 8926 | 25.2% | 25.2% | -11.6 | 75% | ❌ 50 pts to go |
| P09 | 383 | 80.7% | 80.7% | -0.1 | 95% | ❌ 14 pts to go |
| P10 | 2874 | 32.0% | 32.0% | +0.0 | 70% | ❌ 38 pts to go |
| P11 | 607 | 20.3% | 20.3% | -4.6 | 65% | ❌ 45 pts to go |
| P12 | 18 | 77.8% | 77.8% | +4.1 | 80% | 🟡 2 pts to go |
| P13 | 48968 | 51.8% | 51.8% | -0.7 | 60% | 🟡 8 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 38.9% | 38.9% | +0.0 | 50% | ❌ 11 pts to go |
| P01T | 93 | 20.4% | 20.4% | -0.3 | n/a | no target |
| P01_GOLD | 625 | 20.6% | 20.6% | +0.2 | 40% | ❌ 19 pts to go |
| P02 | 403 | 21.6% | 21.6% | -0.2 | 40% | ❌ 18 pts to go |
| P03 | 209 | 26.8% | 26.8% | -0.1 | 40% | ❌ 13 pts to go |
| P04 | 1570 | 27.5% | 27.5% | -0.1 | 40% | ❌ 12 pts to go |
| P05 | 386 | 22.8% | 22.8% | -0.1 | 25% | 🟡 2 pts to go |
| P06M | 168 | 25.6% | 25.6% | +0.0 | n/a | no target |
| P06T | 2983 | 25.7% | 25.7% | -5.2 | n/a | no target |
| P06 | 227 | 10.6% | 10.6% | -0.2 | 35% | ❌ 24 pts to go |
| P07 | 449 | 12.0% | 12.0% | +1.7 | 35% | ❌ 23 pts to go |
| P08 | 8926 | 9.9% | 9.9% | -1.2 | 35% | ❌ 25 pts to go |
| P09 | 383 | 17.2% | 17.2% | +0.1 | n/a | no target |
| P10 | 2874 | 9.9% | 9.9% | +0.3 | 30% | ❌ 20 pts to go |
| P11 | 607 | 6.9% | 6.9% | -1.5 | n/a | no target |
| P12 | 18 | 11.1% | 11.1% | +0.6 | n/a | no target |
| P13 | 48968 | 25.5% | 25.5% | -0.4 | 30% | 🟡 4 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 100.0% | 100.0% | +5.6 | 100% | ✅ met |
| P01T | 93 | 98.9% | 98.9% | +5.4 | 100% | 🟡 1 pts to go |
| P01_GOLD | 625 | 90.2% | 90.2% | +2.5 | 100% | 🟡 10 pts to go |
| P02 | 403 | 97.5% | 97.5% | +0.7 | 100% | 🟡 2 pts to go |
| P03 | 209 | 92.8% | 92.8% | +1.0 | 100% | 🟡 7 pts to go |
| P04 | 1570 | 93.0% | 93.0% | +2.0 | 100% | 🟡 7 pts to go |
| P05 | 386 | 87.6% | 87.6% | +2.7 | 100% | ❌ 12 pts to go |
| P06M | 168 | 81.5% | 81.5% | +9.5 | n/a | no target |
| P06T | 2983 | 87.2% | 87.2% | +7.0 | n/a | no target |
| P06 | 227 | 73.1% | 73.1% | +4.4 | 95% | ❌ 22 pts to go |
| P07 | 449 | 77.1% | 77.1% | +6.5 | 95% | ❌ 18 pts to go |
| P08 | 8926 | 65.4% | 65.4% | -0.8 | 95% | ❌ 30 pts to go |
| P09 | 383 | 95.8% | 95.8% | +0.3 | 100% | 🟡 4 pts to go |
| P10 | 2874 | 65.2% | 65.2% | +0.0 | 95% | ❌ 30 pts to go |
| P11 | 607 | 36.4% | 36.4% | +2.0 | 80% | ❌ 44 pts to go |
| P12 | 18 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 48968 | 81.2% | 81.2% | +5.1 | 95% | ❌ 14 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 88.9% | 88.9% | +0.0 | n/a | no target |
| P01T | 93 | 79.6% | 79.6% | -0.8 | n/a | no target |
| P01_GOLD | 625 | 70.4% | 70.4% | +0.2 | 90% | ❌ 20 pts to go |
| P02 | 403 | 79.7% | 79.7% | +0.0 | 95% | ❌ 15 pts to go |
| P03 | 209 | 73.2% | 73.2% | -0.4 | 95% | ❌ 22 pts to go |
| P04 | 1570 | 84.7% | 84.7% | -0.2 | 95% | ❌ 10 pts to go |
| P05 | 386 | 74.9% | 74.9% | -0.1 | 90% | ❌ 15 pts to go |
| P06M | 168 | 83.9% | 83.9% | +0.0 | n/a | no target |
| P06T | 2983 | 65.8% | 65.8% | -11.5 | n/a | no target |
| P06 | 227 | 55.9% | 55.9% | -8.6 | 95% | ❌ 39 pts to go |
| P07 | 449 | 52.6% | 52.6% | -13.7 | 90% | ❌ 37 pts to go |
| P08 | 8926 | 44.0% | 44.0% | -30.7 | 95% | ❌ 51 pts to go |
| P09 | 383 | 88.8% | 88.8% | -0.2 | 100% | ❌ 11 pts to go |
| P10 | 2874 | 64.5% | 64.5% | -7.0 | 95% | ❌ 30 pts to go |
| P11 | 607 | 27.0% | 27.0% | -1.9 | 75% | ❌ 48 pts to go |
| P12 | 18 | 88.9% | 88.9% | -0.6 | n/a | no target |
| P13 | 48968 | 78.8% | 78.8% | -0.5 | 95% | ❌ 16 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 77.8% | 77.8% | +0.0 | n/a | no target |
| P01T | 93 | 90.3% | 90.3% | -1.0 | 95% | 🟡 5 pts to go |
| P01_GOLD | 625 | 82.2% | 82.2% | +0.0 | 90% | 🟡 8 pts to go |
| P02 | 403 | 88.3% | 88.3% | -0.1 | 95% | 🟡 7 pts to go |
| P03 | 209 | 84.2% | 84.2% | -0.4 | 95% | ❌ 11 pts to go |
| P04 | 1570 | 84.3% | 84.3% | +0.1 | 90% | 🟡 6 pts to go |
| P05 | 386 | 89.6% | 89.6% | +0.0 | 95% | 🟡 5 pts to go |
| P06M | 168 | 85.1% | 85.1% | +0.0 | n/a | no target |
| P06T | 2983 | 79.5% | 79.5% | -14.6 | n/a | no target |
| P06 | 227 | 75.8% | 75.8% | -14.6 | 100% | ❌ 24 pts to go |
| P07 | 449 | 67.5% | 67.5% | -20.6 | 100% | ❌ 32 pts to go |
| P08 | 8926 | 50.5% | 50.5% | -40.2 | 100% | ❌ 50 pts to go |
| P09 | 383 | 73.9% | 73.9% | -0.1 | n/a | no target |
| P10 | 2874 | 82.2% | 82.2% | -7.9 | 100% | ❌ 18 pts to go |
| P11 | 607 | 34.9% | 34.9% | -1.6 | 80% | ❌ 45 pts to go |
| P12 | 18 | 83.3% | 83.3% | -0.9 | n/a | no target |
| P13 | 48968 | 83.7% | 83.7% | -0.5 | 95% | ❌ 11 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 16.7% | 16.7% | +0.0 | n/a | no target |
| P01T | 93 | 23.7% | 23.7% | -0.2 | n/a | no target |
| P01_GOLD | 625 | 14.2% | 14.2% | -0.1 | 25% | ❌ 11 pts to go |
| P02 | 403 | 27.8% | 27.8% | +0.1 | 40% | ❌ 12 pts to go |
| P03 | 209 | 10.5% | 10.5% | -0.1 | 20% | 🟡 10 pts to go |
| P04 | 1570 | 7.4% | 7.4% | +0.0 | 20% | ❌ 13 pts to go |
| P05 | 386 | 3.9% | 3.9% | +0.0 | 15% | ❌ 11 pts to go |
| P06M | 168 | 4.8% | 4.8% | +0.0 | n/a | no target |
| P06T | 2983 | 2.6% | 2.6% | -0.6 | n/a | no target |
| P06 | 227 | 5.3% | 5.3% | -0.1 | n/a | no target |
| P07 | 449 | 6.2% | 6.2% | -0.1 | n/a | no target |
| P08 | 8926 | 0.5% | 0.5% | -0.5 | n/a | no target |
| P09 | 383 | 7.8% | 7.8% | -0.1 | n/a | no target |
| P10 | 2874 | 1.2% | 1.2% | -0.1 | n/a | no target |
| P11 | 607 | 2.0% | 2.0% | -0.5 | n/a | no target |
| P12 | 18 | 11.1% | 11.1% | +0.6 | n/a | no target |
| P13 | 48968 | 0.6% | 0.6% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 38.9% | 38.9% | +0.0 | n/a | no target |
| P01T | 93 | 34.4% | 34.4% | -0.4 | 70% | ❌ 36 pts to go |
| P01_GOLD | 625 | 43.4% | 43.4% | +0.1 | 80% | ❌ 37 pts to go |
| P02 | 403 | 64.3% | 64.3% | +0.2 | 90% | ❌ 26 pts to go |
| P03 | 209 | 23.4% | 23.4% | +0.3 | 60% | ❌ 37 pts to go |
| P04 | 1570 | 50.5% | 50.5% | +0.0 | 85% | ❌ 34 pts to go |
| P05 | 386 | 13.0% | 13.0% | +0.0 | 50% | ❌ 37 pts to go |
| P06M | 168 | 6.5% | 6.5% | +0.0 | n/a | no target |
| P06T | 2983 | 2.2% | 2.2% | -0.5 | n/a | no target |
| P06 | 227 | 18.5% | 18.5% | +0.4 | n/a | no target |
| P07 | 449 | 13.8% | 13.8% | -5.2 | n/a | no target |
| P08 | 8926 | 0.2% | 0.2% | -0.4 | n/a | no target |
| P09 | 383 | 80.4% | 80.4% | -0.2 | 95% | ❌ 15 pts to go |
| P10 | 2874 | 2.9% | 2.9% | -0.2 | n/a | no target |
| P11 | 607 | 27.8% | 27.8% | -1.5 | n/a | no target |
| P12 | 18 | 33.3% | 33.3% | +1.7 | n/a | no target |
| P13 | 48968 | 1.0% | 1.0% | +0.0 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 16.1% | 16.1% | -0.2 | n/a | no target |
| P01_GOLD | 625 | 33.9% | 33.9% | -0.1 | 70% | ❌ 36 pts to go |
| P02 | 403 | 44.4% | 44.4% | +0.1 | 75% | ❌ 31 pts to go |
| P03 | 209 | 23.4% | 23.4% | +0.3 | 55% | ❌ 32 pts to go |
| P04 | 1570 | 50.5% | 50.5% | +0.0 | 75% | ❌ 24 pts to go |
| P05 | 386 | 11.7% | 11.7% | +0.0 | 50% | ❌ 38 pts to go |
| P06M | 168 | 1.8% | 1.8% | +0.0 | n/a | no target |
| P06T | 2983 | 1.2% | 1.2% | -0.3 | n/a | no target |
| P06 | 227 | 11.0% | 11.0% | +0.8 | n/a | no target |
| P07 | 449 | 7.6% | 7.6% | -2.7 | n/a | no target |
| P08 | 8926 | 0.2% | 0.2% | -0.3 | n/a | no target |
| P09 | 383 | 77.5% | 77.5% | -0.2 | 95% | ❌ 18 pts to go |
| P10 | 2874 | 1.6% | 1.6% | -0.2 | n/a | no target |
| P11 | 607 | 27.5% | 27.5% | -1.4 | n/a | no target |
| P12 | 18 | 16.7% | 16.7% | +0.9 | n/a | no target |
| P13 | 48968 | 0.6% | 0.6% | +0.0 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 16.7% | 16.7% | +0.0 | n/a | no target |
| P01T | 93 | 19.4% | 19.4% | -0.2 | n/a | no target |
| P01_GOLD | 625 | 57.9% | 58.1% | +0.0 | 80% | ❌ 22 pts to go |
| P02 | 403 | 52.4% | 52.6% | +0.2 | 75% | ❌ 23 pts to go |
| P03 | 209 | 45.5% | 45.5% | +0.3 | 70% | ❌ 24 pts to go |
| P04 | 1570 | 48.8% | 49.9% | +0.1 | 70% | ❌ 21 pts to go |
| P05 | 386 | 16.3% | 16.3% | -0.1 | 50% | ❌ 34 pts to go |
| P06M | 168 | 4.2% | 4.2% | +0.0 | n/a | no target |
| P06T | 2983 | 1.4% | 1.4% | -0.2 | n/a | no target |
| P06 | 227 | 20.3% | 20.3% | -3.8 | n/a | no target |
| P07 | 449 | 3.3% | 3.3% | -1.9 | n/a | no target |
| P08 | 8926 | 0.4% | 0.4% | -0.6 | n/a | no target |
| P09 | 383 | 44.4% | 44.6% | +0.3 | 80% | ❌ 36 pts to go |
| P10 | 2874 | 1.4% | 1.5% | -0.1 | n/a | no target |
| P11 | 607 | 13.0% | 13.2% | -3.7 | n/a | no target |
| P12 | 18 | 27.8% | 27.8% | -3.8 | n/a | no target |
| P13 | 48968 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 38.9% | 38.9% | +0.0 | n/a | no target |
| P01T | 93 | 57.0% | 57.0% | +0.5 | 60% | 🟡 3 pts to go |
| P01_GOLD | 625 | 63.7% | 63.7% | +0.2 | 70% | 🟡 6 pts to go |
| P02 | 403 | 43.7% | 43.7% | -0.1 | 50% | 🟡 6 pts to go |
| P03 | 209 | 55.0% | 55.0% | -0.3 | 55% | ✅ met |
| P04 | 1570 | 22.9% | 22.9% | +0.0 | 40% | ❌ 17 pts to go |
| P05 | 386 | 17.4% | 17.4% | +0.0 | 40% | ❌ 23 pts to go |
| P06M | 168 | 16.7% | 16.7% | +0.0 | n/a | no target |
| P06T | 2983 | 10.3% | 10.3% | -2.2 | n/a | no target |
| P06 | 227 | 23.8% | 23.8% | -6.9 | n/a | no target |
| P07 | 449 | 9.4% | 9.4% | -6.9 | n/a | no target |
| P08 | 8926 | 1.8% | 1.8% | -2.9 | n/a | no target |
| P09 | 383 | 5.7% | 5.7% | -0.1 | n/a | no target |
| P10 | 2874 | 3.5% | 3.5% | -0.4 | n/a | no target |
| P11 | 607 | 5.9% | 5.9% | -1.7 | n/a | no target |
| P12 | 18 | 11.1% | 11.1% | -4.7 | n/a | no target |
| P13 | 48968 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 44.4% | 44.4% | +0.0 | n/a | no target |
| P01T | 93 | 68.8% | 68.8% | -0.8 | 65% | ✅ met |
| P01_GOLD | 625 | 69.3% | 69.3% | +0.1 | 70% | 🟡 1 pts to go |
| P02 | 403 | 26.1% | 26.1% | -0.1 | 50% | ❌ 24 pts to go |
| P03 | 209 | 56.0% | 56.0% | -0.2 | 60% | 🟡 4 pts to go |
| P04 | 1570 | 9.9% | 9.9% | +0.0 | 40% | ❌ 30 pts to go |
| P05 | 386 | 21.2% | 21.2% | -0.2 | 45% | ❌ 24 pts to go |
| P06M | 168 | 7.1% | 7.1% | +0.0 | n/a | no target |
| P06T | 2983 | 3.6% | 3.6% | -0.7 | n/a | no target |
| P06 | 227 | 37.9% | 37.9% | -10.3 | n/a | no target |
| P07 | 449 | 13.6% | 13.6% | -10.2 | n/a | no target |
| P08 | 8926 | 0.8% | 0.8% | -1.6 | n/a | no target |
| P09 | 383 | 8.6% | 8.6% | -0.1 | n/a | no target |
| P10 | 2874 | 1.9% | 1.9% | -0.2 | n/a | no target |
| P11 | 607 | 5.3% | 5.3% | -1.5 | n/a | no target |
| P12 | 18 | 5.6% | 5.6% | -4.9 | n/a | no target |
| P13 | 48968 | 0.1% | 0.1% | -0.1 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 11.1% | 11.1% | +0.0 | n/a | no target |
| P01T | 93 | 44.1% | 44.1% | -0.5 | n/a | no target |
| P01_GOLD | 625 | 49.8% | 49.8% | +0.0 | 50% | 🟡 0 pts to go |
| P02 | 403 | 42.7% | 42.7% | +0.1 | n/a | no target |
| P03 | 209 | 58.4% | 58.4% | -0.3 | 60% | 🟡 2 pts to go |
| P04 | 1570 | 26.3% | 26.3% | -0.1 | n/a | no target |
| P05 | 386 | 16.6% | 16.6% | -0.1 | n/a | no target |
| P06M | 168 | 4.2% | 4.2% | +0.0 | n/a | no target |
| P06T | 2983 | 3.3% | 3.3% | -0.7 | n/a | no target |
| P06 | 227 | 28.2% | 28.2% | -7.3 | n/a | no target |
| P07 | 449 | 10.5% | 10.5% | -8.2 | n/a | no target |
| P08 | 8926 | 0.6% | 0.6% | -0.9 | n/a | no target |
| P09 | 383 | 18.8% | 18.8% | -0.1 | n/a | no target |
| P10 | 2874 | 2.1% | 2.1% | -0.3 | n/a | no target |
| P11 | 607 | 6.1% | 6.1% | -1.7 | n/a | no target |
| P12 | 18 | 16.7% | 16.7% | -4.4 | n/a | no target |
| P13 | 48968 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 27.8% | 27.8% | +0.0 | 15% | ✅ met |
| P01T | 93 | 29.0% | 29.0% | -0.3 | 15% | ✅ met |
| P01_GOLD | 625 | 35.4% | 35.4% | +0.3 | 40% | 🟡 5 pts to go |
| P02 | 403 | 13.6% | 13.9% | -0.3 | 25% | ❌ 11 pts to go |
| P03 | 209 | 21.5% | 21.5% | -0.1 | 25% | 🟡 4 pts to go |
| P04 | 1570 | 5.2% | 5.2% | +0.0 | 15% | 🟡 10 pts to go |
| P05 | 386 | 8.0% | 8.0% | -0.1 | 15% | 🟡 7 pts to go |
| P06M | 168 | 6.0% | 6.0% | +0.0 | 15% | 🟡 9 pts to go |
| P06T | 2983 | 1.2% | 1.2% | -0.3 | 15% | ❌ 14 pts to go |
| P06 | 227 | 8.8% | 8.8% | -1.4 | 15% | 🟡 6 pts to go |
| P07 | 449 | 4.2% | 4.2% | -2.5 | 15% | ❌ 11 pts to go |
| P08 | 8926 | 0.4% | 0.4% | -0.5 | 15% | ❌ 15 pts to go |
| P09 | 383 | 0.8% | 0.8% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2874 | 1.4% | 1.4% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 607 | 1.0% | 1.0% | -0.3 | 15% | ❌ 14 pts to go |
| P12 | 18 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 48968 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 11.1% | 11.1% | +0.0 | 15% | 🟡 4 pts to go |
| P01T | 93 | 32.3% | 32.3% | -0.3 | 25% | ✅ met |
| P01_GOLD | 625 | 29.1% | 29.1% | -0.1 | 25% | ✅ met |
| P02 | 403 | 28.0% | 28.0% | +0.0 | 15% | ✅ met |
| P03 | 209 | 25.8% | 25.8% | -0.2 | 15% | ✅ met |
| P04 | 1570 | 8.2% | 8.2% | +0.0 | 15% | 🟡 7 pts to go |
| P05 | 386 | 11.9% | 11.9% | -0.1 | 15% | 🟡 3 pts to go |
| P06M | 168 | 2.4% | 2.4% | +0.0 | 15% | ❌ 13 pts to go |
| P06T | 2983 | 2.2% | 2.2% | -0.5 | 15% | ❌ 13 pts to go |
| P06 | 227 | 8.8% | 8.8% | -3.2 | 15% | 🟡 6 pts to go |
| P07 | 449 | 4.5% | 4.5% | -3.0 | 15% | ❌ 10 pts to go |
| P08 | 8926 | 0.3% | 0.3% | -0.7 | 15% | ❌ 15 pts to go |
| P09 | 383 | 0.8% | 0.8% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2874 | 1.3% | 1.3% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 607 | 4.0% | 4.0% | -1.1 | 15% | ❌ 11 pts to go |
| P12 | 18 | 27.8% | 27.8% | +1.5 | 15% | ✅ met |
| P13 | 48968 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 5.6% | 5.6% | +0.0 | 20% | ❌ 14 pts to go |
| P01T | 93 | 9.7% | 9.7% | -0.1 | 20% | ❌ 10 pts to go |
| P01_GOLD | 625 | 4.3% | 4.3% | +0.0 | 20% | ❌ 16 pts to go |
| P02 | 403 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P03 | 209 | 1.9% | 1.9% | +0.0 | 20% | ❌ 18 pts to go |
| P04 | 1570 | 1.0% | 1.0% | +0.0 | 20% | ❌ 19 pts to go |
| P05 | 386 | 1.0% | 1.0% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 2983 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 227 | 2.6% | 2.6% | -1.0 | 20% | ❌ 17 pts to go |
| P07 | 449 | 0.4% | 0.4% | -0.4 | 20% | ❌ 20 pts to go |
| P08 | 8926 | 0.1% | 0.1% | -0.1 | 20% | ❌ 20 pts to go |
| P09 | 383 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2874 | 0.2% | 0.2% | -0.1 | 20% | ❌ 20 pts to go |
| P11 | 607 | 0.5% | 0.5% | -0.1 | 20% | ❌ 20 pts to go |
| P12 | 18 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 48968 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 5.6% | 5.6% | +0.0 | 15% | 🟡 9 pts to go |
| P01T | 93 | 7.5% | 7.5% | -0.1 | 15% | 🟡 8 pts to go |
| P01_GOLD | 625 | 10.6% | 10.6% | +0.0 | 15% | 🟡 4 pts to go |
| P02 | 403 | 13.4% | 13.4% | +0.0 | 15% | 🟡 2 pts to go |
| P03 | 209 | 23.9% | 23.9% | -0.1 | 15% | ✅ met |
| P04 | 1570 | 4.6% | 4.6% | +0.0 | 15% | ❌ 10 pts to go |
| P05 | 386 | 2.8% | 2.8% | -0.1 | 15% | ❌ 12 pts to go |
| P06M | 168 | 2.4% | 2.4% | +0.0 | 15% | ❌ 13 pts to go |
| P06T | 2983 | 1.2% | 1.2% | -0.2 | 15% | ❌ 14 pts to go |
| P06 | 227 | 4.4% | 4.4% | -1.0 | 15% | ❌ 11 pts to go |
| P07 | 449 | 2.2% | 2.2% | -1.4 | 15% | ❌ 13 pts to go |
| P08 | 8926 | 0.3% | 0.3% | -0.4 | 15% | ❌ 15 pts to go |
| P09 | 383 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2874 | 0.7% | 0.7% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 607 | 1.6% | 1.6% | -0.5 | 15% | ❌ 13 pts to go |
| P12 | 18 | 5.6% | 5.6% | +0.3 | 15% | 🟡 9 pts to go |
| P13 | 48968 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 11.1% | 11.1% | +0.0 | 20% | 🟡 9 pts to go |
| P01T | 93 | 40.9% | 40.9% | -0.4 | 40% | ✅ met |
| P01_GOLD | 625 | 45.8% | 45.8% | +0.0 | 40% | ✅ met |
| P02 | 403 | 48.6% | 48.6% | +0.1 | 20% | ✅ met |
| P03 | 209 | 55.5% | 55.5% | -0.3 | 35% | ✅ met |
| P04 | 1570 | 30.2% | 30.2% | -0.1 | 20% | ✅ met |
| P05 | 386 | 16.6% | 16.6% | -0.1 | 20% | 🟡 3 pts to go |
| P06M | 168 | 4.2% | 4.2% | +0.0 | 20% | ❌ 16 pts to go |
| P06T | 2983 | 3.7% | 3.7% | -0.8 | 20% | ❌ 16 pts to go |
| P06 | 227 | 27.8% | 27.8% | -7.7 | 20% | ✅ met |
| P07 | 449 | 8.9% | 8.9% | -5.8 | 20% | ❌ 11 pts to go |
| P08 | 8926 | 1.0% | 1.0% | -1.3 | 20% | ❌ 19 pts to go |
| P09 | 383 | 21.9% | 21.9% | -0.1 | 20% | ✅ met |
| P10 | 2874 | 2.3% | 2.3% | -0.3 | 20% | ❌ 18 pts to go |
| P11 | 607 | 6.3% | 6.3% | -1.7 | 20% | ❌ 14 pts to go |
| P12 | 18 | 11.1% | 11.1% | -4.7 | 20% | 🟡 9 pts to go |
| P13 | 48968 | 0.6% | 0.6% | +0.0 | 20% | ❌ 19 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 1.1% | 1.1% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 69.8% | 69.8% | +0.1 | 95% | ❌ 25 pts to go |
| P02 | 403 | 73.2% | 73.2% | -0.1 | 95% | ❌ 22 pts to go |
| P03 | 209 | 67.0% | 67.0% | -0.3 | 90% | ❌ 23 pts to go |
| P04 | 1570 | 58.5% | 58.5% | +0.1 | 85% | ❌ 26 pts to go |
| P05 | 386 | 34.7% | 34.7% | -0.2 | 75% | ❌ 40 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2983 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 227 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 449 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 8926 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 383 | 90.9% | 90.9% | +0.1 | 100% | 🟡 9 pts to go |
| P10 | 2874 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 607 | 14.7% | 14.7% | -4.1 | 60% | ❌ 45 pts to go |
| P12 | 18 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 48968 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 73.0% | 73.0% | +0.1 | 100% | ❌ 27 pts to go |
| P02 | 403 | 77.2% | 77.2% | +0.0 | 100% | ❌ 23 pts to go |
| P03 | 209 | 74.2% | 74.2% | -0.3 | n/a | no target |
| P04 | 1570 | 60.1% | 60.1% | +0.1 | 95% | ❌ 35 pts to go |
| P05 | 386 | 31.1% | 31.1% | -0.1 | 80% | ❌ 49 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2983 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 227 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 449 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 8926 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 383 | 93.5% | 93.5% | +0.1 | 100% | 🟡 6 pts to go |
| P10 | 2874 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 607 | 15.7% | 15.7% | -4.3 | n/a | no target |
| P12 | 18 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 48968 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 1.1% | 1.1% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 51.8% | 51.8% | -0.1 | 85% | ❌ 33 pts to go |
| P02 | 403 | 66.7% | 66.7% | -0.1 | 90% | ❌ 23 pts to go |
| P03 | 209 | 54.5% | 54.5% | -0.3 | 85% | ❌ 30 pts to go |
| P04 | 1570 | 64.1% | 64.1% | +0.0 | 90% | ❌ 26 pts to go |
| P05 | 386 | 35.0% | 35.0% | -0.2 | 75% | ❌ 40 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2983 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 227 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 449 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 8926 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 383 | 85.6% | 85.6% | +0.0 | 95% | 🟡 9 pts to go |
| P10 | 2874 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 607 | 13.5% | 13.5% | -3.8 | n/a | no target |
| P12 | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 48968 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 1.1% | 1.1% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 52.0% | 52.0% | -0.1 | 85% | ❌ 33 pts to go |
| P02 | 403 | 61.0% | 61.0% | -0.1 | 90% | ❌ 29 pts to go |
| P03 | 209 | 56.0% | 56.0% | -0.2 | 85% | ❌ 29 pts to go |
| P04 | 1570 | 54.4% | 54.4% | +0.1 | 90% | ❌ 36 pts to go |
| P05 | 386 | 41.5% | 41.5% | -0.2 | 75% | ❌ 34 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2983 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 227 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 449 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 8926 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 383 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10 | 2874 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 607 | 11.0% | 11.0% | -3.1 | n/a | no target |
| P12 | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 48968 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 80.6% | 80.6% | -0.9 | n/a | no target |
| P01_GOLD | 625 | 85.8% | 85.8% | +0.1 | 100% | ❌ 14 pts to go |
| P02 | 403 | 81.6% | 81.6% | -0.1 | 100% | ❌ 18 pts to go |
| P03 | 209 | 92.3% | 92.3% | +0.0 | n/a | no target |
| P04 | 1570 | 72.7% | 72.7% | +0.1 | 95% | ❌ 22 pts to go |
| P05 | 386 | 75.4% | 75.4% | -0.1 | 95% | ❌ 20 pts to go |
| P06M | 168 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06T | 2983 | 70.7% | 70.7% | -12.7 | n/a | no target |
| P06 | 227 | 55.9% | 55.9% | -20.0 | n/a | no target |
| P07 | 449 | 42.8% | 42.8% | -34.2 | n/a | no target |
| P08 | 8926 | 29.9% | 29.9% | -55.0 | n/a | no target |
| P09 | 383 | 99.0% | 99.0% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2874 | 86.5% | 86.5% | -11.9 | n/a | no target |
| P11 | 607 | 71.0% | 71.0% | -18.9 | n/a | no target |
| P12 | 18 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 48968 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 80.6% | 80.6% | -0.9 | n/a | no target |
| P01_GOLD | 625 | 89.0% | 89.0% | +0.1 | 100% | ❌ 11 pts to go |
| P02 | 403 | 82.9% | 83.1% | +0.0 | 100% | ❌ 17 pts to go |
| P03 | 209 | 93.8% | 93.8% | +0.0 | n/a | no target |
| P04 | 1570 | 79.0% | 79.0% | +0.0 | 95% | ❌ 16 pts to go |
| P05 | 386 | 89.9% | 89.9% | -0.2 | 70% | ✅ met |
| P06M | 168 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06T | 2983 | 70.7% | 70.7% | -12.7 | n/a | no target |
| P06 | 227 | 55.9% | 55.9% | -20.0 | n/a | no target |
| P07 | 449 | 42.8% | 42.8% | -34.2 | n/a | no target |
| P08 | 8926 | 29.9% | 29.9% | -55.0 | n/a | no target |
| P09 | 383 | 99.0% | 99.0% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2874 | 86.5% | 86.5% | -11.9 | n/a | no target |
| P11 | 607 | 71.3% | 71.3% | -19.0 | n/a | no target |
| P12 | 18 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 48968 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 1.1% | 1.1% | +0.0 | n/a | no target · rows from a source that publishes bids: 3 rows, 33.3% filled |
| P01_GOLD | 625 | 17.3% | 17.3% | +0.0 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 367 rows, 29.4% filled |
| P02 | 403 | 13.2% | 13.2% | +0.1 | n/a | no target · rows from a source that publishes bids: 294 rows, 18.0% filled |
| P03 | 209 | 16.3% | 16.3% | +0.0 | n/a | no target · rows from a source that publishes bids: 140 rows, 24.3% filled |
| P04 | 1570 | 3.7% | 3.7% | +0.0 | n/a | no target · rows from a source that publishes bids: 878 rows, 6.6% filled |
| P05 | 386 | 3.4% | 3.4% | +0.0 | n/a | no target · rows from a source that publishes bids: 53 rows, 24.5% filled |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2983 | 0.1% | 0.1% | +0.0 | n/a | no target · rows from a source that publishes bids: 4 rows, 50.0% filled |
| P06 | 227 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 449 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 8926 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 383 | 3.1% | 3.1% | +0.0 | n/a | no target · rows from a source that publishes bids: 369 rows, 3.3% filled |
| P10 | 2874 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 607 | 2.1% | 2.1% | -0.6 | n/a | no target · rows from a source that publishes bids: 92 rows, 14.1% filled |
| P12 | 18 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 18 rows, 0.0% filled |
| P13 | 48968 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 93 | 0.0% | 96.8% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 53.1% | 82.4% | -0.1 | 90% | ❌ 37 pts to go |
| P02 | 403 | 61.0% | 85.6% | -0.1 | 90% | ❌ 29 pts to go |
| P03 | 209 | 56.0% | 75.6% | -0.2 | 90% | ❌ 34 pts to go |
| P04 | 1570 | 45.4% | 85.6% | +0.1 | 90% | ❌ 45 pts to go |
| P05 | 386 | 0.0% | 81.1% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 168 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 2983 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 227 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 449 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 8926 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 383 | 2.1% | 3.4% | +0.0 | 90% | ❌ 88 pts to go |
| P10 | 2874 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 607 | 9.9% | 92.6% | -2.8 | n/a | no target |
| P12 | 18 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 48968 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 93 | 0.0% | 96.8% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 25.9% | 55.2% | -0.1 | 90% | ❌ 64 pts to go |
| P02 | 403 | 60.0% | 84.6% | +0.1 | n/a | no target |
| P03 | 209 | 30.6% | 50.2% | -0.2 | n/a | no target |
| P04 | 1570 | 49.7% | 89.9% | +0.0 | n/a | no target |
| P05 | 386 | 0.5% | 81.6% | +0.0 | n/a | no target |
| P06M | 168 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 2983 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 227 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 449 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 8926 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 383 | 44.4% | 45.7% | +0.0 | n/a | no target |
| P10 | 2874 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 607 | 9.1% | 91.8% | -2.5 | n/a | no target |
| P12 | 18 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 48968 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 93 | 2.2% | 98.9% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 51.7% | 81.0% | +0.1 | 95% | ❌ 43 pts to go |
| P02 | 403 | 65.8% | 90.3% | +0.2 | n/a | no target |
| P03 | 209 | 58.9% | 78.5% | -0.2 | n/a | no target |
| P04 | 1570 | 50.3% | 90.5% | +0.0 | n/a | no target |
| P05 | 386 | 5.2% | 86.3% | +0.0 | n/a | no target |
| P06M | 168 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 2983 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 227 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 449 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 8926 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 383 | 67.1% | 68.4% | -0.4 | n/a | no target |
| P10 | 2874 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 607 | 9.9% | 92.6% | -2.8 | n/a | no target |
| P12 | 18 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 48968 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 93 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 403 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 209 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1570 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 386 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 168 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 2983 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 227 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 449 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 8926 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 383 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2874 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 607 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 18 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 48968 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 93 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 403 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 209 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1570 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 386 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 168 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 2983 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 227 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 449 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 8926 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 383 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2874 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 607 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 18 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 48968 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 93 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 403 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 209 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1570 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 386 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 168 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 2983 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 227 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 449 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 8926 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 383 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2874 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 607 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 18 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 48968 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |


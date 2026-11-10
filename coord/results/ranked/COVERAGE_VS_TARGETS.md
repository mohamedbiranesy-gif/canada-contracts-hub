# Coverage vs the downstream team's targets — 2026-11-10

Benchmarks (field × package with a numeric target): **93 of 446 met** (20.9%); 56 within 10 points; 297 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 97, P01T 332, P01_GOLD 626, P02 465, P03 256, P04 3409, P05 427, P06M 9350, P06T 59340, P06 290, P07 749, P08 23364, P09 303, P10R 98530, P10 2699, P11 9442, P12 8, P13 17822

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 97 | 0.0% | 17.5% | 8 | vendor GST/HST number (83 rows) |
| P01T | 332 | 0.9% | 21.1% | 7 | payment terms (257 rows) |
| P01_GOLD | 626 | 23.5% | 67.4% | 9 | payment terms (214 rows) |
| P02 | 465 | 7.5% | 51.8% | 9 | PO rule (354 rows) |
| P03 | 256 | 13.7% | 56.6% | 9 | PO rule (122 rows) |
| P04 | 3409 | 1.3% | 17.2% | 6 | PO rule (3212 rows) |
| P05 | 427 | 0.9% | 16.4% | 7 | payment terms (351 rows) |
| P06M | 9350 | 0.0% | 1.5% | 8 | PO rule (9319 rows) |
| P06T | 59340 | 0.0% | 2.1% | 6 | PO rule (58990 rows) |
| P06 | 290 | 0.0% | 6.9% | 6 | reference to quote (PO / contract / vendor id) (290 rows) |
| P07 | 749 | 0.0% | 1.2% | 5 | reference to quote (PO / contract / vendor id) (749 rows) |
| P08 | 23364 | 0.0% | 0.2% | 5 | reference to quote (PO / contract / vendor id) (23364 rows) |
| P09 | 303 | 1.0% | 43.9% | 8 | payment terms (283 rows) |
| P10R | 98530 | 0.0% | 15.9% | 7 | PO rule (98489 rows) |
| P10 | 2699 | 0.0% | 0.7% | 5 | reference to quote (PO / contract / vendor id) (2699 rows) |
| P11 | 9442 | 0.1% | 1.8% | 6 | PO rule (9345 rows) |
| P12 | 8 | 0.0% | 50.0% | 9 | PO rule (8 rows) |
| P13 | 17822 | 0.0% | 0.0% | 5 | reference to quote (PO / contract / vendor id) (17822 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 97 | 7 | 9 | 81 | 0 | 0 | 71 |
| P01T | 332 | 31 | 55 | 246 | 0 | 0 | 71 |
| P01_GOLD | 626 | 224 | 185 | 217 | 0 | 0 | 81 |
| P02 | 465 | 0 | 187 | 278 | 0 | 0 | 66 |
| P03 | 256 | 0 | 0 | 242 | 14 | 0 | 57 |
| P04 | 3409 | 0 | 0 | 2794 | 615 | 0 | 46 |
| P05 | 427 | 15 | 28 | 362 | 22 | 0 | 51 |
| P06M | 9350 | 0 | 3 | 9277 | 70 | 0 | 46 |
| P06T | 59340 | 0 | 41 | 47674 | 11625 | 0 | 38 |
| P06 | 290 | 18 | 42 | 230 | 0 | 0 | 69 |
| P07 | 749 | 0 | 23 | 699 | 27 | 0 | 51 |
| P08 | 23364 | 0 | 0 | 19694 | 3670 | 0 | 38 |
| P09 | 303 | 3 | 12 | 285 | 3 | 0 | 53 |
| P10R | 98530 | 2 | 9 | 63110 | 35409 | 0 | 38 |
| P10 | 2699 | 2 | 13 | 1962 | 722 | 0 | 43 |
| P11 | 9442 | 6 | 9 | 42 | 0 | 9385 | 23 |
| P12 | 8 | 0 | 1 | 7 | 0 | 0 | 54 |
| P13 | 17822 | 2 | 13 | 13974 | 3833 | 0 | 40 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 97 | 77 | 79.4% | bill-to legal name and address (11) |
| P01T | 332 | 141 | 42.5% | bill-to legal name and address (153) |
| P01_GOLD | 626 | 456 | 72.8% | bill-to legal name and address (119) |
| P02 | 465 | 306 | 65.8% | bill-to legal name and address (79) |
| P03 | 256 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (256) |
| P04 | 3409 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3409) |
| P05 | 427 | 46 | 10.8% | a confirmed invoicing / AP or finance channel (340) |
| P06M | 9350 | 87 | 0.9% | a confirmed invoicing / AP or finance channel (9220) |
| P06T | 59340 | 293 | 0.5% | a confirmed invoicing / AP or finance channel (58443) |
| P06 | 290 | 40 | 13.8% | bill-to legal name and address (138) |
| P07 | 749 | 10 | 1.3% | bill-to legal name and address (357) |
| P08 | 23364 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (23364) |
| P09 | 303 | 40 | 13.2% | a confirmed invoicing / AP or finance channel (253) |
| P10R | 98530 | 385 | 0.4% | a confirmed invoicing / AP or finance channel (97415) |
| P10 | 2699 | 4 | 0.1% | a confirmed invoicing / AP or finance channel (2603) |
| P11 | 9442 | 10 | 0.1% | a confirmed invoicing / AP or finance channel (9385) |
| P12 | 8 | 3 | 37.5% | a confirmed invoicing / AP or finance channel (5) |
| P13 | 17822 | 7 | 0.0% | a confirmed invoicing / AP or finance channel (17480) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 97 | 6 | 6.2% | 6 | 0 | the vendor's GST/HST number (BN9) (83) |
| P01T | 332 | 65 | 19.6% | 21 | 0 | the vendor's GST/HST number (BN9) (173) |
| P01_GOLD | 626 | 394 | 62.9% | 12 | 0 | the vendor's GST/HST number (BN9) (151) |
| P02 | 465 | 210 | 45.2% | 21 | 0 | the vendor's GST/HST number (BN9) (194) |
| P03 | 256 | 17 | 6.6% | 0 | 130 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (89) |
| P04 | 3409 | 42 | 1.2% | 8 | 753 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2547) |
| P05 | 427 | 22 | 5.2% | 8 | 103 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (230) |
| P06M | 9350 | 1 | 0.0% | 10 | 116 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (9085) |
| P06T | 59340 | 60 | 0.1% | 91 | 8451 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (49845) |
| P06 | 290 | 14 | 4.8% | 23 | 0 | the vendor's GST/HST number (BN9) (170) |
| P07 | 749 | 4 | 0.5% | 50 | 20 | the vendor's GST/HST number (BN9) (411) |
| P08 | 23364 | 1 | 0.0% | 4 | 1659 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (21640) |
| P09 | 303 | 39 | 12.9% | 1 | 122 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (122) |
| P10R | 98530 | 807 | 0.8% | 0 | 50925 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (46428) |
| P10 | 2699 | 4 | 0.1% | 19 | 342 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2231) |
| P11 | 9442 | 11 | 0.1% | 13 | 0 | a confirmed invoicing / AP or finance channel (9353) |
| P12 | 8 | 2 | 25.0% | 0 | 3 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2) |
| P13 | 17822 | 10 | 0.1% | 236 | 10261 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (7181) |
| **all** | 227509 | 1709 | 0.8% | 523 | 72885 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 90 | 0 | 0 | 0 | 31 | 11 | 0 | 81 | 86 | 0 |
| P01T | 301 | 0 | 0 | 0 | 133 | 145 | 25 | 248 | 259 | 30 |
| P01_GOLD | 402 | 0 | 0 | 0 | 11 | 102 | 37 | 194 | 228 | 59 |
| P02 | 465 | 0 | 465 | 0 | 41 | 69 | 20 | 354 | 284 | 21 |
| P03 | 256 | 0 | 256 | 0 | 13 | 54 | 24 | 122 | 128 | 28 |
| P04 | 3409 | 0 | 3409 | 0 | 1372 | 1487 | 804 | 3212 | 2954 | 140 |
| P05 | 412 | 0 | 359 | 0 | 73 | 138 | 50 | 343 | 353 | 53 |
| P06M | 9350 | 0 | 9350 | 0 | 4609 | 1210 | 112 | 9319 | 9280 | 15 |
| P06T | 59340 | 0 | 59340 | 0 | 45326 | 42139 | 13407 | 58990 | 57901 | 366 |
| P06 | 272 | 0 | 0 | 0 | 105 | 125 | 50 | 198 | 233 | 5 |
| P07 | 749 | 0 | 749 | 0 | 406 | 403 | 121 | 697 | 699 | 15 |
| P08 | 23364 | 0 | 23364 | 0 | 16287 | 14360 | 4610 | 23105 | 22750 | 209 |
| P09 | 300 | 0 | 279 | 0 | 9 | 69 | 3 | 273 | 285 | 44 |
| P10R | 98528 | 0 | 98360 | 0 | 75616 | 73874 | 40576 | 98489 | 98339 | 19 |
| P10 | 2697 | 0 | 2661 | 0 | 1273 | 1647 | 937 | 2628 | 2577 | 115 |
| P11 | 9436 | 9385 | 9329 | 0 | 8051 | 8540 | 969 | 9345 | 9040 | 39 |
| P12 | 8 | 0 | 7 | 0 | 0 | 2 | 0 | 8 | 7 | 0 |
| P13 | 17820 | 0 | 17717 | 0 | 8687 | 10827 | 4404 | 17786 | 17782 | 22 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_ap_cycle_published | P10R | 0.0% | 20% | 19689 |
| ap_system_hint | P10R | 0.2% | 20% | 19513 |
| buyer_tax_exempt_status | P10R | 0.0% | 15% | 14760 |
| buyer_esignature_preference | P10R | 0.0% | 15% | 14748 |
| buyer_payment_method_preference | P10R | 0.4% | 15% | 14386 |
| vendor_registered_address | P08 | 14.1% | 70% | 13071 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 11848 |
| ap_system_hint | P06T | 0.7% | 20% | 11434 |
| vendor_bn9 | P08 | 10.9% | 50% | 9129 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 8764 |
| buyer_tax_exempt_status | P06T | 0.3% | 15% | 8728 |
| buyer_payment_method_preference | P06T | 0.4% | 15% | 8640 |
| buyer_legal_name_as_published | P08 | 38.5% | 75% | 8519 |
| buyer_phone | P08 | 58.8% | 95% | 8453 |
| buyer_phone | P13 | 47.6% | 95% | 8441 |
| buyer_logo_url | P13 | 51.0% | 95% | 7847 |
| vendor_phone | P08 | 56.9% | 85% | 6559 |
| vendor_phone | P11 | 6.4% | 75% | 6482 |
| vendor_emails | P11 | 5.0% | 70% | 6139 |
| buyer_phone | P11 | 11.2% | 75% | 6020 |
| vendor_emails | P08 | 49.9% | 75% | 5854 |
| buyer_logo_url | P11 | 18.8% | 80% | 5776 |
| buyer_bn_as_published | P08 | 10.4% | 35% | 5740 |
| invoice_reference_hint | P08 | 1.1% | 25% | 5582 |
| contract_value | P11 | 0.9% | 60% | 5582 |
| award_or_notice_id | P11 | 0.9% | 60% | 5581 |
| vendor_trading_name | P08 | 26.9% | 50% | 5388 |
| buyer_logo_url | P08 | 77.1% | 100% | 5342 |
| buyer_legal_name_as_published | P11 | 9.6% | 65% | 5236 |
| vendor_logo_url | P08 | 78.9% | 100% | 4920 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 4666 |
| commodity_codes | P11 | 0.6% | 50% | 4660 |
| contract_or_agreement_number | P11 | 12.7% | 60% | 4464 |
| ap_system_hint | P08 | 0.9% | 20% | 4461 |
| invoice_reference_hint | P11 | 13.6% | 60% | 4384 |
| solicitation_or_tender_number | P11 | 0.8% | 40% | 3699 |
| buyer_legal_name_as_published | P13 | 39.2% | 60% | 3699 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 3563 |
| buyer_address | P13 | 75.2% | 95% | 3522 |
| ap_system_hint | P13 | 0.5% | 20% | 3467 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 88.7% | 88.7% | +44.3 | 50% | ✅ met |
| P01T | 332 | 89.5% | 89.5% | +17.8 | 50% | ✅ met |
| P01_GOLD | 626 | 92.2% | 94.4% | -0.3 | 95% | 🟡 3 pts to go |
| P02 | 465 | 73.8% | 75.3% | -10.1 | 95% | ❌ 21 pts to go |
| P03 | 256 | 82.0% | 85.2% | -10.8 | 95% | ❌ 13 pts to go |
| P04 | 3409 | 32.8% | 34.4% | -35.8 | 90% | ❌ 57 pts to go |
| P05 | 427 | 38.6% | 41.7% | -2.5 | 70% | ❌ 31 pts to go |
| P06M | 9350 | 92.6% | 92.6% | +85.5 | n/a | no target |
| P06T | 59340 | 80.3% | 80.3% | +75.9 | n/a | no target |
| P06 | 290 | 31.7% | 31.7% | -16.5 | 30% | ✅ met |
| P07 | 749 | 6.9% | 6.9% | -16.9 | 30% | ❌ 23 pts to go |
| P08 | 23364 | 1.1% | 1.1% | -1.3 | 25% | ❌ 24 pts to go |
| P09 | 303 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10R | 98530 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2699 | 2.6% | 2.7% | +0.4 | 25% | ❌ 22 pts to go |
| P11 | 9442 | 13.6% | 13.7% | -10.5 | 60% | ❌ 46 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17822 | 0.2% | 0.2% | +0.0 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 332 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 626 | 6.1% | 6.1% | -0.1 | 50% | ❌ 44 pts to go |
| P02 | 465 | 6.2% | 6.2% | -1.0 | 50% | ❌ 44 pts to go |
| P03 | 256 | 1.6% | 1.6% | -0.3 | 40% | ❌ 38 pts to go |
| P04 | 3409 | 0.5% | 0.5% | -0.6 | 30% | ❌ 30 pts to go |
| P05 | 427 | 0.2% | 0.2% | -0.1 | 20% | ❌ 20 pts to go |
| P06M | 9350 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59340 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 290 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 749 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 23364 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 0.7% | 0.7% | +0.2 | 50% | ❌ 49 pts to go |
| P10R | 98530 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2699 | 0.0% | 0.0% | -0.1 | n/a | no target |
| P11 | 9442 | 0.0% | 0.0% | -0.8 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 81.4% | 81.4% | +81.4 | n/a | no target |
| P01T | 332 | 70.5% | 70.5% | +65.1 | 50% | ✅ met |
| P01_GOLD | 626 | 66.9% | 66.9% | -0.7 | 85% | ❌ 18 pts to go |
| P02 | 465 | 64.9% | 64.9% | -10.6 | 90% | ❌ 25 pts to go |
| P03 | 256 | 61.3% | 61.3% | -14.2 | 85% | ❌ 24 pts to go |
| P04 | 3409 | 30.1% | 30.1% | -35.4 | 85% | ❌ 55 pts to go |
| P05 | 427 | 29.0% | 29.0% | -2.0 | 60% | ❌ 31 pts to go |
| P06M | 9350 | 92.4% | 92.4% | +92.4 | n/a | no target |
| P06T | 59340 | 80.0% | 80.0% | +79.8 | n/a | no target |
| P06 | 290 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 749 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 23364 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 96.0% | 96.0% | -0.6 | 100% | 🟡 4 pts to go |
| P10R | 98530 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2699 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 9442 | 12.7% | 12.7% | -7.3 | 60% | ❌ 47 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 332 | 0.0% | 0.0% | -2.2 | 30% | ❌ 30 pts to go |
| P01_GOLD | 626 | 50.6% | 50.6% | -0.7 | 80% | ❌ 29 pts to go |
| P02 | 465 | 57.0% | 57.0% | -9.8 | 60% | 🟡 3 pts to go |
| P03 | 256 | 51.6% | 51.6% | -12.3 | 80% | ❌ 28 pts to go |
| P04 | 3409 | 25.0% | 25.0% | -29.5 | 50% | ❌ 25 pts to go |
| P05 | 427 | 11.9% | 11.9% | -1.4 | 40% | ❌ 28 pts to go |
| P06M | 9350 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59340 | 0.0% | 0.0% | -0.2 | n/a | no target |
| P06 | 290 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 749 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 23364 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 83.5% | 83.5% | -2.6 | 50% | ✅ met |
| P10R | 98530 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2699 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 9442 | 0.8% | 0.8% | -16.7 | 40% | ❌ 39 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 332 | 0.3% | 0.3% | -3.0 | n/a | no target |
| P01_GOLD | 626 | 60.4% | 60.4% | -0.7 | 85% | ❌ 25 pts to go |
| P02 | 465 | 56.3% | 56.3% | -9.5 | 90% | ❌ 34 pts to go |
| P03 | 256 | 60.2% | 60.2% | -14.3 | 85% | ❌ 25 pts to go |
| P04 | 3409 | 25.8% | 25.8% | -30.5 | 85% | ❌ 59 pts to go |
| P05 | 427 | 19.9% | 19.9% | -1.2 | 50% | ❌ 30 pts to go |
| P06M | 9350 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59340 | 0.0% | 0.0% | -0.2 | n/a | no target |
| P06 | 290 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 749 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 23364 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 97.0% | 97.0% | -0.1 | 100% | 🟡 3 pts to go |
| P10R | 98530 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2699 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 9442 | 0.9% | 0.9% | -18.1 | 60% | ❌ 59 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 332 | 0.0% | 0.0% | -2.2 | n/a | no target |
| P01_GOLD | 626 | 12.9% | 12.9% | -0.1 | 60% | ❌ 47 pts to go |
| P02 | 465 | 6.0% | 6.0% | -1.2 | 50% | ❌ 44 pts to go |
| P03 | 256 | 8.6% | 8.6% | -2.0 | 50% | ❌ 41 pts to go |
| P04 | 3409 | 2.0% | 2.0% | -2.3 | 40% | ❌ 38 pts to go |
| P05 | 427 | 0.9% | 0.9% | -0.4 | 20% | ❌ 19 pts to go |
| P06M | 9350 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59340 | 0.0% | 0.0% | -0.1 | n/a | no target |
| P06 | 290 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 749 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 23364 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 2.3% | 2.3% | -0.3 | 50% | ❌ 48 pts to go |
| P10R | 98530 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2699 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 9442 | 0.1% | 0.1% | -2.9 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 332 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 34.8% | 34.8% | -0.3 | 80% | ❌ 45 pts to go |
| P02 | 465 | 52.0% | 52.0% | -8.6 | 90% | ❌ 38 pts to go |
| P03 | 256 | 33.6% | 33.6% | -7.7 | 80% | ❌ 46 pts to go |
| P04 | 3409 | 23.6% | 23.6% | -27.7 | 85% | ❌ 61 pts to go |
| P05 | 427 | 5.4% | 5.4% | -0.6 | 50% | ❌ 45 pts to go |
| P06M | 9350 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59340 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 290 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 749 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 23364 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 75.9% | 75.9% | +0.0 | 95% | ❌ 19 pts to go |
| P10R | 98530 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2699 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 9442 | 0.6% | 0.6% | -12.5 | 50% | ❌ 49 pts to go |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 332 | 0.0% | 0.0% | -1.1 | n/a | no target |
| P01_GOLD | 626 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 465 | 6.2% | 6.2% | -1.0 | 50% | ❌ 44 pts to go |
| P03 | 256 | 2.0% | 2.0% | -0.4 | 30% | ❌ 28 pts to go |
| P04 | 3409 | 0.5% | 0.5% | -0.6 | 30% | ❌ 30 pts to go |
| P05 | 427 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 9350 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59340 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 290 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 749 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 23364 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10R | 98530 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2699 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 9442 | 0.0% | 0.0% | -0.8 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 332 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 465 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 256 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3409 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 427 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 9350 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 59340 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 290 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 749 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 23364 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 98530 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2699 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 9442 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17822 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 14.4% | 14.4% | -85.6 | 70% | ❌ 56 pts to go |
| P01T | 332 | 33.7% | 33.7% | -46.7 | 60% | ❌ 26 pts to go |
| P01_GOLD | 626 | 73.0% | 73.0% | -4.9 | 90% | ❌ 17 pts to go |
| P02 | 465 | 55.1% | 55.1% | -12.2 | 85% | ❌ 30 pts to go |
| P03 | 256 | 69.9% | 69.9% | -12.3 | 90% | ❌ 20 pts to go |
| P04 | 3409 | 32.5% | 32.5% | -22.9 | 75% | ❌ 42 pts to go |
| P05 | 427 | 49.9% | 49.9% | -2.7 | 50% | 🟡 0 pts to go |
| P06M | 9350 | 1.8% | 1.8% | -72.6 | n/a | no target |
| P06T | 59340 | 17.3% | 17.3% | -43.4 | n/a | no target |
| P06 | 290 | 22.8% | 22.8% | -21.2 | 40% | ❌ 17 pts to go |
| P07 | 749 | 16.4% | 16.4% | -21.7 | 50% | ❌ 34 pts to go |
| P08 | 23364 | 10.9% | 10.9% | -29.3 | 50% | ❌ 39 pts to go |
| P09 | 303 | 57.8% | 57.8% | +3.5 | 80% | ❌ 22 pts to go |
| P10R | 98530 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2699 | 28.7% | 28.7% | -7.9 | 40% | ❌ 11 pts to go |
| P11 | 9442 | 91.1% | 91.1% | +46.4 | 60% | ✅ met |
| P12 | 8 | 62.5% | 62.5% | +9.9 | 85% | ❌ 22 pts to go |
| P13 | 17822 | 91.0% | 91.0% | -0.7 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 67.0% | 67.0% | +5.9 | n/a | no target |
| P01T | 332 | 38.0% | 38.0% | -25.0 | n/a | no target |
| P01_GOLD | 626 | 70.4% | 70.4% | -4.4 | 95% | ❌ 25 pts to go |
| P02 | 465 | 73.8% | 73.8% | -11.1 | 95% | ❌ 21 pts to go |
| P03 | 256 | 71.9% | 71.9% | -6.0 | 95% | ❌ 23 pts to go |
| P04 | 3409 | 45.6% | 45.6% | -35.1 | 95% | ❌ 49 pts to go |
| P05 | 427 | 53.4% | 53.4% | -2.8 | 70% | ❌ 17 pts to go |
| P06M | 9350 | 54.6% | 54.6% | +33.8 | n/a | no target |
| P06T | 59340 | 30.3% | 30.3% | -47.9 | n/a | no target |
| P06 | 290 | 24.8% | 24.8% | -30.6 | 80% | ❌ 55 pts to go |
| P07 | 749 | 18.0% | 18.0% | -34.0 | 70% | ❌ 52 pts to go |
| P08 | 23364 | 14.1% | 14.1% | -38.3 | 70% | ❌ 56 pts to go |
| P09 | 303 | 87.5% | 87.5% | -1.0 | 100% | ❌ 12 pts to go |
| P10R | 98530 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2699 | 32.5% | 32.5% | -9.9 | 70% | ❌ 38 pts to go |
| P11 | 9442 | 92.2% | 92.2% | +36.9 | 75% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 16.5% | 16.5% | -33.5 | n/a | no target |
| P01T | 332 | 25.9% | 25.9% | +6.3 | n/a | no target |
| P01_GOLD | 626 | 47.9% | 47.9% | -4.5 | 60% | ❌ 12 pts to go |
| P02 | 465 | 55.3% | 55.3% | -12.0 | 60% | 🟡 5 pts to go |
| P03 | 256 | 55.1% | 55.1% | -9.8 | 60% | 🟡 5 pts to go |
| P04 | 3409 | 36.7% | 36.7% | -18.8 | 55% | ❌ 18 pts to go |
| P05 | 427 | 22.2% | 22.2% | -3.1 | 50% | ❌ 28 pts to go |
| P06M | 9350 | 3.6% | 3.6% | -13.7 | n/a | no target |
| P06T | 59340 | 27.0% | 27.0% | -26.6 | n/a | no target |
| P06 | 290 | 35.2% | 35.2% | -17.8 | n/a | no target |
| P07 | 749 | 33.2% | 33.2% | -12.8 | 55% | ❌ 22 pts to go |
| P08 | 23364 | 26.9% | 26.9% | -20.6 | 50% | ❌ 23 pts to go |
| P09 | 303 | 71.0% | 71.0% | -0.4 | 70% | ✅ met |
| P10R | 98530 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2699 | 39.5% | 39.5% | -12.4 | 55% | ❌ 16 pts to go |
| P11 | 9442 | 92.0% | 92.0% | +49.0 | 50% | ✅ met |
| P12 | 8 | 87.5% | 87.5% | +3.3 | n/a | no target |
| P13 | 17822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 14.4% | 14.4% | -46.7 | n/a | no target |
| P01T | 332 | 56.3% | 56.3% | +25.9 | n/a | no target |
| P01_GOLD | 626 | 47.9% | 47.9% | -3.9 | 70% | ❌ 22 pts to go |
| P02 | 465 | 54.0% | 54.0% | -3.2 | 70% | ❌ 16 pts to go |
| P03 | 256 | 49.6% | 49.6% | -7.6 | 70% | ❌ 20 pts to go |
| P04 | 3409 | 47.1% | 47.1% | -4.9 | 65% | ❌ 18 pts to go |
| P05 | 427 | 30.7% | 30.7% | -3.9 | 60% | ❌ 29 pts to go |
| P06M | 9350 | 3.5% | 3.5% | -26.9 | n/a | no target |
| P06T | 59340 | 63.8% | 63.8% | +60.3 | n/a | no target |
| P06 | 290 | 57.6% | 57.6% | -2.0 | 40% | ✅ met |
| P07 | 749 | 57.0% | 57.0% | -10.9 | 85% | ❌ 28 pts to go |
| P08 | 23364 | 56.9% | 56.9% | -11.2 | 85% | ❌ 28 pts to go |
| P09 | 303 | 53.5% | 53.5% | -1.9 | 85% | ❌ 32 pts to go |
| P10R | 98530 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2699 | 61.0% | 61.0% | -5.3 | 85% | ❌ 24 pts to go |
| P11 | 9442 | 6.4% | 6.4% | -48.5 | 75% | ❌ 69 pts to go |
| P12 | 8 | 25.0% | 25.0% | +9.2 | n/a | no target |
| P13 | 17822 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 19.6% | 19.6% | -74.8 | n/a | no target |
| P01T | 332 | 96.4% | 96.4% | +6.2 | n/a | no target |
| P01_GOLD | 626 | 89.3% | 89.3% | -0.1 | 90% | 🟡 1 pts to go |
| P02 | 465 | 89.2% | 89.2% | +1.6 | 90% | 🟡 1 pts to go |
| P03 | 256 | 91.0% | 91.0% | +1.1 | 90% | ✅ met |
| P04 | 3409 | 90.2% | 90.2% | +8.9 | 85% | ✅ met |
| P05 | 427 | 52.2% | 52.2% | +1.2 | 70% | ❌ 18 pts to go |
| P06M | 9350 | 6.2% | 6.2% | -61.7 | n/a | no target |
| P06T | 59340 | 92.0% | 92.0% | +14.1 | n/a | no target |
| P06 | 290 | 98.3% | 98.3% | +1.3 | 50% | ✅ met |
| P07 | 749 | 99.1% | 99.1% | +2.3 | 100% | 🟡 1 pts to go |
| P08 | 23364 | 99.4% | 99.4% | +3.3 | 100% | 🟡 1 pts to go |
| P09 | 303 | 80.2% | 80.2% | +0.4 | 100% | ❌ 20 pts to go |
| P10R | 98530 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2699 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 9442 | 99.7% | 99.7% | +6.7 | 100% | 🟡 0 pts to go |
| P12 | 8 | 37.5% | 37.5% | -4.6 | n/a | no target |
| P13 | 17822 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 14.4% | 14.4% | -35.6 | n/a | no target |
| P01T | 332 | 49.1% | 49.1% | +3.4 | n/a | no target |
| P01_GOLD | 626 | 45.2% | 45.2% | -0.5 | 70% | ❌ 25 pts to go |
| P02 | 465 | 49.5% | 49.5% | -2.0 | 75% | ❌ 26 pts to go |
| P03 | 256 | 44.5% | 44.5% | -6.9 | 75% | ❌ 30 pts to go |
| P04 | 3409 | 37.4% | 37.4% | -5.5 | 70% | ❌ 33 pts to go |
| P05 | 427 | 25.5% | 25.5% | +1.0 | 55% | ❌ 30 pts to go |
| P06M | 9350 | 3.3% | 3.3% | -12.8 | n/a | no target |
| P06T | 59340 | 39.6% | 39.6% | +36.7 | n/a | no target |
| P06 | 290 | 42.8% | 42.8% | +1.8 | n/a | no target |
| P07 | 749 | 45.9% | 45.9% | +9.0 | 70% | ❌ 24 pts to go |
| P08 | 23364 | 49.9% | 49.9% | +1.2 | 75% | ❌ 25 pts to go |
| P09 | 303 | 49.8% | 49.8% | -2.2 | 85% | ❌ 35 pts to go |
| P10R | 98530 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2699 | 43.5% | 43.5% | -7.8 | 80% | ❌ 36 pts to go |
| P11 | 9442 | 5.0% | 5.0% | -35.5 | 70% | ❌ 65 pts to go |
| P12 | 8 | 25.0% | 25.0% | -6.6 | n/a | no target |
| P13 | 17822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 13.4% | 13.4% | -81.0 | n/a | no target |
| P01T | 332 | 89.8% | 89.8% | +0.7 | n/a | no target |
| P01_GOLD | 626 | 77.5% | 77.5% | -2.3 | 90% | ❌ 12 pts to go |
| P02 | 465 | 77.6% | 77.6% | +0.4 | 90% | ❌ 12 pts to go |
| P03 | 256 | 83.2% | 83.2% | +1.5 | 90% | 🟡 7 pts to go |
| P04 | 3409 | 75.6% | 75.6% | +4.7 | 85% | 🟡 9 pts to go |
| P05 | 427 | 48.7% | 48.7% | +0.3 | 75% | ❌ 26 pts to go |
| P06M | 9350 | 4.1% | 4.1% | -63.8 | n/a | no target |
| P06T | 59340 | 83.2% | 83.2% | +6.1 | n/a | no target |
| P06 | 290 | 79.3% | 79.3% | -9.3 | n/a | no target |
| P07 | 749 | 81.6% | 81.6% | -8.9 | 100% | ❌ 18 pts to go |
| P08 | 23364 | 78.9% | 78.9% | -10.1 | 100% | ❌ 21 pts to go |
| P09 | 303 | 61.4% | 61.4% | -1.1 | n/a | no target |
| P10R | 98530 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2699 | 84.2% | 84.2% | -4.8 | 100% | ❌ 16 pts to go |
| P11 | 9442 | 88.4% | 88.4% | +13.9 | n/a | no target |
| P12 | 8 | 37.5% | 37.5% | +0.7 | n/a | no target |
| P13 | 17822 | 83.2% | 83.2% | +0.5 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 53.6% | 53.6% | +53.6 | n/a | no target · QC vendors: 47 rows, 100.0% filled |
| P01T | 332 | 17.8% | 17.8% | -3.9 | n/a | no target · QC vendors: 17 rows, 100.0% filled |
| P01_GOLD | 626 | 43.6% | 43.6% | -4.3 | 95% | ❌ 51 pts to go · QC vendors: 53 rows, 98.1% filled |
| P02 | 465 | 55.1% | 55.1% | -13.5 | 95% | ❌ 40 pts to go · QC vendors: 110 rows, 100.0% filled |
| P03 | 256 | 46.5% | 46.5% | -9.3 | 95% | ❌ 48 pts to go · QC vendors: 18 rows, 100.0% filled |
| P04 | 3409 | 31.9% | 31.9% | -28.3 | 95% | ❌ 63 pts to go · QC vendors: 494 rows, 98.8% filled |
| P05 | 427 | 14.8% | 14.8% | +0.0 | n/a | no target · QC vendors: 35 rows, 94.3% filled |
| P06M | 9350 | 53.3% | 53.3% | +53.3 | n/a | no target · QC vendors: 4829 rows, 100.0% filled |
| P06T | 59340 | 17.5% | 17.5% | -38.4 | n/a | no target · QC vendors: 3295 rows, 100.0% filled |
| P06 | 290 | 8.3% | 8.3% | -18.2 | n/a | no target · QC vendors: 13 rows, 100.0% filled |
| P07 | 749 | 6.8% | 6.8% | -14.6 | n/a | no target · QC vendors: 36 rows, 97.2% filled |
| P08 | 23364 | 6.5% | 6.5% | -22.4 | n/a | no target · QC vendors: 1211 rows, 99.7% filled |
| P09 | 303 | 78.2% | 78.2% | -1.9 | 95% | ❌ 17 pts to go · QC vendors: 111 rows, 100.0% filled |
| P10R | 98530 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2699 | 17.6% | 17.6% | -5.8 | n/a | no target · QC vendors: 311 rows, 94.9% filled |
| P11 | 9442 | 81.5% | 81.5% | +52.2 | n/a | no target · QC vendors: 112 rows, 99.1% filled |
| P12 | 8 | 62.5% | 62.5% | -11.2 | n/a | no target · QC vendors: 1 rows, 100.0% filled |
| P13 | 17822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 64.9% | 64.9% | +3.8 | n/a | no target · vendors with a registry record: 63 rows, 100.0% filled |
| P01T | 332 | 38.3% | 38.3% | -24.7 | n/a | no target · vendors with a registry record: 127 rows, 100.0% filled |
| P01_GOLD | 626 | 79.4% | 79.4% | -4.1 | 100% | ❌ 21 pts to go · vendors with a registry record: 497 rows, 100.0% filled |
| P02 | 465 | 77.4% | 77.4% | -11.7 | 100% | ❌ 23 pts to go · vendors with a registry record: 360 rows, 100.0% filled |
| P03 | 256 | 81.2% | 81.2% | -7.7 | 100% | ❌ 19 pts to go · vendors with a registry record: 208 rows, 100.0% filled |
| P04 | 3409 | 46.1% | 46.1% | -35.3 | 100% | ❌ 54 pts to go · vendors with a registry record: 1570 rows, 100.0% filled |
| P05 | 427 | 58.3% | 58.3% | -3.4 | n/a | no target · vendors with a registry record: 249 rows, 100.0% filled |
| P06M | 9350 | 54.3% | 54.3% | +33.5 | n/a | no target · vendors with a registry record: 5078 rows, 100.0% filled |
| P06T | 59340 | 30.4% | 30.4% | -47.8 | n/a | no target · vendors with a registry record: 18019 rows, 100.0% filled |
| P06 | 290 | 25.5% | 25.5% | -32.3 | n/a | no target · vendors with a registry record: 74 rows, 100.0% filled |
| P07 | 749 | 18.4% | 18.4% | -36.0 | n/a | no target · vendors with a registry record: 138 rows, 100.0% filled |
| P08 | 23364 | 14.3% | 14.3% | -40.0 | n/a | no target · vendors with a registry record: 3333 rows, 100.0% filled |
| P09 | 303 | 91.1% | 91.1% | -0.5 | n/a | no target · vendors with a registry record: 276 rows, 100.0% filled |
| P10R | 98530 | 100.0% | 100.0% |  | n/a | no target · vendors with a registry record: 98530 rows, 100.0% filled |
| P10 | 2699 | 33.2% | 33.2% | -10.5 | n/a | no target · vendors with a registry record: 895 rows, 100.0% filled |
| P11 | 9442 | 92.3% | 92.3% | +34.1 | n/a | no target · vendors with a registry record: 8719 rows, 100.0% filled |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 8 rows, 100.0% filled |
| P13 | 17822 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 88.7% | 88.7% | -5.7 | 90% | 🟡 1 pts to go |
| P01T | 332 | 56.3% | 56.3% | -38.3 | 90% | ❌ 34 pts to go |
| P01_GOLD | 626 | 83.7% | 83.7% | -0.9 | 95% | ❌ 11 pts to go |
| P02 | 465 | 85.2% | 85.2% | -5.4 | 95% | 🟡 10 pts to go |
| P03 | 256 | 78.9% | 78.9% | -4.3 | 85% | 🟡 6 pts to go |
| P04 | 3409 | 56.4% | 56.4% | -22.4 | 90% | ❌ 34 pts to go |
| P05 | 427 | 67.7% | 67.7% | -8.1 | 75% | 🟡 7 pts to go |
| P06M | 9350 | 87.1% | 87.1% | -1.6 | n/a | no target |
| P06T | 59340 | 29.0% | 29.0% | -35.4 | n/a | no target |
| P06 | 290 | 56.9% | 56.9% | +0.3 | 80% | ❌ 23 pts to go |
| P07 | 749 | 46.2% | 46.3% | -7.4 | 80% | ❌ 34 pts to go |
| P08 | 23364 | 38.5% | 38.5% | +1.7 | 75% | ❌ 36 pts to go |
| P09 | 303 | 77.2% | 77.2% | -3.6 | 95% | ❌ 18 pts to go |
| P10R | 98530 | 25.0% | 25.0% |  | n/a | no target |
| P10 | 2699 | 39.0% | 39.0% | +7.0 | 70% | ❌ 31 pts to go |
| P11 | 9442 | 9.6% | 9.6% | -15.3 | 65% | ❌ 55 pts to go |
| P12 | 8 | 75.0% | 75.0% | +1.3 | 80% | 🟡 5 pts to go |
| P13 | 17822 | 39.2% | 39.3% | -13.3 | 60% | ❌ 21 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 19.6% | 19.6% | -19.3 | 50% | ❌ 30 pts to go |
| P01T | 332 | 13.3% | 13.3% | -7.4 | n/a | no target |
| P01_GOLD | 626 | 20.6% | 20.6% | +0.2 | 40% | ❌ 19 pts to go |
| P02 | 465 | 18.9% | 18.9% | -2.9 | 40% | ❌ 21 pts to go |
| P03 | 256 | 22.3% | 22.3% | -4.6 | 40% | ❌ 18 pts to go |
| P04 | 3409 | 16.3% | 16.3% | -11.3 | 40% | ❌ 24 pts to go |
| P05 | 427 | 19.7% | 19.7% | -3.2 | 25% | 🟡 5 pts to go |
| P06M | 9350 | 8.8% | 8.8% | -16.8 | n/a | no target |
| P06T | 59340 | 7.5% | 7.5% | -23.4 | n/a | no target |
| P06 | 290 | 12.8% | 12.8% | +2.0 | 35% | ❌ 22 pts to go |
| P07 | 749 | 11.5% | 11.5% | +1.2 | 35% | ❌ 24 pts to go |
| P08 | 23364 | 10.4% | 10.4% | -0.7 | 35% | ❌ 25 pts to go |
| P09 | 303 | 16.2% | 16.2% | -0.9 | n/a | no target |
| P10R | 98530 | 7.1% | 7.1% |  | n/a | no target |
| P10 | 2699 | 6.5% | 6.5% | -3.1 | 30% | ❌ 24 pts to go |
| P11 | 9442 | 1.2% | 1.2% | -7.2 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | +2.0 | n/a | no target |
| P13 | 17822 | 21.0% | 21.0% | -4.9 | 30% | 🟡 9 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 100.0% | 100.0% | +5.6 | 100% | ✅ met |
| P01T | 332 | 91.9% | 91.9% | -1.6 | 100% | 🟡 8 pts to go |
| P01_GOLD | 626 | 89.5% | 89.5% | +1.8 | 100% | ❌ 10 pts to go |
| P02 | 465 | 95.3% | 95.3% | -1.5 | 100% | 🟡 5 pts to go |
| P03 | 256 | 89.5% | 89.5% | -2.3 | 100% | ❌ 10 pts to go |
| P04 | 3409 | 75.9% | 75.9% | -15.1 | 100% | ❌ 24 pts to go |
| P05 | 427 | 87.4% | 87.4% | +2.5 | 100% | ❌ 13 pts to go |
| P06M | 9350 | 98.8% | 98.8% | +26.8 | n/a | no target |
| P06T | 59340 | 77.4% | 77.4% | -2.8 | n/a | no target |
| P06 | 290 | 81.0% | 81.0% | +12.3 | 95% | ❌ 14 pts to go |
| P07 | 749 | 83.6% | 83.6% | +13.0 | 95% | ❌ 11 pts to go |
| P08 | 23364 | 80.2% | 80.2% | +14.0 | 95% | ❌ 15 pts to go |
| P09 | 303 | 95.7% | 95.7% | +0.2 | 100% | 🟡 4 pts to go |
| P10R | 98530 | 58.8% | 58.8% |  | n/a | no target |
| P10 | 2699 | 65.1% | 65.2% | -0.1 | 95% | ❌ 30 pts to go |
| P11 | 9442 | 87.2% | 87.2% | +52.8 | 80% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17822 | 75.2% | 75.2% | -0.9 | 95% | ❌ 20 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 85.6% | 85.6% | -3.3 | n/a | no target |
| P01T | 332 | 63.6% | 63.6% | -16.8 | n/a | no target |
| P01_GOLD | 626 | 69.5% | 69.5% | -0.7 | 90% | ❌ 20 pts to go |
| P02 | 465 | 75.7% | 75.7% | -4.0 | 95% | ❌ 19 pts to go |
| P03 | 256 | 73.8% | 73.8% | +0.2 | 95% | ❌ 21 pts to go |
| P04 | 3409 | 66.6% | 66.6% | -18.3 | 95% | ❌ 28 pts to go |
| P05 | 427 | 70.5% | 70.5% | -4.5 | 90% | ❌ 20 pts to go |
| P06M | 9350 | 86.4% | 86.4% | +2.5 | n/a | no target |
| P06T | 59340 | 47.9% | 47.9% | -29.4 | n/a | no target |
| P06 | 290 | 63.1% | 63.1% | -1.4 | 95% | ❌ 32 pts to go |
| P07 | 749 | 55.0% | 55.0% | -11.3 | 90% | ❌ 35 pts to go |
| P08 | 23364 | 58.8% | 58.8% | -15.9 | 95% | ❌ 36 pts to go |
| P09 | 303 | 86.1% | 86.1% | -2.9 | 100% | ❌ 14 pts to go |
| P10R | 98530 | 45.1% | 45.1% |  | n/a | no target |
| P10 | 2699 | 56.5% | 56.5% | -15.0 | 95% | ❌ 38 pts to go |
| P11 | 9442 | 11.2% | 11.2% | -17.7 | 75% | ❌ 64 pts to go |
| P12 | 8 | 75.0% | 75.0% | -14.5 | n/a | no target |
| P13 | 17822 | 47.6% | 47.6% | -31.7 | 95% | ❌ 47 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 71.1% | 71.1% | -6.7 | n/a | no target |
| P01T | 332 | 74.1% | 74.1% | -17.2 | 95% | ❌ 21 pts to go |
| P01_GOLD | 626 | 80.7% | 80.7% | -1.5 | 90% | 🟡 9 pts to go |
| P02 | 465 | 85.8% | 85.8% | -2.6 | 95% | 🟡 9 pts to go |
| P03 | 256 | 84.0% | 84.0% | -0.6 | 95% | ❌ 11 pts to go |
| P04 | 3409 | 83.3% | 83.3% | -0.9 | 90% | 🟡 7 pts to go |
| P05 | 427 | 88.5% | 88.5% | -1.1 | 95% | 🟡 6 pts to go |
| P06M | 9350 | 66.7% | 66.7% | -18.4 | n/a | no target |
| P06T | 59340 | 61.5% | 61.5% | -32.6 | n/a | no target |
| P06 | 290 | 82.1% | 82.1% | -8.3 | 100% | ❌ 18 pts to go |
| P07 | 749 | 77.2% | 77.2% | -10.9 | 100% | ❌ 23 pts to go |
| P08 | 23364 | 77.1% | 77.1% | -13.6 | 100% | ❌ 23 pts to go |
| P09 | 303 | 68.6% | 68.6% | -5.4 | n/a | no target |
| P10R | 98530 | 60.0% | 60.0% |  | n/a | no target |
| P10 | 2699 | 86.8% | 86.8% | -3.3 | 100% | ❌ 13 pts to go |
| P11 | 9442 | 18.8% | 18.8% | -17.7 | 80% | ❌ 61 pts to go |
| P12 | 8 | 75.0% | 75.0% | -9.2 | n/a | no target |
| P13 | 17822 | 51.0% | 51.0% | -33.2 | 95% | ❌ 44 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 4.1% | 4.1% | -12.6 | n/a | no target |
| P01T | 332 | 8.4% | 8.4% | -15.5 | n/a | no target |
| P01_GOLD | 626 | 14.2% | 14.2% | -0.1 | 25% | ❌ 11 pts to go |
| P02 | 465 | 24.5% | 24.5% | -3.2 | 40% | ❌ 16 pts to go |
| P03 | 256 | 9.0% | 9.0% | -1.6 | 20% | ❌ 11 pts to go |
| P04 | 3409 | 3.6% | 3.6% | -3.8 | 20% | ❌ 16 pts to go |
| P05 | 427 | 3.3% | 3.3% | -0.6 | 15% | ❌ 12 pts to go |
| P06M | 9350 | 0.3% | 0.3% | -4.5 | n/a | no target |
| P06T | 59340 | 0.4% | 0.4% | -2.8 | n/a | no target |
| P06 | 290 | 6.2% | 6.2% | +0.8 | n/a | no target |
| P07 | 749 | 7.3% | 7.3% | +1.0 | n/a | no target |
| P08 | 23364 | 0.3% | 0.3% | -0.7 | n/a | no target |
| P09 | 303 | 7.6% | 7.6% | -0.3 | n/a | no target |
| P10R | 98530 | 0.2% | 0.2% |  | n/a | no target |
| P10 | 2699 | 1.0% | 1.0% | -0.3 | n/a | no target |
| P11 | 9442 | 0.2% | 0.2% | -2.3 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | -10.5 | n/a | no target |
| P13 | 17822 | 0.4% | 0.4% | -0.2 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 26.8% | 26.8% | -12.1 | n/a | no target |
| P01T | 332 | 24.1% | 24.1% | -10.7 | 70% | ❌ 46 pts to go |
| P01_GOLD | 626 | 43.3% | 43.3% | +0.0 | 80% | ❌ 37 pts to go |
| P02 | 465 | 56.8% | 56.8% | -7.3 | 90% | ❌ 33 pts to go |
| P03 | 256 | 19.1% | 19.1% | -4.0 | 60% | ❌ 41 pts to go |
| P04 | 3409 | 23.7% | 23.7% | -26.8 | 85% | ❌ 61 pts to go |
| P05 | 427 | 11.9% | 11.9% | -1.1 | 50% | ❌ 38 pts to go |
| P06M | 9350 | 0.4% | 0.4% | -6.1 | n/a | no target |
| P06T | 59340 | 0.6% | 0.6% | -2.1 | n/a | no target |
| P06 | 290 | 16.2% | 16.2% | -1.9 | n/a | no target |
| P07 | 749 | 13.0% | 13.0% | -6.0 | n/a | no target |
| P08 | 23364 | 0.5% | 0.5% | -0.1 | n/a | no target |
| P09 | 303 | 77.6% | 77.6% | -3.0 | 95% | ❌ 17 pts to go |
| P10R | 98530 | 0.2% | 0.2% |  | n/a | no target |
| P10 | 2699 | 1.7% | 1.7% | -1.4 | n/a | no target |
| P11 | 9442 | 3.6% | 3.6% | -25.7 | n/a | no target |
| P12 | 8 | 25.0% | 25.0% | -6.6 | n/a | no target |
| P13 | 17822 | 0.7% | 0.7% | -0.3 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 7.2% | 7.2% | +7.2 | n/a | no target |
| P01T | 332 | 12.0% | 12.0% | -4.3 | n/a | no target |
| P01_GOLD | 626 | 33.9% | 33.9% | -0.1 | 70% | ❌ 36 pts to go |
| P02 | 465 | 38.9% | 38.9% | -5.4 | 75% | ❌ 36 pts to go |
| P03 | 256 | 19.1% | 19.1% | -4.0 | 55% | ❌ 36 pts to go |
| P04 | 3409 | 23.6% | 23.6% | -26.9 | 75% | ❌ 51 pts to go |
| P05 | 427 | 10.8% | 10.8% | -0.9 | 50% | ❌ 39 pts to go |
| P06M | 9350 | 0.2% | 0.2% | -1.6 | n/a | no target |
| P06T | 59340 | 0.4% | 0.4% | -1.1 | n/a | no target |
| P06 | 290 | 8.3% | 8.3% | -1.9 | n/a | no target |
| P07 | 749 | 6.4% | 6.4% | -3.9 | n/a | no target |
| P08 | 23364 | 0.2% | 0.2% | -0.3 | n/a | no target |
| P09 | 303 | 75.2% | 75.2% | -2.5 | 95% | ❌ 20 pts to go |
| P10R | 98530 | 0.2% | 0.2% |  | n/a | no target |
| P10 | 2699 | 1.0% | 1.0% | -0.8 | n/a | no target |
| P11 | 9442 | 3.6% | 3.6% | -25.3 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | -3.3 | n/a | no target |
| P13 | 17822 | 0.4% | 0.4% | -0.2 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 6.2% | 6.2% | -10.5 | n/a | no target |
| P01T | 332 | 9.3% | 9.3% | -10.3 | n/a | no target |
| P01_GOLD | 626 | 58.0% | 58.1% | +0.1 | 80% | ❌ 22 pts to go |
| P02 | 465 | 45.8% | 46.0% | -6.4 | 75% | ❌ 29 pts to go |
| P03 | 256 | 37.9% | 37.9% | -7.3 | 70% | ❌ 32 pts to go |
| P04 | 3409 | 23.1% | 23.6% | -25.6 | 70% | ❌ 47 pts to go |
| P05 | 427 | 14.3% | 14.3% | -2.1 | 50% | ❌ 36 pts to go |
| P06M | 9350 | 0.4% | 0.4% | -3.8 | n/a | no target |
| P06T | 59340 | 0.3% | 0.3% | -1.3 | n/a | no target |
| P06 | 290 | 13.4% | 13.4% | -10.7 | n/a | no target |
| P07 | 749 | 2.0% | 2.0% | -3.2 | n/a | no target |
| P08 | 23364 | 0.4% | 0.4% | -0.6 | n/a | no target |
| P09 | 303 | 45.9% | 46.2% | +1.8 | 80% | ❌ 34 pts to go |
| P10R | 98530 | 0.1% | 0.1% |  | n/a | no target |
| P10 | 2699 | 1.2% | 1.3% | -0.3 | n/a | no target |
| P11 | 9442 | 1.1% | 1.1% | -15.6 | n/a | no target |
| P12 | 8 | 37.5% | 37.5% | +5.9 | n/a | no target |
| P13 | 17822 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 11.3% | 11.3% | -27.6 | n/a | no target |
| P01T | 332 | 22.0% | 22.0% | -34.5 | 60% | ❌ 38 pts to go |
| P01_GOLD | 626 | 63.6% | 63.6% | +0.1 | 70% | 🟡 6 pts to go |
| P02 | 465 | 38.9% | 38.9% | -4.9 | 50% | ❌ 11 pts to go |
| P03 | 256 | 50.0% | 50.0% | -5.3 | 55% | 🟡 5 pts to go |
| P04 | 3409 | 13.3% | 13.3% | -9.6 | 40% | ❌ 27 pts to go |
| P05 | 427 | 17.3% | 17.3% | -0.1 | 40% | ❌ 23 pts to go |
| P06M | 9350 | 0.7% | 0.7% | -16.0 | n/a | no target |
| P06T | 59340 | 2.4% | 2.4% | -10.1 | n/a | no target |
| P06 | 290 | 19.7% | 19.7% | -11.0 | n/a | no target |
| P07 | 749 | 6.7% | 6.7% | -9.6 | n/a | no target |
| P08 | 23364 | 2.6% | 2.6% | -2.1 | n/a | no target |
| P09 | 303 | 5.9% | 5.9% | +0.1 | n/a | no target |
| P10R | 98530 | 0.2% | 0.2% |  | n/a | no target |
| P10 | 2699 | 4.5% | 4.5% | +0.6 | n/a | no target |
| P11 | 9442 | 4.3% | 4.3% | -3.3 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | -3.3 | n/a | no target |
| P13 | 17822 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 16.5% | 16.5% | -27.9 | n/a | no target |
| P01T | 332 | 25.3% | 25.3% | -44.3 | 65% | ❌ 40 pts to go |
| P01_GOLD | 626 | 69.0% | 69.0% | -0.2 | 70% | 🟡 1 pts to go |
| P02 | 465 | 23.9% | 23.9% | -2.3 | 50% | ❌ 26 pts to go |
| P03 | 256 | 52.3% | 52.3% | -3.9 | 60% | 🟡 8 pts to go |
| P04 | 3409 | 5.8% | 5.8% | -4.1 | 40% | ❌ 34 pts to go |
| P05 | 427 | 19.7% | 19.7% | -1.7 | 45% | ❌ 25 pts to go |
| P06M | 9350 | 0.3% | 0.3% | -6.8 | n/a | no target |
| P06T | 59340 | 0.6% | 0.6% | -3.7 | n/a | no target |
| P06 | 290 | 31.7% | 31.7% | -16.5 | n/a | no target |
| P07 | 749 | 6.9% | 6.9% | -16.9 | n/a | no target |
| P08 | 23364 | 1.1% | 1.1% | -1.3 | n/a | no target |
| P09 | 303 | 9.9% | 9.9% | +1.2 | n/a | no target |
| P10R | 98530 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2699 | 2.6% | 2.6% | +0.5 | n/a | no target |
| P11 | 9442 | 1.0% | 1.0% | -5.8 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | -10.5 | n/a | no target |
| P13 | 17822 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 6.2% | 6.2% | -4.9 | n/a | no target |
| P01T | 332 | 14.5% | 14.5% | -30.1 | n/a | no target |
| P01_GOLD | 626 | 49.8% | 49.8% | +0.0 | 50% | 🟡 0 pts to go |
| P02 | 465 | 37.4% | 37.4% | -5.2 | n/a | no target |
| P03 | 256 | 53.1% | 53.1% | -5.6 | 60% | 🟡 7 pts to go |
| P04 | 3409 | 12.9% | 12.9% | -13.5 | n/a | no target |
| P05 | 427 | 15.2% | 15.2% | -1.5 | n/a | no target |
| P06M | 9350 | 0.3% | 0.3% | -3.9 | n/a | no target |
| P06T | 59340 | 0.5% | 0.5% | -3.5 | n/a | no target |
| P06 | 290 | 21.7% | 21.7% | -13.8 | n/a | no target |
| P07 | 749 | 7.2% | 7.2% | -11.5 | n/a | no target |
| P08 | 23364 | 0.5% | 0.5% | -1.0 | n/a | no target |
| P09 | 303 | 18.2% | 18.2% | -0.7 | n/a | no target |
| P10R | 98530 | 0.1% | 0.1% |  | n/a | no target |
| P10 | 2699 | 2.3% | 2.3% | -0.1 | n/a | no target |
| P11 | 9442 | 0.8% | 0.8% | -7.0 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | -21.1 | n/a | no target |
| P13 | 17822 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 11.3% | 11.3% | -16.5 | 15% | 🟡 4 pts to go |
| P01T | 332 | 11.1% | 11.1% | -18.2 | 15% | 🟡 4 pts to go |
| P01_GOLD | 626 | 35.3% | 35.3% | +0.2 | 40% | 🟡 5 pts to go |
| P02 | 465 | 12.5% | 12.7% | -1.4 | 25% | ❌ 12 pts to go |
| P03 | 256 | 18.0% | 18.0% | -3.6 | 25% | 🟡 7 pts to go |
| P04 | 3409 | 2.8% | 2.8% | -2.4 | 15% | ❌ 12 pts to go |
| P05 | 427 | 6.8% | 6.8% | -1.3 | 15% | 🟡 8 pts to go |
| P06M | 9350 | 0.6% | 0.6% | -5.4 | 15% | ❌ 14 pts to go |
| P06T | 59340 | 0.4% | 0.4% | -1.1 | 15% | ❌ 15 pts to go |
| P06 | 290 | 9.3% | 9.3% | -0.9 | 15% | 🟡 6 pts to go |
| P07 | 749 | 3.2% | 3.2% | -3.5 | 15% | ❌ 12 pts to go |
| P08 | 23364 | 0.4% | 0.4% | -0.5 | 15% | ❌ 15 pts to go |
| P09 | 303 | 1.0% | 1.0% | +0.2 | 15% | ❌ 14 pts to go |
| P10R | 98530 | 0.4% | 0.4% |  | 15% | ❌ 15 pts to go |
| P10 | 2699 | 1.0% | 1.0% | -0.4 | 15% | ❌ 14 pts to go |
| P11 | 9442 | 0.2% | 0.2% | -1.1 | 15% | ❌ 15 pts to go |
| P12 | 8 | 12.5% | 12.5% | +12.5 | 15% | 🟡 2 pts to go |
| P13 | 17822 | 0.4% | 0.4% | -0.1 | 15% | ❌ 15 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 6.2% | 6.2% | -4.9 | 15% | 🟡 9 pts to go |
| P01T | 332 | 12.0% | 12.0% | -20.6 | 25% | ❌ 13 pts to go |
| P01_GOLD | 626 | 29.2% | 29.2% | +0.0 | 25% | ✅ met |
| P02 | 465 | 25.4% | 25.4% | -2.6 | 15% | ✅ met |
| P03 | 256 | 21.5% | 21.5% | -4.5 | 15% | ✅ met |
| P04 | 3409 | 4.1% | 4.1% | -4.1 | 15% | ❌ 11 pts to go |
| P05 | 427 | 10.8% | 10.8% | -1.2 | 15% | 🟡 4 pts to go |
| P06M | 9350 | 0.2% | 0.2% | -2.2 | 15% | ❌ 15 pts to go |
| P06T | 59340 | 0.3% | 0.3% | -2.4 | 15% | ❌ 15 pts to go |
| P06 | 290 | 7.6% | 7.6% | -4.4 | 15% | 🟡 7 pts to go |
| P07 | 749 | 3.1% | 3.1% | -4.4 | 15% | ❌ 12 pts to go |
| P08 | 23364 | 0.4% | 0.4% | -0.6 | 15% | ❌ 15 pts to go |
| P09 | 303 | 1.0% | 1.0% | +0.2 | 15% | ❌ 14 pts to go |
| P10R | 98530 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P10 | 2699 | 1.6% | 1.6% | +0.2 | 15% | ❌ 13 pts to go |
| P11 | 9442 | 0.5% | 0.5% | -4.6 | 15% | ❌ 14 pts to go |
| P12 | 8 | 25.0% | 25.0% | -1.3 | 15% | ✅ met |
| P13 | 17822 | 0.0% | 0.0% | -0.1 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 0.0% | 0.0% | -5.6 | 20% | ❌ 20 pts to go |
| P01T | 332 | 3.9% | 3.9% | -5.9 | 20% | ❌ 16 pts to go |
| P01_GOLD | 626 | 4.3% | 4.3% | +0.0 | 20% | ❌ 16 pts to go |
| P02 | 465 | 1.3% | 1.3% | -0.2 | 20% | ❌ 19 pts to go |
| P03 | 256 | 1.6% | 1.6% | -0.3 | 20% | ❌ 18 pts to go |
| P04 | 3409 | 0.6% | 0.6% | -0.4 | 20% | ❌ 19 pts to go |
| P05 | 427 | 1.2% | 1.2% | +0.2 | 20% | ❌ 19 pts to go |
| P06M | 9350 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 59340 | 0.0% | 0.0% | -0.2 | 20% | ❌ 20 pts to go |
| P06 | 290 | 1.4% | 1.4% | -2.2 | 20% | ❌ 19 pts to go |
| P07 | 749 | 0.4% | 0.4% | -0.4 | 20% | ❌ 20 pts to go |
| P08 | 23364 | 0.0% | 0.0% | -0.2 | 20% | ❌ 20 pts to go |
| P09 | 303 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10R | 98530 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P10 | 2699 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 9442 | 0.0% | 0.0% | -0.6 | 20% | ❌ 20 pts to go |
| P12 | 8 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 17822 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 1.0% | 1.0% | -4.6 | 15% | ❌ 14 pts to go |
| P01T | 332 | 2.4% | 2.4% | -5.2 | 15% | ❌ 13 pts to go |
| P01_GOLD | 626 | 10.5% | 10.5% | -0.1 | 15% | 🟡 4 pts to go |
| P02 | 465 | 12.0% | 12.0% | -1.4 | 15% | 🟡 3 pts to go |
| P03 | 256 | 20.7% | 20.7% | -3.3 | 15% | ✅ met |
| P04 | 3409 | 2.4% | 2.4% | -2.2 | 15% | ❌ 13 pts to go |
| P05 | 427 | 3.0% | 3.0% | +0.1 | 15% | ❌ 12 pts to go |
| P06M | 9350 | 0.2% | 0.2% | -2.2 | 15% | ❌ 15 pts to go |
| P06T | 59340 | 0.2% | 0.2% | -1.2 | 15% | ❌ 15 pts to go |
| P06 | 290 | 5.2% | 5.2% | -0.2 | 15% | 🟡 10 pts to go |
| P07 | 749 | 1.7% | 1.7% | -1.9 | 15% | ❌ 13 pts to go |
| P08 | 23364 | 0.4% | 0.4% | -0.3 | 15% | ❌ 15 pts to go |
| P09 | 303 | 0.7% | 0.7% | +0.2 | 15% | ❌ 14 pts to go |
| P10R | 98530 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P10 | 2699 | 0.9% | 0.9% | +0.1 | 15% | ❌ 14 pts to go |
| P11 | 9442 | 0.3% | 0.3% | -1.8 | 15% | ❌ 15 pts to go |
| P12 | 8 | 0.0% | 0.0% | -5.3 | 15% | ❌ 15 pts to go |
| P13 | 17822 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 7.2% | 7.2% | -3.9 | 20% | ❌ 13 pts to go |
| P01T | 332 | 15.1% | 15.1% | -26.2 | 40% | ❌ 25 pts to go |
| P01_GOLD | 626 | 45.8% | 45.8% | +0.0 | 40% | ✅ met |
| P02 | 465 | 42.8% | 42.8% | -5.7 | 20% | ✅ met |
| P03 | 256 | 48.8% | 48.8% | -7.0 | 35% | ✅ met |
| P04 | 3409 | 15.4% | 15.4% | -14.9 | 20% | 🟡 5 pts to go |
| P05 | 427 | 14.8% | 14.8% | -1.9 | 20% | 🟡 5 pts to go |
| P06M | 9350 | 0.5% | 0.5% | -3.7 | 20% | ❌ 20 pts to go |
| P06T | 59340 | 0.7% | 0.7% | -3.8 | 20% | ❌ 19 pts to go |
| P06 | 290 | 22.1% | 22.1% | -13.4 | 20% | ✅ met |
| P07 | 749 | 7.1% | 7.1% | -7.6 | 20% | ❌ 13 pts to go |
| P08 | 23364 | 0.9% | 0.9% | -1.4 | 20% | ❌ 19 pts to go |
| P09 | 303 | 18.2% | 18.2% | -3.8 | 20% | 🟡 2 pts to go |
| P10R | 98530 | 0.2% | 0.2% |  | 20% | ❌ 20 pts to go |
| P10 | 2699 | 3.4% | 3.4% | +0.8 | 20% | ❌ 17 pts to go |
| P11 | 9442 | 1.0% | 1.0% | -7.0 | 20% | ❌ 19 pts to go |
| P12 | 8 | 0.0% | 0.0% | -15.8 | 20% | ❌ 20 pts to go |
| P13 | 17822 | 0.5% | 0.5% | -0.1 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 44.3% | 44.3% | +44.3 | n/a | no target |
| P01T | 332 | 0.3% | 0.3% | -0.8 | n/a | no target |
| P01_GOLD | 626 | 69.5% | 69.5% | -0.2 | 95% | ❌ 26 pts to go |
| P02 | 465 | 63.0% | 63.0% | -10.3 | 95% | ❌ 32 pts to go |
| P03 | 256 | 54.7% | 54.7% | -12.6 | 90% | ❌ 35 pts to go |
| P04 | 3409 | 27.1% | 27.1% | -31.3 | 85% | ❌ 58 pts to go |
| P05 | 427 | 36.5% | 36.5% | +1.6 | 75% | ❌ 38 pts to go |
| P06M | 9350 | 50.1% | 50.1% | +50.1 | n/a | no target |
| P06T | 59340 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 290 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 749 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 23364 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 89.4% | 89.4% | -1.4 | 100% | ❌ 11 pts to go |
| P10R | 98530 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2699 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 9442 | 0.9% | 0.9% | -17.9 | 60% | ❌ 59 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 44.3% | 44.3% | +44.3 | n/a | no target |
| P01T | 332 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 626 | 72.8% | 72.8% | -0.1 | 100% | ❌ 27 pts to go |
| P02 | 465 | 66.5% | 66.5% | -10.7 | 100% | ❌ 34 pts to go |
| P03 | 256 | 60.5% | 60.5% | -14.0 | n/a | no target |
| P04 | 3409 | 27.8% | 27.8% | -32.2 | 95% | ❌ 67 pts to go |
| P05 | 427 | 33.0% | 33.0% | +1.8 | 80% | ❌ 47 pts to go |
| P06M | 9350 | 50.1% | 50.1% | +50.1 | n/a | no target |
| P06T | 59340 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 290 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 749 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 23364 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 92.7% | 92.7% | -0.7 | 100% | 🟡 7 pts to go |
| P10R | 98530 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2699 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 9442 | 1.0% | 1.0% | -19.0 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 78.4% | 78.4% | +78.4 | n/a | no target |
| P01T | 332 | 0.3% | 0.3% | -0.8 | n/a | no target |
| P01_GOLD | 626 | 51.6% | 51.6% | -0.3 | 85% | ❌ 33 pts to go |
| P02 | 465 | 57.6% | 57.6% | -9.2 | 90% | ❌ 32 pts to go |
| P03 | 256 | 44.1% | 44.1% | -10.7 | 85% | ❌ 41 pts to go |
| P04 | 3409 | 30.4% | 30.4% | -33.7 | 90% | ❌ 60 pts to go |
| P05 | 427 | 32.8% | 32.8% | -2.4 | 75% | ❌ 42 pts to go |
| P06M | 9350 | 90.4% | 90.4% | +90.4 | n/a | no target |
| P06T | 59340 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 290 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 749 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 23364 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 85.1% | 85.1% | -0.5 | 95% | 🟡 10 pts to go |
| P10R | 98530 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2699 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 9442 | 0.8% | 0.8% | -16.5 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 79.4% | 79.4% | +79.4 | n/a | no target |
| P01T | 332 | 0.3% | 0.3% | -0.8 | n/a | no target |
| P01_GOLD | 626 | 51.8% | 51.8% | -0.3 | 85% | ❌ 33 pts to go |
| P02 | 465 | 52.7% | 52.7% | -8.4 | 90% | ❌ 37 pts to go |
| P03 | 256 | 45.3% | 45.3% | -10.9 | 85% | ❌ 40 pts to go |
| P04 | 3409 | 26.0% | 26.0% | -28.3 | 90% | ❌ 64 pts to go |
| P05 | 427 | 42.9% | 42.9% | +1.2 | 75% | ❌ 32 pts to go |
| P06M | 9350 | 83.7% | 83.7% | +83.7 | n/a | no target |
| P06T | 59340 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 290 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 749 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 23364 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10R | 98530 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2699 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 9442 | 0.7% | 0.7% | -13.4 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 85.6% | 85.6% | +85.6 | n/a | no target |
| P01T | 332 | 92.2% | 92.2% | +10.7 | n/a | no target |
| P01_GOLD | 626 | 85.5% | 85.5% | -0.2 | 100% | ❌ 14 pts to go |
| P02 | 465 | 75.7% | 75.7% | -6.0 | 100% | ❌ 24 pts to go |
| P03 | 256 | 92.2% | 92.2% | -0.1 | n/a | no target |
| P04 | 3409 | 51.5% | 51.5% | -21.1 | 95% | ❌ 44 pts to go |
| P05 | 427 | 77.8% | 77.8% | +2.3 | 95% | ❌ 17 pts to go |
| P06M | 9350 | 98.3% | 98.3% | +97.7 | n/a | no target |
| P06T | 59340 | 83.7% | 83.7% | +0.3 | n/a | no target |
| P06 | 290 | 26.2% | 26.2% | -49.7 | n/a | no target |
| P07 | 749 | 19.1% | 19.1% | -57.9 | n/a | no target |
| P08 | 23364 | 11.0% | 11.0% | -73.9 | n/a | no target |
| P09 | 303 | 98.7% | 98.7% | -0.3 | 100% | 🟡 1 pts to go |
| P10R | 98530 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2699 | 71.7% | 71.7% | -26.7 | n/a | no target |
| P11 | 9442 | 16.1% | 16.1% | -73.8 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 85.6% | 85.6% | +85.6 | n/a | no target |
| P01T | 332 | 92.2% | 92.2% | +10.7 | n/a | no target |
| P01_GOLD | 626 | 88.7% | 88.7% | -0.2 | 100% | ❌ 11 pts to go |
| P02 | 465 | 76.8% | 77.0% | -6.1 | 100% | ❌ 23 pts to go |
| P03 | 256 | 93.0% | 93.0% | -0.8 | n/a | no target |
| P04 | 3409 | 55.1% | 55.1% | -23.9 | 95% | ❌ 40 pts to go |
| P05 | 427 | 90.2% | 90.2% | +0.1 | 70% | ✅ met |
| P06M | 9350 | 98.3% | 98.3% | +97.7 | n/a | no target |
| P06T | 59340 | 83.7% | 83.7% | +0.3 | n/a | no target |
| P06 | 290 | 26.2% | 26.2% | -49.7 | n/a | no target |
| P07 | 749 | 19.1% | 19.1% | -57.9 | n/a | no target |
| P08 | 23364 | 11.0% | 11.0% | -73.9 | n/a | no target |
| P09 | 303 | 98.7% | 98.7% | -0.3 | 100% | 🟡 1 pts to go |
| P10R | 98530 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2699 | 71.7% | 71.7% | -26.7 | n/a | no target |
| P11 | 9442 | 16.1% | 16.1% | -74.2 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17822 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 332 | 0.0% | 0.0% | -1.1 | n/a | no target |
| P01_GOLD | 626 | 16.8% | 16.8% | -0.5 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 363 rows, 28.9% filled |
| P02 | 465 | 11.2% | 11.2% | -1.9 | n/a | no target · rows from a source that publishes bids: 290 rows, 17.9% filled |
| P03 | 256 | 13.3% | 13.3% | -3.0 | n/a | no target · rows from a source that publishes bids: 139 rows, 24.5% filled |
| P04 | 3409 | 1.6% | 1.6% | -2.1 | n/a | no target · rows from a source that publishes bids: 872 rows, 6.3% filled |
| P05 | 427 | 3.0% | 3.0% | -0.4 | n/a | no target · rows from a source that publishes bids: 53 rows, 24.5% filled |
| P06M | 9350 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 59340 | 0.0% | 0.0% | -0.1 | n/a | no target |
| P06 | 290 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 749 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 23364 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 3.0% | 3.0% | -0.1 | n/a | no target · rows from a source that publishes bids: 290 rows, 3.1% filled |
| P10R | 98530 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2699 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 9442 | 0.1% | 0.1% | -2.6 | n/a | no target · rows from a source that publishes bids: 87 rows, 12.6% filled |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 8 rows, 0.0% filled |
| P13 | 17822 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 332 | 0.3% | 98.5% | +0.3 | n/a | no target |
| P01_GOLD | 626 | 53.2% | 82.4% | +0.0 | 90% | ❌ 37 pts to go |
| P02 | 465 | 52.5% | 87.5% | -8.6 | 90% | ❌ 38 pts to go |
| P03 | 256 | 45.7% | 80.1% | -10.5 | 90% | ❌ 44 pts to go |
| P04 | 3409 | 20.9% | 93.3% | -24.4 | 90% | ❌ 69 pts to go |
| P05 | 427 | 0.0% | 82.9% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 9350 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 59340 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 290 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 749 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 23364 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 303 | 2.3% | 4.0% | +0.2 | 90% | ❌ 88 pts to go |
| P10R | 98530 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2699 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 9442 | 0.6% | 99.5% | -12.1 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17822 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 332 | 0.6% | 98.8% | +0.6 | n/a | no target |
| P01_GOLD | 626 | 25.9% | 55.1% | -0.1 | 90% | ❌ 64 pts to go |
| P02 | 465 | 51.6% | 86.7% | -8.3 | n/a | no target |
| P03 | 256 | 25.0% | 59.4% | -5.8 | n/a | no target |
| P04 | 3409 | 22.9% | 95.3% | -26.8 | n/a | no target |
| P05 | 427 | 0.5% | 83.4% | +0.0 | n/a | no target |
| P06M | 9350 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 59340 | 0.1% | 99.9% | +0.1 | n/a | no target |
| P06 | 290 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 749 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 23364 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 303 | 41.9% | 43.6% | -2.5 | n/a | no target |
| P10R | 98530 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2699 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 9442 | 0.6% | 99.5% | -11.0 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17822 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 332 | 1.5% | 99.7% | -0.7 | n/a | no target |
| P01_GOLD | 626 | 51.8% | 81.0% | +0.2 | 95% | ❌ 43 pts to go |
| P02 | 465 | 56.6% | 91.6% | -9.0 | n/a | no target |
| P03 | 256 | 48.0% | 82.4% | -11.1 | n/a | no target |
| P04 | 3409 | 23.1% | 95.6% | -27.2 | n/a | no target |
| P05 | 427 | 4.7% | 87.6% | -0.5 | n/a | no target |
| P06M | 9350 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 59340 | 0.1% | 100.0% | +0.1 | n/a | no target |
| P06 | 290 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 749 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 23364 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 303 | 64.0% | 65.7% | -3.5 | n/a | no target |
| P10R | 98530 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2699 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 9442 | 0.6% | 99.5% | -12.1 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17822 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 332 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 465 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 256 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3409 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 427 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 9350 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 59340 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 290 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 749 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 23364 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 98530 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2699 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 9442 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17822 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 332 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 465 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 256 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3409 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 427 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 9350 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 59340 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 290 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 749 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 23364 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 98530 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2699 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 9442 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17822 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 97 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 332 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 626 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 465 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 256 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3409 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 427 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 9350 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 59340 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 290 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 749 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 23364 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 98530 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2699 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 9442 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17822 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |


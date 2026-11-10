# Coverage vs the downstream team's targets — 2026-11-10

Benchmarks (field × package with a numeric target): **54 of 446 met** (12.1%); 91 within 10 points; 301 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 65, P01T 304, P01_GOLD 625, P02 462, P03 255, P04 3254, P05 413, P06M 6002, P06T 53606, P06 278, P07 680, P08 20545, P09 303, P10R 96430, P10 2607, P11 9344, P12 8, P13 17855

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 65 | 0.0% | 23.1% | 8 | PO rule (53 rows) |
| P01T | 304 | 1.0% | 23.0% | 7 | payment terms (229 rows) |
| P01_GOLD | 625 | 23.5% | 67.4% | 9 | payment terms (214 rows) |
| P02 | 462 | 7.6% | 52.2% | 9 | PO rule (351 rows) |
| P03 | 255 | 13.7% | 56.9% | 9 | PO rule (121 rows) |
| P04 | 3254 | 1.4% | 17.9% | 6 | PO rule (3055 rows) |
| P05 | 413 | 1.0% | 16.9% | 7 | payment terms (337 rows) |
| P06M | 6002 | 0.0% | 2.1% | 8 | PO rule (5972 rows) |
| P06T | 53606 | 0.0% | 2.3% | 6 | PO rule (53266 rows) |
| P06 | 278 | 0.0% | 7.2% | 6 | reference to quote (PO / contract / vendor id) (278 rows) |
| P07 | 680 | 0.0% | 1.6% | 6 | reference to quote (PO / contract / vendor id) (680 rows) |
| P08 | 20545 | 0.0% | 0.2% | 5 | reference to quote (PO / contract / vendor id) (20545 rows) |
| P09 | 303 | 1.0% | 43.9% | 8 | payment terms (283 rows) |
| P10R | 96430 | 0.0% | 17.1% | 7 | PO rule (96392 rows) |
| P10 | 2607 | 0.0% | 0.7% | 5 | reference to quote (PO / contract / vendor id) (2607 rows) |
| P11 | 9344 | 0.1% | 2.3% | 6 | PO rule (9241 rows) |
| P12 | 8 | 0.0% | 50.0% | 9 | PO rule (8 rows) |
| P13 | 17855 | 0.0% | 0.0% | 6 | reference to quote (PO / contract / vendor id) (17855 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 65 | 6 | 6 | 53 | 0 | 0 | 71 |
| P01T | 304 | 31 | 55 | 218 | 0 | 0 | 71 |
| P01_GOLD | 625 | 223 | 184 | 218 | 0 | 0 | 81 |
| P02 | 462 | 0 | 187 | 275 | 0 | 0 | 66 |
| P03 | 255 | 0 | 0 | 241 | 14 | 0 | 57 |
| P04 | 3254 | 0 | 0 | 2732 | 522 | 0 | 46 |
| P05 | 413 | 15 | 28 | 350 | 20 | 0 | 51 |
| P06M | 6002 | 0 | 3 | 5931 | 68 | 0 | 51 |
| P06T | 53606 | 0 | 40 | 43449 | 10117 | 0 | 38 |
| P06 | 278 | 19 | 43 | 216 | 0 | 0 | 70 |
| P07 | 680 | 0 | 23 | 632 | 25 | 0 | 53 |
| P08 | 20545 | 0 | 0 | 17414 | 3131 | 0 | 43 |
| P09 | 303 | 3 | 12 | 285 | 3 | 0 | 53 |
| P10R | 96430 | 2 | 10 | 62440 | 33978 | 0 | 38 |
| P10 | 2607 | 2 | 13 | 1899 | 693 | 0 | 43 |
| P11 | 9344 | 6 | 9 | 42 | 0 | 9287 | 23 |
| P12 | 8 | 0 | 1 | 7 | 0 | 0 | 54 |
| P13 | 17855 | 2 | 13 | 14119 | 3721 | 0 | 43 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 65 | 50 | 76.9% | the buyer's PO / reference rule (7) |
| P01T | 304 | 141 | 46.4% | bill-to legal name and address (125) |
| P01_GOLD | 625 | 453 | 72.5% | bill-to legal name and address (121) |
| P02 | 462 | 306 | 66.2% | the buyer's PO / reference rule (79) |
| P03 | 255 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (255) |
| P04 | 3254 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3254) |
| P05 | 413 | 46 | 11.1% | a confirmed invoicing / AP or finance channel (326) |
| P06M | 6002 | 39 | 0.6% | a confirmed invoicing / AP or finance channel (5930) |
| P06T | 53606 | 294 | 0.5% | a confirmed invoicing / AP or finance channel (52805) |
| P06 | 278 | 43 | 15.5% | bill-to legal name and address (124) |
| P07 | 680 | 10 | 1.5% | bill-to legal name and address (302) |
| P08 | 20545 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (20545) |
| P09 | 303 | 40 | 13.2% | a confirmed invoicing / AP or finance channel (253) |
| P10R | 96430 | 416 | 0.4% | a confirmed invoicing / AP or finance channel (95308) |
| P10 | 2607 | 4 | 0.2% | a confirmed invoicing / AP or finance channel (2512) |
| P11 | 9344 | 10 | 0.1% | a confirmed invoicing / AP or finance channel (9287) |
| P12 | 8 | 3 | 37.5% | a confirmed invoicing / AP or finance channel (5) |
| P13 | 17855 | 7 | 0.0% | a confirmed invoicing / AP or finance channel (17498) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 65 | 6 | 9.2% | 6 | 0 | the vendor's GST/HST number (BN9) (51) |
| P01T | 304 | 63 | 20.7% | 19 | 0 | the vendor's GST/HST number (BN9) (160) |
| P01_GOLD | 625 | 392 | 62.7% | 12 | 0 | the vendor's GST/HST number (BN9) (151) |
| P02 | 462 | 210 | 45.5% | 21 | 0 | the vendor's GST/HST number (BN9) (192) |
| P03 | 255 | 17 | 6.7% | 0 | 129 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (89) |
| P04 | 3254 | 42 | 1.3% | 8 | 746 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2399) |
| P05 | 413 | 22 | 5.3% | 8 | 100 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (219) |
| P06M | 6002 | 1 | 0.0% | 10 | 112 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (5803) |
| P06T | 53606 | 56 | 0.1% | 83 | 6665 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (45998) |
| P06 | 278 | 15 | 5.4% | 24 | 0 | the vendor's GST/HST number (BN9) (163) |
| P07 | 680 | 6 | 0.9% | 47 | 20 | the vendor's GST/HST number (BN9) (371) |
| P08 | 20545 | 2 | 0.0% | 5 | 1547 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (18933) |
| P09 | 303 | 39 | 12.9% | 1 | 122 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (122) |
| P10R | 96430 | 827 | 0.9% | 0 | 50572 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (44670) |
| P10 | 2607 | 4 | 0.2% | 18 | 338 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2144) |
| P11 | 9344 | 11 | 0.1% | 18 | 0 | a confirmed invoicing / AP or finance channel (9250) |
| P12 | 8 | 2 | 25.0% | 0 | 3 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2) |
| P13 | 17855 | 10 | 0.1% | 256 | 10544 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (6914) |
| **all** | 213036 | 1725 | 0.8% | 536 | 70898 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 59 | 0 | 0 | 0 | 14 | 7 | 0 | 53 | 56 | 0 |
| P01T | 273 | 0 | 0 | 0 | 105 | 117 | 18 | 220 | 231 | 30 |
| P01_GOLD | 402 | 0 | 0 | 0 | 11 | 103 | 38 | 193 | 228 | 59 |
| P02 | 462 | 0 | 462 | 0 | 38 | 66 | 20 | 351 | 281 | 21 |
| P03 | 255 | 0 | 255 | 0 | 12 | 54 | 24 | 121 | 127 | 27 |
| P04 | 3254 | 0 | 3254 | 0 | 1248 | 1359 | 705 | 3055 | 2799 | 137 |
| P05 | 398 | 0 | 345 | 0 | 64 | 130 | 48 | 329 | 339 | 52 |
| P06M | 6002 | 0 | 6002 | 0 | 2045 | 629 | 110 | 5972 | 5938 | 4 |
| P06T | 53606 | 0 | 53606 | 0 | 39638 | 36715 | 11859 | 53266 | 52299 | 347 |
| P06 | 259 | 0 | 0 | 0 | 92 | 111 | 49 | 183 | 221 | 5 |
| P07 | 680 | 0 | 680 | 0 | 359 | 343 | 108 | 626 | 630 | 15 |
| P08 | 20545 | 0 | 20545 | 0 | 14224 | 11744 | 4018 | 20278 | 19899 | 206 |
| P09 | 300 | 0 | 279 | 0 | 9 | 69 | 3 | 273 | 285 | 44 |
| P10R | 96428 | 0 | 96257 | 0 | 72563 | 70661 | 39220 | 96392 | 96242 | 20 |
| P10 | 2605 | 0 | 2569 | 0 | 1177 | 1571 | 898 | 2537 | 2486 | 111 |
| P11 | 9338 | 9287 | 9226 | 0 | 7955 | 8115 | 2725 | 9241 | 8929 | 39 |
| P12 | 8 | 0 | 7 | 0 | 0 | 2 | 0 | 8 | 7 | 0 |
| P13 | 17853 | 0 | 17745 | 0 | 8102 | 10230 | 4316 | 17818 | 17814 | 22 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_ap_cycle_published | P10R | 0.0% | 20% | 19269 |
| ap_system_hint | P10R | 0.2% | 20% | 19092 |
| buyer_tax_exempt_status | P10R | 0.0% | 15% | 14444 |
| buyer_esignature_preference | P10R | 0.0% | 15% | 14431 |
| buyer_payment_method_preference | P10R | 0.4% | 15% | 14063 |
| vendor_registered_address | P08 | 15.0% | 70% | 11305 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 10703 |
| ap_system_hint | P06T | 0.8% | 20% | 10298 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 7910 |
| vendor_bn9 | P08 | 11.6% | 50% | 7880 |
| buyer_tax_exempt_status | P06T | 0.3% | 15% | 7876 |
| buyer_phone | P13 | 51.0% | 95% | 7855 |
| buyer_payment_method_preference | P06T | 0.5% | 15% | 7782 |
| buyer_logo_url | P13 | 54.4% | 95% | 7247 |
| buyer_legal_name_as_published | P08 | 42.8% | 75% | 6608 |
| buyer_phone | P08 | 63.6% | 95% | 6442 |
| vendor_phone | P11 | 8.9% | 75% | 6172 |
| vendor_emails | P11 | 6.7% | 70% | 5914 |
| contract_value | P11 | 0.9% | 60% | 5520 |
| award_or_notice_id | P11 | 0.9% | 60% | 5519 |
| buyer_phone | P11 | 16.2% | 75% | 5496 |
| vendor_phone | P08 | 58.3% | 85% | 5489 |
| buyer_logo_url | P11 | 26.8% | 80% | 4973 |
| vendor_emails | P08 | 51.1% | 75% | 4914 |
| buyer_bn_as_published | P08 | 11.1% | 35% | 4905 |
| invoice_reference_hint | P08 | 1.3% | 25% | 4870 |
| buyer_legal_name_as_published | P11 | 13.2% | 65% | 4845 |
| mta_sts | P10R | 95.0% | 100% | 4796 |
| tls_rpt | P10R | 95.0% | 100% | 4796 |
| bimi | P10R | 95.0% | 100% | 4796 |
| commodity_codes | P11 | 0.7% | 50% | 4609 |
| vendor_trading_name | P08 | 28.5% | 50% | 4423 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 4101 |
| ap_system_hint | P08 | 1.0% | 20% | 3900 |
| solicitation_or_tender_number | P11 | 0.9% | 40% | 3657 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 3569 |
| vendor_logo_url | P08 | 82.6% | 100% | 3567 |
| ap_system_hint | P13 | 0.6% | 20% | 3465 |
| buyer_address | P13 | 75.8% | 95% | 3433 |
| buyer_logo_url | P08 | 84.0% | 100% | 3295 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 84.6% | 84.6% | +40.2 | 50% | ✅ met |
| P01T | 304 | 89.1% | 89.1% | +17.4 | 50% | ✅ met |
| P01_GOLD | 625 | 92.2% | 94.4% | -0.3 | 95% | 🟡 3 pts to go |
| P02 | 462 | 74.2% | 75.8% | -9.7 | 95% | ❌ 21 pts to go |
| P03 | 255 | 82.4% | 85.5% | -10.4 | 95% | ❌ 13 pts to go |
| P04 | 3254 | 34.4% | 35.9% | -34.2 | 90% | ❌ 56 pts to go |
| P05 | 413 | 39.5% | 42.4% | -1.6 | 70% | ❌ 30 pts to go |
| P06M | 6002 | 92.0% | 92.0% | +84.9 | n/a | no target |
| P06T | 53606 | 81.3% | 81.3% | +76.9 | n/a | no target |
| P06 | 278 | 34.2% | 34.2% | -14.0 | 30% | ✅ met |
| P07 | 680 | 7.9% | 7.9% | -15.9 | 30% | ❌ 22 pts to go |
| P08 | 20545 | 1.3% | 1.3% | -1.1 | 25% | ❌ 24 pts to go |
| P09 | 303 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10R | 96430 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2607 | 2.7% | 2.7% | +0.5 | 25% | ❌ 22 pts to go |
| P11 | 9344 | 49.2% | 49.4% | +25.1 | 60% | ❌ 11 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17855 | 0.2% | 0.2% | +0.0 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 304 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 625 | 6.1% | 6.1% | -0.1 | 50% | ❌ 44 pts to go |
| P02 | 462 | 6.3% | 6.3% | -0.9 | 50% | ❌ 44 pts to go |
| P03 | 255 | 1.6% | 1.6% | -0.3 | 40% | ❌ 38 pts to go |
| P04 | 3254 | 0.6% | 0.6% | -0.5 | 30% | ❌ 29 pts to go |
| P05 | 413 | 0.2% | 0.2% | -0.1 | 20% | ❌ 20 pts to go |
| P06M | 6002 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 53606 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 278 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 680 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 20545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 0.7% | 0.7% | +0.2 | 50% | ❌ 49 pts to go |
| P10R | 96430 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2607 | 0.0% | 0.0% | -0.1 | n/a | no target |
| P11 | 9344 | 0.0% | 0.0% | -0.8 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17855 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 73.8% | 73.8% | +73.8 | n/a | no target |
| P01T | 304 | 68.4% | 68.4% | +63.0 | 50% | ✅ met |
| P01_GOLD | 625 | 66.9% | 66.9% | -0.7 | 85% | ❌ 18 pts to go |
| P02 | 462 | 65.4% | 65.4% | -10.1 | 90% | ❌ 25 pts to go |
| P03 | 255 | 61.6% | 61.6% | -13.9 | 85% | ❌ 23 pts to go |
| P04 | 3254 | 31.5% | 31.5% | -34.0 | 85% | ❌ 54 pts to go |
| P05 | 413 | 29.5% | 29.5% | -1.5 | 60% | ❌ 30 pts to go |
| P06M | 6002 | 91.8% | 91.8% | +91.8 | n/a | no target |
| P06T | 53606 | 80.9% | 80.9% | +80.7 | n/a | no target |
| P06 | 278 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 680 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 20545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 96.0% | 96.0% | -0.6 | 100% | 🟡 4 pts to go |
| P10R | 96430 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2607 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 9344 | 48.3% | 48.3% | +28.3 | 60% | ❌ 12 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17855 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 304 | 0.0% | 0.0% | -2.2 | 30% | ❌ 30 pts to go |
| P01_GOLD | 625 | 50.6% | 50.6% | -0.7 | 80% | ❌ 29 pts to go |
| P02 | 462 | 57.4% | 57.4% | -9.4 | 60% | 🟡 3 pts to go |
| P03 | 255 | 51.8% | 51.8% | -12.1 | 80% | ❌ 28 pts to go |
| P04 | 3254 | 26.1% | 26.1% | -28.4 | 50% | ❌ 24 pts to go |
| P05 | 413 | 12.3% | 12.3% | -1.0 | 40% | ❌ 28 pts to go |
| P06M | 6002 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 53606 | 0.0% | 0.0% | -0.2 | n/a | no target |
| P06 | 278 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 680 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 20545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 83.5% | 83.5% | -2.6 | 50% | ✅ met |
| P10R | 96430 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2607 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 9344 | 0.9% | 0.9% | -16.6 | 40% | ❌ 39 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17855 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 304 | 0.3% | 0.3% | -3.0 | n/a | no target |
| P01_GOLD | 625 | 60.3% | 60.3% | -0.8 | 85% | ❌ 25 pts to go |
| P02 | 462 | 56.7% | 56.7% | -9.1 | 90% | ❌ 33 pts to go |
| P03 | 255 | 60.4% | 60.4% | -14.1 | 85% | ❌ 25 pts to go |
| P04 | 3254 | 27.0% | 27.0% | -29.3 | 85% | ❌ 58 pts to go |
| P05 | 413 | 20.3% | 20.3% | -0.8 | 50% | ❌ 30 pts to go |
| P06M | 6002 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 53606 | 0.0% | 0.0% | -0.2 | n/a | no target |
| P06 | 278 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 680 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 20545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 97.0% | 97.0% | -0.1 | 100% | 🟡 3 pts to go |
| P10R | 96430 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2607 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 9344 | 0.9% | 0.9% | -18.1 | 60% | ❌ 59 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17855 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 304 | 0.0% | 0.0% | -2.2 | n/a | no target |
| P01_GOLD | 625 | 13.0% | 13.0% | +0.0 | 60% | ❌ 47 pts to go |
| P02 | 462 | 6.1% | 6.1% | -1.1 | 50% | ❌ 44 pts to go |
| P03 | 255 | 8.6% | 8.6% | -2.0 | 50% | ❌ 41 pts to go |
| P04 | 3254 | 2.1% | 2.1% | -2.2 | 40% | ❌ 38 pts to go |
| P05 | 413 | 1.0% | 1.0% | -0.3 | 20% | ❌ 19 pts to go |
| P06M | 6002 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 53606 | 0.0% | 0.0% | -0.1 | n/a | no target |
| P06 | 278 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 680 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 20545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 2.3% | 2.3% | -0.3 | 50% | ❌ 48 pts to go |
| P10R | 96430 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2607 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 9344 | 0.1% | 0.1% | -2.9 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17855 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 304 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 34.9% | 34.9% | -0.2 | 80% | ❌ 45 pts to go |
| P02 | 462 | 52.4% | 52.4% | -8.2 | 90% | ❌ 38 pts to go |
| P03 | 255 | 33.7% | 33.7% | -7.6 | 80% | ❌ 46 pts to go |
| P04 | 3254 | 24.6% | 24.6% | -26.7 | 85% | ❌ 60 pts to go |
| P05 | 413 | 5.6% | 5.6% | -0.4 | 50% | ❌ 44 pts to go |
| P06M | 6002 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 53606 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 278 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 680 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 20545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 75.9% | 75.9% | +0.0 | 95% | ❌ 19 pts to go |
| P10R | 96430 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2607 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 9344 | 0.7% | 0.7% | -12.4 | 50% | ❌ 49 pts to go |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17855 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 304 | 0.0% | 0.0% | -1.1 | n/a | no target |
| P01_GOLD | 625 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 462 | 6.3% | 6.3% | -0.9 | 50% | ❌ 44 pts to go |
| P03 | 255 | 2.0% | 2.0% | -0.4 | 30% | ❌ 28 pts to go |
| P04 | 3254 | 0.5% | 0.5% | -0.6 | 30% | ❌ 30 pts to go |
| P05 | 413 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 6002 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 53606 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 278 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 680 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 20545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10R | 96430 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2607 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 9344 | 0.0% | 0.0% | -0.8 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17855 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 304 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 462 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 255 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3254 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 413 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 6002 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 53606 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 278 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 680 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 20545 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 96430 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2607 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 9344 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17855 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 21.5% | 21.5% | -78.5 | 70% | ❌ 48 pts to go |
| P01T | 304 | 35.2% | 35.2% | -45.2 | 60% | ❌ 25 pts to go |
| P01_GOLD | 625 | 73.0% | 73.0% | -4.9 | 90% | ❌ 17 pts to go |
| P02 | 462 | 55.4% | 55.4% | -11.9 | 85% | ❌ 30 pts to go |
| P03 | 255 | 69.8% | 69.8% | -12.4 | 90% | ❌ 20 pts to go |
| P04 | 3254 | 33.6% | 33.6% | -21.8 | 75% | ❌ 41 pts to go |
| P05 | 413 | 50.6% | 50.6% | -2.0 | 50% | ✅ met |
| P06M | 6002 | 2.8% | 2.8% | -71.6 | n/a | no target |
| P06T | 53606 | 15.5% | 15.5% | -45.2 | n/a | no target |
| P06 | 278 | 24.1% | 24.1% | -19.9 | 40% | ❌ 16 pts to go |
| P07 | 680 | 17.6% | 17.6% | -20.5 | 50% | ❌ 32 pts to go |
| P08 | 20545 | 11.6% | 11.6% | -28.6 | 50% | ❌ 38 pts to go |
| P09 | 303 | 57.8% | 57.8% | +3.5 | 80% | ❌ 22 pts to go |
| P10R | 96430 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2607 | 29.1% | 29.1% | -7.5 | 40% | ❌ 11 pts to go |
| P11 | 9344 | 88.1% | 88.1% | +43.4 | 60% | ✅ met |
| P12 | 8 | 62.5% | 62.5% | +9.9 | 85% | ❌ 22 pts to go |
| P13 | 17855 | 91.0% | 91.0% | -0.7 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 76.9% | 76.9% | +15.8 | n/a | no target |
| P01T | 304 | 38.8% | 38.8% | -24.2 | n/a | no target |
| P01_GOLD | 625 | 70.6% | 70.6% | -4.2 | 95% | ❌ 24 pts to go |
| P02 | 462 | 74.0% | 74.0% | -10.9 | 95% | ❌ 21 pts to go |
| P03 | 255 | 71.8% | 71.8% | -6.1 | 95% | ❌ 23 pts to go |
| P04 | 3254 | 47.4% | 47.4% | -33.3 | 95% | ❌ 48 pts to go |
| P05 | 413 | 53.5% | 53.5% | -2.7 | 70% | ❌ 16 pts to go |
| P06M | 6002 | 69.5% | 69.5% | +48.7 | n/a | no target |
| P06T | 53606 | 29.4% | 29.4% | -48.8 | n/a | no target |
| P06 | 278 | 26.3% | 26.3% | -29.1 | 80% | ❌ 54 pts to go |
| P07 | 680 | 19.4% | 19.4% | -32.6 | 70% | ❌ 51 pts to go |
| P08 | 20545 | 15.0% | 15.0% | -37.4 | 70% | ❌ 55 pts to go |
| P09 | 303 | 87.5% | 87.5% | -1.0 | 100% | ❌ 12 pts to go |
| P10R | 96430 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2607 | 33.1% | 33.1% | -9.3 | 70% | ❌ 37 pts to go |
| P11 | 9344 | 89.4% | 89.4% | +34.1 | 75% | ✅ met |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17855 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 16.9% | 16.9% | -33.1 | n/a | no target |
| P01T | 304 | 26.3% | 26.3% | +6.7 | n/a | no target |
| P01_GOLD | 625 | 48.0% | 48.0% | -4.4 | 60% | ❌ 12 pts to go |
| P02 | 462 | 55.6% | 55.6% | -11.7 | 60% | 🟡 4 pts to go |
| P03 | 255 | 54.9% | 54.9% | -10.0 | 60% | 🟡 5 pts to go |
| P04 | 3254 | 37.9% | 37.9% | -17.6 | 55% | ❌ 17 pts to go |
| P05 | 413 | 22.3% | 22.3% | -3.0 | 50% | ❌ 28 pts to go |
| P06M | 6002 | 2.5% | 2.5% | -14.8 | n/a | no target |
| P06T | 53606 | 25.4% | 25.4% | -28.2 | n/a | no target |
| P06 | 278 | 35.6% | 35.6% | -17.4 | n/a | no target |
| P07 | 680 | 32.8% | 32.8% | -13.2 | 55% | ❌ 22 pts to go |
| P08 | 20545 | 28.5% | 28.5% | -19.0 | 50% | ❌ 22 pts to go |
| P09 | 303 | 71.0% | 71.0% | -0.4 | 70% | ✅ met |
| P10R | 96430 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2607 | 40.1% | 40.1% | -11.8 | 55% | ❌ 15 pts to go |
| P11 | 9344 | 89.4% | 89.4% | +46.4 | 50% | ✅ met |
| P12 | 8 | 87.5% | 87.5% | +3.3 | n/a | no target |
| P13 | 17855 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 21.5% | 21.5% | -39.6 | n/a | no target |
| P01T | 304 | 55.9% | 55.9% | +25.5 | n/a | no target |
| P01_GOLD | 625 | 48.0% | 48.0% | -3.8 | 70% | ❌ 22 pts to go |
| P02 | 462 | 54.1% | 54.1% | -3.1 | 70% | ❌ 16 pts to go |
| P03 | 255 | 49.8% | 49.8% | -7.4 | 70% | ❌ 20 pts to go |
| P04 | 3254 | 48.2% | 48.2% | -3.8 | 65% | ❌ 17 pts to go |
| P05 | 413 | 30.3% | 30.3% | -4.3 | 60% | ❌ 30 pts to go |
| P06M | 6002 | 4.7% | 4.7% | -25.7 | n/a | no target |
| P06T | 53606 | 64.9% | 64.9% | +61.4 | n/a | no target |
| P06 | 278 | 59.7% | 59.7% | +0.1 | 40% | ✅ met |
| P07 | 680 | 59.0% | 59.0% | -8.9 | 85% | ❌ 26 pts to go |
| P08 | 20545 | 58.3% | 58.3% | -9.8 | 85% | ❌ 27 pts to go |
| P09 | 303 | 53.5% | 53.5% | -1.9 | 85% | ❌ 32 pts to go |
| P10R | 96430 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2607 | 61.4% | 61.4% | -4.9 | 85% | ❌ 24 pts to go |
| P11 | 9344 | 8.9% | 8.9% | -46.0 | 75% | ❌ 66 pts to go |
| P12 | 8 | 25.0% | 25.0% | +9.2 | n/a | no target |
| P13 | 17855 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 24.6% | 24.6% | -69.8 | n/a | no target |
| P01T | 304 | 96.4% | 96.4% | +6.2 | n/a | no target |
| P01_GOLD | 625 | 89.4% | 89.4% | +0.0 | 90% | 🟡 1 pts to go |
| P02 | 462 | 89.2% | 89.2% | +1.6 | 90% | 🟡 1 pts to go |
| P03 | 255 | 91.0% | 91.0% | +1.1 | 90% | ✅ met |
| P04 | 3254 | 89.9% | 89.9% | +8.6 | 85% | ✅ met |
| P05 | 413 | 51.3% | 51.3% | +0.3 | 70% | ❌ 19 pts to go |
| P06M | 6002 | 7.2% | 7.2% | -60.7 | n/a | no target |
| P06T | 53606 | 91.1% | 91.1% | +13.2 | n/a | no target |
| P06 | 278 | 98.2% | 98.2% | +1.2 | 50% | ✅ met |
| P07 | 680 | 98.8% | 98.8% | +2.0 | 100% | 🟡 1 pts to go |
| P08 | 20545 | 99.4% | 99.4% | +3.3 | 100% | 🟡 1 pts to go |
| P09 | 303 | 80.2% | 80.2% | +0.4 | 100% | ❌ 20 pts to go |
| P10R | 96430 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2607 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 9344 | 99.6% | 99.6% | +6.6 | 100% | 🟡 0 pts to go |
| P12 | 8 | 37.5% | 37.5% | -4.6 | n/a | no target |
| P13 | 17855 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 16.9% | 16.9% | -33.1 | n/a | no target |
| P01T | 304 | 51.0% | 51.0% | +5.3 | n/a | no target |
| P01_GOLD | 625 | 45.3% | 45.3% | -0.4 | 70% | ❌ 25 pts to go |
| P02 | 462 | 49.6% | 49.6% | -1.9 | 75% | ❌ 25 pts to go |
| P03 | 255 | 44.3% | 44.3% | -7.1 | 75% | ❌ 31 pts to go |
| P04 | 3254 | 38.0% | 38.0% | -4.9 | 70% | ❌ 32 pts to go |
| P05 | 413 | 24.9% | 24.9% | +0.4 | 55% | ❌ 30 pts to go |
| P06M | 6002 | 3.3% | 3.3% | -12.8 | n/a | no target |
| P06T | 53606 | 40.6% | 40.6% | +37.7 | n/a | no target |
| P06 | 278 | 43.5% | 43.5% | +2.5 | n/a | no target |
| P07 | 680 | 46.9% | 46.9% | +10.0 | 70% | ❌ 23 pts to go |
| P08 | 20545 | 51.1% | 51.1% | +2.4 | 75% | ❌ 24 pts to go |
| P09 | 303 | 49.8% | 49.8% | -2.2 | 85% | ❌ 35 pts to go |
| P10R | 96430 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2607 | 43.6% | 43.6% | -7.7 | 80% | ❌ 36 pts to go |
| P11 | 9344 | 6.7% | 6.7% | -33.8 | 70% | ❌ 63 pts to go |
| P12 | 8 | 25.0% | 25.0% | -6.6 | n/a | no target |
| P13 | 17855 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 20.0% | 20.0% | -74.4 | n/a | no target |
| P01T | 304 | 90.5% | 90.5% | +1.4 | n/a | no target |
| P01_GOLD | 625 | 77.6% | 77.6% | -2.2 | 90% | ❌ 12 pts to go |
| P02 | 462 | 77.7% | 77.7% | +0.5 | 90% | ❌ 12 pts to go |
| P03 | 255 | 83.1% | 83.1% | +1.4 | 90% | 🟡 7 pts to go |
| P04 | 3254 | 76.9% | 76.9% | +6.0 | 85% | 🟡 8 pts to go |
| P05 | 413 | 47.7% | 47.7% | -0.7 | 75% | ❌ 27 pts to go |
| P06M | 6002 | 5.3% | 5.3% | -62.6 | n/a | no target |
| P06T | 53606 | 82.6% | 82.6% | +5.5 | n/a | no target |
| P06 | 278 | 82.4% | 82.4% | -6.2 | n/a | no target |
| P07 | 680 | 84.1% | 84.1% | -6.4 | 100% | ❌ 16 pts to go |
| P08 | 20545 | 82.6% | 82.6% | -6.4 | 100% | ❌ 17 pts to go |
| P09 | 303 | 61.4% | 61.4% | -1.1 | n/a | no target |
| P10R | 96430 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2607 | 84.6% | 84.6% | -4.4 | 100% | ❌ 15 pts to go |
| P11 | 9344 | 55.3% | 55.3% | -19.2 | n/a | no target |
| P12 | 8 | 37.5% | 37.5% | +0.7 | n/a | no target |
| P13 | 17855 | 82.2% | 82.2% | -0.5 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 56.9% | 56.9% | +56.9 | n/a | no target · QC vendors: 37 rows, 100.0% filled |
| P01T | 304 | 17.8% | 17.8% | -3.9 | n/a | no target · QC vendors: 17 rows, 100.0% filled |
| P01_GOLD | 625 | 43.7% | 43.7% | -4.2 | 95% | ❌ 51 pts to go · QC vendors: 53 rows, 98.1% filled |
| P02 | 462 | 55.4% | 55.4% | -13.2 | 95% | ❌ 40 pts to go · QC vendors: 110 rows, 100.0% filled |
| P03 | 255 | 46.7% | 46.7% | -9.1 | 95% | ❌ 48 pts to go · QC vendors: 18 rows, 100.0% filled |
| P04 | 3254 | 33.1% | 33.1% | -27.1 | 95% | ❌ 62 pts to go · QC vendors: 495 rows, 98.8% filled |
| P05 | 413 | 14.5% | 14.5% | -0.3 | n/a | no target · QC vendors: 34 rows, 94.1% filled |
| P06M | 6002 | 67.4% | 67.4% | +67.4 | n/a | no target · QC vendors: 4045 rows, 100.0% filled |
| P06T | 53606 | 15.8% | 15.8% | -40.1 | n/a | no target · QC vendors: 3093 rows, 100.0% filled |
| P06 | 278 | 9.0% | 9.0% | -17.5 | n/a | no target · QC vendors: 14 rows, 100.0% filled |
| P07 | 680 | 7.4% | 7.4% | -14.0 | n/a | no target · QC vendors: 35 rows, 97.1% filled |
| P08 | 20545 | 7.1% | 7.1% | -21.8 | n/a | no target · QC vendors: 1155 rows, 99.7% filled |
| P09 | 303 | 78.2% | 78.2% | -1.9 | 95% | ❌ 17 pts to go · QC vendors: 111 rows, 100.0% filled |
| P10R | 96430 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2607 | 18.0% | 18.0% | -5.4 | n/a | no target · QC vendors: 306 rows, 94.4% filled |
| P11 | 9344 | 45.6% | 45.6% | +16.3 | n/a | no target · QC vendors: 126 rows, 99.2% filled |
| P12 | 8 | 62.5% | 62.5% | -11.2 | n/a | no target · QC vendors: 1 rows, 100.0% filled |
| P13 | 17855 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 73.8% | 73.8% | +12.7 | n/a | no target · vendors with a registry record: 48 rows, 100.0% filled |
| P01T | 304 | 39.1% | 39.1% | -23.9 | n/a | no target · vendors with a registry record: 119 rows, 100.0% filled |
| P01_GOLD | 625 | 79.4% | 79.4% | -4.1 | 100% | ❌ 21 pts to go · vendors with a registry record: 496 rows, 100.0% filled |
| P02 | 462 | 77.7% | 77.7% | -11.4 | 100% | ❌ 22 pts to go · vendors with a registry record: 359 rows, 100.0% filled |
| P03 | 255 | 81.2% | 81.2% | -7.7 | 100% | ❌ 19 pts to go · vendors with a registry record: 207 rows, 100.0% filled |
| P04 | 3254 | 47.8% | 47.8% | -33.6 | 100% | ❌ 52 pts to go · vendors with a registry record: 1555 rows, 100.0% filled |
| P05 | 413 | 58.4% | 58.4% | -3.3 | n/a | no target · vendors with a registry record: 241 rows, 100.0% filled |
| P06M | 6002 | 68.8% | 68.8% | +48.0 | n/a | no target · vendors with a registry record: 4130 rows, 100.0% filled |
| P06T | 53606 | 29.4% | 29.4% | -48.8 | n/a | no target · vendors with a registry record: 15775 rows, 100.0% filled |
| P06 | 278 | 27.0% | 27.0% | -30.8 | n/a | no target · vendors with a registry record: 75 rows, 100.0% filled |
| P07 | 680 | 19.7% | 19.7% | -34.7 | n/a | no target · vendors with a registry record: 134 rows, 100.0% filled |
| P08 | 20545 | 15.2% | 15.2% | -39.1 | n/a | no target · vendors with a registry record: 3122 rows, 100.0% filled |
| P09 | 303 | 91.1% | 91.1% | -0.5 | n/a | no target · vendors with a registry record: 276 rows, 100.0% filled |
| P10R | 96430 | 100.0% | 100.0% |  | n/a | no target · vendors with a registry record: 96430 rows, 100.0% filled |
| P10 | 2607 | 33.7% | 33.7% | -10.0 | n/a | no target · vendors with a registry record: 879 rows, 100.0% filled |
| P11 | 9344 | 89.6% | 89.6% | +31.4 | n/a | no target · vendors with a registry record: 8368 rows, 100.0% filled |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 8 rows, 100.0% filled |
| P13 | 17855 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 89.2% | 89.2% | -5.2 | 90% | 🟡 1 pts to go |
| P01T | 304 | 61.5% | 61.5% | -33.1 | 90% | ❌ 28 pts to go |
| P01_GOLD | 625 | 83.5% | 83.5% | -1.1 | 95% | ❌ 12 pts to go |
| P02 | 462 | 85.7% | 85.7% | -4.9 | 95% | 🟡 9 pts to go |
| P03 | 255 | 78.8% | 78.8% | -4.4 | 85% | 🟡 6 pts to go |
| P04 | 3254 | 58.2% | 58.2% | -20.6 | 90% | ❌ 32 pts to go |
| P05 | 413 | 68.5% | 68.5% | -7.3 | 75% | 🟡 6 pts to go |
| P06M | 6002 | 89.5% | 89.5% | +0.8 | n/a | no target |
| P06T | 53606 | 31.5% | 31.5% | -32.9 | n/a | no target |
| P06 | 278 | 60.1% | 60.1% | +3.5 | 80% | ❌ 20 pts to go |
| P07 | 680 | 49.6% | 49.7% | -4.0 | 80% | ❌ 30 pts to go |
| P08 | 20545 | 42.8% | 42.8% | +6.0 | 75% | ❌ 32 pts to go |
| P09 | 303 | 77.2% | 77.2% | -3.6 | 95% | ❌ 18 pts to go |
| P10R | 96430 | 26.7% | 26.7% |  | n/a | no target |
| P10 | 2607 | 39.7% | 39.8% | +7.7 | 70% | ❌ 30 pts to go |
| P11 | 9344 | 13.2% | 13.2% | -11.7 | 65% | ❌ 52 pts to go |
| P12 | 8 | 75.0% | 75.0% | +1.3 | 80% | 🟡 5 pts to go |
| P13 | 17855 | 42.7% | 42.7% | -9.8 | 60% | ❌ 17 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 21.5% | 21.5% | -17.4 | 50% | ❌ 28 pts to go |
| P01T | 304 | 14.5% | 14.5% | -6.2 | n/a | no target |
| P01_GOLD | 625 | 20.5% | 20.5% | +0.1 | 40% | ❌ 20 pts to go |
| P02 | 462 | 19.0% | 19.0% | -2.8 | 40% | ❌ 21 pts to go |
| P03 | 255 | 22.4% | 22.4% | -4.5 | 40% | ❌ 18 pts to go |
| P04 | 3254 | 16.7% | 16.7% | -10.9 | 40% | ❌ 23 pts to go |
| P05 | 413 | 20.1% | 20.1% | -2.8 | 25% | 🟡 5 pts to go |
| P06M | 6002 | 8.1% | 8.1% | -17.5 | n/a | no target |
| P06T | 53606 | 8.3% | 8.3% | -22.6 | n/a | no target |
| P06 | 278 | 12.9% | 12.9% | +2.1 | 35% | ❌ 22 pts to go |
| P07 | 680 | 10.9% | 10.9% | +0.6 | 35% | ❌ 24 pts to go |
| P08 | 20545 | 11.1% | 11.1% | +0.0 | 35% | ❌ 24 pts to go |
| P09 | 303 | 16.2% | 16.2% | -0.9 | n/a | no target |
| P10R | 96430 | 7.7% | 7.7% |  | n/a | no target |
| P10 | 2607 | 7.0% | 7.0% | -2.6 | 30% | ❌ 23 pts to go |
| P11 | 9344 | 1.4% | 1.4% | -7.0 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | +2.0 | n/a | no target |
| P13 | 17855 | 22.9% | 22.9% | -3.0 | 30% | 🟡 7 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 100.0% | 100.0% | +5.6 | 100% | ✅ met |
| P01T | 304 | 93.4% | 93.4% | -0.1 | 100% | 🟡 7 pts to go |
| P01_GOLD | 625 | 89.3% | 89.3% | +1.6 | 100% | ❌ 11 pts to go |
| P02 | 462 | 95.2% | 95.2% | -1.6 | 100% | 🟡 5 pts to go |
| P03 | 255 | 89.4% | 89.4% | -2.4 | 100% | ❌ 11 pts to go |
| P04 | 3254 | 77.8% | 77.8% | -13.2 | 100% | ❌ 22 pts to go |
| P05 | 413 | 87.4% | 87.4% | +2.5 | 100% | ❌ 13 pts to go |
| P06M | 6002 | 98.2% | 98.2% | +26.2 | n/a | no target |
| P06T | 53606 | 77.9% | 77.9% | -2.3 | n/a | no target |
| P06 | 278 | 80.6% | 80.6% | +11.9 | 95% | ❌ 14 pts to go |
| P07 | 680 | 83.8% | 83.8% | +13.2 | 95% | ❌ 11 pts to go |
| P08 | 20545 | 80.4% | 80.4% | +14.2 | 95% | ❌ 15 pts to go |
| P09 | 303 | 95.7% | 95.7% | +0.2 | 100% | 🟡 4 pts to go |
| P10R | 96430 | 59.3% | 59.3% |  | n/a | no target |
| P10 | 2607 | 65.4% | 65.4% | +0.2 | 95% | ❌ 30 pts to go |
| P11 | 9344 | 68.3% | 68.3% | +33.9 | 80% | ❌ 12 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17855 | 75.8% | 75.8% | -0.3 | 95% | ❌ 19 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 89.2% | 89.2% | +0.3 | n/a | no target |
| P01T | 304 | 69.1% | 69.1% | -11.3 | n/a | no target |
| P01_GOLD | 625 | 69.4% | 69.4% | -0.8 | 90% | ❌ 21 pts to go |
| P02 | 462 | 76.2% | 76.2% | -3.5 | 95% | ❌ 19 pts to go |
| P03 | 255 | 74.1% | 74.1% | +0.5 | 95% | ❌ 21 pts to go |
| P04 | 3254 | 69.0% | 69.0% | -15.9 | 95% | ❌ 26 pts to go |
| P05 | 413 | 70.9% | 70.9% | -4.1 | 90% | ❌ 19 pts to go |
| P06M | 6002 | 93.7% | 93.7% | +9.8 | n/a | no target |
| P06T | 53606 | 52.1% | 52.1% | -25.2 | n/a | no target |
| P06 | 278 | 65.8% | 65.8% | +1.3 | 95% | ❌ 29 pts to go |
| P07 | 680 | 60.4% | 60.4% | -5.9 | 90% | ❌ 30 pts to go |
| P08 | 20545 | 63.6% | 63.6% | -11.1 | 95% | ❌ 31 pts to go |
| P09 | 303 | 86.1% | 86.1% | -2.9 | 100% | ❌ 14 pts to go |
| P10R | 96430 | 47.8% | 47.8% |  | n/a | no target |
| P10 | 2607 | 57.8% | 57.8% | -13.7 | 95% | ❌ 37 pts to go |
| P11 | 9344 | 16.2% | 16.2% | -12.7 | 75% | ❌ 59 pts to go |
| P12 | 8 | 75.0% | 75.0% | -14.5 | n/a | no target |
| P13 | 17855 | 51.0% | 51.0% | -28.3 | 95% | ❌ 44 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 76.9% | 76.9% | -0.9 | n/a | no target |
| P01T | 304 | 80.9% | 80.9% | -10.4 | 95% | ❌ 14 pts to go |
| P01_GOLD | 625 | 80.6% | 80.6% | -1.6 | 90% | 🟡 9 pts to go |
| P02 | 462 | 86.1% | 86.1% | -2.3 | 95% | 🟡 9 pts to go |
| P03 | 255 | 83.9% | 83.9% | -0.7 | 95% | ❌ 11 pts to go |
| P04 | 3254 | 85.5% | 85.5% | +1.3 | 90% | 🟡 4 pts to go |
| P05 | 413 | 88.6% | 88.6% | -1.0 | 95% | 🟡 6 pts to go |
| P06M | 6002 | 70.8% | 70.8% | -14.3 | n/a | no target |
| P06T | 53606 | 66.6% | 66.6% | -27.5 | n/a | no target |
| P06 | 278 | 86.3% | 86.3% | -4.1 | 100% | ❌ 14 pts to go |
| P07 | 680 | 82.8% | 82.8% | -5.3 | 100% | ❌ 17 pts to go |
| P08 | 20545 | 84.0% | 84.0% | -6.7 | 100% | ❌ 16 pts to go |
| P09 | 303 | 68.6% | 68.6% | -5.4 | n/a | no target |
| P10R | 96430 | 63.3% | 63.3% |  | n/a | no target |
| P10 | 2607 | 88.0% | 88.0% | -2.1 | 100% | ❌ 12 pts to go |
| P11 | 9344 | 26.8% | 26.8% | -9.7 | 80% | ❌ 53 pts to go |
| P12 | 8 | 75.0% | 75.0% | -9.2 | n/a | no target |
| P13 | 17855 | 54.4% | 54.4% | -29.8 | 95% | ❌ 41 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 6.2% | 6.2% | -10.5 | n/a | no target |
| P01T | 304 | 9.2% | 9.2% | -14.7 | n/a | no target |
| P01_GOLD | 625 | 14.2% | 14.2% | -0.1 | 25% | ❌ 11 pts to go |
| P02 | 462 | 24.7% | 24.7% | -3.0 | 40% | ❌ 15 pts to go |
| P03 | 255 | 9.0% | 9.0% | -1.6 | 20% | ❌ 11 pts to go |
| P04 | 3254 | 3.7% | 3.7% | -3.7 | 20% | ❌ 16 pts to go |
| P05 | 413 | 3.4% | 3.4% | -0.5 | 15% | ❌ 12 pts to go |
| P06M | 6002 | 0.3% | 0.3% | -4.5 | n/a | no target |
| P06T | 53606 | 0.4% | 0.4% | -2.8 | n/a | no target |
| P06 | 278 | 5.8% | 5.8% | +0.4 | n/a | no target |
| P07 | 680 | 7.4% | 7.4% | +1.1 | n/a | no target |
| P08 | 20545 | 0.3% | 0.3% | -0.7 | n/a | no target |
| P09 | 303 | 7.6% | 7.6% | -0.3 | n/a | no target |
| P10R | 96430 | 0.2% | 0.2% |  | n/a | no target |
| P10 | 2607 | 1.0% | 1.0% | -0.3 | n/a | no target |
| P11 | 9344 | 0.2% | 0.2% | -2.3 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | -10.5 | n/a | no target |
| P13 | 17855 | 0.4% | 0.4% | -0.2 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 27.7% | 27.7% | -11.2 | n/a | no target |
| P01T | 304 | 26.6% | 26.6% | -8.2 | 70% | ❌ 43 pts to go |
| P01_GOLD | 625 | 43.2% | 43.2% | -0.1 | 80% | ❌ 37 pts to go |
| P02 | 462 | 57.1% | 57.1% | -7.0 | 90% | ❌ 33 pts to go |
| P03 | 255 | 19.2% | 19.2% | -3.9 | 60% | ❌ 41 pts to go |
| P04 | 3254 | 24.7% | 24.7% | -25.8 | 85% | ❌ 60 pts to go |
| P05 | 413 | 12.3% | 12.3% | -0.7 | 50% | ❌ 38 pts to go |
| P06M | 6002 | 0.6% | 0.6% | -5.9 | n/a | no target |
| P06T | 53606 | 0.7% | 0.7% | -2.0 | n/a | no target |
| P06 | 278 | 17.3% | 17.3% | -0.8 | n/a | no target |
| P07 | 680 | 13.4% | 13.4% | -5.6 | n/a | no target |
| P08 | 20545 | 0.5% | 0.5% | -0.1 | n/a | no target |
| P09 | 303 | 77.6% | 77.6% | -3.0 | 95% | ❌ 17 pts to go |
| P10R | 96430 | 0.2% | 0.2% |  | n/a | no target |
| P10 | 2607 | 1.8% | 1.8% | -1.3 | n/a | no target |
| P11 | 9344 | 3.8% | 3.8% | -25.5 | n/a | no target |
| P12 | 8 | 25.0% | 25.0% | -6.6 | n/a | no target |
| P13 | 17855 | 0.7% | 0.7% | -0.3 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 4.6% | 4.6% | +4.6 | n/a | no target |
| P01T | 304 | 13.5% | 13.5% | -2.8 | n/a | no target |
| P01_GOLD | 625 | 33.8% | 33.8% | -0.2 | 70% | ❌ 36 pts to go |
| P02 | 462 | 39.2% | 39.2% | -5.1 | 75% | ❌ 36 pts to go |
| P03 | 255 | 19.2% | 19.2% | -3.9 | 55% | ❌ 36 pts to go |
| P04 | 3254 | 24.6% | 24.6% | -25.9 | 75% | ❌ 50 pts to go |
| P05 | 413 | 11.1% | 11.1% | -0.6 | 50% | ❌ 39 pts to go |
| P06M | 6002 | 0.1% | 0.1% | -1.7 | n/a | no target |
| P06T | 53606 | 0.4% | 0.4% | -1.1 | n/a | no target |
| P06 | 278 | 9.0% | 9.0% | -1.2 | n/a | no target |
| P07 | 680 | 6.3% | 6.3% | -4.0 | n/a | no target |
| P08 | 20545 | 0.2% | 0.2% | -0.3 | n/a | no target |
| P09 | 303 | 75.2% | 75.2% | -2.5 | 95% | ❌ 20 pts to go |
| P10R | 96430 | 0.2% | 0.2% |  | n/a | no target |
| P10 | 2607 | 1.1% | 1.1% | -0.7 | n/a | no target |
| P11 | 9344 | 3.7% | 3.7% | -25.2 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | -3.3 | n/a | no target |
| P13 | 17855 | 0.5% | 0.5% | -0.1 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 6.2% | 6.2% | -10.5 | n/a | no target |
| P01T | 304 | 10.2% | 10.2% | -9.4 | n/a | no target |
| P01_GOLD | 625 | 57.9% | 58.1% | +0.0 | 80% | ❌ 22 pts to go |
| P02 | 462 | 46.1% | 46.3% | -6.1 | 75% | ❌ 29 pts to go |
| P03 | 255 | 38.0% | 38.0% | -7.2 | 70% | ❌ 32 pts to go |
| P04 | 3254 | 24.1% | 24.6% | -24.6 | 70% | ❌ 46 pts to go |
| P05 | 413 | 14.8% | 14.8% | -1.6 | 50% | ❌ 35 pts to go |
| P06M | 6002 | 0.6% | 0.6% | -3.6 | n/a | no target |
| P06T | 53606 | 0.3% | 0.3% | -1.3 | n/a | no target |
| P06 | 278 | 14.4% | 14.4% | -9.7 | n/a | no target |
| P07 | 680 | 2.5% | 2.5% | -2.7 | n/a | no target |
| P08 | 20545 | 0.4% | 0.4% | -0.6 | n/a | no target |
| P09 | 303 | 45.9% | 46.2% | +1.8 | 80% | ❌ 34 pts to go |
| P10R | 96430 | 0.1% | 0.1% |  | n/a | no target |
| P10 | 2607 | 1.3% | 1.3% | -0.2 | n/a | no target |
| P11 | 9344 | 1.2% | 1.2% | -15.5 | n/a | no target |
| P12 | 8 | 37.5% | 37.5% | +5.9 | n/a | no target |
| P13 | 17855 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 13.8% | 13.8% | -25.1 | n/a | no target |
| P01T | 304 | 24.0% | 24.0% | -32.5 | 60% | ❌ 36 pts to go |
| P01_GOLD | 625 | 63.5% | 63.5% | +0.0 | 70% | 🟡 6 pts to go |
| P02 | 462 | 39.2% | 39.2% | -4.6 | 50% | ❌ 11 pts to go |
| P03 | 255 | 50.2% | 50.2% | -5.1 | 55% | 🟡 5 pts to go |
| P04 | 3254 | 14.0% | 14.0% | -8.9 | 40% | ❌ 26 pts to go |
| P05 | 413 | 17.9% | 17.9% | +0.5 | 40% | ❌ 22 pts to go |
| P06M | 6002 | 1.1% | 1.1% | -15.6 | n/a | no target |
| P06T | 53606 | 2.4% | 2.4% | -10.1 | n/a | no target |
| P06 | 278 | 20.5% | 20.5% | -10.2 | n/a | no target |
| P07 | 680 | 7.4% | 7.4% | -8.9 | n/a | no target |
| P08 | 20545 | 3.1% | 3.1% | -1.6 | n/a | no target |
| P09 | 303 | 5.9% | 5.9% | +0.1 | n/a | no target |
| P10R | 96430 | 0.2% | 0.2% |  | n/a | no target |
| P10 | 2607 | 4.6% | 4.6% | +0.7 | n/a | no target |
| P11 | 9344 | 4.4% | 4.4% | -3.2 | n/a | no target |
| P12 | 8 | 12.5% | 12.5% | -3.3 | n/a | no target |
| P13 | 17855 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 18.5% | 18.5% | -25.9 | n/a | no target |
| P01T | 304 | 27.6% | 27.6% | -42.0 | 65% | ❌ 37 pts to go |
| P01_GOLD | 625 | 69.1% | 69.1% | -0.1 | 70% | 🟡 1 pts to go |
| P02 | 462 | 24.0% | 24.0% | -2.2 | 50% | ❌ 26 pts to go |
| P03 | 255 | 52.5% | 52.5% | -3.7 | 60% | 🟡 8 pts to go |
| P04 | 3254 | 6.1% | 6.1% | -3.8 | 40% | ❌ 34 pts to go |
| P05 | 413 | 20.3% | 20.3% | -1.1 | 45% | ❌ 25 pts to go |
| P06M | 6002 | 0.5% | 0.5% | -6.6 | n/a | no target |
| P06T | 53606 | 0.6% | 0.6% | -3.7 | n/a | no target |
| P06 | 278 | 34.2% | 34.2% | -14.0 | n/a | no target |
| P07 | 680 | 7.9% | 7.9% | -15.9 | n/a | no target |
| P08 | 20545 | 1.3% | 1.3% | -1.1 | n/a | no target |
| P09 | 303 | 9.9% | 9.9% | +1.2 | n/a | no target |
| P10R | 96430 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2607 | 2.7% | 2.7% | +0.6 | n/a | no target |
| P11 | 9344 | 1.1% | 1.1% | -5.7 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | -10.5 | n/a | no target |
| P13 | 17855 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 4.6% | 4.6% | -6.5 | n/a | no target |
| P01T | 304 | 15.8% | 15.8% | -28.8 | n/a | no target |
| P01_GOLD | 625 | 49.8% | 49.8% | +0.0 | 50% | 🟡 0 pts to go |
| P02 | 462 | 37.7% | 37.7% | -4.9 | n/a | no target |
| P03 | 255 | 53.3% | 53.3% | -5.4 | 60% | 🟡 7 pts to go |
| P04 | 3254 | 13.5% | 13.5% | -12.9 | n/a | no target |
| P05 | 413 | 15.7% | 15.7% | -1.0 | n/a | no target |
| P06M | 6002 | 0.4% | 0.4% | -3.8 | n/a | no target |
| P06T | 53606 | 0.5% | 0.5% | -3.5 | n/a | no target |
| P06 | 278 | 23.4% | 23.4% | -12.1 | n/a | no target |
| P07 | 680 | 8.2% | 8.2% | -10.5 | n/a | no target |
| P08 | 20545 | 0.6% | 0.6% | -0.9 | n/a | no target |
| P09 | 303 | 18.2% | 18.2% | -0.7 | n/a | no target |
| P10R | 96430 | 0.1% | 0.1% |  | n/a | no target |
| P10 | 2607 | 2.4% | 2.4% | +0.0 | n/a | no target |
| P11 | 9344 | 0.9% | 0.9% | -6.9 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | -21.1 | n/a | no target |
| P13 | 17855 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 13.8% | 13.8% | -14.0 | 15% | 🟡 1 pts to go |
| P01T | 304 | 12.2% | 12.2% | -17.1 | 15% | 🟡 3 pts to go |
| P01_GOLD | 625 | 35.4% | 35.4% | +0.3 | 40% | 🟡 5 pts to go |
| P02 | 462 | 12.6% | 12.8% | -1.3 | 25% | ❌ 12 pts to go |
| P03 | 255 | 18.0% | 18.0% | -3.6 | 25% | 🟡 7 pts to go |
| P04 | 3254 | 3.0% | 3.0% | -2.2 | 15% | ❌ 12 pts to go |
| P05 | 413 | 7.0% | 7.0% | -1.1 | 15% | 🟡 8 pts to go |
| P06M | 6002 | 0.7% | 0.7% | -5.3 | 15% | ❌ 14 pts to go |
| P06T | 53606 | 0.5% | 0.5% | -1.0 | 15% | ❌ 14 pts to go |
| P06 | 278 | 9.7% | 9.7% | -0.5 | 15% | 🟡 5 pts to go |
| P07 | 680 | 3.7% | 3.7% | -3.0 | 15% | ❌ 11 pts to go |
| P08 | 20545 | 0.5% | 0.5% | -0.4 | 15% | ❌ 14 pts to go |
| P09 | 303 | 1.0% | 1.0% | +0.2 | 15% | ❌ 14 pts to go |
| P10R | 96430 | 0.4% | 0.4% |  | 15% | ❌ 15 pts to go |
| P10 | 2607 | 1.0% | 1.0% | -0.4 | 15% | ❌ 14 pts to go |
| P11 | 9344 | 0.2% | 0.2% | -1.1 | 15% | ❌ 15 pts to go |
| P12 | 8 | 12.5% | 12.5% | +12.5 | 15% | 🟡 2 pts to go |
| P13 | 17855 | 0.4% | 0.4% | -0.1 | 15% | ❌ 15 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 6.2% | 6.2% | -4.9 | 15% | 🟡 9 pts to go |
| P01T | 304 | 13.2% | 13.2% | -19.4 | 25% | ❌ 12 pts to go |
| P01_GOLD | 625 | 29.1% | 29.1% | -0.1 | 25% | ✅ met |
| P02 | 462 | 25.5% | 25.5% | -2.5 | 15% | ✅ met |
| P03 | 255 | 21.6% | 21.6% | -4.4 | 15% | ✅ met |
| P04 | 3254 | 4.3% | 4.3% | -3.9 | 15% | ❌ 11 pts to go |
| P05 | 413 | 11.1% | 11.1% | -0.9 | 15% | 🟡 4 pts to go |
| P06M | 6002 | 0.3% | 0.3% | -2.1 | 15% | ❌ 15 pts to go |
| P06T | 53606 | 0.3% | 0.3% | -2.4 | 15% | ❌ 15 pts to go |
| P06 | 278 | 7.9% | 7.9% | -4.1 | 15% | 🟡 7 pts to go |
| P07 | 680 | 3.4% | 3.4% | -4.1 | 15% | ❌ 12 pts to go |
| P08 | 20545 | 0.5% | 0.5% | -0.5 | 15% | ❌ 14 pts to go |
| P09 | 303 | 1.0% | 1.0% | +0.2 | 15% | ❌ 14 pts to go |
| P10R | 96430 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P10 | 2607 | 1.6% | 1.6% | +0.2 | 15% | ❌ 13 pts to go |
| P11 | 9344 | 0.6% | 0.6% | -4.5 | 15% | ❌ 14 pts to go |
| P12 | 8 | 25.0% | 25.0% | -1.3 | 15% | ✅ met |
| P13 | 17855 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 0.0% | 0.0% | -5.6 | 20% | ❌ 20 pts to go |
| P01T | 304 | 4.3% | 4.3% | -5.5 | 20% | ❌ 16 pts to go |
| P01_GOLD | 625 | 4.3% | 4.3% | +0.0 | 20% | ❌ 16 pts to go |
| P02 | 462 | 1.3% | 1.3% | -0.2 | 20% | ❌ 19 pts to go |
| P03 | 255 | 1.6% | 1.6% | -0.3 | 20% | ❌ 18 pts to go |
| P04 | 3254 | 0.6% | 0.6% | -0.4 | 20% | ❌ 19 pts to go |
| P05 | 413 | 1.2% | 1.2% | +0.2 | 20% | ❌ 19 pts to go |
| P06M | 6002 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 53606 | 0.0% | 0.0% | -0.2 | 20% | ❌ 20 pts to go |
| P06 | 278 | 1.4% | 1.4% | -2.2 | 20% | ❌ 19 pts to go |
| P07 | 680 | 0.6% | 0.6% | -0.2 | 20% | ❌ 19 pts to go |
| P08 | 20545 | 0.0% | 0.0% | -0.2 | 20% | ❌ 20 pts to go |
| P09 | 303 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10R | 96430 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P10 | 2607 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 9344 | 0.1% | 0.1% | -0.5 | 20% | ❌ 20 pts to go |
| P12 | 8 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 17855 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 1.5% | 1.5% | -4.1 | 15% | ❌ 14 pts to go |
| P01T | 304 | 2.6% | 2.6% | -5.0 | 15% | ❌ 12 pts to go |
| P01_GOLD | 625 | 10.6% | 10.6% | +0.0 | 15% | 🟡 4 pts to go |
| P02 | 462 | 12.1% | 12.1% | -1.3 | 15% | 🟡 3 pts to go |
| P03 | 255 | 20.8% | 20.8% | -3.2 | 15% | ✅ met |
| P04 | 3254 | 2.6% | 2.6% | -2.0 | 15% | ❌ 12 pts to go |
| P05 | 413 | 3.1% | 3.1% | +0.2 | 15% | ❌ 12 pts to go |
| P06M | 6002 | 0.2% | 0.2% | -2.2 | 15% | ❌ 15 pts to go |
| P06T | 53606 | 0.2% | 0.2% | -1.2 | 15% | ❌ 15 pts to go |
| P06 | 278 | 5.8% | 5.8% | +0.4 | 15% | 🟡 9 pts to go |
| P07 | 680 | 1.9% | 1.9% | -1.7 | 15% | ❌ 13 pts to go |
| P08 | 20545 | 0.4% | 0.4% | -0.3 | 15% | ❌ 15 pts to go |
| P09 | 303 | 0.7% | 0.7% | +0.2 | 15% | ❌ 14 pts to go |
| P10R | 96430 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P10 | 2607 | 1.0% | 1.0% | +0.2 | 15% | ❌ 14 pts to go |
| P11 | 9344 | 0.4% | 0.4% | -1.7 | 15% | ❌ 15 pts to go |
| P12 | 8 | 0.0% | 0.0% | -5.3 | 15% | ❌ 15 pts to go |
| P13 | 17855 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 6.2% | 6.2% | -4.9 | 20% | ❌ 14 pts to go |
| P01T | 304 | 16.4% | 16.4% | -24.9 | 40% | ❌ 24 pts to go |
| P01_GOLD | 625 | 45.8% | 45.8% | +0.0 | 40% | ✅ met |
| P02 | 462 | 43.1% | 43.1% | -5.4 | 20% | ✅ met |
| P03 | 255 | 49.0% | 49.0% | -6.8 | 35% | ✅ met |
| P04 | 3254 | 16.1% | 16.1% | -14.2 | 20% | 🟡 4 pts to go |
| P05 | 413 | 15.3% | 15.3% | -1.4 | 20% | 🟡 5 pts to go |
| P06M | 6002 | 0.6% | 0.6% | -3.6 | 20% | ❌ 19 pts to go |
| P06T | 53606 | 0.8% | 0.8% | -3.7 | 20% | ❌ 19 pts to go |
| P06 | 278 | 23.7% | 23.7% | -11.8 | 20% | ✅ met |
| P07 | 680 | 8.1% | 8.1% | -6.6 | 20% | ❌ 12 pts to go |
| P08 | 20545 | 1.0% | 1.0% | -1.3 | 20% | ❌ 19 pts to go |
| P09 | 303 | 18.2% | 18.2% | -3.8 | 20% | 🟡 2 pts to go |
| P10R | 96430 | 0.2% | 0.2% |  | 20% | ❌ 20 pts to go |
| P10 | 2607 | 3.5% | 3.5% | +0.9 | 20% | ❌ 16 pts to go |
| P11 | 9344 | 1.1% | 1.1% | -6.9 | 20% | ❌ 19 pts to go |
| P12 | 8 | 0.0% | 0.0% | -15.8 | 20% | ❌ 20 pts to go |
| P13 | 17855 | 0.6% | 0.6% | +0.0 | 20% | ❌ 19 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 52.3% | 52.3% | +52.3 | n/a | no target |
| P01T | 304 | 0.3% | 0.3% | -0.8 | n/a | no target |
| P01_GOLD | 625 | 69.4% | 69.4% | -0.3 | 95% | ❌ 26 pts to go |
| P02 | 462 | 63.4% | 63.4% | -9.9 | 95% | ❌ 32 pts to go |
| P03 | 255 | 54.9% | 54.9% | -12.4 | 90% | ❌ 35 pts to go |
| P04 | 3254 | 28.4% | 28.4% | -30.0 | 85% | ❌ 57 pts to go |
| P05 | 413 | 36.8% | 36.8% | +1.9 | 75% | ❌ 38 pts to go |
| P06M | 6002 | 63.1% | 63.1% | +63.1 | n/a | no target |
| P06T | 53606 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 278 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 680 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 20545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 89.4% | 89.4% | -1.4 | 100% | ❌ 11 pts to go |
| P10R | 96430 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2607 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 9344 | 0.9% | 0.9% | -17.9 | 60% | ❌ 59 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17855 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 52.3% | 52.3% | +52.3 | n/a | no target |
| P01T | 304 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 625 | 72.8% | 72.8% | -0.1 | 100% | ❌ 27 pts to go |
| P02 | 462 | 66.9% | 66.9% | -10.3 | 100% | ❌ 33 pts to go |
| P03 | 255 | 60.8% | 60.8% | -13.7 | n/a | no target |
| P04 | 3254 | 29.1% | 29.1% | -30.9 | 95% | ❌ 66 pts to go |
| P05 | 413 | 33.4% | 33.4% | +2.2 | 80% | ❌ 47 pts to go |
| P06M | 6002 | 63.1% | 63.1% | +63.1 | n/a | no target |
| P06T | 53606 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 278 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 680 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 20545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 92.7% | 92.7% | -0.7 | 100% | 🟡 7 pts to go |
| P10R | 96430 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2607 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 9344 | 1.0% | 1.0% | -19.0 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17855 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 70.8% | 70.8% | +70.8 | n/a | no target |
| P01T | 304 | 0.3% | 0.3% | -0.8 | n/a | no target |
| P01_GOLD | 625 | 51.7% | 51.7% | -0.2 | 85% | ❌ 33 pts to go |
| P02 | 462 | 58.0% | 58.0% | -8.8 | 90% | ❌ 32 pts to go |
| P03 | 255 | 44.3% | 44.3% | -10.5 | 85% | ❌ 41 pts to go |
| P04 | 3254 | 31.6% | 31.6% | -32.5 | 90% | ❌ 58 pts to go |
| P05 | 413 | 32.4% | 32.4% | -2.8 | 75% | ❌ 43 pts to go |
| P06M | 6002 | 90.3% | 90.3% | +90.3 | n/a | no target |
| P06T | 53606 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 278 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 680 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 20545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 85.1% | 85.1% | -0.5 | 95% | 🟡 10 pts to go |
| P10R | 96430 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2607 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 9344 | 0.9% | 0.9% | -16.4 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17855 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 70.8% | 70.8% | +70.8 | n/a | no target |
| P01T | 304 | 0.3% | 0.3% | -0.8 | n/a | no target |
| P01_GOLD | 625 | 51.7% | 51.7% | -0.4 | 85% | ❌ 33 pts to go |
| P02 | 462 | 53.0% | 53.0% | -8.1 | 90% | ❌ 37 pts to go |
| P03 | 255 | 45.5% | 45.5% | -10.7 | 85% | ❌ 40 pts to go |
| P04 | 3254 | 26.9% | 26.9% | -27.4 | 90% | ❌ 63 pts to go |
| P05 | 413 | 42.4% | 42.4% | +0.7 | 75% | ❌ 33 pts to go |
| P06M | 6002 | 83.5% | 83.5% | +83.5 | n/a | no target |
| P06T | 53606 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 278 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 680 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 20545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10R | 96430 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2607 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 9344 | 0.7% | 0.7% | -13.4 | n/a | no target |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 17855 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 78.5% | 78.5% | +78.5 | n/a | no target |
| P01T | 304 | 91.8% | 91.8% | +10.3 | n/a | no target |
| P01_GOLD | 625 | 85.4% | 85.4% | -0.3 | 100% | ❌ 15 pts to go |
| P02 | 462 | 76.0% | 76.0% | -5.7 | 100% | ❌ 24 pts to go |
| P03 | 255 | 92.2% | 92.2% | -0.1 | n/a | no target |
| P04 | 3254 | 52.5% | 52.5% | -20.1 | 95% | ❌ 42 pts to go |
| P05 | 413 | 77.7% | 77.7% | +2.2 | 95% | ❌ 17 pts to go |
| P06M | 6002 | 97.4% | 97.4% | +96.8 | n/a | no target |
| P06T | 53606 | 85.0% | 85.0% | +1.6 | n/a | no target |
| P06 | 278 | 28.1% | 28.1% | -47.8 | n/a | no target |
| P07 | 680 | 20.9% | 20.9% | -56.1 | n/a | no target |
| P08 | 20545 | 12.3% | 12.4% | -72.6 | n/a | no target |
| P09 | 303 | 98.7% | 98.7% | -0.3 | 100% | 🟡 1 pts to go |
| P10R | 96430 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2607 | 72.1% | 72.1% | -26.3 | n/a | no target |
| P11 | 9344 | 51.7% | 51.7% | -38.2 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17855 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 78.5% | 78.5% | +78.5 | n/a | no target |
| P01T | 304 | 91.8% | 91.8% | +10.3 | n/a | no target |
| P01_GOLD | 625 | 88.6% | 88.6% | -0.3 | 100% | ❌ 11 pts to go |
| P02 | 462 | 77.1% | 77.3% | -5.8 | 100% | ❌ 23 pts to go |
| P03 | 255 | 92.9% | 92.9% | -0.9 | n/a | no target |
| P04 | 3254 | 56.2% | 56.2% | -22.8 | 95% | ❌ 39 pts to go |
| P05 | 413 | 90.3% | 90.3% | +0.2 | 70% | ✅ met |
| P06M | 6002 | 97.4% | 97.4% | +96.8 | n/a | no target |
| P06T | 53606 | 85.0% | 85.0% | +1.6 | n/a | no target |
| P06 | 278 | 28.1% | 28.1% | -47.8 | n/a | no target |
| P07 | 680 | 20.9% | 20.9% | -56.1 | n/a | no target |
| P08 | 20545 | 12.3% | 12.4% | -72.6 | n/a | no target |
| P09 | 303 | 98.7% | 98.7% | -0.3 | 100% | 🟡 1 pts to go |
| P10R | 96430 | 100.0% | 100.0% |  | n/a | no target |
| P10 | 2607 | 72.1% | 72.1% | -26.3 | n/a | no target |
| P11 | 9344 | 51.7% | 51.7% | -38.6 | n/a | no target |
| P12 | 8 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17855 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 304 | 0.0% | 0.0% | -1.1 | n/a | no target |
| P01_GOLD | 625 | 16.8% | 16.8% | -0.5 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 362 rows, 29.0% filled |
| P02 | 462 | 11.3% | 11.3% | -1.8 | n/a | no target · rows from a source that publishes bids: 290 rows, 17.9% filled |
| P03 | 255 | 13.3% | 13.3% | -3.0 | n/a | no target · rows from a source that publishes bids: 139 rows, 24.5% filled |
| P04 | 3254 | 1.7% | 1.7% | -2.0 | n/a | no target · rows from a source that publishes bids: 870 rows, 6.3% filled |
| P05 | 413 | 3.1% | 3.1% | -0.3 | n/a | no target · rows from a source that publishes bids: 53 rows, 24.5% filled |
| P06M | 6002 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 53606 | 0.0% | 0.0% | -0.1 | n/a | no target |
| P06 | 278 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 680 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 20545 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 303 | 3.0% | 3.0% | -0.1 | n/a | no target · rows from a source that publishes bids: 290 rows, 3.1% filled |
| P10R | 96430 | 0.0% | 0.0% |  | n/a | no target |
| P10 | 2607 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 9344 | 0.1% | 0.1% | -2.6 | n/a | no target · rows from a source that publishes bids: 90 rows, 12.2% filled |
| P12 | 8 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 8 rows, 0.0% filled |
| P13 | 17855 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 304 | 0.3% | 98.4% | +0.3 | n/a | no target |
| P01_GOLD | 625 | 53.1% | 82.4% | -0.1 | 90% | ❌ 37 pts to go |
| P02 | 462 | 52.8% | 87.4% | -8.3 | 90% | ❌ 37 pts to go |
| P03 | 255 | 45.9% | 80.0% | -10.3 | 90% | ❌ 44 pts to go |
| P04 | 3254 | 21.9% | 93.1% | -23.4 | 90% | ❌ 68 pts to go |
| P05 | 413 | 0.0% | 82.3% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 6002 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 53606 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 278 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 680 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 20545 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 303 | 2.3% | 4.0% | +0.2 | 90% | ❌ 88 pts to go |
| P10R | 96430 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2607 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 9344 | 0.7% | 99.5% | -12.0 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17855 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 304 | 0.7% | 98.7% | +0.7 | n/a | no target |
| P01_GOLD | 625 | 25.9% | 55.2% | -0.1 | 90% | ❌ 64 pts to go |
| P02 | 462 | 51.9% | 86.6% | -8.0 | n/a | no target |
| P03 | 255 | 25.1% | 59.2% | -5.7 | n/a | no target |
| P04 | 3254 | 23.9% | 95.1% | -25.8 | n/a | no target |
| P05 | 413 | 0.5% | 82.8% | +0.0 | n/a | no target |
| P06M | 6002 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 53606 | 0.1% | 99.9% | +0.1 | n/a | no target |
| P06 | 278 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 680 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 20545 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 303 | 41.9% | 43.6% | -2.5 | n/a | no target |
| P10R | 96430 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2607 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 9344 | 0.6% | 99.5% | -11.0 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17855 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 304 | 1.6% | 99.7% | -0.6 | n/a | no target |
| P01_GOLD | 625 | 51.7% | 81.0% | +0.1 | 95% | ❌ 43 pts to go |
| P02 | 462 | 56.9% | 91.6% | -8.7 | n/a | no target |
| P03 | 255 | 48.2% | 82.4% | -10.9 | n/a | no target |
| P04 | 3254 | 24.2% | 95.4% | -26.1 | n/a | no target |
| P05 | 413 | 4.8% | 87.2% | -0.4 | n/a | no target |
| P06M | 6002 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 53606 | 0.1% | 100.0% | +0.1 | n/a | no target |
| P06 | 278 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 680 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 20545 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 303 | 64.0% | 65.7% | -3.5 | n/a | no target |
| P10R | 96430 | 0.0% | 100.0% |  | n/a | no target |
| P10 | 2607 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 9344 | 0.6% | 99.5% | -12.1 | n/a | no target |
| P12 | 8 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 17855 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P01T | 304 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 462 | 99.4% | 99.4% | -0.6 | 100% | 🟡 1 pts to go |
| P03 | 255 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3254 | 99.4% | 99.4% | -0.6 | 100% | 🟡 1 pts to go |
| P05 | 413 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P06M | 6002 | 98.2% | 98.2% | -1.8 | 100% | 🟡 2 pts to go |
| P06T | 53606 | 96.5% | 96.5% | -3.5 | 100% | 🟡 4 pts to go |
| P06 | 278 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 680 | 98.7% | 98.7% | -1.3 | 100% | 🟡 1 pts to go |
| P08 | 20545 | 99.1% | 99.1% | -0.9 | 100% | 🟡 1 pts to go |
| P09 | 303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 96430 | 95.0% | 95.0% |  | 100% | 🟡 5 pts to go |
| P10 | 2607 | 99.2% | 99.2% | -0.8 | 100% | 🟡 1 pts to go |
| P11 | 9344 | 89.6% | 89.6% | -10.4 | 100% | ❌ 10 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17855 | 97.0% | 97.0% | -3.0 | 100% | 🟡 3 pts to go |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P01T | 304 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 462 | 99.4% | 99.4% | -0.6 | 100% | 🟡 1 pts to go |
| P03 | 255 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3254 | 99.4% | 99.4% | -0.6 | 100% | 🟡 1 pts to go |
| P05 | 413 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P06M | 6002 | 98.2% | 98.2% | -1.8 | 100% | 🟡 2 pts to go |
| P06T | 53606 | 96.5% | 96.5% | -3.5 | 100% | 🟡 4 pts to go |
| P06 | 278 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 680 | 98.7% | 98.7% | -1.3 | 100% | 🟡 1 pts to go |
| P08 | 20545 | 99.1% | 99.1% | -0.9 | 100% | 🟡 1 pts to go |
| P09 | 303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 96430 | 95.0% | 95.0% |  | 100% | 🟡 5 pts to go |
| P10 | 2607 | 99.2% | 99.2% | -0.8 | 100% | 🟡 1 pts to go |
| P11 | 9344 | 89.6% | 89.6% | -10.4 | 100% | ❌ 10 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17855 | 97.0% | 97.0% | -3.0 | 100% | 🟡 3 pts to go |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 65 | 98.5% | 98.5% | -1.5 | 100% | 🟡 2 pts to go |
| P01T | 304 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P01_GOLD | 625 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 462 | 99.4% | 99.4% | -0.6 | 100% | 🟡 1 pts to go |
| P03 | 255 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 3254 | 99.4% | 99.4% | -0.6 | 100% | 🟡 1 pts to go |
| P05 | 413 | 99.3% | 99.3% | -0.7 | 100% | 🟡 1 pts to go |
| P06M | 6002 | 98.2% | 98.2% | -1.8 | 100% | 🟡 2 pts to go |
| P06T | 53606 | 96.5% | 96.5% | -3.5 | 100% | 🟡 4 pts to go |
| P06 | 278 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 680 | 98.7% | 98.7% | -1.3 | 100% | 🟡 1 pts to go |
| P08 | 20545 | 99.1% | 99.1% | -0.9 | 100% | 🟡 1 pts to go |
| P09 | 303 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10R | 96430 | 95.0% | 95.0% |  | 100% | 🟡 5 pts to go |
| P10 | 2607 | 99.2% | 99.2% | -0.8 | 100% | 🟡 1 pts to go |
| P11 | 9344 | 89.6% | 89.6% | -10.4 | 100% | ❌ 10 pts to go |
| P12 | 8 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 17855 | 97.0% | 97.0% | -3.0 | 100% | 🟡 3 pts to go |


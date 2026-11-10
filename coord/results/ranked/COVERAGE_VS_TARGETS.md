# Coverage vs the downstream team's targets — 2026-11-10

Benchmarks (field × package with a numeric target): **98 of 438 met** (22.4%); 76 within 10 points; 264 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 18, P01T 93, P01_GOLD 624, P02 404, P03 208, P04 1566, P05 384, P06M 168, P06T 2616, P06 210, P07 384, P08 6837, P09 381, P10 2386, P11 592, P12 18, P13 48867

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 33.3% | 8 | reference to quote (PO / contract / vendor id) (18 rows) |
| P01T | 93 | 1.1% | 46.2% | 8 | reference to quote (PO / contract / vendor id) (88 rows) |
| P01_GOLD | 624 | 24.2% | 71.2% | 10 | payment terms (214 rows) |
| P02 | 404 | 9.2% | 62.9% | 9 | PO rule (298 rows) |
| P03 | 208 | 17.8% | 70.2% | 9 | PO rule (91 rows) |
| P04 | 1566 | 2.9% | 38.4% | 8 | PO rule (1411 rows) |
| P05 | 384 | 1.3% | 18.5% | 7 | payment terms (315 rows) |
| P06M | 168 | 0.0% | 5.4% | 7 | reference to quote (PO / contract / vendor id) (168 rows) |
| P06T | 2616 | 0.0% | 5.3% | 6 | reference to quote (PO / contract / vendor id) (2612 rows) |
| P06 | 210 | 0.0% | 11.0% | 6 | reference to quote (PO / contract / vendor id) (210 rows) |
| P07 | 384 | 0.0% | 3.9% | 6 | reference to quote (PO / contract / vendor id) (384 rows) |
| P08 | 6837 | 0.0% | 0.4% | 5 | reference to quote (PO / contract / vendor id) (6837 rows) |
| P09 | 381 | 1.0% | 44.6% | 8 | payment terms (355 rows) |
| P10 | 2386 | 0.0% | 0.9% | 6 | reference to quote (PO / contract / vendor id) (2383 rows) |
| P11 | 592 | 1.0% | 9.8% | 4 | PO rule (560 rows) |
| P12 | 18 | 0.0% | 44.4% | 8 | PO rule (17 rows) |
| P13 | 48867 | 0.0% | 0.0% | 6 | reference to quote (PO / contract / vendor id) (48867 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 18 | 5 | 3 | 10 | 0 | 0 | 77 |
| P01T | 93 | 27 | 40 | 26 | 0 | 0 | 80 |
| P01_GOLD | 624 | 230 | 186 | 208 | 0 | 0 | 82 |
| P02 | 404 | 0 | 184 | 220 | 0 | 0 | 66 |
| P03 | 208 | 0 | 0 | 201 | 7 | 0 | 58 |
| P04 | 1566 | 0 | 0 | 1516 | 50 | 0 | 53 |
| P05 | 384 | 15 | 29 | 324 | 16 | 0 | 51 |
| P06M | 168 | 0 | 5 | 159 | 4 | 0 | 51 |
| P06T | 2616 | 0 | 25 | 2368 | 223 | 0 | 51 |
| P06 | 210 | 21 | 33 | 156 | 0 | 0 | 71 |
| P07 | 384 | 0 | 16 | 335 | 33 | 0 | 53 |
| P08 | 6837 | 0 | 0 | 4298 | 2539 | 0 | 43 |
| P09 | 381 | 5 | 13 | 360 | 3 | 0 | 53 |
| P10 | 2386 | 3 | 13 | 1817 | 553 | 0 | 43 |
| P11 | 592 | 0 | 0 | 0 | 0 | 592 | 28 |
| P12 | 18 | 0 | 1 | 17 | 0 | 0 | 54 |
| P13 | 48867 | 5 | 21 | 42195 | 6646 | 0 | 45 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 18 | 7 | 38.9% | the buyer's PO / reference rule (10) |
| P01T | 93 | 53 | 57.0% | the buyer's PO / reference rule (24) |
| P01_GOLD | 624 | 463 | 74.2% | bill-to legal name and address (109) |
| P02 | 404 | 306 | 75.7% | the buyer's PO / reference rule (54) |
| P03 | 208 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (208) |
| P04 | 1566 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (1566) |
| P05 | 384 | 47 | 12.2% | a confirmed invoicing / AP or finance channel (296) |
| P06M | 168 | 2 | 1.2% | a confirmed invoicing / AP or finance channel (143) |
| P06T | 2616 | 16 | 0.6% | a confirmed invoicing / AP or finance channel (2530) |
| P06 | 210 | 34 | 16.2% | bill-to legal name and address (105) |
| P07 | 384 | 9 | 2.3% | a confirmed invoicing / AP or finance channel (145) |
| P08 | 6837 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (6837) |
| P09 | 381 | 50 | 13.1% | a confirmed invoicing / AP or finance channel (322) |
| P10 | 2386 | 8 | 0.3% | a confirmed invoicing / AP or finance channel (2264) |
| P11 | 592 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (592) |
| P12 | 18 | 5 | 27.8% | a confirmed invoicing / AP or finance channel (13) |
| P13 | 48867 | 10 | 0.0% | a confirmed invoicing / AP or finance channel (47705) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 18 | 7 | 38.9% | 9 | 0 | tax treatment (1) |
| P01T | 93 | 41 | 44.1% | 15 | 0 | the vendor's GST/HST number (BN9) (18) |
| P01_GOLD | 624 | 408 | 65.4% | 20 | 0 | the vendor's GST/HST number (BN9) (124) |
| P02 | 404 | 219 | 54.2% | 35 | 0 | the vendor's GST/HST number (BN9) (130) |
| P03 | 208 | 17 | 8.2% | 1 | 131 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (48) |
| P04 | 1566 | 43 | 2.7% | 10 | 706 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (769) |
| P05 | 384 | 22 | 5.7% | 10 | 95 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (192) |
| P06M | 168 | 3 | 1.8% | 18 | 81 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (59) |
| P06T | 2616 | 17 | 0.6% | 54 | 1163 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1306) |
| P06 | 210 | 16 | 7.6% | 23 | 0 | the vendor's GST/HST number (BN9) (87) |
| P07 | 384 | 7 | 1.8% | 32 | 17 | the vendor's GST/HST number (BN9) (121) |
| P08 | 6837 | 2 | 0.0% | 3 | 774 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (6026) |
| P09 | 381 | 46 | 12.1% | 1 | 145 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (166) |
| P10 | 2386 | 5 | 0.2% | 21 | 437 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1806) |
| P11 | 592 | 6 | 1.0% | 0 | 0 | a confirmed invoicing / AP or finance channel (575) |
| P12 | 18 | 3 | 16.7% | 0 | 6 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (7) |
| P13 | 48867 | 12 | 0.0% | 893 | 32569 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (15010) |
| **all** | 65756 | 874 | 1.3% | 1145 | 36124 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 13 | 0 | 0 | 0 | 0 | 1 | 0 | 10 | 11 | 1 |
| P01T | 66 | 0 | 0 | 0 | 2 | 6 | 1 | 29 | 40 | 30 |
| P01_GOLD | 394 | 0 | 0 | 0 | 11 | 94 | 34 | 192 | 227 | 60 |
| P02 | 404 | 0 | 404 | 0 | 4 | 38 | 8 | 298 | 227 | 22 |
| P03 | 208 | 0 | 208 | 0 | 2 | 33 | 11 | 91 | 93 | 25 |
| P04 | 1566 | 0 | 1566 | 0 | 11 | 329 | 93 | 1411 | 1207 | 106 |
| P05 | 369 | 0 | 319 | 0 | 8 | 93 | 43 | 302 | 317 | 56 |
| P06M | 168 | 0 | 168 | 0 | 0 | 19 | 31 | 156 | 140 | 0 |
| P06T | 2616 | 0 | 2616 | 0 | 206 | 1044 | 374 | 2511 | 2309 | 88 |
| P06 | 189 | 0 | 0 | 0 | 12 | 93 | 50 | 123 | 157 | 8 |
| P07 | 384 | 0 | 384 | 0 | 55 | 191 | 105 | 321 | 337 | 17 |
| P08 | 6837 | 0 | 6837 | 0 | 1737 | 4478 | 2835 | 6762 | 6673 | 179 |
| P09 | 376 | 0 | 354 | 0 | 9 | 73 | 4 | 348 | 359 | 53 |
| P10 | 2383 | 0 | 2331 | 0 | 29 | 1580 | 700 | 2336 | 2295 | 116 |
| P11 | 592 | 592 | 554 | 0 | 20 | 470 | 275 | 560 | 556 | 32 |
| P12 | 18 | 0 | 16 | 0 | 0 | 4 | 0 | 17 | 16 | 1 |
| P13 | 48862 | 0 | 48585 | 0 | 464 | 23413 | 9142 | 48796 | 48747 | 61 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 9766 |
| ap_system_hint | P13 | 0.6% | 20% | 9498 |
| buyer_phone | P13 | 79.1% | 95% | 7767 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 7296 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 7294 |
| buyer_payment_method_preference | P13 | 0.5% | 15% | 7066 |
| buyer_address | P13 | 81.2% | 95% | 6743 |
| buyer_logo_url | P13 | 84.0% | 95% | 5363 |
| buyer_legal_name_as_published | P13 | 52.1% | 60% | 3867 |
| vendor_registered_address | P08 | 26.1% | 70% | 3002 |
| vendor_logo_url | P08 | 59.1% | 100% | 2798 |
| buyer_legal_name_as_published | P08 | 34.5% | 75% | 2769 |
| vendor_phone | P08 | 46.4% | 85% | 2639 |
| vendor_emails | P08 | 37.3% | 75% | 2576 |
| buyer_phone | P08 | 58.4% | 95% | 2501 |
| buyer_address | P08 | 58.4% | 95% | 2500 |
| buyer_logo_url | P08 | 67.3% | 100% | 2233 |
| buyer_bn_as_published | P13 | 25.6% | 30% | 2144 |
| vendor_bn9 | P08 | 20.5% | 50% | 2017 |
| invoice_reference_hint | P08 | 1.1% | 25% | 1635 |
| buyer_bn_as_published | P08 | 14.0% | 35% | 1434 |
| vendor_trading_name | P08 | 29.5% | 50% | 1403 |
| buyer_ap_cycle_published | P08 | 0.1% | 20% | 1362 |
| ap_system_hint | P08 | 1.3% | 20% | 1280 |
| buyer_esignature_preference | P08 | 0.4% | 15% | 1002 |
| buyer_tax_exempt_status | P08 | 0.5% | 15% | 994 |
| buyer_payment_method_preference | P08 | 0.5% | 15% | 991 |
| buyer_legal_name_as_published | P10 | 33.8% | 70% | 865 |
| average_contract_duration_days | P04 | 45.3% | 90% | 700 |
| vendor_registered_address | P10 | 41.0% | 70% | 692 |
| vendor_emails | P10 | 52.0% | 80% | 668 |
| buyer_phone | P10 | 70.5% | 95% | 585 |
| buyer_address | P10 | 70.5% | 95% | 584 |
| buyer_vendor_id | P04 | 4.3% | 40% | 560 |
| end_date | P04 | 54.3% | 90% | 559 |
| currency | P04 | 60.0% | 95% | 549 |
| vendor_neq | P04 | 60.2% | 95% | 545 |
| invoice_reference_hint | P10 | 2.2% | 25% | 544 |
| ap_phone | P04 | 50.5% | 85% | 541 |
| commodity_codes | P04 | 51.3% | 85% | 529 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 44.4% | 44.4% | +0.0 | 50% | 🟡 6 pts to go |
| P01T | 93 | 71.0% | 71.0% | -0.7 | 50% | ✅ met |
| P01_GOLD | 624 | 92.5% | 94.6% | +0.0 | 95% | 🟡 2 pts to go |
| P02 | 404 | 83.9% | 85.6% | +0.0 | 95% | ❌ 11 pts to go |
| P03 | 208 | 92.8% | 95.7% | +0.0 | 95% | 🟡 2 pts to go |
| P04 | 1566 | 68.6% | 71.3% | +0.0 | 90% | ❌ 21 pts to go |
| P05 | 384 | 41.1% | 44.0% | +0.0 | 70% | ❌ 29 pts to go |
| P06M | 168 | 7.1% | 7.1% | +0.0 | n/a | no target |
| P06T | 2616 | 4.1% | 4.2% | -0.3 | n/a | no target |
| P06 | 210 | 41.4% | 41.4% | -6.8 | 30% | ✅ met |
| P07 | 384 | 16.4% | 16.4% | -7.4 | 30% | ❌ 14 pts to go |
| P08 | 6837 | 1.1% | 1.1% | -1.3 | 25% | ❌ 24 pts to go |
| P09 | 381 | 99.0% | 99.7% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2386 | 2.2% | 3.1% | +0.0 | 25% | ❌ 23 pts to go |
| P11 | 592 | 19.3% | 21.8% | -4.8 | 60% | ❌ 41 pts to go |
| P12 | 18 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 48867 | 0.1% | 0.3% | -0.1 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 624 | 6.2% | 6.2% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 404 | 7.2% | 7.2% | +0.0 | 50% | ❌ 43 pts to go |
| P03 | 208 | 1.9% | 1.9% | +0.0 | 40% | ❌ 38 pts to go |
| P04 | 1566 | 1.1% | 1.1% | +0.0 | 30% | ❌ 29 pts to go |
| P05 | 384 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2616 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 210 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 384 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 6837 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 381 | 0.5% | 0.5% | +0.0 | 50% | ❌ 50 pts to go |
| P10 | 2386 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P11 | 592 | 0.7% | 0.7% | -0.1 | n/a | no target |
| P12 | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 48867 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 5.4% | 5.4% | +0.0 | 50% | ❌ 45 pts to go |
| P01_GOLD | 624 | 67.6% | 67.6% | +0.0 | 85% | ❌ 17 pts to go |
| P02 | 404 | 75.5% | 75.5% | +0.0 | 90% | ❌ 14 pts to go |
| P03 | 208 | 75.5% | 75.5% | +0.0 | 85% | 🟡 10 pts to go |
| P04 | 1566 | 65.5% | 65.5% | +0.0 | 85% | ❌ 20 pts to go |
| P05 | 384 | 31.0% | 31.0% | +0.0 | 60% | ❌ 29 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2616 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06 | 210 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 384 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 6837 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 381 | 96.6% | 96.6% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 2386 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 592 | 16.0% | 16.0% | -4.0 | 60% | ❌ 44 pts to go |
| P12 | 18 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 48867 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 2.2% | 2.2% | +0.0 | 30% | ❌ 28 pts to go |
| P01_GOLD | 624 | 51.3% | 51.3% | +0.0 | 80% | ❌ 29 pts to go |
| P02 | 404 | 66.8% | 66.8% | +0.0 | 60% | ✅ met |
| P03 | 208 | 63.9% | 63.9% | +0.0 | 80% | ❌ 16 pts to go |
| P04 | 1566 | 54.5% | 54.5% | +0.0 | 50% | ✅ met |
| P05 | 384 | 13.3% | 13.3% | +0.0 | 40% | ❌ 27 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2616 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06 | 210 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 384 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 6837 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 381 | 86.1% | 86.1% | +0.0 | 50% | ✅ met |
| P10 | 2386 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 592 | 14.0% | 14.0% | -3.5 | 40% | ❌ 26 pts to go |
| P12 | 18 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 48867 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 3.2% | 3.2% | -0.1 | n/a | no target |
| P01_GOLD | 624 | 61.1% | 61.1% | +0.0 | 85% | ❌ 24 pts to go |
| P02 | 404 | 65.8% | 65.8% | +0.0 | 90% | ❌ 24 pts to go |
| P03 | 208 | 74.5% | 74.5% | +0.0 | 85% | ❌ 10 pts to go |
| P04 | 1566 | 56.3% | 56.3% | +0.0 | 85% | ❌ 29 pts to go |
| P05 | 384 | 21.1% | 21.1% | +0.0 | 50% | ❌ 29 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2616 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06 | 210 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 384 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 6837 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 381 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 2386 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 592 | 15.2% | 15.2% | -3.8 | 60% | ❌ 45 pts to go |
| P12 | 18 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 48867 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 2.2% | 2.2% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 13.0% | 13.0% | +0.0 | 60% | ❌ 47 pts to go |
| P02 | 404 | 7.2% | 7.2% | +0.0 | 50% | ❌ 43 pts to go |
| P03 | 208 | 10.6% | 10.6% | +0.0 | 50% | ❌ 39 pts to go |
| P04 | 1566 | 4.3% | 4.3% | +0.0 | 40% | ❌ 36 pts to go |
| P05 | 384 | 1.3% | 1.3% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2616 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P06 | 210 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 384 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 6837 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 381 | 2.6% | 2.6% | +0.0 | 50% | ❌ 47 pts to go |
| P10 | 2386 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 592 | 2.4% | 2.4% | -0.6 | n/a | no target |
| P12 | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 48867 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 35.1% | 35.1% | +0.0 | 80% | ❌ 45 pts to go |
| P02 | 404 | 60.6% | 60.6% | +0.0 | 90% | ❌ 29 pts to go |
| P03 | 208 | 41.3% | 41.3% | +0.0 | 80% | ❌ 39 pts to go |
| P04 | 1566 | 51.3% | 51.3% | +0.0 | 85% | ❌ 34 pts to go |
| P05 | 384 | 6.0% | 6.0% | +0.0 | 50% | ❌ 44 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2616 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 210 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 384 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 6837 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 381 | 75.9% | 75.9% | +0.0 | 95% | ❌ 19 pts to go |
| P10 | 2386 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 592 | 10.5% | 10.5% | -2.6 | 50% | ❌ 40 pts to go |
| P12 | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 48867 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 1.1% | 1.1% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 404 | 7.2% | 7.2% | +0.0 | 50% | ❌ 43 pts to go |
| P03 | 208 | 2.4% | 2.4% | +0.0 | 30% | ❌ 28 pts to go |
| P04 | 1566 | 1.1% | 1.1% | +0.0 | 30% | ❌ 29 pts to go |
| P05 | 384 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2616 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 210 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 384 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 6837 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 381 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10 | 2386 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 592 | 0.7% | 0.7% | -0.1 | n/a | no target |
| P12 | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 48867 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 93 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 624 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 404 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 208 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1566 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 384 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 168 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 2616 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 210 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 384 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 6837 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 381 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2386 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 592 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 18 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 48867 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P01T | 93 | 80.6% | 80.6% | +0.2 | 60% | ✅ met |
| P01_GOLD | 624 | 77.7% | 77.7% | -0.2 | 90% | ❌ 12 pts to go |
| P02 | 404 | 67.3% | 67.3% | +0.0 | 85% | ❌ 18 pts to go |
| P03 | 208 | 82.2% | 82.2% | +0.0 | 90% | 🟡 8 pts to go |
| P04 | 1566 | 55.4% | 55.4% | +0.0 | 75% | ❌ 20 pts to go |
| P05 | 384 | 52.9% | 52.9% | +0.3 | 50% | ✅ met |
| P06M | 168 | 74.4% | 74.4% | +0.0 | n/a | no target |
| P06T | 2616 | 62.3% | 62.3% | +1.6 | n/a | no target |
| P06 | 210 | 36.2% | 36.2% | -7.8 | 40% | 🟡 4 pts to go |
| P07 | 384 | 26.8% | 26.8% | -11.3 | 50% | ❌ 23 pts to go |
| P08 | 6837 | 20.5% | 20.5% | -19.7 | 50% | ❌ 30 pts to go |
| P09 | 381 | 54.3% | 54.3% | +0.0 | 80% | ❌ 26 pts to go |
| P10 | 2386 | 35.8% | 35.8% | -0.8 | 40% | 🟡 4 pts to go |
| P11 | 592 | 36.3% | 36.3% | -8.4 | 60% | ❌ 24 pts to go |
| P12 | 18 | 50.0% | 50.0% | -2.6 | 85% | ❌ 35 pts to go |
| P13 | 48867 | 91.8% | 91.8% | +0.1 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 94.4% | 94.4% | +33.3 | n/a | no target |
| P01T | 93 | 63.4% | 63.4% | +0.4 | n/a | no target |
| P01_GOLD | 624 | 74.8% | 74.8% | +0.0 | 95% | ❌ 20 pts to go |
| P02 | 404 | 84.9% | 84.9% | +0.0 | 95% | ❌ 10 pts to go |
| P03 | 208 | 77.9% | 77.9% | +0.0 | 95% | ❌ 17 pts to go |
| P04 | 1566 | 80.7% | 80.7% | +0.0 | 95% | ❌ 14 pts to go |
| P05 | 384 | 56.2% | 56.2% | +0.0 | 70% | ❌ 14 pts to go |
| P06M | 168 | 58.3% | 58.3% | +37.5 | n/a | no target |
| P06T | 2616 | 79.7% | 79.7% | +1.5 | n/a | no target |
| P06 | 210 | 44.3% | 44.3% | -11.1 | 80% | ❌ 36 pts to go |
| P07 | 384 | 36.2% | 36.2% | -15.8 | 70% | ❌ 34 pts to go |
| P08 | 6837 | 26.1% | 26.1% | -26.3 | 70% | ❌ 44 pts to go |
| P09 | 381 | 88.5% | 88.5% | +0.0 | 100% | ❌ 12 pts to go |
| P10 | 2386 | 41.0% | 41.0% | -1.4 | 70% | ❌ 29 pts to go |
| P11 | 592 | 45.8% | 45.8% | -9.5 | 75% | ❌ 29 pts to go |
| P12 | 18 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 48867 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 50.0% | 50.0% | +0.0 | n/a | no target |
| P01T | 93 | 20.4% | 20.4% | +0.8 | n/a | no target |
| P01_GOLD | 624 | 52.2% | 52.2% | -0.2 | 60% | 🟡 8 pts to go |
| P02 | 404 | 67.3% | 67.3% | +0.0 | 60% | ✅ met |
| P03 | 208 | 64.9% | 64.9% | +0.0 | 60% | ✅ met |
| P04 | 1566 | 55.6% | 55.6% | +0.1 | 55% | ✅ met |
| P05 | 384 | 25.3% | 25.3% | +0.0 | 50% | ❌ 25 pts to go |
| P06M | 168 | 17.3% | 17.3% | +0.0 | n/a | no target |
| P06T | 2616 | 55.7% | 55.7% | +2.1 | n/a | no target |
| P06 | 210 | 45.2% | 45.2% | -7.8 | n/a | no target |
| P07 | 384 | 35.4% | 35.4% | -10.6 | 55% | ❌ 20 pts to go |
| P08 | 6837 | 29.5% | 29.5% | -18.0 | 50% | ❌ 20 pts to go |
| P09 | 381 | 71.4% | 71.4% | +0.0 | 70% | ✅ met |
| P10 | 2386 | 51.3% | 51.3% | -0.6 | 55% | 🟡 4 pts to go |
| P11 | 592 | 37.8% | 37.8% | -5.2 | 50% | ❌ 12 pts to go |
| P12 | 18 | 83.3% | 83.3% | -0.9 | n/a | no target |
| P13 | 48867 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 61.1% | 61.1% | +0.0 | n/a | no target |
| P01T | 93 | 30.1% | 30.1% | -0.3 | n/a | no target |
| P01_GOLD | 624 | 51.8% | 51.8% | +0.0 | 70% | ❌ 18 pts to go |
| P02 | 404 | 57.2% | 57.2% | +0.0 | 70% | ❌ 13 pts to go |
| P03 | 208 | 57.2% | 57.2% | +0.0 | 70% | ❌ 13 pts to go |
| P04 | 1566 | 52.0% | 52.0% | +0.0 | 65% | ❌ 13 pts to go |
| P05 | 384 | 34.6% | 34.6% | +0.0 | 60% | ❌ 25 pts to go |
| P06M | 168 | 30.4% | 30.4% | +0.0 | n/a | no target |
| P06T | 2616 | 3.2% | 3.2% | -0.3 | n/a | no target |
| P06 | 210 | 53.8% | 53.8% | -5.8 | 40% | ✅ met |
| P07 | 384 | 55.5% | 55.5% | -12.4 | 85% | ❌ 30 pts to go |
| P08 | 6837 | 46.4% | 46.4% | -21.7 | 85% | ❌ 39 pts to go |
| P09 | 381 | 55.4% | 55.4% | +0.0 | 85% | ❌ 30 pts to go |
| P10 | 2386 | 66.4% | 66.4% | +0.1 | 85% | ❌ 19 pts to go |
| P11 | 592 | 51.9% | 51.9% | -3.0 | 75% | ❌ 23 pts to go |
| P12 | 18 | 11.1% | 11.1% | -4.7 | n/a | no target |
| P13 | 48867 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 94.4% | 94.4% | +0.0 | n/a | no target |
| P01T | 93 | 90.3% | 90.3% | +0.1 | n/a | no target |
| P01_GOLD | 624 | 89.4% | 89.4% | +0.0 | 90% | 🟡 1 pts to go |
| P02 | 404 | 87.9% | 87.9% | +0.3 | 90% | 🟡 2 pts to go |
| P03 | 208 | 89.9% | 89.9% | +0.0 | 90% | 🟡 0 pts to go |
| P04 | 1566 | 81.3% | 81.3% | +0.0 | 85% | 🟡 4 pts to go |
| P05 | 384 | 51.0% | 51.0% | +0.0 | 70% | ❌ 19 pts to go |
| P06M | 168 | 67.9% | 67.9% | +0.0 | n/a | no target |
| P06T | 2616 | 78.4% | 78.4% | +0.5 | n/a | no target |
| P06 | 210 | 97.6% | 97.6% | +0.6 | 50% | ✅ met |
| P07 | 384 | 97.9% | 97.9% | +1.1 | 100% | 🟡 2 pts to go |
| P08 | 6837 | 98.2% | 98.2% | +2.1 | 100% | 🟡 2 pts to go |
| P09 | 381 | 79.8% | 79.8% | +0.0 | 100% | ❌ 20 pts to go |
| P10 | 2386 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 592 | 94.4% | 94.4% | +1.4 | 100% | 🟡 6 pts to go |
| P12 | 18 | 38.9% | 38.9% | -3.2 | n/a | no target |
| P13 | 48867 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 50.0% | 50.0% | +0.0 | n/a | no target |
| P01T | 93 | 45.2% | 45.2% | -0.5 | n/a | no target |
| P01_GOLD | 624 | 45.7% | 45.7% | +0.0 | 70% | ❌ 24 pts to go |
| P02 | 404 | 51.7% | 51.7% | +0.2 | 75% | ❌ 23 pts to go |
| P03 | 208 | 51.4% | 51.4% | +0.0 | 75% | ❌ 24 pts to go |
| P04 | 1566 | 42.9% | 42.9% | +0.0 | 70% | ❌ 27 pts to go |
| P05 | 384 | 24.5% | 24.5% | +0.0 | 55% | ❌ 30 pts to go |
| P06M | 168 | 16.1% | 16.1% | +0.0 | n/a | no target |
| P06T | 2616 | 2.7% | 2.7% | -0.2 | n/a | no target |
| P06 | 210 | 40.5% | 40.5% | -0.5 | n/a | no target |
| P07 | 384 | 33.6% | 33.6% | -3.3 | 70% | ❌ 36 pts to go |
| P08 | 6837 | 37.3% | 37.3% | -11.4 | 75% | ❌ 38 pts to go |
| P09 | 381 | 52.0% | 52.0% | +0.0 | 85% | ❌ 33 pts to go |
| P10 | 2386 | 52.0% | 52.0% | +0.7 | 80% | ❌ 28 pts to go |
| P11 | 592 | 40.7% | 40.7% | +0.2 | 70% | ❌ 29 pts to go |
| P12 | 18 | 27.8% | 27.8% | -3.8 | n/a | no target |
| P13 | 48867 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 94.4% | 94.4% | +0.0 | n/a | no target |
| P01T | 93 | 89.2% | 89.2% | +0.1 | n/a | no target |
| P01_GOLD | 624 | 79.8% | 79.8% | +0.0 | 90% | ❌ 10 pts to go |
| P02 | 404 | 77.5% | 77.5% | +0.3 | 90% | ❌ 12 pts to go |
| P03 | 208 | 81.7% | 81.7% | +0.0 | 90% | 🟡 8 pts to go |
| P04 | 1566 | 70.9% | 70.9% | +0.0 | 85% | ❌ 14 pts to go |
| P05 | 384 | 48.4% | 48.4% | +0.0 | 75% | ❌ 27 pts to go |
| P06M | 168 | 67.9% | 67.9% | +0.0 | n/a | no target |
| P06T | 2616 | 77.6% | 77.6% | +0.5 | n/a | no target |
| P06 | 210 | 80.0% | 80.0% | -8.6 | n/a | no target |
| P07 | 384 | 71.9% | 71.9% | -18.6 | 100% | ❌ 28 pts to go |
| P08 | 6837 | 59.1% | 59.1% | -29.9 | 100% | ❌ 41 pts to go |
| P09 | 381 | 62.5% | 62.5% | +0.0 | n/a | no target |
| P10 | 2386 | 89.3% | 89.3% | +0.3 | 100% | ❌ 11 pts to go |
| P11 | 592 | 69.1% | 69.1% | -5.4 | n/a | no target |
| P12 | 18 | 33.3% | 33.3% | -3.5 | n/a | no target |
| P13 | 48867 | 82.8% | 82.8% | +0.1 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 22.6% | 22.6% | +0.9 | n/a | no target · QC vendors: 2 rows, 100.0% filled |
| P01_GOLD | 624 | 47.9% | 47.9% | +0.0 | 95% | ❌ 47 pts to go · QC vendors: 52 rows, 98.1% filled |
| P02 | 404 | 68.6% | 68.6% | +0.0 | 95% | ❌ 26 pts to go · QC vendors: 107 rows, 100.0% filled |
| P03 | 208 | 55.8% | 55.8% | +0.0 | 95% | ❌ 39 pts to go · QC vendors: 17 rows, 100.0% filled |
| P04 | 1566 | 60.2% | 60.2% | +0.0 | 95% | ❌ 35 pts to go · QC vendors: 435 rows, 98.6% filled |
| P05 | 384 | 14.8% | 14.8% | +0.0 | n/a | no target · QC vendors: 30 rows, 93.3% filled |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2616 | 58.8% | 58.8% | +2.9 | n/a | no target · QC vendors: 82 rows, 100.0% filled |
| P06 | 210 | 21.4% | 21.4% | -5.1 | n/a | no target · QC vendors: 21 rows, 100.0% filled |
| P07 | 384 | 15.4% | 15.4% | -6.0 | n/a | no target · QC vendors: 34 rows, 97.1% filled |
| P08 | 6837 | 14.6% | 14.6% | -14.3 | n/a | no target · QC vendors: 672 rows, 99.3% filled |
| P09 | 381 | 80.1% | 80.1% | +0.0 | 95% | ❌ 15 pts to go · QC vendors: 154 rows, 99.4% filled |
| P10 | 2386 | 23.1% | 23.1% | -0.3 | n/a | no target · QC vendors: 432 rows, 97.7% filled |
| P11 | 592 | 24.8% | 24.8% | -4.5 | n/a | no target · QC vendors: 89 rows, 98.9% filled |
| P12 | 18 | 72.2% | 72.2% | -1.5 | n/a | no target · QC vendors: 3 rows, 100.0% filled |
| P13 | 48867 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 61.1% | 61.1% | +0.0 | n/a | no target · vendors with a registry record: 11 rows, 100.0% filled |
| P01T | 93 | 63.4% | 63.4% | +0.4 | n/a | no target · vendors with a registry record: 59 rows, 100.0% filled |
| P01_GOLD | 624 | 83.3% | 83.3% | -0.2 | 100% | ❌ 17 pts to go · vendors with a registry record: 520 rows, 100.0% filled |
| P02 | 404 | 89.1% | 89.1% | +0.0 | 100% | ❌ 11 pts to go · vendors with a registry record: 360 rows, 100.0% filled |
| P03 | 208 | 88.9% | 88.9% | +0.0 | 100% | ❌ 11 pts to go · vendors with a registry record: 185 rows, 100.0% filled |
| P04 | 1566 | 81.4% | 81.4% | +0.0 | 100% | ❌ 19 pts to go · vendors with a registry record: 1275 rows, 100.0% filled |
| P05 | 384 | 61.7% | 61.7% | +0.0 | n/a | no target · vendors with a registry record: 237 rows, 100.0% filled |
| P06M | 168 | 20.8% | 20.8% | +0.0 | n/a | no target · vendors with a registry record: 35 rows, 100.0% filled |
| P06T | 2616 | 79.7% | 79.7% | +1.5 | n/a | no target · vendors with a registry record: 2085 rows, 100.0% filled |
| P06 | 210 | 46.2% | 46.2% | -11.6 | n/a | no target · vendors with a registry record: 97 rows, 100.0% filled |
| P07 | 384 | 37.2% | 37.2% | -17.2 | n/a | no target · vendors with a registry record: 143 rows, 100.0% filled |
| P08 | 6837 | 26.9% | 26.9% | -27.4 | n/a | no target · vendors with a registry record: 1837 rows, 100.0% filled |
| P09 | 381 | 91.6% | 91.6% | +0.0 | n/a | no target · vendors with a registry record: 349 rows, 100.0% filled |
| P10 | 2386 | 42.3% | 42.3% | -1.4 | n/a | no target · vendors with a registry record: 1010 rows, 100.0% filled |
| P11 | 592 | 48.0% | 48.0% | -10.2 | n/a | no target · vendors with a registry record: 284 rows, 100.0% filled |
| P12 | 18 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 18 rows, 100.0% filled |
| P13 | 48867 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 94.4% | 94.4% | +0.0 | 90% | ✅ met |
| P01T | 93 | 93.5% | 93.5% | -1.1 | 90% | ✅ met |
| P01_GOLD | 624 | 84.9% | 84.9% | +0.3 | 95% | ❌ 10 pts to go |
| P02 | 404 | 90.6% | 90.6% | +0.0 | 95% | 🟡 4 pts to go |
| P03 | 208 | 84.1% | 84.1% | +0.9 | 85% | 🟡 1 pts to go |
| P04 | 1566 | 79.0% | 79.0% | +0.2 | 90% | ❌ 11 pts to go |
| P05 | 384 | 75.8% | 75.8% | +0.0 | 75% | ✅ met |
| P06M | 168 | 88.7% | 88.7% | +0.0 | n/a | no target |
| P06T | 2616 | 60.1% | 60.1% | -4.3 | n/a | no target |
| P06 | 210 | 55.7% | 55.7% | -0.9 | 80% | ❌ 24 pts to go |
| P07 | 384 | 50.3% | 50.3% | -3.3 | 80% | ❌ 30 pts to go |
| P08 | 6837 | 34.5% | 34.5% | -2.3 | 75% | ❌ 40 pts to go |
| P09 | 381 | 80.8% | 80.8% | +0.0 | 95% | ❌ 14 pts to go |
| P10 | 2386 | 33.8% | 33.8% | +1.8 | 70% | ❌ 36 pts to go |
| P11 | 592 | 20.6% | 20.6% | -4.3 | 65% | ❌ 44 pts to go |
| P12 | 18 | 77.8% | 77.8% | +4.1 | 80% | 🟡 2 pts to go |
| P13 | 48867 | 52.1% | 52.1% | -0.4 | 60% | 🟡 8 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 38.9% | 38.9% | +0.0 | 50% | ❌ 11 pts to go |
| P01T | 93 | 20.4% | 20.4% | -0.3 | n/a | no target |
| P01_GOLD | 624 | 20.5% | 20.5% | +0.1 | 40% | ❌ 20 pts to go |
| P02 | 404 | 21.8% | 21.8% | +0.0 | 40% | ❌ 18 pts to go |
| P03 | 208 | 26.9% | 26.9% | +0.0 | 40% | ❌ 13 pts to go |
| P04 | 1566 | 27.6% | 27.6% | +0.0 | 40% | ❌ 12 pts to go |
| P05 | 384 | 22.9% | 22.9% | +0.0 | 25% | 🟡 2 pts to go |
| P06M | 168 | 25.6% | 25.6% | +0.0 | n/a | no target |
| P06T | 2616 | 28.8% | 28.8% | -2.1 | n/a | no target |
| P06 | 210 | 11.9% | 11.9% | +1.1 | 35% | ❌ 23 pts to go |
| P07 | 384 | 13.3% | 13.3% | +3.0 | 35% | ❌ 22 pts to go |
| P08 | 6837 | 14.0% | 14.0% | +2.9 | 35% | ❌ 21 pts to go |
| P09 | 381 | 17.1% | 17.1% | +0.0 | n/a | no target |
| P10 | 2386 | 9.8% | 9.8% | +0.2 | 30% | ❌ 20 pts to go |
| P11 | 592 | 7.3% | 7.3% | -1.1 | n/a | no target |
| P12 | 18 | 11.1% | 11.1% | +0.6 | n/a | no target |
| P13 | 48867 | 25.6% | 25.6% | -0.3 | 30% | 🟡 4 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 100.0% | 100.0% | +5.6 | 100% | ✅ met |
| P01T | 93 | 98.9% | 98.9% | +5.4 | 100% | 🟡 1 pts to go |
| P01_GOLD | 624 | 90.2% | 90.2% | +2.5 | 100% | 🟡 10 pts to go |
| P02 | 404 | 97.5% | 97.5% | +0.7 | 100% | 🟡 2 pts to go |
| P03 | 208 | 93.3% | 93.3% | +1.5 | 100% | 🟡 7 pts to go |
| P04 | 1566 | 93.0% | 93.0% | +2.0 | 100% | 🟡 7 pts to go |
| P05 | 384 | 87.8% | 87.8% | +2.9 | 100% | ❌ 12 pts to go |
| P06M | 168 | 81.5% | 81.5% | +9.5 | n/a | no target |
| P06T | 2616 | 85.6% | 85.7% | +5.4 | n/a | no target |
| P06 | 210 | 72.4% | 72.4% | +3.7 | 95% | ❌ 23 pts to go |
| P07 | 384 | 71.9% | 71.9% | +1.3 | 95% | ❌ 23 pts to go |
| P08 | 6837 | 58.4% | 58.4% | -7.8 | 95% | ❌ 37 pts to go |
| P09 | 381 | 95.8% | 95.8% | +0.3 | 100% | 🟡 4 pts to go |
| P10 | 2386 | 70.5% | 70.6% | +5.3 | 95% | ❌ 24 pts to go |
| P11 | 592 | 36.1% | 36.1% | +1.7 | 80% | ❌ 44 pts to go |
| P12 | 18 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 48867 | 81.2% | 81.2% | +5.1 | 95% | ❌ 14 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 88.9% | 88.9% | +0.0 | n/a | no target |
| P01T | 93 | 79.6% | 79.6% | -0.8 | n/a | no target |
| P01_GOLD | 624 | 70.4% | 70.4% | +0.2 | 90% | ❌ 20 pts to go |
| P02 | 404 | 79.7% | 79.7% | +0.0 | 95% | ❌ 15 pts to go |
| P03 | 208 | 73.6% | 73.6% | +0.0 | 95% | ❌ 21 pts to go |
| P04 | 1566 | 84.7% | 84.7% | -0.2 | 95% | ❌ 10 pts to go |
| P05 | 384 | 75.0% | 75.0% | +0.0 | 90% | ❌ 15 pts to go |
| P06M | 168 | 83.9% | 83.9% | +0.0 | n/a | no target |
| P06T | 2616 | 72.2% | 72.2% | -5.1 | n/a | no target |
| P06 | 210 | 61.4% | 61.4% | -3.1 | 95% | ❌ 34 pts to go |
| P07 | 384 | 59.4% | 59.4% | -6.9 | 90% | ❌ 31 pts to go |
| P08 | 6837 | 58.4% | 58.4% | -16.3 | 95% | ❌ 37 pts to go |
| P09 | 381 | 89.0% | 89.0% | +0.0 | 100% | ❌ 11 pts to go |
| P10 | 2386 | 70.5% | 70.5% | -1.0 | 95% | ❌ 24 pts to go |
| P11 | 592 | 28.2% | 28.2% | -0.7 | 75% | ❌ 47 pts to go |
| P12 | 18 | 88.9% | 88.9% | -0.6 | n/a | no target |
| P13 | 48867 | 79.1% | 79.1% | -0.2 | 95% | ❌ 16 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 77.8% | 77.8% | +0.0 | n/a | no target |
| P01T | 93 | 90.3% | 90.3% | -1.0 | 95% | 🟡 5 pts to go |
| P01_GOLD | 624 | 82.2% | 82.2% | +0.0 | 90% | 🟡 8 pts to go |
| P02 | 404 | 88.4% | 88.4% | +0.0 | 95% | 🟡 7 pts to go |
| P03 | 208 | 84.6% | 84.6% | +0.0 | 95% | ❌ 10 pts to go |
| P04 | 1566 | 84.2% | 84.2% | +0.0 | 90% | 🟡 6 pts to go |
| P05 | 384 | 89.6% | 89.6% | +0.0 | 95% | 🟡 5 pts to go |
| P06M | 168 | 85.1% | 85.1% | +0.0 | n/a | no target |
| P06T | 2616 | 87.8% | 87.8% | -6.3 | n/a | no target |
| P06 | 210 | 83.8% | 83.8% | -6.6 | 100% | ❌ 16 pts to go |
| P07 | 384 | 77.1% | 77.1% | -11.0 | 100% | ❌ 23 pts to go |
| P08 | 6837 | 67.3% | 67.3% | -23.4 | 100% | ❌ 33 pts to go |
| P09 | 381 | 74.0% | 74.0% | +0.0 | n/a | no target |
| P10 | 2386 | 90.2% | 90.2% | +0.1 | 100% | 🟡 10 pts to go |
| P11 | 592 | 35.8% | 35.8% | -0.7 | 80% | ❌ 44 pts to go |
| P12 | 18 | 83.3% | 83.3% | -0.9 | n/a | no target |
| P13 | 48867 | 84.0% | 84.0% | -0.2 | 95% | ❌ 11 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 16.7% | 16.7% | +0.0 | n/a | no target |
| P01T | 93 | 23.7% | 23.7% | -0.2 | n/a | no target |
| P01_GOLD | 624 | 14.3% | 14.3% | +0.0 | 25% | ❌ 11 pts to go |
| P02 | 404 | 27.7% | 27.7% | +0.0 | 40% | ❌ 12 pts to go |
| P03 | 208 | 10.6% | 10.6% | +0.0 | 20% | 🟡 9 pts to go |
| P04 | 1566 | 7.4% | 7.4% | +0.0 | 20% | ❌ 13 pts to go |
| P05 | 384 | 3.9% | 3.9% | +0.0 | 15% | ❌ 11 pts to go |
| P06M | 168 | 4.8% | 4.8% | +0.0 | n/a | no target |
| P06T | 2616 | 3.0% | 3.0% | -0.2 | n/a | no target |
| P06 | 210 | 5.7% | 5.7% | +0.3 | n/a | no target |
| P07 | 384 | 6.0% | 6.0% | -0.3 | n/a | no target |
| P08 | 6837 | 0.7% | 0.7% | -0.3 | n/a | no target |
| P09 | 381 | 7.9% | 7.9% | +0.0 | n/a | no target |
| P10 | 2386 | 1.3% | 1.3% | +0.0 | n/a | no target |
| P11 | 592 | 2.0% | 2.0% | -0.5 | n/a | no target |
| P12 | 18 | 11.1% | 11.1% | +0.6 | n/a | no target |
| P13 | 48867 | 0.6% | 0.6% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 38.9% | 38.9% | +0.0 | n/a | no target |
| P01T | 93 | 34.4% | 34.4% | -0.4 | 70% | ❌ 36 pts to go |
| P01_GOLD | 624 | 43.3% | 43.3% | +0.0 | 80% | ❌ 37 pts to go |
| P02 | 404 | 64.1% | 64.1% | +0.0 | 90% | ❌ 26 pts to go |
| P03 | 208 | 23.1% | 23.1% | +0.0 | 60% | ❌ 37 pts to go |
| P04 | 1566 | 50.5% | 50.5% | +0.0 | 85% | ❌ 34 pts to go |
| P05 | 384 | 13.0% | 13.0% | +0.0 | 50% | ❌ 37 pts to go |
| P06M | 168 | 6.5% | 6.5% | +0.0 | n/a | no target |
| P06T | 2616 | 2.6% | 2.6% | -0.1 | n/a | no target |
| P06 | 210 | 20.5% | 20.5% | +2.4 | n/a | no target |
| P07 | 384 | 17.4% | 17.4% | -1.6 | n/a | no target |
| P08 | 6837 | 0.3% | 0.3% | -0.3 | n/a | no target |
| P09 | 381 | 80.6% | 80.6% | +0.0 | 95% | ❌ 14 pts to go |
| P10 | 2386 | 3.2% | 3.2% | +0.1 | n/a | no target |
| P11 | 592 | 28.5% | 28.5% | -0.8 | n/a | no target |
| P12 | 18 | 33.3% | 33.3% | +1.7 | n/a | no target |
| P13 | 48867 | 1.0% | 1.0% | +0.0 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 16.1% | 16.1% | -0.2 | n/a | no target |
| P01_GOLD | 624 | 34.0% | 34.0% | +0.0 | 70% | ❌ 36 pts to go |
| P02 | 404 | 44.3% | 44.3% | +0.0 | 75% | ❌ 31 pts to go |
| P03 | 208 | 23.1% | 23.1% | +0.0 | 55% | ❌ 32 pts to go |
| P04 | 1566 | 50.5% | 50.5% | +0.0 | 75% | ❌ 24 pts to go |
| P05 | 384 | 11.7% | 11.7% | +0.0 | 50% | ❌ 38 pts to go |
| P06M | 168 | 1.8% | 1.8% | +0.0 | n/a | no target |
| P06T | 2616 | 1.4% | 1.4% | -0.1 | n/a | no target |
| P06 | 210 | 11.9% | 11.9% | +1.7 | n/a | no target |
| P07 | 384 | 9.1% | 9.1% | -1.2 | n/a | no target |
| P08 | 6837 | 0.3% | 0.3% | -0.2 | n/a | no target |
| P09 | 381 | 77.7% | 77.7% | +0.0 | 95% | ❌ 17 pts to go |
| P10 | 2386 | 1.8% | 1.8% | +0.0 | n/a | no target |
| P11 | 592 | 28.2% | 28.2% | -0.7 | n/a | no target |
| P12 | 18 | 16.7% | 16.7% | +0.9 | n/a | no target |
| P13 | 48867 | 0.6% | 0.6% | +0.0 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 16.7% | 16.7% | +0.0 | n/a | no target |
| P01T | 93 | 19.4% | 19.4% | -0.2 | n/a | no target |
| P01_GOLD | 624 | 57.9% | 58.0% | +0.0 | 80% | ❌ 22 pts to go |
| P02 | 404 | 52.2% | 52.5% | +0.0 | 75% | ❌ 23 pts to go |
| P03 | 208 | 45.2% | 45.2% | +0.0 | 70% | ❌ 25 pts to go |
| P04 | 1566 | 48.7% | 49.8% | +0.0 | 70% | ❌ 21 pts to go |
| P05 | 384 | 16.4% | 16.4% | +0.0 | 50% | ❌ 34 pts to go |
| P06M | 168 | 4.2% | 4.2% | +0.0 | n/a | no target |
| P06T | 2616 | 1.5% | 1.6% | -0.1 | n/a | no target |
| P06 | 210 | 21.9% | 21.9% | -2.2 | n/a | no target |
| P07 | 384 | 4.2% | 4.2% | -1.0 | n/a | no target |
| P08 | 6837 | 0.6% | 0.6% | -0.4 | n/a | no target |
| P09 | 381 | 44.1% | 44.4% | +0.0 | 80% | ❌ 36 pts to go |
| P10 | 2386 | 1.6% | 1.7% | +0.1 | n/a | no target |
| P11 | 592 | 13.3% | 13.5% | -3.4 | n/a | no target |
| P12 | 18 | 27.8% | 27.8% | -3.8 | n/a | no target |
| P13 | 48867 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 38.9% | 38.9% | +0.0 | n/a | no target |
| P01T | 93 | 57.0% | 57.0% | +0.5 | 60% | 🟡 3 pts to go |
| P01_GOLD | 624 | 63.6% | 63.6% | +0.1 | 70% | 🟡 6 pts to go |
| P02 | 404 | 43.8% | 43.8% | +0.0 | 50% | 🟡 6 pts to go |
| P03 | 208 | 55.3% | 55.3% | +0.0 | 55% | ✅ met |
| P04 | 1566 | 22.9% | 22.9% | +0.0 | 40% | ❌ 17 pts to go |
| P05 | 384 | 17.4% | 17.4% | +0.0 | 40% | ❌ 23 pts to go |
| P06M | 168 | 16.7% | 16.7% | +0.0 | n/a | no target |
| P06T | 2616 | 11.7% | 11.7% | -0.8 | n/a | no target |
| P06 | 210 | 25.2% | 25.2% | -5.5 | n/a | no target |
| P07 | 384 | 12.2% | 12.2% | -4.1 | n/a | no target |
| P08 | 6837 | 2.4% | 2.4% | -2.3 | n/a | no target |
| P09 | 381 | 5.8% | 5.8% | +0.0 | n/a | no target |
| P10 | 2386 | 3.8% | 3.8% | -0.1 | n/a | no target |
| P11 | 592 | 6.1% | 6.1% | -1.5 | n/a | no target |
| P12 | 18 | 11.1% | 11.1% | -4.7 | n/a | no target |
| P13 | 48867 | 0.2% | 0.2% | -0.1 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 44.4% | 44.4% | +0.0 | n/a | no target |
| P01T | 93 | 68.8% | 68.8% | -0.8 | 65% | ✅ met |
| P01_GOLD | 624 | 69.2% | 69.2% | +0.0 | 70% | 🟡 1 pts to go |
| P02 | 404 | 26.2% | 26.2% | +0.0 | 50% | ❌ 24 pts to go |
| P03 | 208 | 56.2% | 56.2% | +0.0 | 60% | 🟡 4 pts to go |
| P04 | 1566 | 9.9% | 9.9% | +0.0 | 40% | ❌ 30 pts to go |
| P05 | 384 | 21.4% | 21.4% | +0.0 | 45% | ❌ 24 pts to go |
| P06M | 168 | 7.1% | 7.1% | +0.0 | n/a | no target |
| P06T | 2616 | 4.0% | 4.0% | -0.3 | n/a | no target |
| P06 | 210 | 41.4% | 41.4% | -6.8 | n/a | no target |
| P07 | 384 | 16.4% | 16.4% | -7.4 | n/a | no target |
| P08 | 6837 | 1.1% | 1.1% | -1.3 | n/a | no target |
| P09 | 381 | 8.7% | 8.7% | +0.0 | n/a | no target |
| P10 | 2386 | 2.1% | 2.1% | +0.0 | n/a | no target |
| P11 | 592 | 5.4% | 5.4% | -1.4 | n/a | no target |
| P12 | 18 | 5.6% | 5.6% | -4.9 | n/a | no target |
| P13 | 48867 | 0.1% | 0.1% | -0.1 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 11.1% | 11.1% | +0.0 | n/a | no target |
| P01T | 93 | 44.1% | 44.1% | -0.5 | n/a | no target |
| P01_GOLD | 624 | 49.8% | 49.8% | +0.0 | 50% | 🟡 0 pts to go |
| P02 | 404 | 42.6% | 42.6% | +0.0 | n/a | no target |
| P03 | 208 | 58.7% | 58.7% | +0.0 | 60% | 🟡 1 pts to go |
| P04 | 1566 | 26.4% | 26.4% | +0.0 | n/a | no target |
| P05 | 384 | 16.7% | 16.7% | +0.0 | n/a | no target |
| P06M | 168 | 4.2% | 4.2% | +0.0 | n/a | no target |
| P06T | 2616 | 3.7% | 3.7% | -0.3 | n/a | no target |
| P06 | 210 | 30.5% | 30.5% | -5.0 | n/a | no target |
| P07 | 384 | 13.0% | 13.0% | -5.7 | n/a | no target |
| P08 | 6837 | 0.8% | 0.8% | -0.7 | n/a | no target |
| P09 | 381 | 18.9% | 18.9% | +0.0 | n/a | no target |
| P10 | 2386 | 2.3% | 2.3% | -0.1 | n/a | no target |
| P11 | 592 | 6.2% | 6.2% | -1.6 | n/a | no target |
| P12 | 18 | 16.7% | 16.7% | -4.4 | n/a | no target |
| P13 | 48867 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 27.8% | 27.8% | +0.0 | 15% | ✅ met |
| P01T | 93 | 29.0% | 29.0% | -0.3 | 15% | ✅ met |
| P01_GOLD | 624 | 35.3% | 35.3% | +0.2 | 40% | 🟡 5 pts to go |
| P02 | 404 | 13.9% | 14.1% | +0.0 | 25% | ❌ 11 pts to go |
| P03 | 208 | 21.6% | 21.6% | +0.0 | 25% | 🟡 3 pts to go |
| P04 | 1566 | 5.2% | 5.2% | +0.0 | 15% | 🟡 10 pts to go |
| P05 | 384 | 8.1% | 8.1% | +0.0 | 15% | 🟡 7 pts to go |
| P06M | 168 | 6.0% | 6.0% | +0.0 | 15% | 🟡 9 pts to go |
| P06T | 2616 | 1.4% | 1.4% | -0.1 | 15% | ❌ 14 pts to go |
| P06 | 210 | 9.5% | 9.5% | -0.7 | 15% | 🟡 6 pts to go |
| P07 | 384 | 5.2% | 5.2% | -1.5 | 15% | 🟡 10 pts to go |
| P08 | 6837 | 0.5% | 0.5% | -0.4 | 15% | ❌ 14 pts to go |
| P09 | 381 | 0.8% | 0.8% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2386 | 1.5% | 1.5% | +0.1 | 15% | ❌ 14 pts to go |
| P11 | 592 | 1.0% | 1.0% | -0.3 | 15% | ❌ 14 pts to go |
| P12 | 18 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 48867 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 11.1% | 11.1% | +0.0 | 15% | 🟡 4 pts to go |
| P01T | 93 | 32.3% | 32.3% | -0.3 | 25% | ✅ met |
| P01_GOLD | 624 | 29.2% | 29.2% | +0.0 | 25% | ✅ met |
| P02 | 404 | 28.0% | 28.0% | +0.0 | 15% | ✅ met |
| P03 | 208 | 26.0% | 26.0% | +0.0 | 15% | ✅ met |
| P04 | 1566 | 8.2% | 8.2% | +0.0 | 15% | 🟡 7 pts to go |
| P05 | 384 | 12.0% | 12.0% | +0.0 | 15% | 🟡 3 pts to go |
| P06M | 168 | 2.4% | 2.4% | +0.0 | 15% | ❌ 13 pts to go |
| P06T | 2616 | 2.5% | 2.5% | -0.2 | 15% | ❌ 12 pts to go |
| P06 | 210 | 9.5% | 9.5% | -2.5 | 15% | 🟡 6 pts to go |
| P07 | 384 | 5.2% | 5.2% | -2.3 | 15% | 🟡 10 pts to go |
| P08 | 6837 | 0.5% | 0.5% | -0.5 | 15% | ❌ 14 pts to go |
| P09 | 381 | 0.8% | 0.8% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2386 | 1.4% | 1.4% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 592 | 4.1% | 4.1% | -1.0 | 15% | ❌ 11 pts to go |
| P12 | 18 | 27.8% | 27.8% | +1.5 | 15% | ✅ met |
| P13 | 48867 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 5.6% | 5.6% | +0.0 | 20% | ❌ 14 pts to go |
| P01T | 93 | 9.7% | 9.7% | -0.1 | 20% | ❌ 10 pts to go |
| P01_GOLD | 624 | 4.3% | 4.3% | +0.0 | 20% | ❌ 16 pts to go |
| P02 | 404 | 1.5% | 1.5% | +0.0 | 20% | ❌ 18 pts to go |
| P03 | 208 | 1.9% | 1.9% | +0.0 | 20% | ❌ 18 pts to go |
| P04 | 1566 | 1.0% | 1.0% | +0.0 | 20% | ❌ 19 pts to go |
| P05 | 384 | 1.0% | 1.0% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 2616 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 210 | 2.9% | 2.9% | -0.7 | 20% | ❌ 17 pts to go |
| P07 | 384 | 0.5% | 0.5% | -0.3 | 20% | ❌ 20 pts to go |
| P08 | 6837 | 0.1% | 0.1% | -0.1 | 20% | ❌ 20 pts to go |
| P09 | 381 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2386 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 592 | 0.5% | 0.5% | -0.1 | 20% | ❌ 20 pts to go |
| P12 | 18 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 48867 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 5.6% | 5.6% | +0.0 | 15% | 🟡 9 pts to go |
| P01T | 93 | 7.5% | 7.5% | -0.1 | 15% | 🟡 8 pts to go |
| P01_GOLD | 624 | 10.6% | 10.6% | +0.0 | 15% | 🟡 4 pts to go |
| P02 | 404 | 13.4% | 13.4% | +0.0 | 15% | 🟡 2 pts to go |
| P03 | 208 | 24.0% | 24.0% | +0.0 | 15% | ✅ met |
| P04 | 1566 | 4.6% | 4.6% | +0.0 | 15% | ❌ 10 pts to go |
| P05 | 384 | 2.9% | 2.9% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 168 | 2.4% | 2.4% | +0.0 | 15% | ❌ 13 pts to go |
| P06T | 2616 | 1.3% | 1.3% | -0.1 | 15% | ❌ 14 pts to go |
| P06 | 210 | 4.8% | 4.8% | -0.6 | 15% | ❌ 10 pts to go |
| P07 | 384 | 2.9% | 2.9% | -0.7 | 15% | ❌ 12 pts to go |
| P08 | 6837 | 0.4% | 0.4% | -0.3 | 15% | ❌ 15 pts to go |
| P09 | 381 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2386 | 0.8% | 0.8% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 592 | 1.7% | 1.7% | -0.4 | 15% | ❌ 13 pts to go |
| P12 | 18 | 5.6% | 5.6% | +0.3 | 15% | 🟡 9 pts to go |
| P13 | 48867 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 11.1% | 11.1% | +0.0 | 20% | 🟡 9 pts to go |
| P01T | 93 | 40.9% | 40.9% | -0.4 | 40% | ✅ met |
| P01_GOLD | 624 | 45.8% | 45.8% | +0.0 | 40% | ✅ met |
| P02 | 404 | 48.5% | 48.5% | +0.0 | 20% | ✅ met |
| P03 | 208 | 55.8% | 55.8% | +0.0 | 35% | ✅ met |
| P04 | 1566 | 30.3% | 30.3% | +0.0 | 20% | ✅ met |
| P05 | 384 | 16.7% | 16.7% | +0.0 | 20% | 🟡 3 pts to go |
| P06M | 168 | 4.2% | 4.2% | +0.0 | 20% | ❌ 16 pts to go |
| P06T | 2616 | 4.2% | 4.2% | -0.3 | 20% | ❌ 16 pts to go |
| P06 | 210 | 30.0% | 30.0% | -5.5 | 20% | ✅ met |
| P07 | 384 | 10.7% | 10.7% | -4.0 | 20% | 🟡 9 pts to go |
| P08 | 6837 | 1.3% | 1.3% | -1.0 | 20% | ❌ 19 pts to go |
| P09 | 381 | 22.0% | 22.0% | +0.0 | 20% | ✅ met |
| P10 | 2386 | 2.5% | 2.5% | -0.1 | 20% | ❌ 18 pts to go |
| P11 | 592 | 6.4% | 6.4% | -1.6 | 20% | ❌ 14 pts to go |
| P12 | 18 | 11.1% | 11.1% | -4.7 | 20% | 🟡 9 pts to go |
| P13 | 48867 | 0.6% | 0.6% | +0.0 | 20% | ❌ 19 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 1.1% | 1.1% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 69.7% | 69.7% | +0.0 | 95% | ❌ 25 pts to go |
| P02 | 404 | 73.3% | 73.3% | +0.0 | 95% | ❌ 22 pts to go |
| P03 | 208 | 67.3% | 67.3% | +0.0 | 90% | ❌ 23 pts to go |
| P04 | 1566 | 58.4% | 58.4% | +0.0 | 85% | ❌ 27 pts to go |
| P05 | 384 | 34.9% | 34.9% | +0.0 | 75% | ❌ 40 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2616 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 210 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 384 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 6837 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 381 | 90.8% | 90.8% | +0.0 | 100% | 🟡 9 pts to go |
| P10 | 2386 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 592 | 15.0% | 15.0% | -3.8 | 60% | ❌ 45 pts to go |
| P12 | 18 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 48867 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 72.9% | 72.9% | +0.0 | 100% | ❌ 27 pts to go |
| P02 | 404 | 77.2% | 77.2% | +0.0 | 100% | ❌ 23 pts to go |
| P03 | 208 | 74.5% | 74.5% | +0.0 | n/a | no target |
| P04 | 1566 | 60.0% | 60.0% | +0.0 | 95% | ❌ 35 pts to go |
| P05 | 384 | 31.2% | 31.2% | +0.0 | 80% | ❌ 49 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2616 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 210 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 384 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 6837 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 381 | 93.4% | 93.4% | +0.0 | 100% | 🟡 7 pts to go |
| P10 | 2386 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 592 | 16.0% | 16.0% | -4.0 | n/a | no target |
| P12 | 18 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 48867 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 1.1% | 1.1% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 51.9% | 51.9% | +0.0 | 85% | ❌ 33 pts to go |
| P02 | 404 | 66.6% | 66.6% | -0.2 | 90% | ❌ 23 pts to go |
| P03 | 208 | 54.8% | 54.8% | +0.0 | 85% | ❌ 30 pts to go |
| P04 | 1566 | 64.1% | 64.1% | +0.0 | 90% | ❌ 26 pts to go |
| P05 | 384 | 35.2% | 35.2% | +0.0 | 75% | ❌ 40 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2616 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 210 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 384 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 6837 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 381 | 85.6% | 85.6% | +0.0 | 95% | 🟡 9 pts to go |
| P10 | 2386 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 592 | 13.9% | 13.9% | -3.4 | n/a | no target |
| P12 | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 48867 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 1.1% | 1.1% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 52.1% | 52.1% | +0.0 | 85% | ❌ 33 pts to go |
| P02 | 404 | 60.9% | 60.9% | -0.2 | 90% | ❌ 29 pts to go |
| P03 | 208 | 56.2% | 56.2% | +0.0 | 85% | ❌ 29 pts to go |
| P04 | 1566 | 54.3% | 54.3% | +0.0 | 90% | ❌ 36 pts to go |
| P05 | 384 | 41.7% | 41.7% | +0.0 | 75% | ❌ 33 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2616 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 210 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 384 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 6837 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 381 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10 | 2386 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 592 | 11.3% | 11.3% | -2.8 | n/a | no target |
| P12 | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 48867 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 80.6% | 80.6% | -0.9 | n/a | no target |
| P01_GOLD | 624 | 85.7% | 85.7% | +0.0 | 100% | ❌ 14 pts to go |
| P02 | 404 | 81.7% | 81.7% | +0.0 | 100% | ❌ 18 pts to go |
| P03 | 208 | 92.3% | 92.3% | +0.0 | n/a | no target |
| P04 | 1566 | 72.6% | 72.6% | +0.0 | 95% | ❌ 22 pts to go |
| P05 | 384 | 75.5% | 75.5% | +0.0 | 95% | ❌ 20 pts to go |
| P06M | 168 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06T | 2616 | 77.8% | 77.8% | -5.6 | n/a | no target |
| P06 | 210 | 61.4% | 61.4% | -14.5 | n/a | no target |
| P07 | 384 | 52.9% | 52.9% | -24.1 | n/a | no target |
| P08 | 6837 | 40.6% | 40.6% | -44.3 | n/a | no target |
| P09 | 381 | 99.0% | 99.0% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2386 | 98.6% | 98.6% | +0.2 | n/a | no target |
| P11 | 592 | 72.0% | 72.0% | -17.9 | n/a | no target |
| P12 | 18 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 48867 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 80.6% | 80.6% | -0.9 | n/a | no target |
| P01_GOLD | 624 | 88.9% | 88.9% | +0.0 | 100% | ❌ 11 pts to go |
| P02 | 404 | 82.9% | 83.2% | +0.0 | 100% | ❌ 17 pts to go |
| P03 | 208 | 93.8% | 93.8% | +0.0 | n/a | no target |
| P04 | 1566 | 79.0% | 79.0% | +0.0 | 95% | ❌ 16 pts to go |
| P05 | 384 | 90.1% | 90.1% | +0.0 | 70% | ✅ met |
| P06M | 168 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06T | 2616 | 77.8% | 77.8% | -5.6 | n/a | no target |
| P06 | 210 | 61.4% | 61.4% | -14.5 | n/a | no target |
| P07 | 384 | 52.9% | 52.9% | -24.1 | n/a | no target |
| P08 | 6837 | 40.6% | 40.6% | -44.3 | n/a | no target |
| P09 | 381 | 99.0% | 99.0% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2386 | 98.6% | 98.6% | +0.2 | n/a | no target |
| P11 | 592 | 72.3% | 72.3% | -18.0 | n/a | no target |
| P12 | 18 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 48867 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 93 | 1.1% | 1.1% | +0.0 | n/a | no target · rows from a source that publishes bids: 3 rows, 33.3% filled |
| P01_GOLD | 624 | 17.3% | 17.3% | +0.0 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 366 rows, 29.5% filled |
| P02 | 404 | 13.1% | 13.1% | +0.0 | n/a | no target · rows from a source that publishes bids: 295 rows, 18.0% filled |
| P03 | 208 | 16.3% | 16.3% | +0.0 | n/a | no target · rows from a source that publishes bids: 140 rows, 24.3% filled |
| P04 | 1566 | 3.7% | 3.7% | +0.0 | n/a | no target · rows from a source that publishes bids: 874 rows, 6.6% filled |
| P05 | 384 | 3.4% | 3.4% | +0.0 | n/a | no target · rows from a source that publishes bids: 53 rows, 24.5% filled |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2616 | 0.1% | 0.1% | +0.0 | n/a | no target · rows from a source that publishes bids: 4 rows, 50.0% filled |
| P06 | 210 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 384 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 6837 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 381 | 3.1% | 3.1% | +0.0 | n/a | no target · rows from a source that publishes bids: 367 rows, 3.3% filled |
| P10 | 2386 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 592 | 2.2% | 2.2% | -0.5 | n/a | no target · rows from a source that publishes bids: 92 rows, 14.1% filled |
| P12 | 18 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 18 rows, 0.0% filled |
| P13 | 48867 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 93 | 0.0% | 96.8% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 53.2% | 82.5% | +0.0 | 90% | ❌ 37 pts to go |
| P02 | 404 | 60.9% | 85.4% | -0.2 | 90% | ❌ 29 pts to go |
| P03 | 208 | 56.2% | 76.0% | +0.0 | 90% | ❌ 34 pts to go |
| P04 | 1566 | 45.3% | 85.6% | +0.0 | 90% | ❌ 45 pts to go |
| P05 | 384 | 0.0% | 81.0% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 168 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 2616 | 0.0% | 99.8% | +0.0 | n/a | no target |
| P06 | 210 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 384 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 6837 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 381 | 2.1% | 3.4% | +0.0 | 90% | ❌ 88 pts to go |
| P10 | 2386 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 592 | 10.1% | 92.4% | -2.6 | n/a | no target |
| P12 | 18 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 48867 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 93 | 0.0% | 96.8% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 26.0% | 55.3% | +0.0 | 90% | ❌ 64 pts to go |
| P02 | 404 | 59.9% | 84.4% | +0.0 | n/a | no target |
| P03 | 208 | 30.8% | 50.5% | +0.0 | n/a | no target |
| P04 | 1566 | 49.7% | 90.0% | +0.0 | n/a | no target |
| P05 | 384 | 0.5% | 81.5% | +0.0 | n/a | no target |
| P06M | 168 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 2616 | 0.0% | 99.8% | +0.0 | n/a | no target |
| P06 | 210 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 384 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 6837 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 381 | 44.4% | 45.7% | +0.0 | n/a | no target |
| P10 | 2386 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 592 | 9.3% | 91.6% | -2.3 | n/a | no target |
| P12 | 18 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 48867 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 93 | 2.2% | 98.9% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 51.6% | 80.9% | +0.0 | 95% | ❌ 43 pts to go |
| P02 | 404 | 65.8% | 90.3% | +0.2 | n/a | no target |
| P03 | 208 | 59.1% | 78.8% | +0.0 | n/a | no target |
| P04 | 1566 | 50.3% | 90.6% | +0.0 | n/a | no target |
| P05 | 384 | 5.2% | 86.2% | +0.0 | n/a | no target |
| P06M | 168 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 2616 | 0.0% | 99.8% | +0.0 | n/a | no target |
| P06 | 210 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 384 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 6837 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 381 | 67.5% | 68.8% | +0.0 | n/a | no target |
| P10 | 2386 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 592 | 10.1% | 92.4% | -2.6 | n/a | no target |
| P12 | 18 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 48867 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 93 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 624 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 404 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 208 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1566 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 384 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 168 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 2616 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 210 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 384 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 6837 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 381 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2386 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 592 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P12 | 18 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 48867 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 93 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 624 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 404 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 208 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1566 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 384 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 168 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 2616 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 210 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 384 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 6837 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 381 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2386 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 592 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P12 | 18 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 48867 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 93 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 624 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 404 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 208 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1566 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 384 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 168 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 2616 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 210 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 384 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 6837 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 381 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2386 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 592 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P12 | 18 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 48867 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |


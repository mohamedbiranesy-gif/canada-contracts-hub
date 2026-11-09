# Coverage vs the downstream team's targets — 2026-11-09

Benchmarks (field × package with a numeric target): **97 of 438 met** (22.1%); 87 within 10 points; 254 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 18, P01T 92, P01_GOLD 624, P02 404, P03 208, P04 1566, P05 384, P06M 168, P06T 2440, P06 166, P07 252, P08 3039, P09 381, P10 2596, P11 475, P12 19, P13 50802

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 33.3% | 8 | reference to quote (PO / contract / vendor id) (18 rows) |
| P01T | 92 | 1.1% | 44.6% | 8 | reference to quote (PO / contract / vendor id) (87 rows) |
| P01_GOLD | 624 | 23.7% | 70.5% | 9 | payment terms (217 rows) |
| P02 | 404 | 8.4% | 62.6% | 9 | PO rule (301 rows) |
| P03 | 208 | 17.3% | 68.3% | 9 | PO rule (92 rows) |
| P04 | 1566 | 2.7% | 38.3% | 8 | PO rule (1414 rows) |
| P05 | 384 | 1.3% | 17.7% | 7 | payment terms (316 rows) |
| P06M | 168 | 0.0% | 4.8% | 7 | reference to quote (PO / contract / vendor id) (168 rows) |
| P06T | 2440 | 0.0% | 5.4% | 7 | reference to quote (PO / contract / vendor id) (2436 rows) |
| P06 | 166 | 0.0% | 14.5% | 6 | reference to quote (PO / contract / vendor id) (166 rows) |
| P07 | 252 | 0.0% | 4.8% | 6 | reference to quote (PO / contract / vendor id) (252 rows) |
| P08 | 3039 | 0.0% | 0.7% | 6 | reference to quote (PO / contract / vendor id) (3039 rows) |
| P09 | 381 | 1.0% | 44.4% | 8 | payment terms (356 rows) |
| P10 | 2596 | 0.0% | 0.8% | 5 | reference to quote (PO / contract / vendor id) (2594 rows) |
| P11 | 475 | 1.3% | 12.2% | 4 | PO rule (444 rows) |
| P12 | 19 | 0.0% | 47.4% | 8 | PO rule (17 rows) |
| P13 | 50802 | 0.0% | 0.0% | 6 | reference to quote (PO / contract / vendor id) (50802 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 18 | 5 | 3 | 10 | 0 | 0 | 77 |
| P01T | 92 | 26 | 39 | 27 | 0 | 0 | 79 |
| P01_GOLD | 624 | 225 | 184 | 215 | 0 | 0 | 81 |
| P02 | 404 | 0 | 183 | 221 | 0 | 0 | 66 |
| P03 | 208 | 0 | 0 | 199 | 9 | 0 | 57 |
| P04 | 1566 | 0 | 0 | 1506 | 60 | 0 | 53 |
| P05 | 384 | 15 | 28 | 322 | 19 | 0 | 51 |
| P06M | 168 | 0 | 5 | 155 | 8 | 0 | 51 |
| P06T | 2440 | 0 | 23 | 2140 | 277 | 0 | 51 |
| P06 | 166 | 20 | 30 | 116 | 0 | 0 | 71 |
| P07 | 252 | 0 | 15 | 212 | 25 | 0 | 53 |
| P08 | 3039 | 0 | 0 | 2266 | 773 | 0 | 43 |
| P09 | 381 | 5 | 13 | 360 | 3 | 0 | 53 |
| P10 | 2596 | 3 | 13 | 1863 | 717 | 0 | 43 |
| P11 | 475 | 0 | 0 | 0 | 0 | 475 | 28 |
| P12 | 19 | 0 | 1 | 18 | 0 | 0 | 54 |
| P13 | 50802 | 7 | 24 | 41765 | 9006 | 0 | 45 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 18 | 7 | 38.9% | the buyer's PO / reference rule (9) |
| P01T | 92 | 50 | 54.3% | the buyer's PO / reference rule (24) |
| P01_GOLD | 624 | 452 | 72.4% | bill-to legal name and address (120) |
| P02 | 404 | 306 | 75.7% | the buyer's PO / reference rule (55) |
| P03 | 208 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (208) |
| P04 | 1566 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (1566) |
| P05 | 384 | 45 | 11.7% | a confirmed invoicing / AP or finance channel (296) |
| P06M | 168 | 2 | 1.2% | a confirmed invoicing / AP or finance channel (143) |
| P06T | 2440 | 14 | 0.6% | a confirmed invoicing / AP or finance channel (2356) |
| P06 | 166 | 32 | 19.3% | bill-to legal name and address (84) |
| P07 | 252 | 8 | 3.2% | a confirmed invoicing / AP or finance channel (111) |
| P08 | 3039 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (3039) |
| P09 | 381 | 50 | 13.1% | a confirmed invoicing / AP or finance channel (322) |
| P10 | 2596 | 8 | 0.3% | a confirmed invoicing / AP or finance channel (2465) |
| P11 | 475 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (475) |
| P12 | 19 | 5 | 26.3% | a confirmed invoicing / AP or finance channel (13) |
| P13 | 50802 | 14 | 0.0% | a confirmed invoicing / AP or finance channel (49561) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 18 | 6 | 33.3% | 4 | 0 | the vendor's remit-to address (5) |
| P01T | 92 | 36 | 39.1% | 12 | 0 | the vendor's GST/HST number (BN9) (18) |
| P01_GOLD | 624 | 395 | 63.3% | 20 | 0 | the vendor's GST/HST number (BN9) (110) |
| P02 | 404 | 212 | 52.5% | 32 | 0 | the vendor's GST/HST number (BN9) (127) |
| P03 | 208 | 81 | 38.9% | 1 | 53 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (38) |
| P04 | 1566 | 200 | 12.8% | 16 | 424 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (755) |
| P05 | 384 | 29 | 7.6% | 9 | 62 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (207) |
| P06M | 168 | 4 | 2.4% | 6 | 32 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (104) |
| P06T | 2440 | 19 | 0.8% | 47 | 604 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1669) |
| P06 | 166 | 14 | 8.4% | 17 | 0 | bill-to legal name and address (47) |
| P07 | 252 | 6 | 2.4% | 21 | 6 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (68) |
| P08 | 3039 | 3 | 0.1% | 1 | 293 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2702) |
| P09 | 381 | 70 | 18.4% | 1 | 112 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (148) |
| P10 | 2596 | 5 | 0.2% | 12 | 187 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (2233) |
| P11 | 475 | 15 | 3.2% | 0 | 0 | a confirmed invoicing / AP or finance channel (440) |
| P12 | 19 | 4 | 21.1% | 0 | 5 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (6) |
| P13 | 50802 | 14 | 0.0% | 688 | 20246 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (29130) |
| **all** | 63634 | 1113 | 1.7% | 887 | 22024 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 13 | 0 | 0 | 0 | 0 | 1 | 1 | 10 | 11 | 1 |
| P01T | 66 | 0 | 0 | 0 | 1 | 4 | 4 | 28 | 40 | 30 |
| P01_GOLD | 399 | 0 | 0 | 0 | 11 | 96 | 50 | 195 | 230 | 60 |
| P02 | 404 | 0 | 404 | 0 | 4 | 36 | 10 | 301 | 227 | 22 |
| P03 | 208 | 0 | 208 | 0 | 2 | 35 | 14 | 92 | 94 | 25 |
| P04 | 1566 | 0 | 1566 | 0 | 11 | 330 | 125 | 1414 | 1209 | 106 |
| P05 | 369 | 0 | 319 | 0 | 8 | 93 | 54 | 303 | 318 | 57 |
| P06M | 168 | 0 | 168 | 0 | 0 | 19 | 46 | 156 | 141 | 0 |
| P06T | 2440 | 0 | 2440 | 0 | 33 | 866 | 481 | 2336 | 2137 | 88 |
| P06 | 146 | 0 | 0 | 0 | 5 | 69 | 47 | 86 | 115 | 8 |
| P07 | 252 | 0 | 252 | 0 | 8 | 115 | 71 | 194 | 212 | 17 |
| P08 | 3039 | 0 | 3039 | 0 | 21 | 1913 | 1027 | 2968 | 2899 | 170 |
| P09 | 376 | 0 | 354 | 0 | 9 | 72 | 4 | 348 | 360 | 53 |
| P10 | 2593 | 0 | 2538 | 0 | 26 | 1749 | 898 | 2544 | 2506 | 130 |
| P11 | 475 | 475 | 437 | 0 | 14 | 356 | 235 | 444 | 440 | 32 |
| P12 | 19 | 0 | 16 | 0 | 0 | 4 | 0 | 17 | 16 | 1 |
| P13 | 50795 | 0 | 50491 | 0 | 465 | 24124 | 12163 | 50725 | 50672 | 62 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 10153 |
| ap_system_hint | P13 | 0.6% | 20% | 9871 |
| buyer_address | P13 | 76.0% | 95% | 9668 |
| buyer_phone | P13 | 79.3% | 95% | 7997 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 7585 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 7582 |
| buyer_payment_method_preference | P13 | 0.5% | 15% | 7343 |
| buyer_logo_url | P13 | 84.2% | 95% | 5497 |
| buyer_legal_name_as_published | P13 | 52.5% | 60% | 3804 |
| buyer_bn_as_published | P13 | 24.7% | 30% | 2711 |
| buyer_legal_name_as_published | P08 | 37.1% | 75% | 1154 |
| buyer_legal_name_as_published | P10 | 32.6% | 70% | 971 |
| buyer_address | P08 | 66.1% | 95% | 879 |
| vendor_emails | P08 | 48.7% | 75% | 801 |
| buyer_address | P10 | 65.1% | 95% | 778 |
| vendor_emails | P10 | 51.3% | 80% | 745 |
| buyer_bn_as_published | P08 | 11.1% | 35% | 726 |
| vendor_registered_address | P10 | 42.4% | 70% | 718 |
| average_contract_duration_days | P04 | 45.3% | 90% | 700 |
| invoice_reference_hint | P08 | 2.3% | 25% | 689 |
| buyer_phone | P08 | 74.7% | 95% | 619 |
| buyer_phone | P10 | 71.5% | 95% | 612 |
| buyer_ap_cycle_published | P08 | 0.2% | 20% | 603 |
| invoice_reference_hint | P10 | 2.1% | 25% | 595 |
| buyer_vendor_id | P04 | 4.3% | 40% | 560 |
| end_date | P04 | 54.3% | 90% | 559 |
| currency | P04 | 60.0% | 95% | 549 |
| vendor_neq | P04 | 60.2% | 95% | 546 |
| ap_phone | P04 | 50.5% | 85% | 541 |
| ap_system_hint | P08 | 2.2% | 20% | 540 |
| vendor_registered_address | P08 | 52.5% | 70% | 533 |
| commodity_codes | P04 | 51.3% | 85% | 529 |
| buyer_bn_as_published | P10 | 9.6% | 30% | 529 |
| vendor_phone | P08 | 68.1% | 85% | 515 |
| buyer_ap_cycle_published | P10 | 0.3% | 20% | 513 |
| vendor_phone | P10 | 66.1% | 85% | 492 |
| buyer_ap_cycle_published | P06T | 0.2% | 20% | 482 |
| po_required_as_published | P04 | 9.7% | 40% | 475 |
| ap_system_hint | P10 | 2.5% | 20% | 455 |
| buyer_org_codes | P04 | 1.1% | 30% | 453 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 44.4% | 44.4% | +0.0 | 50% | 🟡 6 pts to go |
| P01T | 92 | 71.7% | 71.7% | +0.0 | 50% | ✅ met |
| P01_GOLD | 624 | 92.1% | 94.6% | -0.4 | 95% | 🟡 3 pts to go |
| P02 | 404 | 83.9% | 85.6% | +0.9 | 95% | ❌ 11 pts to go |
| P03 | 208 | 92.8% | 95.7% | +0.0 | 95% | 🟡 2 pts to go |
| P04 | 1566 | 68.6% | 71.3% | -0.2 | 90% | ❌ 21 pts to go |
| P05 | 384 | 41.1% | 44.0% | +0.7 | 70% | ❌ 29 pts to go |
| P06M | 168 | 7.1% | 7.1% | +0.0 | n/a | no target |
| P06T | 2440 | 4.4% | 4.5% | +0.7 | n/a | no target |
| P06 | 166 | 48.2% | 48.2% | +0.3 | 30% | ✅ met |
| P07 | 252 | 23.0% | 23.0% | +0.0 | 30% | 🟡 7 pts to go |
| P08 | 3039 | 2.3% | 2.3% | +0.0 | 25% | ❌ 23 pts to go |
| P09 | 381 | 99.0% | 99.7% | +0.1 | 100% | 🟡 1 pts to go |
| P10 | 2596 | 2.1% | 3.0% | +0.0 | 25% | ❌ 23 pts to go |
| P11 | 475 | 24.0% | 27.2% | -0.6 | 60% | ❌ 36 pts to go |
| P12 | 19 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 50802 | 0.2% | 0.3% | +0.0 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 92 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 624 | 6.2% | 6.2% | -0.2 | 50% | ❌ 44 pts to go |
| P02 | 404 | 7.2% | 7.2% | -0.3 | 50% | ❌ 43 pts to go |
| P03 | 208 | 1.9% | 1.9% | +0.1 | 40% | ❌ 38 pts to go |
| P04 | 1566 | 1.1% | 1.1% | +0.0 | 30% | ❌ 29 pts to go |
| P05 | 384 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 166 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 252 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 3039 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 381 | 0.5% | 0.5% | +0.0 | 50% | ❌ 50 pts to go |
| P10 | 2596 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P11 | 475 | 0.8% | 0.8% | +0.0 | n/a | no target |
| P12 | 19 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 50802 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 92 | 5.4% | 5.4% | +0.0 | 50% | ❌ 45 pts to go |
| P01_GOLD | 624 | 67.6% | 67.6% | -2.1 | 85% | ❌ 17 pts to go |
| P02 | 404 | 75.5% | 75.5% | +1.8 | 90% | ❌ 14 pts to go |
| P03 | 208 | 75.5% | 75.5% | +4.6 | 85% | 🟡 10 pts to go |
| P04 | 1566 | 65.5% | 65.5% | -0.1 | 85% | ❌ 20 pts to go |
| P05 | 384 | 31.0% | 31.0% | +0.9 | 60% | ❌ 29 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2440 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06 | 166 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 252 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 3039 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 381 | 96.6% | 96.6% | +0.1 | 100% | 🟡 3 pts to go |
| P10 | 2596 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 475 | 20.2% | 20.2% | -0.6 | 60% | ❌ 40 pts to go |
| P12 | 19 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 50802 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 92 | 2.2% | 2.2% | +0.0 | 30% | ❌ 28 pts to go |
| P01_GOLD | 624 | 51.3% | 51.3% | -2.0 | 80% | ❌ 29 pts to go |
| P02 | 404 | 66.8% | 66.8% | +1.9 | 60% | ✅ met |
| P03 | 208 | 63.9% | 63.9% | +5.6 | 80% | ❌ 16 pts to go |
| P04 | 1566 | 54.5% | 54.5% | +0.0 | 50% | ✅ met |
| P05 | 384 | 13.3% | 13.3% | +0.9 | 40% | ❌ 27 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2440 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06 | 166 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 252 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 3039 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 381 | 86.1% | 86.1% | -1.3 | 50% | ✅ met |
| P10 | 2596 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 475 | 17.7% | 17.7% | -0.2 | 40% | ❌ 22 pts to go |
| P12 | 19 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 50802 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 92 | 3.3% | 3.3% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 61.1% | 61.1% | -1.9 | 85% | ❌ 24 pts to go |
| P02 | 404 | 65.8% | 65.8% | +1.6 | 90% | ❌ 24 pts to go |
| P03 | 208 | 74.5% | 74.5% | +5.4 | 85% | ❌ 10 pts to go |
| P04 | 1566 | 56.3% | 56.3% | +0.0 | 85% | ❌ 29 pts to go |
| P05 | 384 | 21.1% | 21.1% | +0.8 | 50% | ❌ 29 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2440 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06 | 166 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 252 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 3039 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 381 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 2596 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 475 | 19.2% | 19.2% | -0.6 | 60% | ❌ 41 pts to go |
| P12 | 19 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 50802 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 92 | 2.2% | 2.2% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 13.0% | 13.0% | -0.1 | 60% | ❌ 47 pts to go |
| P02 | 404 | 7.2% | 7.2% | -0.6 | 50% | ❌ 43 pts to go |
| P03 | 208 | 10.6% | 10.6% | +0.3 | 50% | ❌ 39 pts to go |
| P04 | 1566 | 4.3% | 4.3% | +0.0 | 40% | ❌ 36 pts to go |
| P05 | 384 | 1.3% | 1.3% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2440 | 0.1% | 0.1% | +0.0 | n/a | no target |
| P06 | 166 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 252 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 3039 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 381 | 2.6% | 2.6% | +0.2 | 50% | ❌ 47 pts to go |
| P10 | 2596 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 475 | 3.2% | 3.2% | -1.0 | n/a | no target |
| P12 | 19 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 50802 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 92 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 35.1% | 35.1% | -1.4 | 80% | ❌ 45 pts to go |
| P02 | 404 | 60.6% | 60.6% | +1.7 | 90% | ❌ 29 pts to go |
| P03 | 208 | 41.3% | 41.3% | +5.0 | 80% | ❌ 39 pts to go |
| P04 | 1566 | 51.3% | 51.3% | +0.1 | 85% | ❌ 34 pts to go |
| P05 | 384 | 6.0% | 6.0% | +1.0 | 50% | ❌ 44 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 166 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 252 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 3039 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 381 | 76.1% | 76.1% | +0.4 | 95% | ❌ 19 pts to go |
| P10 | 2596 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 475 | 13.3% | 13.3% | -0.4 | 50% | ❌ 37 pts to go |
| P12 | 19 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 50802 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 92 | 1.1% | 1.1% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 8.5% | 8.5% | +0.0 | 50% | ❌ 42 pts to go |
| P02 | 404 | 7.2% | 7.2% | -0.3 | 50% | ❌ 43 pts to go |
| P03 | 208 | 2.4% | 2.4% | -0.3 | 30% | ❌ 28 pts to go |
| P04 | 1566 | 1.1% | 1.1% | +0.0 | 30% | ❌ 29 pts to go |
| P05 | 384 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 166 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 252 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 3039 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 381 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P10 | 2596 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 475 | 0.8% | 0.8% | +0.0 | n/a | no target |
| P12 | 19 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 50802 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 92 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 624 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 404 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 208 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1566 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 384 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 168 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 2440 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 166 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 252 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 3039 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 381 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2596 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 475 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 19 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 50802 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P01T | 92 | 80.4% | 80.4% | +0.0 | 60% | ✅ met |
| P01_GOLD | 624 | 77.9% | 77.9% | -0.3 | 90% | ❌ 12 pts to go |
| P02 | 404 | 67.3% | 67.3% | +1.4 | 85% | ❌ 18 pts to go |
| P03 | 208 | 82.2% | 82.2% | +1.5 | 90% | 🟡 8 pts to go |
| P04 | 1566 | 55.4% | 55.4% | +1.8 | 75% | ❌ 20 pts to go |
| P05 | 384 | 52.9% | 52.9% | +0.1 | 50% | ✅ met |
| P06M | 168 | 74.4% | 74.4% | +0.0 | n/a | no target |
| P06T | 2440 | 60.7% | 60.7% | +0.0 | n/a | no target |
| P06 | 166 | 46.4% | 46.4% | -0.3 | 40% | ✅ met |
| P07 | 252 | 40.1% | 40.1% | +0.0 | 50% | 🟡 10 pts to go |
| P08 | 3039 | 41.9% | 41.9% | +0.1 | 50% | 🟡 8 pts to go |
| P09 | 381 | 54.3% | 54.3% | -0.5 | 80% | ❌ 26 pts to go |
| P10 | 2596 | 36.6% | 36.6% | +0.0 | 40% | 🟡 3 pts to go |
| P11 | 475 | 44.8% | 44.8% | +0.2 | 60% | ❌ 15 pts to go |
| P12 | 19 | 52.6% | 52.6% | +0.2 | 85% | ❌ 32 pts to go |
| P13 | 50802 | 91.7% | 91.7% | +0.0 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 61.1% | 61.1% | +0.0 | n/a | no target |
| P01T | 92 | 63.0% | 63.0% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 74.8% | 74.8% | -0.4 | 95% | ❌ 20 pts to go |
| P02 | 404 | 84.9% | 84.9% | +3.2 | 95% | ❌ 10 pts to go |
| P03 | 208 | 77.9% | 77.9% | +1.2 | 95% | ❌ 17 pts to go |
| P04 | 1566 | 80.7% | 80.7% | +2.1 | 95% | ❌ 14 pts to go |
| P05 | 384 | 56.0% | 56.0% | +0.3 | 70% | ❌ 14 pts to go |
| P06M | 168 | 20.8% | 20.8% | +0.0 | n/a | no target |
| P06T | 2440 | 78.2% | 78.2% | -0.1 | n/a | no target |
| P06 | 166 | 55.4% | 55.4% | +0.2 | 80% | ❌ 25 pts to go |
| P07 | 252 | 52.0% | 52.0% | +0.0 | 70% | ❌ 18 pts to go |
| P08 | 3039 | 52.5% | 52.5% | +0.3 | 70% | ❌ 18 pts to go |
| P09 | 381 | 88.7% | 88.7% | -0.9 | 100% | ❌ 11 pts to go |
| P10 | 2596 | 42.4% | 42.4% | +0.0 | 70% | ❌ 28 pts to go |
| P11 | 475 | 54.7% | 54.7% | +0.8 | 75% | ❌ 20 pts to go |
| P12 | 19 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 50802 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 50.0% | 50.0% | +0.0 | n/a | no target |
| P01T | 92 | 19.6% | 19.6% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 52.4% | 52.4% | -1.4 | 60% | 🟡 8 pts to go |
| P02 | 404 | 67.3% | 67.3% | +1.1 | 60% | ✅ met |
| P03 | 208 | 64.9% | 64.9% | +2.6 | 60% | ✅ met |
| P04 | 1566 | 55.6% | 55.6% | +0.0 | 55% | ✅ met |
| P05 | 384 | 25.3% | 25.3% | +0.0 | 50% | ❌ 25 pts to go |
| P06M | 168 | 17.3% | 17.3% | +0.0 | n/a | no target |
| P06T | 2440 | 53.6% | 53.6% | +0.0 | n/a | no target |
| P06 | 166 | 53.0% | 53.0% | +0.3 | n/a | no target |
| P07 | 252 | 46.8% | 46.8% | +0.0 | 55% | 🟡 8 pts to go |
| P08 | 3039 | 49.2% | 49.2% | +0.0 | 50% | 🟡 1 pts to go |
| P09 | 381 | 71.9% | 71.9% | -1.1 | 70% | ✅ met |
| P10 | 2596 | 52.7% | 52.7% | +0.0 | 55% | 🟡 2 pts to go |
| P11 | 475 | 44.4% | 44.4% | +1.0 | 50% | 🟡 6 pts to go |
| P12 | 19 | 84.2% | 84.2% | -1.5 | n/a | no target |
| P13 | 50802 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 61.1% | 61.1% | +22.2 | n/a | no target |
| P01T | 92 | 30.4% | 30.4% | +30.4 | n/a | no target |
| P01_GOLD | 624 | 51.8% | 51.8% | +18.1 | 70% | ❌ 18 pts to go |
| P02 | 404 | 56.7% | 56.7% | +14.8 | 70% | ❌ 13 pts to go |
| P03 | 208 | 57.2% | 57.2% | +16.4 | 70% | ❌ 13 pts to go |
| P04 | 1566 | 51.4% | 51.4% | +17.5 | 65% | ❌ 14 pts to go |
| P05 | 384 | 34.4% | 34.4% | +17.2 | 60% | ❌ 26 pts to go |
| P06M | 168 | 30.4% | 30.4% | +23.9 | n/a | no target |
| P06T | 2440 | 3.5% | 3.5% | +3.5 | n/a | no target |
| P06 | 166 | 59.6% | 59.6% | +0.2 | 40% | ✅ met |
| P07 | 252 | 67.9% | 67.9% | +2.0 | 85% | ❌ 17 pts to go |
| P08 | 3039 | 68.1% | 68.1% | +2.7 | 85% | ❌ 17 pts to go |
| P09 | 381 | 55.1% | 55.1% | +1.1 | 85% | ❌ 30 pts to go |
| P10 | 2596 | 66.1% | 66.1% | +0.0 | 85% | ❌ 19 pts to go |
| P11 | 475 | 54.9% | 54.9% | +4.2 | 75% | ❌ 20 pts to go |
| P12 | 19 | 15.8% | 15.8% | +6.3 | n/a | no target |
| P13 | 50802 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 94.4% | 94.4% | +0.0 | n/a | no target |
| P01T | 92 | 90.2% | 90.2% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 89.4% | 89.4% | -0.7 | 90% | 🟡 1 pts to go |
| P02 | 404 | 87.6% | 87.6% | +0.1 | 90% | 🟡 2 pts to go |
| P03 | 208 | 89.9% | 89.9% | -0.2 | 90% | 🟡 0 pts to go |
| P04 | 1566 | 81.3% | 81.3% | +0.2 | 85% | 🟡 4 pts to go |
| P05 | 384 | 51.0% | 51.0% | -0.5 | 70% | ❌ 19 pts to go |
| P06M | 168 | 67.9% | 67.9% | +0.0 | n/a | no target |
| P06T | 2440 | 77.9% | 77.9% | +0.0 | n/a | no target |
| P06 | 166 | 97.0% | 97.0% | +0.0 | 50% | ✅ met |
| P07 | 252 | 96.8% | 96.8% | +0.0 | 100% | 🟡 3 pts to go |
| P08 | 3039 | 96.1% | 96.1% | +0.0 | 100% | 🟡 4 pts to go |
| P09 | 381 | 79.8% | 79.8% | -1.2 | 100% | ❌ 20 pts to go |
| P10 | 2596 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 475 | 93.1% | 93.1% | -0.2 | 100% | 🟡 7 pts to go |
| P12 | 19 | 42.1% | 42.1% | -0.8 | n/a | no target |
| P13 | 50802 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 50.0% | 50.0% | +11.1 | n/a | no target |
| P01T | 92 | 45.7% | 45.7% | +45.7 | n/a | no target |
| P01_GOLD | 624 | 45.7% | 45.7% | +9.0 | 70% | ❌ 24 pts to go |
| P02 | 404 | 51.5% | 51.5% | +7.4 | 75% | ❌ 24 pts to go |
| P03 | 208 | 51.4% | 51.4% | +9.2 | 75% | ❌ 24 pts to go |
| P04 | 1566 | 42.8% | 42.8% | +10.2 | 70% | ❌ 27 pts to go |
| P05 | 384 | 24.5% | 24.5% | +10.8 | 55% | ❌ 30 pts to go |
| P06M | 168 | 16.1% | 16.1% | +9.6 | n/a | no target |
| P06T | 2440 | 2.9% | 2.9% | +2.9 | n/a | no target |
| P06 | 166 | 41.0% | 41.0% | +1.0 | n/a | no target |
| P07 | 252 | 36.9% | 36.9% | +1.2 | 70% | ❌ 33 pts to go |
| P08 | 3039 | 48.7% | 48.7% | +1.5 | 75% | ❌ 26 pts to go |
| P09 | 381 | 52.0% | 52.0% | -0.4 | 85% | ❌ 33 pts to go |
| P10 | 2596 | 51.3% | 51.3% | +0.0 | 80% | ❌ 29 pts to go |
| P11 | 475 | 40.4% | 40.4% | +3.6 | 70% | ❌ 30 pts to go |
| P12 | 19 | 31.6% | 31.6% | +12.6 | n/a | no target |
| P13 | 50802 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 94.4% | 94.4% | +55.5 | n/a | no target |
| P01T | 92 | 89.1% | 89.1% | +89.1 | n/a | no target |
| P01_GOLD | 624 | 79.8% | 79.8% | +30.6 | 90% | ❌ 10 pts to go |
| P02 | 404 | 76.5% | 76.5% | +18.9 | 90% | ❌ 14 pts to go |
| P03 | 208 | 81.7% | 81.7% | +25.2 | 90% | 🟡 8 pts to go |
| P04 | 1566 | 70.6% | 70.6% | +26.7 | 85% | ❌ 14 pts to go |
| P05 | 384 | 48.4% | 48.4% | +26.0 | 75% | ❌ 27 pts to go |
| P06M | 168 | 67.9% | 67.9% | +61.4 | n/a | no target |
| P06T | 2440 | 77.1% | 77.1% | +77.1 | n/a | no target |
| P06 | 166 | 88.6% | 88.6% | +0.7 | n/a | no target |
| P07 | 252 | 90.5% | 90.5% | +2.4 | 100% | 🟡 10 pts to go |
| P08 | 3039 | 89.0% | 89.0% | +3.3 | 100% | ❌ 11 pts to go |
| P09 | 381 | 62.2% | 62.2% | +1.8 | n/a | no target |
| P10 | 2596 | 88.7% | 88.7% | +0.0 | 100% | ❌ 11 pts to go |
| P11 | 475 | 74.5% | 74.5% | +8.4 | n/a | no target |
| P12 | 19 | 36.8% | 36.8% | +17.8 | n/a | no target |
| P13 | 50802 | 82.7% | 82.7% | +82.7 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 92 | 21.7% | 21.7% | +0.0 | n/a | no target · QC vendors: 2 rows, 100.0% filled |
| P01_GOLD | 624 | 47.8% | 47.8% | -1.3 | 95% | ❌ 47 pts to go · QC vendors: 52 rows, 98.1% filled |
| P02 | 404 | 68.6% | 68.6% | +1.4 | 95% | ❌ 26 pts to go · QC vendors: 107 rows, 100.0% filled |
| P03 | 208 | 55.8% | 55.8% | +2.0 | 95% | ❌ 39 pts to go · QC vendors: 17 rows, 100.0% filled |
| P04 | 1566 | 60.2% | 60.2% | +0.1 | 95% | ❌ 35 pts to go · QC vendors: 434 rows, 98.6% filled |
| P05 | 384 | 14.1% | 14.1% | +0.4 | n/a | no target · QC vendors: 27 rows, 92.6% filled |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2440 | 55.9% | 55.9% | +0.0 | n/a | no target · QC vendors: 56 rows, 100.0% filled |
| P06 | 166 | 24.1% | 24.1% | -0.1 | n/a | no target · QC vendors: 16 rows, 100.0% filled |
| P07 | 252 | 19.4% | 19.4% | +0.0 | n/a | no target · QC vendors: 26 rows, 96.2% filled |
| P08 | 3039 | 26.9% | 26.9% | +0.0 | n/a | no target · QC vendors: 546 rows, 98.4% filled |
| P09 | 381 | 80.3% | 80.3% | -1.5 | 95% | ❌ 15 pts to go · QC vendors: 155 rows, 99.4% filled |
| P10 | 2596 | 22.8% | 22.8% | +0.0 | n/a | no target · QC vendors: 444 rows, 94.6% filled |
| P11 | 475 | 29.1% | 29.1% | +1.1 | n/a | no target · QC vendors: 79 rows, 98.7% filled |
| P12 | 19 | 73.7% | 73.7% | -2.5 | n/a | no target · QC vendors: 3 rows, 100.0% filled |
| P13 | 50802 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 61.1% | 61.1% | +0.0 | n/a | no target · vendors with a registry record: 11 rows, 100.0% filled |
| P01T | 92 | 63.0% | 63.0% | +0.0 | n/a | no target · vendors with a registry record: 58 rows, 100.0% filled |
| P01_GOLD | 624 | 83.5% | 83.5% | -1.4 | 100% | ❌ 16 pts to go · vendors with a registry record: 521 rows, 100.0% filled |
| P02 | 404 | 89.1% | 89.1% | +1.1 | 100% | ❌ 11 pts to go · vendors with a registry record: 360 rows, 100.0% filled |
| P03 | 208 | 88.9% | 88.9% | +1.5 | 100% | ❌ 11 pts to go · vendors with a registry record: 185 rows, 100.0% filled |
| P04 | 1566 | 81.4% | 81.4% | +0.1 | 100% | ❌ 19 pts to go · vendors with a registry record: 1275 rows, 100.0% filled |
| P05 | 384 | 61.2% | 61.2% | +0.0 | n/a | no target · vendors with a registry record: 235 rows, 100.0% filled |
| P06M | 168 | 20.8% | 20.8% | +0.0 | n/a | no target · vendors with a registry record: 35 rows, 100.0% filled |
| P06T | 2440 | 78.2% | 78.2% | -0.1 | n/a | no target · vendors with a registry record: 1909 rows, 100.0% filled |
| P06 | 166 | 57.8% | 57.8% | -0.4 | n/a | no target · vendors with a registry record: 96 rows, 100.0% filled |
| P07 | 252 | 54.4% | 54.4% | +0.0 | n/a | no target · vendors with a registry record: 137 rows, 100.0% filled |
| P08 | 3039 | 54.4% | 54.4% | +0.1 | n/a | no target · vendors with a registry record: 1652 rows, 100.0% filled |
| P09 | 381 | 91.9% | 91.9% | -0.9 | n/a | no target · vendors with a registry record: 350 rows, 100.0% filled |
| P10 | 2596 | 43.6% | 43.6% | +0.0 | n/a | no target · vendors with a registry record: 1133 rows, 100.0% filled |
| P11 | 475 | 57.9% | 57.9% | +0.6 | n/a | no target · vendors with a registry record: 275 rows, 100.0% filled |
| P12 | 19 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 19 rows, 100.0% filled |
| P13 | 50802 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 94.4% | 94.4% | +0.0 | 90% | ✅ met |
| P01T | 92 | 95.7% | 95.7% | +0.0 | 90% | ✅ met |
| P01_GOLD | 624 | 84.6% | 84.6% | -0.8 | 95% | ❌ 10 pts to go |
| P02 | 404 | 91.1% | 91.1% | +0.4 | 95% | 🟡 4 pts to go |
| P03 | 208 | 83.2% | 83.2% | +0.7 | 85% | 🟡 2 pts to go |
| P04 | 1566 | 78.9% | 78.9% | +0.0 | 90% | ❌ 11 pts to go |
| P05 | 384 | 75.8% | 75.8% | -0.2 | 75% | ✅ met |
| P06M | 168 | 88.7% | 88.7% | +0.0 | n/a | no target |
| P06T | 2440 | 64.5% | 64.5% | +0.1 | n/a | no target |
| P06 | 166 | 58.4% | 58.4% | +0.8 | 80% | ❌ 22 pts to go |
| P07 | 252 | 54.4% | 54.4% | +0.0 | 80% | ❌ 26 pts to go |
| P08 | 3039 | 37.1% | 37.1% | +0.0 | 75% | ❌ 38 pts to go |
| P09 | 381 | 81.1% | 81.1% | -1.0 | 95% | ❌ 14 pts to go |
| P10 | 2596 | 32.6% | 32.6% | +0.0 | 70% | ❌ 37 pts to go |
| P11 | 475 | 25.1% | 25.1% | -0.2 | 65% | ❌ 40 pts to go |
| P12 | 19 | 78.9% | 78.9% | -2.1 | 80% | 🟡 1 pts to go |
| P13 | 50802 | 52.5% | 52.5% | +3.2 | 60% | 🟡 8 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 38.9% | 38.9% | +0.0 | 50% | ❌ 11 pts to go |
| P01T | 92 | 20.7% | 20.7% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 20.4% | 20.4% | -0.2 | 40% | ❌ 20 pts to go |
| P02 | 404 | 21.8% | 21.8% | -0.8 | 40% | ❌ 18 pts to go |
| P03 | 208 | 26.9% | 26.9% | +0.4 | 40% | ❌ 13 pts to go |
| P04 | 1566 | 27.5% | 27.5% | +0.0 | 40% | ❌ 12 pts to go |
| P05 | 384 | 23.2% | 23.2% | -0.3 | 25% | 🟡 2 pts to go |
| P06M | 168 | 25.6% | 25.6% | +0.0 | n/a | no target |
| P06T | 2440 | 31.0% | 31.0% | +0.1 | n/a | no target |
| P06 | 166 | 10.2% | 10.2% | +0.5 | 35% | ❌ 25 pts to go |
| P07 | 252 | 10.3% | 10.3% | +0.4 | 35% | ❌ 25 pts to go |
| P08 | 3039 | 11.1% | 11.1% | +0.6 | 35% | ❌ 24 pts to go |
| P09 | 381 | 17.3% | 17.3% | -0.6 | n/a | no target |
| P10 | 2596 | 9.6% | 9.6% | +0.7 | 30% | ❌ 20 pts to go |
| P11 | 475 | 8.4% | 8.4% | +0.0 | n/a | no target |
| P12 | 19 | 10.5% | 10.5% | -8.5 | n/a | no target |
| P13 | 50802 | 24.7% | 24.7% | +3.0 | 30% | 🟡 5 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 94.4% | 94.4% | +0.0 | 100% | 🟡 6 pts to go |
| P01T | 92 | 93.5% | 93.5% | +0.0 | 100% | 🟡 6 pts to go |
| P01_GOLD | 624 | 87.5% | 87.5% | -1.9 | 100% | ❌ 12 pts to go |
| P02 | 404 | 96.8% | 96.8% | +0.3 | 100% | 🟡 3 pts to go |
| P03 | 208 | 91.8% | 91.8% | -2.4 | 100% | 🟡 8 pts to go |
| P04 | 1566 | 90.9% | 90.9% | +0.0 | 100% | 🟡 9 pts to go |
| P05 | 384 | 84.6% | 84.6% | -0.6 | 100% | ❌ 15 pts to go |
| P06M | 168 | 72.0% | 72.0% | +0.0 | n/a | no target |
| P06T | 2440 | 80.2% | 80.2% | +0.2 | n/a | no target |
| P06 | 166 | 68.7% | 68.7% | +0.2 | 95% | ❌ 26 pts to go |
| P07 | 252 | 70.6% | 70.6% | +0.4 | 95% | ❌ 24 pts to go |
| P08 | 3039 | 66.1% | 66.1% | +0.0 | 95% | ❌ 29 pts to go |
| P09 | 381 | 95.5% | 95.5% | -2.9 | 100% | 🟡 4 pts to go |
| P10 | 2596 | 65.1% | 65.1% | -0.1 | 95% | ❌ 30 pts to go |
| P11 | 475 | 34.3% | 34.3% | -1.9 | 80% | ❌ 46 pts to go |
| P12 | 19 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 50802 | 76.0% | 76.0% | +0.4 | 95% | ❌ 19 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 88.9% | 88.9% | +0.0 | n/a | no target |
| P01T | 92 | 80.4% | 80.4% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 70.0% | 70.0% | -0.4 | 90% | ❌ 20 pts to go |
| P02 | 404 | 79.7% | 79.7% | +1.5 | 95% | ❌ 15 pts to go |
| P03 | 208 | 73.6% | 73.6% | -1.3 | 95% | ❌ 21 pts to go |
| P04 | 1566 | 84.8% | 84.8% | -0.2 | 95% | ❌ 10 pts to go |
| P05 | 384 | 75.0% | 75.0% | -0.7 | 90% | ❌ 15 pts to go |
| P06M | 168 | 83.9% | 83.9% | +0.0 | n/a | no target |
| P06T | 2440 | 77.3% | 77.3% | +0.1 | n/a | no target |
| P06 | 166 | 64.5% | 64.5% | +0.3 | 95% | ❌ 30 pts to go |
| P07 | 252 | 66.3% | 66.3% | +0.0 | 90% | ❌ 24 pts to go |
| P08 | 3039 | 74.7% | 74.7% | +0.0 | 95% | ❌ 20 pts to go |
| P09 | 381 | 88.7% | 88.7% | -0.9 | 100% | ❌ 11 pts to go |
| P10 | 2596 | 71.5% | 71.5% | +0.1 | 95% | ❌ 24 pts to go |
| P11 | 475 | 29.1% | 29.1% | -0.2 | 75% | ❌ 46 pts to go |
| P12 | 19 | 89.5% | 89.5% | -1.0 | n/a | no target |
| P13 | 50802 | 79.3% | 79.3% | +0.1 | 95% | ❌ 16 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 77.8% | 77.8% | +0.0 | n/a | no target |
| P01T | 92 | 91.3% | 91.3% | +0.0 | 95% | 🟡 4 pts to go |
| P01_GOLD | 624 | 81.6% | 81.6% | +11.4 | 90% | 🟡 8 pts to go |
| P02 | 404 | 88.1% | 88.1% | +6.6 | 95% | 🟡 7 pts to go |
| P03 | 208 | 84.6% | 84.6% | +12.0 | 95% | ❌ 10 pts to go |
| P04 | 1566 | 83.8% | 83.8% | +18.1 | 90% | 🟡 6 pts to go |
| P05 | 384 | 89.3% | 89.3% | +10.1 | 95% | 🟡 6 pts to go |
| P06M | 168 | 85.1% | 85.1% | +0.0 | n/a | no target |
| P06T | 2440 | 94.0% | 94.0% | +0.2 | n/a | no target |
| P06 | 166 | 90.4% | 90.4% | +0.1 | 100% | 🟡 10 pts to go |
| P07 | 252 | 88.1% | 88.1% | +0.4 | 100% | ❌ 12 pts to go |
| P08 | 3039 | 90.6% | 90.6% | +0.0 | 100% | 🟡 9 pts to go |
| P09 | 381 | 73.8% | 73.8% | +19.0 | n/a | no target |
| P10 | 2596 | 90.0% | 90.0% | +0.0 | 100% | 🟡 10 pts to go |
| P11 | 475 | 36.2% | 36.2% | +2.3 | 80% | ❌ 44 pts to go |
| P12 | 19 | 84.2% | 84.2% | +22.3 | n/a | no target |
| P13 | 50802 | 84.2% | 84.2% | +0.0 | 95% | ❌ 11 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 16.7% | 16.7% | +0.0 | n/a | no target |
| P01T | 92 | 23.9% | 23.9% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 14.3% | 14.3% | +0.6 | 25% | ❌ 11 pts to go |
| P02 | 404 | 27.7% | 27.7% | +1.1 | 40% | ❌ 12 pts to go |
| P03 | 208 | 10.1% | 10.1% | +1.6 | 20% | 🟡 10 pts to go |
| P04 | 1566 | 7.4% | 7.4% | +0.9 | 20% | ❌ 13 pts to go |
| P05 | 384 | 3.9% | 3.9% | -0.1 | 15% | ❌ 11 pts to go |
| P06M | 168 | 4.8% | 4.8% | +0.0 | n/a | no target |
| P06T | 2440 | 3.2% | 3.2% | +0.8 | n/a | no target |
| P06 | 166 | 5.4% | 5.4% | -0.1 | n/a | no target |
| P07 | 252 | 6.3% | 6.3% | +0.0 | n/a | no target |
| P08 | 3039 | 1.0% | 1.0% | +0.0 | n/a | no target |
| P09 | 381 | 7.9% | 7.9% | -0.1 | n/a | no target |
| P10 | 2596 | 1.3% | 1.3% | +0.0 | n/a | no target |
| P11 | 475 | 2.5% | 2.5% | +0.4 | n/a | no target |
| P12 | 19 | 10.5% | 10.5% | +1.0 | n/a | no target |
| P13 | 50802 | 0.6% | 0.6% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 38.9% | 38.9% | +0.0 | n/a | no target |
| P01T | 92 | 34.8% | 34.8% | +0.0 | 70% | ❌ 35 pts to go |
| P01_GOLD | 624 | 43.3% | 43.3% | -0.1 | 80% | ❌ 37 pts to go |
| P02 | 404 | 64.1% | 64.1% | -0.1 | 90% | ❌ 26 pts to go |
| P03 | 208 | 23.1% | 23.1% | +1.6 | 60% | ❌ 37 pts to go |
| P04 | 1566 | 50.5% | 50.5% | +0.3 | 85% | ❌ 34 pts to go |
| P05 | 384 | 13.0% | 13.0% | +0.1 | 50% | ❌ 37 pts to go |
| P06M | 168 | 6.5% | 6.5% | +0.0 | n/a | no target |
| P06T | 2440 | 2.7% | 2.7% | +0.3 | n/a | no target |
| P06 | 166 | 18.1% | 18.1% | -0.1 | n/a | no target |
| P07 | 252 | 19.0% | 19.0% | +0.0 | n/a | no target |
| P08 | 3039 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P09 | 381 | 80.6% | 80.6% | -0.4 | 95% | ❌ 14 pts to go |
| P10 | 2596 | 3.1% | 3.1% | +0.0 | n/a | no target |
| P11 | 475 | 29.5% | 29.5% | -1.0 | n/a | no target |
| P12 | 19 | 31.6% | 31.6% | -1.7 | n/a | no target |
| P13 | 50802 | 1.0% | 1.0% | +0.0 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 92 | 16.3% | 16.3% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 33.8% | 33.8% | +0.3 | 70% | ❌ 36 pts to go |
| P02 | 404 | 44.3% | 44.3% | +1.7 | 75% | ❌ 31 pts to go |
| P03 | 208 | 23.1% | 23.1% | +2.0 | 55% | ❌ 32 pts to go |
| P04 | 1566 | 50.5% | 50.5% | +0.7 | 75% | ❌ 24 pts to go |
| P05 | 384 | 11.7% | 11.7% | +0.6 | 50% | ❌ 38 pts to go |
| P06M | 168 | 1.8% | 1.8% | +0.0 | n/a | no target |
| P06T | 2440 | 1.5% | 1.5% | +0.4 | n/a | no target |
| P06 | 166 | 10.2% | 10.2% | -0.1 | n/a | no target |
| P07 | 252 | 10.3% | 10.3% | +0.0 | n/a | no target |
| P08 | 3039 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P09 | 381 | 77.7% | 77.7% | +0.2 | 95% | ❌ 17 pts to go |
| P10 | 2596 | 1.8% | 1.8% | +0.0 | n/a | no target |
| P11 | 475 | 28.6% | 28.6% | -1.1 | n/a | no target |
| P12 | 19 | 15.8% | 15.8% | -3.2 | n/a | no target |
| P13 | 50802 | 0.6% | 0.6% | +0.0 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 16.7% | 16.7% | +0.0 | n/a | no target |
| P01T | 92 | 19.6% | 19.6% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 57.9% | 58.0% | +2.0 | 80% | ❌ 22 pts to go |
| P02 | 404 | 52.2% | 52.5% | +4.6 | 75% | ❌ 23 pts to go |
| P03 | 208 | 45.2% | 45.2% | +8.9 | 70% | ❌ 25 pts to go |
| P04 | 1566 | 48.7% | 49.8% | +8.9 | 70% | ❌ 21 pts to go |
| P05 | 384 | 16.4% | 16.4% | +1.4 | 50% | ❌ 34 pts to go |
| P06M | 168 | 4.2% | 4.2% | +0.0 | n/a | no target |
| P06T | 2440 | 1.6% | 1.7% | +0.1 | n/a | no target |
| P06 | 166 | 23.5% | 23.5% | -0.1 | n/a | no target |
| P07 | 252 | 5.2% | 5.2% | +0.0 | n/a | no target |
| P08 | 3039 | 1.0% | 1.0% | +0.0 | n/a | no target |
| P09 | 381 | 44.1% | 44.4% | +1.9 | 80% | ❌ 36 pts to go |
| P10 | 2596 | 1.5% | 1.6% | +0.0 | n/a | no target |
| P11 | 475 | 16.8% | 17.1% | -0.5 | n/a | no target |
| P12 | 19 | 31.6% | 31.6% | -6.5 | n/a | no target |
| P13 | 50802 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 38.9% | 38.9% | +0.0 | n/a | no target |
| P01T | 92 | 56.5% | 56.5% | +0.0 | 60% | 🟡 4 pts to go |
| P01_GOLD | 624 | 63.1% | 63.1% | +3.3 | 70% | 🟡 7 pts to go |
| P02 | 404 | 43.8% | 43.8% | +0.9 | 50% | 🟡 6 pts to go |
| P03 | 208 | 54.8% | 54.8% | +0.1 | 55% | 🟡 0 pts to go |
| P04 | 1566 | 22.8% | 22.8% | +4.3 | 40% | ❌ 17 pts to go |
| P05 | 384 | 17.2% | 17.2% | -0.2 | 40% | ❌ 23 pts to go |
| P06M | 168 | 16.1% | 16.1% | +0.0 | n/a | no target |
| P06T | 2440 | 12.4% | 12.4% | +2.5 | n/a | no target |
| P06 | 166 | 30.7% | 30.7% | +0.4 | n/a | no target |
| P07 | 252 | 15.9% | 15.9% | +0.0 | n/a | no target |
| P08 | 3039 | 4.6% | 4.6% | +0.0 | n/a | no target |
| P09 | 381 | 5.5% | 5.5% | +0.4 | n/a | no target |
| P10 | 2596 | 3.5% | 3.5% | +0.0 | n/a | no target |
| P11 | 475 | 7.4% | 7.4% | +0.2 | n/a | no target |
| P12 | 19 | 15.8% | 15.8% | -3.2 | n/a | no target |
| P13 | 50802 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 44.4% | 44.4% | +0.0 | n/a | no target |
| P01T | 92 | 69.6% | 69.6% | +0.0 | 65% | ✅ met |
| P01_GOLD | 624 | 68.8% | 68.8% | +1.3 | 70% | 🟡 1 pts to go |
| P02 | 404 | 25.5% | 25.5% | +0.2 | 50% | ❌ 24 pts to go |
| P03 | 208 | 55.8% | 55.8% | -3.4 | 60% | 🟡 4 pts to go |
| P04 | 1566 | 9.7% | 9.7% | -0.2 | 40% | ❌ 30 pts to go |
| P05 | 384 | 21.1% | 21.1% | +0.3 | 45% | ❌ 24 pts to go |
| P06M | 168 | 7.1% | 7.1% | +0.0 | n/a | no target |
| P06T | 2440 | 4.3% | 4.3% | +0.7 | n/a | no target |
| P06 | 166 | 48.2% | 48.2% | +0.3 | n/a | no target |
| P07 | 252 | 23.0% | 23.0% | +0.0 | n/a | no target |
| P08 | 3039 | 2.3% | 2.3% | +0.0 | n/a | no target |
| P09 | 381 | 8.7% | 8.7% | +0.9 | n/a | no target |
| P10 | 2596 | 2.0% | 2.0% | +0.0 | n/a | no target |
| P11 | 475 | 6.5% | 6.5% | -0.4 | n/a | no target |
| P12 | 19 | 10.5% | 10.5% | -3.8 | n/a | no target |
| P13 | 50802 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 11.1% | 11.1% | +0.0 | n/a | no target |
| P01T | 92 | 44.6% | 44.6% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 49.8% | 49.8% | +0.4 | 50% | 🟡 0 pts to go |
| P02 | 404 | 42.6% | 42.6% | +4.3 | n/a | no target |
| P03 | 208 | 58.7% | 58.7% | +0.0 | 60% | 🟡 1 pts to go |
| P04 | 1566 | 25.9% | 25.9% | +1.9 | n/a | no target |
| P05 | 384 | 16.1% | 16.1% | +0.0 | n/a | no target |
| P06M | 168 | 4.2% | 4.2% | +0.0 | n/a | no target |
| P06T | 2440 | 4.0% | 4.0% | +1.0 | n/a | no target |
| P06 | 166 | 34.9% | 34.9% | -0.3 | n/a | no target |
| P07 | 252 | 17.9% | 17.9% | +0.0 | n/a | no target |
| P08 | 3039 | 1.4% | 1.4% | +0.0 | n/a | no target |
| P09 | 381 | 18.6% | 18.6% | -0.7 | n/a | no target |
| P10 | 2596 | 2.3% | 2.3% | +0.0 | n/a | no target |
| P11 | 475 | 7.8% | 7.8% | +0.6 | n/a | no target |
| P12 | 19 | 21.1% | 21.1% | +2.1 | n/a | no target |
| P13 | 50802 | 0.4% | 0.4% | +0.0 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 27.8% | 27.8% | +0.0 | 15% | ✅ met |
| P01T | 92 | 29.3% | 29.3% | +0.0 | 15% | ✅ met |
| P01_GOLD | 624 | 35.1% | 35.1% | -0.2 | 40% | 🟡 5 pts to go |
| P02 | 404 | 13.9% | 14.1% | -0.1 | 25% | ❌ 11 pts to go |
| P03 | 208 | 21.6% | 21.6% | -0.4 | 25% | 🟡 3 pts to go |
| P04 | 1566 | 5.2% | 5.2% | +0.1 | 15% | 🟡 10 pts to go |
| P05 | 384 | 8.1% | 8.1% | -0.1 | 15% | 🟡 7 pts to go |
| P06M | 168 | 6.0% | 6.0% | +0.0 | 15% | 🟡 9 pts to go |
| P06T | 2440 | 1.5% | 1.5% | +0.3 | 15% | ❌ 14 pts to go |
| P06 | 166 | 10.2% | 10.2% | -0.1 | 15% | 🟡 5 pts to go |
| P07 | 252 | 6.7% | 6.7% | +0.0 | 15% | 🟡 8 pts to go |
| P08 | 3039 | 0.9% | 0.9% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 381 | 0.8% | 0.8% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2596 | 1.4% | 1.4% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 475 | 1.3% | 1.3% | +0.0 | 15% | ❌ 14 pts to go |
| P12 | 19 | 0.0% | 0.0% | -4.8 | 15% | ❌ 15 pts to go |
| P13 | 50802 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 11.1% | 11.1% | +0.0 | 15% | 🟡 4 pts to go |
| P01T | 92 | 32.6% | 32.6% | +0.0 | 25% | ✅ met |
| P01_GOLD | 624 | 29.2% | 29.2% | +2.9 | 25% | ✅ met |
| P02 | 404 | 28.0% | 28.0% | +1.2 | 15% | ✅ met |
| P03 | 208 | 26.0% | 26.0% | -0.9 | 15% | ✅ met |
| P04 | 1566 | 8.1% | 8.1% | +1.2 | 15% | 🟡 7 pts to go |
| P05 | 384 | 11.7% | 11.7% | -0.2 | 15% | 🟡 3 pts to go |
| P06M | 168 | 2.4% | 2.4% | +0.0 | 15% | ❌ 13 pts to go |
| P06T | 2440 | 2.7% | 2.7% | +0.5 | 15% | ❌ 12 pts to go |
| P06 | 166 | 12.0% | 12.0% | -0.1 | 15% | 🟡 3 pts to go |
| P07 | 252 | 7.5% | 7.5% | +0.0 | 15% | 🟡 8 pts to go |
| P08 | 3039 | 1.0% | 1.0% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 381 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2596 | 1.2% | 1.2% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 475 | 5.1% | 5.1% | +0.7 | 15% | 🟡 10 pts to go |
| P12 | 19 | 26.3% | 26.3% | +2.5 | 15% | ✅ met |
| P13 | 50802 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 5.6% | 5.6% | +0.0 | 20% | ❌ 14 pts to go |
| P01T | 92 | 9.8% | 9.8% | +0.0 | 20% | ❌ 10 pts to go |
| P01_GOLD | 624 | 4.3% | 4.3% | -0.1 | 20% | ❌ 16 pts to go |
| P02 | 404 | 1.5% | 1.5% | -0.3 | 20% | ❌ 18 pts to go |
| P03 | 208 | 1.9% | 1.9% | +0.6 | 20% | ❌ 18 pts to go |
| P04 | 1566 | 1.0% | 1.0% | +0.0 | 20% | ❌ 19 pts to go |
| P05 | 384 | 1.0% | 1.0% | -0.1 | 20% | ❌ 19 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 2440 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 166 | 3.6% | 3.6% | +0.0 | 20% | ❌ 16 pts to go |
| P07 | 252 | 0.8% | 0.8% | +0.0 | 20% | ❌ 19 pts to go |
| P08 | 3039 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 381 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2596 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 475 | 0.6% | 0.6% | +0.0 | 20% | ❌ 19 pts to go |
| P12 | 19 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 50802 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 5.6% | 5.6% | +0.0 | 15% | 🟡 9 pts to go |
| P01T | 92 | 7.6% | 7.6% | +0.0 | 15% | 🟡 7 pts to go |
| P01_GOLD | 624 | 10.4% | 10.4% | +1.2 | 15% | 🟡 5 pts to go |
| P02 | 404 | 13.4% | 13.4% | +0.6 | 15% | 🟡 2 pts to go |
| P03 | 208 | 24.0% | 24.0% | +2.5 | 15% | ✅ met |
| P04 | 1566 | 4.6% | 4.6% | +0.3 | 15% | ❌ 10 pts to go |
| P05 | 384 | 2.9% | 2.9% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 168 | 2.4% | 2.4% | +0.0 | 15% | ❌ 13 pts to go |
| P06T | 2440 | 1.4% | 1.4% | +0.4 | 15% | ❌ 14 pts to go |
| P06 | 166 | 5.4% | 5.4% | -0.1 | 15% | 🟡 10 pts to go |
| P07 | 252 | 3.2% | 3.2% | +0.0 | 15% | ❌ 12 pts to go |
| P08 | 3039 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P09 | 381 | 0.5% | 0.5% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2596 | 0.8% | 0.8% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 475 | 2.1% | 2.1% | +0.6 | 15% | ❌ 13 pts to go |
| P12 | 19 | 5.3% | 5.3% | +0.5 | 15% | 🟡 10 pts to go |
| P13 | 50802 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 11.1% | 11.1% | +0.0 | 20% | 🟡 9 pts to go |
| P01T | 92 | 41.3% | 41.3% | +0.0 | 40% | ✅ met |
| P01_GOLD | 624 | 45.7% | 45.7% | +1.3 | 40% | ✅ met |
| P02 | 404 | 48.5% | 48.5% | +3.6 | 20% | ✅ met |
| P03 | 208 | 55.8% | 55.8% | +2.0 | 35% | ✅ met |
| P04 | 1566 | 29.8% | 29.8% | +1.9 | 20% | ✅ met |
| P05 | 384 | 16.1% | 16.1% | -0.3 | 20% | 🟡 4 pts to go |
| P06M | 168 | 4.2% | 4.2% | +0.0 | 20% | ❌ 16 pts to go |
| P06T | 2440 | 4.4% | 4.4% | +1.1 | 20% | ❌ 16 pts to go |
| P06 | 166 | 34.9% | 34.9% | -0.3 | 20% | ✅ met |
| P07 | 252 | 14.3% | 14.3% | +0.0 | 20% | 🟡 6 pts to go |
| P08 | 3039 | 2.2% | 2.2% | +0.0 | 20% | ❌ 18 pts to go |
| P09 | 381 | 22.0% | 22.0% | -0.5 | 20% | ✅ met |
| P10 | 2596 | 2.5% | 2.5% | +0.0 | 20% | ❌ 18 pts to go |
| P11 | 475 | 8.2% | 8.2% | +0.6 | 20% | ❌ 12 pts to go |
| P12 | 19 | 15.8% | 15.8% | +1.5 | 20% | 🟡 4 pts to go |
| P13 | 50802 | 0.6% | 0.6% | +0.0 | 20% | ❌ 19 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 92 | 1.1% | 1.1% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 69.7% | 69.7% | -0.8 | 95% | ❌ 25 pts to go |
| P02 | 404 | 73.3% | 73.3% | +0.4 | 95% | ❌ 22 pts to go |
| P03 | 208 | 67.3% | 67.3% | +4.1 | 90% | ❌ 23 pts to go |
| P04 | 1566 | 58.4% | 58.4% | -0.3 | 85% | ❌ 27 pts to go |
| P05 | 384 | 34.9% | 34.9% | +0.6 | 75% | ❌ 40 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 166 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 252 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 3039 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 381 | 90.8% | 90.8% | -0.1 | 100% | 🟡 9 pts to go |
| P10 | 2596 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 475 | 18.9% | 18.9% | +0.0 | 60% | ❌ 41 pts to go |
| P12 | 19 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 50802 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 92 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 72.9% | 72.9% | -1.1 | 100% | ❌ 27 pts to go |
| P02 | 404 | 77.2% | 77.2% | +0.5 | 100% | ❌ 23 pts to go |
| P03 | 208 | 74.5% | 74.5% | +4.1 | n/a | no target |
| P04 | 1566 | 60.0% | 60.0% | -0.1 | 95% | ❌ 35 pts to go |
| P05 | 384 | 31.2% | 31.2% | +0.6 | 80% | ❌ 49 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 166 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 252 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 3039 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 381 | 93.4% | 93.4% | -0.2 | 100% | 🟡 7 pts to go |
| P10 | 2596 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 475 | 20.2% | 20.2% | +0.0 | n/a | no target |
| P12 | 19 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 50802 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 92 | 1.1% | 1.1% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 51.9% | 51.9% | -1.2 | 85% | ❌ 33 pts to go |
| P02 | 404 | 66.8% | 66.8% | +1.9 | 90% | ❌ 23 pts to go |
| P03 | 208 | 54.8% | 54.8% | +3.7 | 85% | ❌ 30 pts to go |
| P04 | 1566 | 64.1% | 64.1% | +0.0 | 90% | ❌ 26 pts to go |
| P05 | 384 | 35.2% | 35.2% | +0.1 | 75% | ❌ 40 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 166 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 252 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 3039 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 381 | 85.6% | 85.6% | +0.6 | 95% | 🟡 9 pts to go |
| P10 | 2596 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 475 | 17.5% | 17.5% | -0.8 | n/a | no target |
| P12 | 19 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 50802 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 92 | 1.1% | 1.1% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 52.1% | 52.1% | -1.7 | 85% | ❌ 33 pts to go |
| P02 | 404 | 61.1% | 61.1% | +0.9 | 90% | ❌ 29 pts to go |
| P03 | 208 | 56.2% | 56.2% | +4.2 | 85% | ❌ 29 pts to go |
| P04 | 1566 | 54.3% | 54.3% | +0.3 | 90% | ❌ 36 pts to go |
| P05 | 384 | 41.7% | 41.7% | -0.5 | 75% | ❌ 33 pts to go |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2440 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 166 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 252 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 3039 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 381 | 0.3% | 0.3% | +0.0 | 95% | ❌ 95 pts to go |
| P10 | 2596 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 475 | 14.3% | 14.3% | -0.4 | n/a | no target |
| P12 | 19 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 50802 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 92 | 81.5% | 81.5% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 85.7% | 85.7% | -0.7 | 100% | ❌ 14 pts to go |
| P02 | 404 | 81.7% | 81.7% | +1.2 | 100% | ❌ 18 pts to go |
| P03 | 208 | 92.3% | 92.3% | +1.3 | n/a | no target |
| P04 | 1566 | 72.6% | 72.6% | +0.0 | 95% | ❌ 22 pts to go |
| P05 | 384 | 75.5% | 75.5% | +0.3 | 95% | ❌ 20 pts to go |
| P06M | 168 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06T | 2440 | 83.4% | 83.4% | +0.0 | n/a | no target |
| P06 | 166 | 75.9% | 75.9% | +0.1 | n/a | no target |
| P07 | 252 | 77.0% | 77.0% | +0.0 | n/a | no target |
| P08 | 3039 | 84.9% | 85.0% | +0.0 | n/a | no target |
| P09 | 381 | 99.0% | 99.0% | +0.1 | 100% | 🟡 1 pts to go |
| P10 | 2596 | 98.4% | 98.4% | +0.0 | n/a | no target |
| P11 | 475 | 89.9% | 89.9% | +0.0 | n/a | no target |
| P12 | 19 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 50802 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 92 | 81.5% | 81.5% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 88.9% | 88.9% | -0.9 | 100% | ❌ 11 pts to go |
| P02 | 404 | 82.9% | 83.2% | +1.2 | 100% | ❌ 17 pts to go |
| P03 | 208 | 93.8% | 93.8% | +1.9 | n/a | no target |
| P04 | 1566 | 79.0% | 79.0% | +0.0 | 95% | ❌ 16 pts to go |
| P05 | 384 | 90.1% | 90.1% | +0.1 | 70% | ✅ met |
| P06M | 168 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06T | 2440 | 83.4% | 83.4% | +0.0 | n/a | no target |
| P06 | 166 | 75.9% | 75.9% | +0.1 | n/a | no target |
| P07 | 252 | 77.0% | 77.0% | +0.0 | n/a | no target |
| P08 | 3039 | 84.9% | 85.0% | +0.0 | n/a | no target |
| P09 | 381 | 99.0% | 99.0% | +0.1 | 100% | 🟡 1 pts to go |
| P10 | 2596 | 98.4% | 98.4% | +0.0 | n/a | no target |
| P11 | 475 | 90.3% | 90.3% | +0.0 | n/a | no target |
| P12 | 19 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 50802 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 92 | 1.1% | 1.1% | +0.0 | n/a | no target · rows from a source that publishes bids: 3 rows, 33.3% filled |
| P01_GOLD | 624 | 17.3% | 17.3% | -0.6 | 60% | ❌ 43 pts to go · rows from a source that publishes bids: 366 rows, 29.5% filled |
| P02 | 404 | 13.1% | 13.1% | -0.2 | n/a | no target · rows from a source that publishes bids: 295 rows, 18.0% filled |
| P03 | 208 | 16.3% | 16.3% | +0.6 | n/a | no target · rows from a source that publishes bids: 140 rows, 24.3% filled |
| P04 | 1566 | 3.7% | 3.7% | +0.0 | n/a | no target · rows from a source that publishes bids: 874 rows, 6.6% filled |
| P05 | 384 | 3.4% | 3.4% | +0.0 | n/a | no target · rows from a source that publishes bids: 53 rows, 24.5% filled |
| P06M | 168 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 2440 | 0.1% | 0.1% | +0.0 | n/a | no target · rows from a source that publishes bids: 4 rows, 50.0% filled |
| P06 | 166 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 252 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 3039 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 381 | 3.1% | 3.1% | -0.1 | n/a | no target · rows from a source that publishes bids: 367 rows, 3.3% filled |
| P10 | 2596 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 475 | 2.7% | 2.7% | +0.0 | n/a | no target · rows from a source that publishes bids: 93 rows, 14.0% filled |
| P12 | 19 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 19 rows, 0.0% filled |
| P13 | 50802 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 92 | 0.0% | 96.7% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 53.2% | 82.5% | -1.7 | 90% | ❌ 37 pts to go |
| P02 | 404 | 61.1% | 85.6% | +0.9 | 90% | ❌ 29 pts to go |
| P03 | 208 | 56.2% | 76.0% | +4.2 | 90% | ❌ 34 pts to go |
| P04 | 1566 | 45.3% | 85.6% | +0.4 | 90% | ❌ 45 pts to go |
| P05 | 384 | 0.0% | 81.0% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 168 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 2440 | 0.0% | 99.8% | +0.0 | n/a | no target |
| P06 | 166 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 252 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 3039 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 381 | 2.1% | 3.4% | +0.8 | 90% | ❌ 88 pts to go |
| P10 | 2596 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 475 | 12.8% | 90.5% | -0.7 | n/a | no target |
| P12 | 19 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 50802 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 92 | 0.0% | 96.7% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 26.0% | 55.3% | -1.1 | 90% | ❌ 64 pts to go |
| P02 | 404 | 59.9% | 84.4% | +1.8 | n/a | no target |
| P03 | 208 | 30.8% | 50.5% | +3.4 | n/a | no target |
| P04 | 1566 | 49.7% | 90.0% | +0.0 | n/a | no target |
| P05 | 384 | 0.5% | 81.5% | +0.2 | n/a | no target |
| P06M | 168 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 2440 | 0.0% | 99.8% | +0.0 | n/a | no target |
| P06 | 166 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 252 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 3039 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 381 | 44.4% | 45.7% | -0.8 | n/a | no target |
| P10 | 2596 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 475 | 11.8% | 89.5% | -0.4 | n/a | no target |
| P12 | 19 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 50802 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 92 | 2.2% | 98.9% | +0.0 | n/a | no target |
| P01_GOLD | 624 | 51.6% | 80.9% | -1.8 | 95% | ❌ 43 pts to go |
| P02 | 404 | 65.6% | 90.1% | +1.4 | n/a | no target |
| P03 | 208 | 59.1% | 78.8% | +2.1 | n/a | no target |
| P04 | 1566 | 50.3% | 90.6% | +0.0 | n/a | no target |
| P05 | 384 | 5.2% | 86.2% | +0.7 | n/a | no target |
| P06M | 168 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 2440 | 0.0% | 99.8% | +0.0 | n/a | no target |
| P06 | 166 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 252 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 3039 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 381 | 67.5% | 68.8% | -1.5 | n/a | no target |
| P10 | 2596 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 475 | 12.8% | 90.5% | +0.4 | n/a | no target |
| P12 | 19 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 50802 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 92 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 624 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 404 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 208 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1566 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 384 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 168 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 2440 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 166 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 252 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 3039 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 381 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2596 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 475 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P12 | 19 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 50802 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 92 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 624 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 404 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 208 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1566 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 384 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 168 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 2440 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 166 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 252 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 3039 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 381 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2596 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 475 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P12 | 19 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 50802 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 18 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 92 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 624 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 404 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 208 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 1566 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 384 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 168 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 2440 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 166 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 252 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 3039 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 381 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2596 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 475 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P12 | 19 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 50802 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |


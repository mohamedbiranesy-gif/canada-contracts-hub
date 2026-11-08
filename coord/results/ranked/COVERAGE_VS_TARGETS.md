# Coverage vs the downstream team's targets — 2026-11-08

Benchmarks (field × package with a numeric target): **41 of 438 met** (9.4%); 72 within 10 points; 325 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 20, P01T 92, P01_GOLD 582, P02 369, P03 225, P04 1615, P05 379, P06M 167, P06T 2435, P06 163, P07 249, P08 3037, P09 369, P10 2590, P11 498, P12 21, P13 50788

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% | 6 | reference to quote (PO / contract / vendor id) (20 rows) |
| P01T | 92 | 0.0% | 6.5% | 6 | currency (92 rows) |
| P01_GOLD | 582 | 1.9% | 43.3% | 8 | payment terms (357 rows) |
| P02 | 369 | 0.0% | 34.4% | 8 | PO rule (345 rows) |
| P03 | 225 | 0.4% | 20.0% | 7 | payment terms (178 rows) |
| P04 | 1615 | 0.0% | 18.7% | 7 | PO rule (1598 rows) |
| P05 | 379 | 0.3% | 2.9% | 6 | payment terms (354 rows) |
| P06M | 167 | 0.0% | 0.0% | 5 | reference to quote (PO / contract / vendor id) (167 rows) |
| P06T | 2435 | 0.0% | 0.0% | 5 | currency (2435 rows) |
| P06 | 163 | 0.0% | 0.6% | 5 | reference to quote (PO / contract / vendor id) (163 rows) |
| P07 | 249 | 0.0% | 0.0% | 4 | reference to quote (PO / contract / vendor id) (249 rows) |
| P08 | 3037 | 0.0% | 0.0% | 4 | reference to quote (PO / contract / vendor id) (3037 rows) |
| P09 | 369 | 0.0% | 33.3% | 8 | PO rule (355 rows) |
| P10 | 2590 | 0.0% | 0.0% | 4 | currency (2590 rows) |
| P11 | 498 | 0.0% | 5.6% | 3 | PO rule (487 rows) |
| P12 | 21 | 0.0% | 4.8% | 7 | reference to quote (PO / contract / vendor id) (21 rows) |
| P13 | 50788 | 0.0% | 0.0% | 4 | reference to quote (PO / contract / vendor id) (50788 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 20 | 4 | 2 | 14 | 0 | 0 | 71 |
| P01T | 92 | 6 | 33 | 53 | 0 | 0 | 71 |
| P01_GOLD | 582 | 67 | 207 | 308 | 0 | 0 | 75 |
| P02 | 369 | 0 | 42 | 327 | 0 | 0 | 61 |
| P03 | 225 | 0 | 0 | 216 | 9 | 0 | 51 |
| P04 | 1615 | 0 | 0 | 1555 | 60 | 0 | 49 |
| P05 | 379 | 9 | 24 | 327 | 19 | 0 | 48 |
| P06M | 167 | 0 | 1 | 157 | 9 | 0 | 46 |
| P06T | 2435 | 0 | 1 | 2153 | 281 | 0 | 46 |
| P06 | 163 | 8 | 26 | 129 | 0 | 0 | 68 |
| P07 | 249 | 0 | 3 | 221 | 25 | 0 | 49 |
| P08 | 3037 | 0 | 0 | 2246 | 791 | 0 | 39 |
| P09 | 369 | 4 | 5 | 359 | 1 | 0 | 50 |
| P10 | 2590 | 2 | 5 | 1852 | 731 | 0 | 38 |
| P11 | 498 | 0 | 0 | 0 | 0 | 498 | 24 |
| P12 | 21 | 0 | 0 | 21 | 0 | 0 | 51 |
| P13 | 50788 | 3 | 16 | 40450 | 10319 | 0 | 40 |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 16 | 0 | 0 | 0 | 0 | 1 | 1 | 13 | 14 | 6 |
| P01T | 86 | 0 | 0 | 0 | 1 | 4 | 4 | 52 | 70 | 58 |
| P01_GOLD | 515 | 0 | 0 | 0 | 1 | 82 | 40 | 303 | 387 | 260 |
| P02 | 369 | 0 | 369 | 0 | 0 | 31 | 13 | 345 | 337 | 209 |
| P03 | 225 | 0 | 225 | 0 | 1 | 41 | 13 | 166 | 191 | 85 |
| P04 | 1615 | 0 | 1615 | 0 | 1 | 337 | 127 | 1598 | 1591 | 981 |
| P05 | 370 | 0 | 316 | 0 | 3 | 91 | 54 | 338 | 357 | 237 |
| P06M | 167 | 0 | 167 | 0 | 0 | 19 | 47 | 165 | 166 | 94 |
| P06T | 2435 | 0 | 2435 | 0 | 18 | 865 | 485 | 2427 | 2421 | 1909 |
| P06 | 155 | 0 | 0 | 0 | 3 | 71 | 47 | 106 | 140 | 40 |
| P07 | 249 | 0 | 249 | 0 | 5 | 118 | 72 | 232 | 240 | 117 |
| P08 | 3037 | 0 | 3037 | 0 | 19 | 1924 | 1048 | 3029 | 3023 | 2067 |
| P09 | 365 | 0 | 346 | 0 | 2 | 64 | 1 | 355 | 359 | 278 |
| P10 | 2588 | 0 | 2535 | 0 | 21 | 1753 | 919 | 2569 | 2576 | 1866 |
| P11 | 498 | 498 | 461 | 0 | 5 | 358 | 235 | 487 | 495 | 322 |
| P12 | 21 | 0 | 16 | 0 | 0 | 6 | 0 | 20 | 19 | 16 |
| P13 | 50785 | 0 | 50477 | 0 | 460 | 28752 | 12600 | 50715 | 50664 | 40176 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 10152 |
| buyer_address | P13 | 75.1% | 95% | 10103 |
| ap_system_hint | P13 | 0.4% | 20% | 9973 |
| buyer_phone | P13 | 78.3% | 95% | 8479 |
| buyer_legal_name_as_published | P13 | 43.4% | 60% | 8437 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 7587 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 7554 |
| buyer_payment_method_preference | P13 | 0.8% | 15% | 7208 |
| buyer_logo_url | P13 | 81.4% | 95% | 6913 |
| buyer_bn_as_published | P13 | 19.5% | 30% | 5315 |
| buyer_legal_name_as_published | P08 | 36.6% | 75% | 1165 |
| buyer_legal_name_as_published | P10 | 32.3% | 70% | 976 |
| buyer_address | P08 | 65.4% | 95% | 900 |
| vendor_emails | P08 | 47.0% | 75% | 851 |
| buyer_address | P10 | 64.2% | 95% | 799 |
| average_contract_duration_days | P04 | 42.6% | 90% | 766 |
| invoice_reference_hint | P08 | 0.0% | 25% | 760 |
| vendor_emails | P10 | 50.7% | 80% | 758 |
| buyer_bn_as_published | P08 | 10.5% | 35% | 744 |
| vendor_registered_address | P10 | 42.4% | 70% | 714 |
| vendor_logo_url | P04 | 42.7% | 85% | 683 |
| invoice_reference_hint | P10 | 0.1% | 25% | 646 |
| solicitation_or_tender_number | P04 | 10.0% | 50% | 646 |
| po_required_as_published | P04 | 1.1% | 40% | 629 |
| vendor_phone | P08 | 64.5% | 85% | 624 |
| buyer_phone | P08 | 74.5% | 95% | 622 |
| payment_terms_as_published | P04 | 1.5% | 40% | 622 |
| buyer_phone | P10 | 71.4% | 95% | 613 |
| vendor_emails | P04 | 32.4% | 70% | 607 |
| buyer_ap_cycle_published | P08 | 0.1% | 20% | 606 |
| contract_description | P04 | 57.9% | 95% | 600 |
| end_date | P04 | 53.1% | 90% | 596 |
| currency | P04 | 58.5% | 95% | 590 |
| ap_system_hint | P08 | 0.9% | 20% | 582 |
| ap_phone | P04 | 49.2% | 85% | 578 |
| buyer_vendor_id | P04 | 4.3% | 40% | 576 |
| records_with_this_vendor | P04 | 59.7% | 95% | 571 |
| vendor_neq | P04 | 60.2% | 95% | 562 |
| invoicing_requirements | P04 | 35.4% | 70% | 560 |
| buyer_bn_as_published | P10 | 8.9% | 30% | 547 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | 50% | ❌ 50 pts to go |
| P01T | 92 | 5.4% | 6.5% |  | 50% | ❌ 45 pts to go |
| P01_GOLD | 582 | 77.3% | 85.7% |  | 95% | ❌ 18 pts to go |
| P02 | 369 | 75.9% | 78.6% |  | 95% | ❌ 19 pts to go |
| P03 | 225 | 77.8% | 87.6% |  | 95% | ❌ 17 pts to go |
| P04 | 1615 | 66.1% | 69.2% |  | 90% | ❌ 24 pts to go |
| P05 | 379 | 32.7% | 36.4% |  | 70% | ❌ 37 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2435 | 0.2% | 0.2% |  | n/a | no target |
| P06 | 163 | 0.0% | 0.0% |  | 30% | ❌ 30 pts to go |
| P07 | 249 | 0.0% | 0.0% |  | 30% | ❌ 30 pts to go |
| P08 | 3037 | 0.0% | 0.0% |  | 25% | ❌ 25 pts to go |
| P09 | 369 | 98.4% | 99.2% |  | 100% | 🟡 2 pts to go |
| P10 | 2590 | 0.1% | 1.0% |  | 25% | ❌ 25 pts to go |
| P11 | 498 | 24.9% | 28.5% |  | 60% | ❌ 35 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50788 | 0.0% | 0.1% |  | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | 10% | 🟡 10 pts to go |
| P01_GOLD | 582 | 6.5% | 6.5% |  | 50% | ❌ 44 pts to go |
| P02 | 369 | 7.9% | 7.9% |  | 50% | ❌ 42 pts to go |
| P03 | 225 | 1.3% | 1.3% |  | 40% | ❌ 39 pts to go |
| P04 | 1615 | 1.1% | 1.1% |  | 30% | ❌ 29 pts to go |
| P05 | 379 | 0.3% | 0.3% |  | 20% | ❌ 20 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2435 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 163 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 249 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 0.5% | 0.5% |  | 50% | ❌ 50 pts to go |
| P10 | 2590 | 0.1% | 0.1% |  | n/a | no target |
| P11 | 498 | 1.4% | 1.4% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50788 | 0.0% | 0.0% |  | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 4.3% | 4.3% |  | 50% | ❌ 46 pts to go |
| P01_GOLD | 582 | 45.7% | 45.7% |  | 85% | ❌ 39 pts to go |
| P02 | 369 | 62.6% | 62.6% |  | 90% | ❌ 27 pts to go |
| P03 | 225 | 45.8% | 45.8% |  | 85% | ❌ 39 pts to go |
| P04 | 1615 | 61.2% | 61.2% |  | 85% | ❌ 24 pts to go |
| P05 | 379 | 21.9% | 21.9% |  | 60% | ❌ 38 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2435 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 163 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 249 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 87.0% | 87.0% |  | 100% | ❌ 13 pts to go |
| P10 | 2590 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 498 | 18.5% | 18.5% |  | 60% | ❌ 42 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50788 | 0.0% | 0.0% |  | n/a | no target |

### `solicitation_or_tender_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 2.2% | 2.2% |  | 30% | ❌ 28 pts to go |
| P01_GOLD | 582 | 38.1% | 38.1% |  | 80% | ❌ 42 pts to go |
| P02 | 369 | 22.5% | 22.5% |  | 60% | ❌ 38 pts to go |
| P03 | 225 | 40.9% | 40.9% |  | 80% | ❌ 39 pts to go |
| P04 | 1615 | 10.0% | 10.0% |  | 50% | ❌ 40 pts to go |
| P05 | 379 | 12.4% | 12.4% |  | 40% | ❌ 28 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2435 | 0.2% | 0.2% |  | n/a | no target |
| P06 | 163 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 249 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 11.1% | 11.1% |  | 50% | ❌ 39 pts to go |
| P10 | 2590 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 498 | 11.6% | 11.6% |  | 40% | ❌ 28 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50788 | 0.0% | 0.0% |  | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 3.3% | 3.3% |  | n/a | no target |
| P01_GOLD | 582 | 44.3% | 44.3% |  | 85% | ❌ 41 pts to go |
| P02 | 369 | 54.2% | 54.2% |  | 90% | ❌ 36 pts to go |
| P03 | 225 | 50.7% | 50.7% |  | 85% | ❌ 34 pts to go |
| P04 | 1615 | 52.6% | 52.6% |  | 85% | ❌ 32 pts to go |
| P05 | 379 | 15.0% | 15.0% |  | 50% | ❌ 35 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2435 | 0.1% | 0.1% |  | n/a | no target |
| P06 | 163 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 249 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 90.8% | 90.8% |  | 100% | 🟡 9 pts to go |
| P10 | 2590 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 498 | 18.7% | 18.7% |  | 60% | ❌ 41 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50788 | 0.0% | 0.0% |  | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 2.2% | 2.2% |  | n/a | no target |
| P01_GOLD | 582 | 13.6% | 13.6% |  | 60% | ❌ 46 pts to go |
| P02 | 369 | 7.3% | 7.3% |  | 50% | ❌ 43 pts to go |
| P03 | 225 | 10.2% | 10.2% |  | 50% | ❌ 40 pts to go |
| P04 | 1615 | 4.3% | 4.3% |  | 40% | ❌ 36 pts to go |
| P05 | 379 | 1.3% | 1.3% |  | 20% | ❌ 19 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2435 | 0.1% | 0.1% |  | n/a | no target |
| P06 | 163 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 249 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 2.4% | 2.4% |  | 50% | ❌ 48 pts to go |
| P10 | 2590 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 498 | 4.8% | 4.8% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50788 | 0.0% | 0.0% |  | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 582 | 36.4% | 36.4% |  | 80% | ❌ 44 pts to go |
| P02 | 369 | 59.3% | 59.3% |  | 90% | ❌ 31 pts to go |
| P03 | 225 | 36.9% | 36.9% |  | 80% | ❌ 43 pts to go |
| P04 | 1615 | 51.2% | 51.2% |  | 85% | ❌ 34 pts to go |
| P05 | 379 | 5.3% | 5.3% |  | 50% | ❌ 45 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2435 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 163 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 249 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 75.9% | 75.9% |  | 95% | ❌ 19 pts to go |
| P10 | 2590 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 498 | 15.9% | 15.9% |  | 50% | ❌ 34 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50788 | 0.0% | 0.0% |  | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 1.1% | 1.1% |  | n/a | no target |
| P01_GOLD | 582 | 8.8% | 8.8% |  | 50% | ❌ 41 pts to go |
| P02 | 369 | 7.9% | 7.9% |  | 50% | ❌ 42 pts to go |
| P03 | 225 | 2.2% | 2.2% |  | 30% | ❌ 28 pts to go |
| P04 | 1615 | 1.1% | 1.1% |  | 30% | ❌ 29 pts to go |
| P05 | 379 | 0.0% | 0.0% |  | n/a | no target |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2435 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 163 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 249 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 0.3% | 0.3% |  | n/a | no target |
| P10 | 2590 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 498 | 1.4% | 1.4% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50788 | 0.0% | 0.0% |  | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 100.0% |  | n/a | no target |
| P01T | 92 | 3.3% | 100.0% |  | 60% | ❌ 57 pts to go |
| P01_GOLD | 582 | 72.9% | 100.0% |  | 100% | ❌ 27 pts to go |
| P02 | 369 | 75.1% | 100.0% |  | 100% | ❌ 25 pts to go |
| P03 | 225 | 74.7% | 100.0% |  | 100% | ❌ 25 pts to go |
| P04 | 1615 | 59.7% | 100.0% |  | 95% | ❌ 35 pts to go |
| P05 | 379 | 17.9% | 100.0% |  | 70% | ❌ 52 pts to go |
| P06M | 167 | 0.0% | 100.0% |  | n/a | no target |
| P06T | 2435 | 0.2% | 100.0% |  | n/a | no target |
| P06 | 163 | 0.0% | 100.0% |  | 50% | ❌ 50 pts to go |
| P07 | 249 | 0.0% | 100.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 100.0% |  | n/a | no target |
| P09 | 369 | 98.6% | 100.0% |  | 100% | 🟡 1 pts to go |
| P10 | 2590 | 0.0% | 100.0% |  | n/a | no target |
| P11 | 498 | 26.3% | 100.0% |  | 70% | ❌ 44 pts to go |
| P12 | 21 | 0.0% | 100.0% |  | n/a | no target |
| P13 | 50788 | 0.0% | 0.0% |  | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 100.0% | 100.0% |  | 70% | ✅ met |
| P01T | 92 | 80.4% | 80.4% |  | 60% | ✅ met |
| P01_GOLD | 582 | 79.0% | 79.0% |  | 90% | ❌ 11 pts to go |
| P02 | 369 | 65.3% | 65.3% |  | 85% | ❌ 20 pts to go |
| P03 | 225 | 80.9% | 80.9% |  | 90% | 🟡 9 pts to go |
| P04 | 1615 | 54.1% | 54.1% |  | 75% | ❌ 21 pts to go |
| P05 | 379 | 53.3% | 53.3% |  | 50% | ✅ met |
| P06M | 167 | 74.3% | 74.3% |  | n/a | no target |
| P06T | 2435 | 60.6% | 60.6% |  | n/a | no target |
| P06 | 163 | 46.0% | 46.0% |  | 40% | ✅ met |
| P07 | 249 | 39.8% | 39.8% |  | 50% | ❌ 10 pts to go |
| P08 | 3037 | 41.8% | 41.8% |  | 50% | 🟡 8 pts to go |
| P09 | 369 | 54.5% | 54.5% |  | 80% | ❌ 26 pts to go |
| P10 | 2590 | 36.6% | 36.6% |  | 40% | 🟡 3 pts to go |
| P11 | 498 | 46.2% | 46.2% |  | 60% | ❌ 14 pts to go |
| P12 | 21 | 52.4% | 52.4% |  | 85% | ❌ 33 pts to go |
| P13 | 50788 | 91.7% | 91.7% |  | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 60.0% | 60.0% |  | n/a | no target |
| P01T | 92 | 63.0% | 63.0% |  | n/a | no target |
| P01_GOLD | 582 | 75.9% | 75.9% |  | 95% | ❌ 19 pts to go |
| P02 | 369 | 81.8% | 81.8% |  | 95% | ❌ 13 pts to go |
| P03 | 225 | 77.3% | 77.3% |  | 95% | ❌ 18 pts to go |
| P04 | 1615 | 78.6% | 78.6% |  | 95% | ❌ 16 pts to go |
| P05 | 379 | 55.7% | 55.7% |  | 70% | ❌ 14 pts to go |
| P06M | 167 | 21.0% | 21.0% |  | n/a | no target |
| P06T | 2435 | 78.2% | 78.2% |  | n/a | no target |
| P06 | 163 | 54.6% | 54.6% |  | 80% | ❌ 25 pts to go |
| P07 | 249 | 51.4% | 51.4% |  | 70% | ❌ 19 pts to go |
| P08 | 3037 | 52.2% | 52.2% |  | 70% | ❌ 18 pts to go |
| P09 | 369 | 89.7% | 89.7% |  | 100% | ❌ 10 pts to go |
| P10 | 2590 | 42.4% | 42.4% |  | 70% | ❌ 28 pts to go |
| P11 | 498 | 54.8% | 54.8% |  | 75% | ❌ 20 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50788 | 0.0% | 0.0% |  | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 50.0% | 50.0% |  | n/a | no target |
| P01T | 92 | 19.6% | 19.6% |  | n/a | no target |
| P01_GOLD | 582 | 50.0% | 50.0% |  | 60% | 🟡 10 pts to go |
| P02 | 369 | 63.1% | 63.1% |  | 60% | ✅ met |
| P03 | 225 | 56.9% | 56.9% |  | 60% | 🟡 3 pts to go |
| P04 | 1615 | 53.7% | 53.7% |  | 55% | 🟡 1 pts to go |
| P05 | 379 | 23.7% | 23.7% |  | 50% | ❌ 26 pts to go |
| P06M | 167 | 17.4% | 17.4% |  | n/a | no target |
| P06T | 2435 | 53.5% | 53.5% |  | n/a | no target |
| P06 | 163 | 49.1% | 49.1% |  | n/a | no target |
| P07 | 249 | 43.8% | 43.8% |  | 55% | ❌ 11 pts to go |
| P08 | 3037 | 44.3% | 44.3% |  | 50% | 🟡 6 pts to go |
| P09 | 369 | 71.5% | 71.5% |  | 70% | ✅ met |
| P10 | 2590 | 50.4% | 50.4% |  | 55% | 🟡 5 pts to go |
| P11 | 498 | 42.0% | 42.0% |  | 50% | 🟡 8 pts to go |
| P12 | 21 | 85.7% | 85.7% |  | n/a | no target |
| P13 | 50788 | 0.0% | 0.0% |  | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 35.0% | 35.0% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 582 | 33.3% | 33.3% |  | 70% | ❌ 37 pts to go |
| P02 | 369 | 42.0% | 42.0% |  | 70% | ❌ 28 pts to go |
| P03 | 225 | 38.7% | 38.7% |  | 70% | ❌ 31 pts to go |
| P04 | 1615 | 33.2% | 33.2% |  | 65% | ❌ 32 pts to go |
| P05 | 379 | 16.6% | 16.6% |  | 60% | ❌ 43 pts to go |
| P06M | 167 | 6.6% | 6.6% |  | n/a | no target |
| P06T | 2435 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 163 | 58.9% | 58.9% |  | 40% | ✅ met |
| P07 | 249 | 65.1% | 65.1% |  | 85% | ❌ 20 pts to go |
| P08 | 3037 | 64.5% | 64.5% |  | 85% | ❌ 20 pts to go |
| P09 | 369 | 52.3% | 52.3% |  | 85% | ❌ 33 pts to go |
| P10 | 2590 | 65.1% | 65.1% |  | 85% | ❌ 20 pts to go |
| P11 | 498 | 48.0% | 48.0% |  | 75% | ❌ 27 pts to go |
| P12 | 21 | 4.8% | 4.8% |  | n/a | no target |
| P13 | 50788 | 100.0% | 100.0% |  | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 45.0% | 45.0% |  | n/a | no target |
| P01T | 92 | 10.9% | 10.9% |  | n/a | no target |
| P01_GOLD | 582 | 82.0% | 82.0% |  | 90% | 🟡 8 pts to go |
| P02 | 369 | 79.9% | 79.9% |  | 90% | ❌ 10 pts to go |
| P03 | 225 | 82.7% | 82.7% |  | 90% | 🟡 7 pts to go |
| P04 | 1615 | 62.0% | 62.0% |  | 85% | ❌ 23 pts to go |
| P05 | 379 | 42.7% | 42.7% |  | 70% | ❌ 27 pts to go |
| P06M | 167 | 10.2% | 10.2% |  | n/a | no target |
| P06T | 2435 | 2.5% | 2.5% |  | n/a | no target |
| P06 | 163 | 96.9% | 96.9% |  | 50% | ✅ met |
| P07 | 249 | 94.4% | 94.4% |  | 100% | 🟡 6 pts to go |
| P08 | 3037 | 92.9% | 92.9% |  | 100% | 🟡 7 pts to go |
| P09 | 369 | 80.5% | 80.5% |  | 100% | ❌ 20 pts to go |
| P10 | 2590 | 100.0% | 100.0% |  | 100% | ✅ met |
| P11 | 498 | 87.6% | 87.6% |  | 100% | ❌ 12 pts to go |
| P12 | 21 | 42.9% | 42.9% |  | n/a | no target |
| P13 | 50788 | 100.0% | 100.0% |  | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 35.0% | 35.0% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 582 | 36.8% | 36.8% |  | 70% | ❌ 33 pts to go |
| P02 | 369 | 45.0% | 45.0% |  | 75% | ❌ 30 pts to go |
| P03 | 225 | 41.8% | 41.8% |  | 75% | ❌ 33 pts to go |
| P04 | 1615 | 32.4% | 32.4% |  | 70% | ❌ 38 pts to go |
| P05 | 379 | 14.0% | 14.0% |  | 55% | ❌ 41 pts to go |
| P06M | 167 | 6.6% | 6.6% |  | n/a | no target |
| P06T | 2435 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 163 | 40.5% | 40.5% |  | n/a | no target |
| P07 | 249 | 36.1% | 36.1% |  | 70% | ❌ 34 pts to go |
| P08 | 3037 | 47.0% | 47.0% |  | 75% | ❌ 28 pts to go |
| P09 | 369 | 52.8% | 52.8% |  | 85% | ❌ 32 pts to go |
| P10 | 2590 | 50.7% | 50.7% |  | 80% | ❌ 29 pts to go |
| P11 | 498 | 36.3% | 36.3% |  | 70% | ❌ 34 pts to go |
| P12 | 21 | 19.0% | 19.0% |  | n/a | no target |
| P13 | 50788 | 0.0% | 0.0% |  | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 35.0% | 35.0% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 582 | 49.1% | 49.1% |  | 90% | ❌ 41 pts to go |
| P02 | 369 | 57.7% | 57.7% |  | 90% | ❌ 32 pts to go |
| P03 | 225 | 54.7% | 54.7% |  | 90% | ❌ 35 pts to go |
| P04 | 1615 | 42.7% | 42.7% |  | 85% | ❌ 42 pts to go |
| P05 | 379 | 22.7% | 22.7% |  | 75% | ❌ 52 pts to go |
| P06M | 167 | 6.6% | 6.6% |  | n/a | no target |
| P06T | 2435 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 163 | 87.7% | 87.7% |  | n/a | no target |
| P07 | 249 | 88.0% | 88.0% |  | 100% | ❌ 12 pts to go |
| P08 | 3037 | 85.3% | 85.3% |  | 100% | ❌ 15 pts to go |
| P09 | 369 | 58.8% | 58.8% |  | n/a | no target |
| P10 | 2590 | 87.6% | 87.6% |  | 100% | ❌ 12 pts to go |
| P11 | 498 | 64.3% | 64.3% |  | n/a | no target |
| P12 | 21 | 14.3% | 14.3% |  | n/a | no target |
| P13 | 50788 | 0.0% | 0.0% |  | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 21.7% | 21.7% |  | n/a | no target · QC vendors: 2 rows, 100.0% filled |
| P01_GOLD | 582 | 49.1% | 49.1% |  | 95% | ❌ 46 pts to go · QC vendors: 49 rows, 98.0% filled |
| P02 | 369 | 66.9% | 66.9% |  | 95% | ❌ 28 pts to go · QC vendors: 93 rows, 100.0% filled |
| P03 | 225 | 54.7% | 54.7% |  | 95% | ❌ 40 pts to go · QC vendors: 16 rows, 100.0% filled |
| P04 | 1615 | 60.2% | 60.2% |  | 95% | ❌ 35 pts to go · QC vendors: 449 rows, 98.7% filled |
| P05 | 379 | 13.5% | 13.5% |  | n/a | no target · QC vendors: 26 rows, 92.3% filled |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2435 | 55.8% | 55.8% |  | n/a | no target · QC vendors: 56 rows, 100.0% filled |
| P06 | 163 | 24.5% | 24.5% |  | n/a | no target · QC vendors: 16 rows, 100.0% filled |
| P07 | 249 | 18.5% | 18.5% |  | n/a | no target · QC vendors: 26 rows, 96.2% filled |
| P08 | 3037 | 26.8% | 26.8% |  | n/a | no target · QC vendors: 544 rows, 98.5% filled |
| P09 | 369 | 82.1% | 82.1% |  | 95% | ❌ 13 pts to go · QC vendors: 156 rows, 99.4% filled |
| P10 | 2590 | 22.9% | 22.9% |  | n/a | no target · QC vendors: 444 rows, 94.6% filled |
| P11 | 498 | 29.5% | 29.5% |  | n/a | no target · QC vendors: 79 rows, 98.7% filled |
| P12 | 21 | 76.2% | 76.2% |  | n/a | no target · QC vendors: 4 rows, 100.0% filled |
| P13 | 50788 | 0.0% | 0.0% |  | n/a | no target |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 60.0% | 60.0% |  | n/a | no target · vendors with a registry record: 12 rows, 100.0% filled |
| P01T | 92 | 63.0% | 63.0% |  | n/a | no target · vendors with a registry record: 58 rows, 100.0% filled |
| P01_GOLD | 582 | 85.7% | 85.7% |  | 100% | ❌ 14 pts to go · vendors with a registry record: 499 rows, 100.0% filled |
| P02 | 369 | 88.3% | 88.3% |  | 100% | ❌ 12 pts to go · vendors with a registry record: 326 rows, 100.0% filled |
| P03 | 225 | 87.6% | 87.6% |  | 100% | ❌ 12 pts to go · vendors with a registry record: 197 rows, 100.0% filled |
| P04 | 1615 | 81.4% | 81.4% |  | 100% | ❌ 19 pts to go · vendors with a registry record: 1314 rows, 100.0% filled |
| P05 | 379 | 61.2% | 61.2% |  | n/a | no target · vendors with a registry record: 232 rows, 100.0% filled |
| P06M | 167 | 21.0% | 21.0% |  | n/a | no target · vendors with a registry record: 35 rows, 100.0% filled |
| P06T | 2435 | 78.2% | 78.2% |  | n/a | no target · vendors with a registry record: 1905 rows, 100.0% filled |
| P06 | 163 | 57.7% | 57.7% |  | n/a | no target · vendors with a registry record: 94 rows, 100.0% filled |
| P07 | 249 | 53.8% | 53.8% |  | n/a | no target · vendors with a registry record: 134 rows, 100.0% filled |
| P08 | 3037 | 54.3% | 54.3% |  | n/a | no target · vendors with a registry record: 1650 rows, 100.0% filled |
| P09 | 369 | 92.7% | 92.7% |  | n/a | no target · vendors with a registry record: 342 rows, 100.0% filled |
| P10 | 2590 | 43.7% | 43.7% |  | n/a | no target · vendors with a registry record: 1132 rows, 100.0% filled |
| P11 | 498 | 59.0% | 59.0% |  | n/a | no target · vendors with a registry record: 294 rows, 100.0% filled |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target · vendors with a registry record: 21 rows, 100.0% filled |
| P13 | 50788 | 0.0% | 0.0% |  | n/a | no target |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 95.0% | 95.0% |  | 90% | ✅ met |
| P01T | 92 | 95.7% | 95.7% |  | 90% | ✅ met |
| P01_GOLD | 582 | 85.9% | 85.9% |  | 95% | 🟡 9 pts to go |
| P02 | 369 | 91.6% | 91.6% |  | 95% | 🟡 3 pts to go |
| P03 | 225 | 81.8% | 81.8% |  | 85% | 🟡 3 pts to go |
| P04 | 1615 | 79.1% | 79.1% |  | 90% | ❌ 11 pts to go |
| P05 | 379 | 76.0% | 76.0% |  | 75% | ✅ met |
| P06M | 167 | 88.6% | 88.6% |  | n/a | no target |
| P06T | 2435 | 64.5% | 64.5% |  | n/a | no target |
| P06 | 163 | 56.4% | 56.4% |  | 80% | ❌ 24 pts to go |
| P07 | 249 | 52.6% | 52.6% |  | 80% | ❌ 27 pts to go |
| P08 | 3037 | 36.6% | 36.6% |  | 75% | ❌ 38 pts to go |
| P09 | 369 | 82.7% | 82.7% |  | 95% | ❌ 12 pts to go |
| P10 | 2590 | 32.3% | 32.3% |  | 70% | ❌ 38 pts to go |
| P11 | 498 | 28.1% | 28.1% |  | 65% | ❌ 37 pts to go |
| P12 | 21 | 71.4% | 71.4% |  | 80% | 🟡 9 pts to go |
| P13 | 50788 | 43.4% | 43.4% |  | 60% | ❌ 17 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 40.0% | 40.0% |  | 50% | 🟡 10 pts to go |
| P01T | 92 | 20.7% | 20.7% |  | n/a | no target |
| P01_GOLD | 582 | 20.1% | 20.1% |  | 40% | ❌ 20 pts to go |
| P02 | 369 | 20.3% | 20.3% |  | 40% | ❌ 20 pts to go |
| P03 | 225 | 26.7% | 26.7% |  | 40% | ❌ 13 pts to go |
| P04 | 1615 | 27.4% | 27.4% |  | 40% | ❌ 13 pts to go |
| P05 | 379 | 23.2% | 23.2% |  | 25% | 🟡 2 pts to go |
| P06M | 167 | 24.6% | 24.6% |  | n/a | no target |
| P06T | 2435 | 30.8% | 30.8% |  | n/a | no target |
| P06 | 163 | 9.8% | 9.8% |  | 35% | ❌ 25 pts to go |
| P07 | 249 | 10.0% | 10.0% |  | 35% | ❌ 25 pts to go |
| P08 | 3037 | 10.5% | 10.5% |  | 35% | ❌ 24 pts to go |
| P09 | 369 | 17.9% | 17.9% |  | n/a | no target |
| P10 | 2590 | 8.9% | 8.9% |  | 30% | ❌ 21 pts to go |
| P11 | 498 | 9.6% | 9.6% |  | n/a | no target |
| P12 | 21 | 19.0% | 19.0% |  | n/a | no target |
| P13 | 50788 | 19.5% | 19.5% |  | 30% | ❌ 10 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 95.0% | 95.0% |  | 100% | 🟡 5 pts to go |
| P01T | 92 | 93.5% | 93.5% |  | 100% | 🟡 6 pts to go |
| P01_GOLD | 582 | 89.3% | 89.3% |  | 100% | ❌ 11 pts to go |
| P02 | 369 | 95.7% | 95.7% |  | 100% | 🟡 4 pts to go |
| P03 | 225 | 94.2% | 94.2% |  | 100% | 🟡 6 pts to go |
| P04 | 1615 | 91.1% | 91.1% |  | 100% | 🟡 9 pts to go |
| P05 | 379 | 84.7% | 84.7% |  | 100% | ❌ 15 pts to go |
| P06M | 167 | 71.3% | 71.3% |  | n/a | no target |
| P06T | 2435 | 80.0% | 80.0% |  | n/a | no target |
| P06 | 163 | 67.5% | 67.5% |  | 95% | ❌ 28 pts to go |
| P07 | 249 | 69.9% | 69.9% |  | 95% | ❌ 25 pts to go |
| P08 | 3037 | 65.4% | 65.4% |  | 95% | ❌ 30 pts to go |
| P09 | 369 | 98.4% | 98.4% |  | 100% | 🟡 2 pts to go |
| P10 | 2590 | 64.2% | 64.2% |  | 95% | ❌ 31 pts to go |
| P11 | 498 | 37.8% | 37.8% |  | 80% | ❌ 42 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50788 | 75.1% | 75.1% |  | 95% | ❌ 20 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 90.0% | 90.0% |  | n/a | no target |
| P01T | 92 | 80.4% | 80.4% |  | n/a | no target |
| P01_GOLD | 582 | 69.6% | 69.6% |  | 90% | ❌ 20 pts to go |
| P02 | 369 | 78.3% | 78.3% |  | 95% | ❌ 17 pts to go |
| P03 | 225 | 74.7% | 74.7% |  | 95% | ❌ 20 pts to go |
| P04 | 1615 | 85.4% | 85.4% |  | 95% | 🟡 10 pts to go |
| P05 | 379 | 74.9% | 74.9% |  | 90% | ❌ 15 pts to go |
| P06M | 167 | 83.8% | 83.8% |  | n/a | no target |
| P06T | 2435 | 77.2% | 77.2% |  | n/a | no target |
| P06 | 163 | 64.4% | 64.4% |  | 95% | ❌ 31 pts to go |
| P07 | 249 | 65.1% | 65.1% |  | 90% | ❌ 25 pts to go |
| P08 | 3037 | 74.5% | 74.5% |  | 95% | ❌ 20 pts to go |
| P09 | 369 | 89.7% | 89.7% |  | 100% | ❌ 10 pts to go |
| P10 | 2590 | 71.4% | 71.4% |  | 95% | ❌ 24 pts to go |
| P11 | 498 | 27.5% | 27.5% |  | 75% | ❌ 48 pts to go |
| P12 | 21 | 85.7% | 85.7% |  | n/a | no target |
| P13 | 50788 | 78.3% | 78.3% |  | 95% | ❌ 17 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 80.0% | 80.0% |  | n/a | no target |
| P01T | 92 | 91.3% | 91.3% |  | 95% | 🟡 4 pts to go |
| P01_GOLD | 582 | 68.7% | 68.7% |  | 90% | ❌ 21 pts to go |
| P02 | 369 | 77.8% | 77.8% |  | 95% | ❌ 17 pts to go |
| P03 | 225 | 70.2% | 70.2% |  | 95% | ❌ 25 pts to go |
| P04 | 1615 | 63.3% | 63.3% |  | 90% | ❌ 27 pts to go |
| P05 | 379 | 78.6% | 78.6% |  | 95% | ❌ 16 pts to go |
| P06M | 167 | 84.4% | 84.4% |  | n/a | no target |
| P06T | 2435 | 93.6% | 93.6% |  | n/a | no target |
| P06 | 163 | 88.3% | 88.3% |  | 100% | ❌ 12 pts to go |
| P07 | 249 | 86.7% | 86.7% |  | 100% | ❌ 13 pts to go |
| P08 | 3037 | 90.2% | 90.2% |  | 100% | 🟡 10 pts to go |
| P09 | 369 | 53.1% | 53.1% |  | n/a | no target |
| P10 | 2590 | 89.3% | 89.3% |  | 100% | ❌ 11 pts to go |
| P11 | 498 | 31.7% | 31.7% |  | 80% | ❌ 48 pts to go |
| P12 | 21 | 61.9% | 61.9% |  | n/a | no target |
| P13 | 50788 | 81.4% | 81.4% |  | 95% | ❌ 14 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 15.0% | 15.0% |  | n/a | no target |
| P01T | 92 | 16.3% | 16.3% |  | n/a | no target |
| P01_GOLD | 582 | 7.4% | 7.4% |  | 25% | ❌ 18 pts to go |
| P02 | 369 | 20.3% | 20.3% |  | 40% | ❌ 20 pts to go |
| P03 | 225 | 2.7% | 2.7% |  | 20% | ❌ 17 pts to go |
| P04 | 1615 | 1.1% | 1.1% |  | 20% | ❌ 19 pts to go |
| P05 | 379 | 1.1% | 1.1% |  | 15% | ❌ 14 pts to go |
| P06M | 167 | 1.8% | 1.8% |  | n/a | no target |
| P06T | 2435 | 0.1% | 0.1% |  | n/a | no target |
| P06 | 163 | 2.5% | 2.5% |  | n/a | no target |
| P07 | 249 | 4.4% | 4.4% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 5.4% | 5.4% |  | n/a | no target |
| P10 | 2590 | 0.3% | 0.3% |  | n/a | no target |
| P11 | 498 | 0.6% | 0.6% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50788 | 0.2% | 0.2% |  | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 40.0% | 40.0% |  | n/a | no target |
| P01T | 92 | 38.0% | 38.0% |  | 70% | ❌ 32 pts to go |
| P01_GOLD | 582 | 45.0% | 45.0% |  | 80% | ❌ 35 pts to go |
| P02 | 369 | 66.4% | 66.4% |  | 90% | ❌ 24 pts to go |
| P03 | 225 | 20.0% | 20.0% |  | 60% | ❌ 40 pts to go |
| P04 | 1615 | 49.2% | 49.2% |  | 85% | ❌ 36 pts to go |
| P05 | 379 | 12.7% | 12.7% |  | 50% | ❌ 37 pts to go |
| P06M | 167 | 6.0% | 6.0% |  | n/a | no target |
| P06T | 2435 | 2.3% | 2.3% |  | n/a | no target |
| P06 | 163 | 18.4% | 18.4% |  | n/a | no target |
| P07 | 249 | 19.3% | 19.3% |  | n/a | no target |
| P08 | 3037 | 0.5% | 0.5% |  | n/a | no target |
| P09 | 369 | 81.0% | 81.0% |  | 95% | ❌ 14 pts to go |
| P10 | 2590 | 3.1% | 3.1% |  | n/a | no target |
| P11 | 498 | 33.3% | 33.3% |  | n/a | no target |
| P12 | 21 | 33.3% | 33.3% |  | n/a | no target |
| P13 | 50788 | 0.9% | 0.9% |  | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 5.0% | 5.0% |  | n/a | no target |
| P01T | 92 | 18.5% | 18.5% |  | n/a | no target |
| P01_GOLD | 582 | 34.0% | 34.0% |  | 70% | ❌ 36 pts to go |
| P02 | 369 | 39.8% | 39.8% |  | 75% | ❌ 35 pts to go |
| P03 | 225 | 20.0% | 20.0% |  | 55% | ❌ 35 pts to go |
| P04 | 1615 | 48.5% | 48.5% |  | 75% | ❌ 26 pts to go |
| P05 | 379 | 10.8% | 10.8% |  | 50% | ❌ 39 pts to go |
| P06M | 167 | 1.8% | 1.8% |  | n/a | no target |
| P06T | 2435 | 1.1% | 1.1% |  | n/a | no target |
| P06 | 163 | 10.4% | 10.4% |  | n/a | no target |
| P07 | 249 | 10.4% | 10.4% |  | n/a | no target |
| P08 | 3037 | 0.5% | 0.5% |  | n/a | no target |
| P09 | 369 | 77.2% | 77.2% |  | 95% | ❌ 18 pts to go |
| P10 | 2590 | 1.8% | 1.8% |  | n/a | no target |
| P11 | 498 | 32.7% | 32.7% |  | n/a | no target |
| P12 | 21 | 19.0% | 19.0% |  | n/a | no target |
| P13 | 50788 | 0.6% | 0.6% |  | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 15.0% | 15.0% |  | n/a | no target |
| P01T | 92 | 12.0% | 12.0% |  | n/a | no target |
| P01_GOLD | 582 | 51.9% | 51.9% |  | 80% | ❌ 28 pts to go |
| P02 | 369 | 41.5% | 41.5% |  | 75% | ❌ 34 pts to go |
| P03 | 225 | 28.4% | 28.4% |  | 70% | ❌ 42 pts to go |
| P04 | 1615 | 35.4% | 35.4% |  | 70% | ❌ 35 pts to go |
| P05 | 379 | 12.4% | 12.4% |  | 50% | ❌ 38 pts to go |
| P06M | 167 | 0.6% | 0.6% |  | n/a | no target |
| P06T | 2435 | 0.6% | 0.6% |  | n/a | no target |
| P06 | 163 | 16.0% | 16.0% |  | n/a | no target |
| P07 | 249 | 1.6% | 1.6% |  | n/a | no target |
| P08 | 3037 | 0.4% | 0.4% |  | n/a | no target |
| P09 | 369 | 40.9% | 40.9% |  | 80% | ❌ 39 pts to go |
| P10 | 2590 | 1.0% | 1.0% |  | n/a | no target |
| P11 | 498 | 17.1% | 17.1% |  | n/a | no target |
| P12 | 21 | 33.3% | 33.3% |  | n/a | no target |
| P13 | 50788 | 0.3% | 0.3% |  | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 30.0% | 30.0% |  | n/a | no target |
| P01T | 92 | 23.9% | 23.9% |  | 60% | ❌ 36 pts to go |
| P01_GOLD | 582 | 33.5% | 33.5% |  | 70% | ❌ 36 pts to go |
| P02 | 369 | 8.7% | 8.7% |  | 50% | ❌ 41 pts to go |
| P03 | 225 | 15.1% | 15.1% |  | 55% | ❌ 40 pts to go |
| P04 | 1615 | 1.5% | 1.5% |  | 40% | ❌ 38 pts to go |
| P05 | 379 | 5.8% | 5.8% |  | 40% | ❌ 34 pts to go |
| P06M | 167 | 0.6% | 0.6% |  | n/a | no target |
| P06T | 2435 | 0.6% | 0.6% |  | n/a | no target |
| P06 | 163 | 14.1% | 14.1% |  | n/a | no target |
| P07 | 249 | 3.6% | 3.6% |  | n/a | no target |
| P08 | 3037 | 0.5% | 0.5% |  | n/a | no target |
| P09 | 369 | 2.7% | 2.7% |  | n/a | no target |
| P10 | 2590 | 0.5% | 0.5% |  | n/a | no target |
| P11 | 498 | 0.6% | 0.6% |  | n/a | no target |
| P12 | 21 | 9.5% | 9.5% |  | n/a | no target |
| P13 | 50788 | 0.2% | 0.2% |  | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 35.0% | 35.0% |  | n/a | no target |
| P01T | 92 | 43.5% | 43.5% |  | 65% | ❌ 22 pts to go |
| P01_GOLD | 582 | 47.9% | 47.9% |  | 70% | ❌ 22 pts to go |
| P02 | 369 | 6.5% | 6.5% |  | 50% | ❌ 44 pts to go |
| P03 | 225 | 26.2% | 26.2% |  | 60% | ❌ 34 pts to go |
| P04 | 1615 | 1.1% | 1.1% |  | 40% | ❌ 39 pts to go |
| P05 | 379 | 10.8% | 10.8% |  | 45% | ❌ 34 pts to go |
| P06M | 167 | 1.2% | 1.2% |  | n/a | no target |
| P06T | 2435 | 0.3% | 0.3% |  | n/a | no target |
| P06 | 163 | 35.0% | 35.0% |  | n/a | no target |
| P07 | 249 | 6.8% | 6.8% |  | n/a | no target |
| P08 | 3037 | 0.3% | 0.3% |  | n/a | no target |
| P09 | 369 | 3.8% | 3.8% |  | n/a | no target |
| P10 | 2590 | 0.8% | 0.8% |  | n/a | no target |
| P11 | 498 | 2.2% | 2.2% |  | n/a | no target |
| P12 | 21 | 4.8% | 4.8% |  | n/a | no target |
| P13 | 50788 | 0.1% | 0.1% |  | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 10.0% | 10.0% |  | n/a | no target |
| P01T | 92 | 29.3% | 29.3% |  | n/a | no target |
| P01_GOLD | 582 | 30.8% | 30.8% |  | 50% | ❌ 19 pts to go |
| P02 | 369 | 14.4% | 14.4% |  | n/a | no target |
| P03 | 225 | 46.7% | 46.7% |  | 60% | ❌ 13 pts to go |
| P04 | 1615 | 6.6% | 6.6% |  | n/a | no target |
| P05 | 379 | 10.0% | 10.0% |  | n/a | no target |
| P06M | 167 | 2.4% | 2.4% |  | n/a | no target |
| P06T | 2435 | 0.9% | 0.9% |  | n/a | no target |
| P06 | 163 | 17.8% | 17.8% |  | n/a | no target |
| P07 | 249 | 11.2% | 11.2% |  | n/a | no target |
| P08 | 3037 | 0.5% | 0.5% |  | n/a | no target |
| P09 | 369 | 6.5% | 6.5% |  | n/a | no target |
| P10 | 2590 | 1.4% | 1.4% |  | n/a | no target |
| P11 | 498 | 2.2% | 2.2% |  | n/a | no target |
| P12 | 21 | 4.8% | 4.8% |  | n/a | no target |
| P13 | 50788 | 0.4% | 0.4% |  | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 15.0% | 15.0% |  | 15% | ✅ met |
| P01T | 92 | 9.8% | 9.8% |  | 15% | 🟡 5 pts to go |
| P01_GOLD | 582 | 18.7% | 18.7% |  | 40% | ❌ 21 pts to go |
| P02 | 369 | 7.3% | 7.3% |  | 25% | ❌ 18 pts to go |
| P03 | 225 | 9.3% | 9.3% |  | 25% | ❌ 16 pts to go |
| P04 | 1615 | 1.0% | 1.0% |  | 15% | ❌ 14 pts to go |
| P05 | 379 | 4.2% | 4.2% |  | 15% | ❌ 11 pts to go |
| P06M | 167 | 2.4% | 2.4% |  | 15% | ❌ 13 pts to go |
| P06T | 2435 | 0.7% | 0.7% |  | 15% | ❌ 14 pts to go |
| P06 | 163 | 5.5% | 5.5% |  | 15% | 🟡 10 pts to go |
| P07 | 249 | 2.4% | 2.4% |  | 15% | ❌ 13 pts to go |
| P08 | 3037 | 0.8% | 0.8% |  | 15% | ❌ 14 pts to go |
| P09 | 369 | 0.3% | 0.3% |  | 15% | ❌ 15 pts to go |
| P10 | 2590 | 0.9% | 0.9% |  | 15% | ❌ 14 pts to go |
| P11 | 498 | 0.6% | 0.6% |  | 15% | ❌ 14 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P13 | 50788 | 0.8% | 0.8% |  | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P01T | 92 | 15.2% | 15.2% |  | 25% | 🟡 10 pts to go |
| P01_GOLD | 582 | 12.2% | 12.2% |  | 25% | ❌ 13 pts to go |
| P02 | 369 | 5.1% | 5.1% |  | 15% | 🟡 10 pts to go |
| P03 | 225 | 4.0% | 4.0% |  | 15% | ❌ 11 pts to go |
| P04 | 1615 | 0.6% | 0.6% |  | 15% | ❌ 14 pts to go |
| P05 | 379 | 6.9% | 6.9% |  | 15% | 🟡 8 pts to go |
| P06M | 167 | 0.6% | 0.6% |  | 15% | ❌ 14 pts to go |
| P06T | 2435 | 0.5% | 0.5% |  | 15% | ❌ 14 pts to go |
| P06 | 163 | 3.7% | 3.7% |  | 15% | ❌ 11 pts to go |
| P07 | 249 | 2.0% | 2.0% |  | 15% | ❌ 13 pts to go |
| P08 | 3037 | 0.2% | 0.2% |  | 15% | ❌ 15 pts to go |
| P09 | 369 | 0.3% | 0.3% |  | 15% | ❌ 15 pts to go |
| P10 | 2590 | 0.2% | 0.2% |  | 15% | ❌ 15 pts to go |
| P11 | 498 | 1.4% | 1.4% |  | 15% | ❌ 14 pts to go |
| P12 | 21 | 9.5% | 9.5% |  | 15% | 🟡 6 pts to go |
| P13 | 50788 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P01T | 92 | 5.4% | 5.4% |  | 20% | ❌ 15 pts to go |
| P01_GOLD | 582 | 2.1% | 2.1% |  | 20% | ❌ 18 pts to go |
| P02 | 369 | 0.3% | 0.3% |  | 20% | ❌ 20 pts to go |
| P03 | 225 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P04 | 1615 | 0.1% | 0.1% |  | 20% | ❌ 20 pts to go |
| P05 | 379 | 0.8% | 0.8% |  | 20% | ❌ 19 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P06T | 2435 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P06 | 163 | 1.8% | 1.8% |  | 20% | ❌ 18 pts to go |
| P07 | 249 | 0.4% | 0.4% |  | 20% | ❌ 20 pts to go |
| P08 | 3037 | 0.1% | 0.1% |  | 20% | ❌ 20 pts to go |
| P09 | 369 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P10 | 2590 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P11 | 498 | 0.2% | 0.2% |  | 20% | ❌ 20 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P13 | 50788 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P01T | 92 | 2.2% | 2.2% |  | 15% | ❌ 13 pts to go |
| P01_GOLD | 582 | 1.7% | 1.7% |  | 15% | ❌ 13 pts to go |
| P02 | 369 | 1.1% | 1.1% |  | 15% | ❌ 14 pts to go |
| P03 | 225 | 3.6% | 3.6% |  | 15% | ❌ 11 pts to go |
| P04 | 1615 | 0.4% | 0.4% |  | 15% | ❌ 15 pts to go |
| P05 | 379 | 0.3% | 0.3% |  | 15% | ❌ 15 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P06T | 2435 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |
| P06 | 163 | 1.2% | 1.2% |  | 15% | ❌ 14 pts to go |
| P07 | 249 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P08 | 3037 | 0.2% | 0.2% |  | 15% | ❌ 15 pts to go |
| P09 | 369 | 0.3% | 0.3% |  | 15% | ❌ 15 pts to go |
| P10 | 2590 | 0.2% | 0.2% |  | 15% | ❌ 15 pts to go |
| P11 | 498 | 0.2% | 0.2% |  | 15% | ❌ 15 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P13 | 50788 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 10.0% | 10.0% |  | 20% | 🟡 10 pts to go |
| P01T | 92 | 23.9% | 23.9% |  | 40% | ❌ 16 pts to go |
| P01_GOLD | 582 | 15.1% | 15.1% |  | 40% | ❌ 25 pts to go |
| P02 | 369 | 5.7% | 5.7% |  | 20% | ❌ 14 pts to go |
| P03 | 225 | 11.6% | 11.6% |  | 35% | ❌ 23 pts to go |
| P04 | 1615 | 4.5% | 4.5% |  | 20% | ❌ 16 pts to go |
| P05 | 379 | 5.5% | 5.5% |  | 20% | ❌ 14 pts to go |
| P06M | 167 | 2.4% | 2.4% |  | 20% | ❌ 18 pts to go |
| P06T | 2435 | 1.2% | 1.2% |  | 20% | ❌ 19 pts to go |
| P06 | 163 | 17.8% | 17.8% |  | 20% | 🟡 2 pts to go |
| P07 | 249 | 9.2% | 9.2% |  | 20% | ❌ 11 pts to go |
| P08 | 3037 | 0.9% | 0.9% |  | 20% | ❌ 19 pts to go |
| P09 | 369 | 9.5% | 9.5% |  | 20% | ❌ 10 pts to go |
| P10 | 2590 | 1.4% | 1.4% |  | 20% | ❌ 19 pts to go |
| P11 | 498 | 2.2% | 2.2% |  | 20% | ❌ 18 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P13 | 50788 | 0.4% | 0.4% |  | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 1.1% | 1.1% |  | n/a | no target |
| P01_GOLD | 582 | 68.4% | 68.4% |  | 95% | ❌ 27 pts to go |
| P02 | 369 | 74.3% | 74.3% |  | 95% | ❌ 21 pts to go |
| P03 | 225 | 63.6% | 63.6% |  | 90% | ❌ 26 pts to go |
| P04 | 1615 | 57.0% | 57.0% |  | 85% | ❌ 28 pts to go |
| P05 | 379 | 34.6% | 34.6% |  | 75% | ❌ 40 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2435 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 163 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 249 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 90.8% | 90.8% |  | 100% | 🟡 9 pts to go |
| P10 | 2590 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 498 | 21.9% | 21.9% |  | 60% | ❌ 38 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50788 | 0.0% | 0.0% |  | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 582 | 72.5% | 72.5% |  | 100% | ❌ 28 pts to go |
| P02 | 369 | 77.8% | 77.8% |  | 100% | ❌ 22 pts to go |
| P03 | 225 | 70.7% | 70.7% |  | n/a | no target |
| P04 | 1615 | 58.5% | 58.5% |  | 95% | ❌ 36 pts to go |
| P05 | 379 | 30.9% | 30.9% |  | 80% | ❌ 49 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2435 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 163 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 249 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 93.5% | 93.5% |  | 100% | 🟡 6 pts to go |
| P10 | 2590 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 498 | 23.3% | 23.3% |  | n/a | no target |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50788 | 0.0% | 0.0% |  | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 1.1% | 1.1% |  | n/a | no target |
| P01_GOLD | 582 | 52.4% | 52.4% |  | 85% | ❌ 33 pts to go |
| P02 | 369 | 65.3% | 65.3% |  | 90% | ❌ 25 pts to go |
| P03 | 225 | 52.0% | 52.0% |  | 85% | ❌ 33 pts to go |
| P04 | 1615 | 63.5% | 63.5% |  | 90% | ❌ 26 pts to go |
| P05 | 379 | 35.4% | 35.4% |  | 75% | ❌ 40 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2435 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 163 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 249 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 85.4% | 85.4% |  | 95% | 🟡 10 pts to go |
| P10 | 2590 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 498 | 21.3% | 21.3% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50788 | 0.0% | 0.0% |  | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 1.1% | 1.1% |  | n/a | no target |
| P01_GOLD | 582 | 52.9% | 52.9% |  | 85% | ❌ 32 pts to go |
| P02 | 369 | 60.7% | 60.7% |  | 90% | ❌ 29 pts to go |
| P03 | 225 | 52.4% | 52.4% |  | 85% | ❌ 33 pts to go |
| P04 | 1615 | 53.1% | 53.1% |  | 90% | ❌ 37 pts to go |
| P05 | 379 | 42.2% | 42.2% |  | 75% | ❌ 33 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2435 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 163 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 249 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 0.3% | 0.3% |  | 95% | ❌ 95 pts to go |
| P10 | 2590 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 498 | 17.5% | 17.5% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50788 | 0.0% | 0.0% |  | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 77.2% | 77.2% |  | n/a | no target |
| P01_GOLD | 582 | 82.1% | 82.1% |  | 100% | ❌ 18 pts to go |
| P02 | 369 | 80.5% | 80.5% |  | 100% | ❌ 20 pts to go |
| P03 | 225 | 86.2% | 86.2% |  | n/a | no target |
| P04 | 1615 | 71.6% | 71.6% |  | 95% | ❌ 23 pts to go |
| P05 | 379 | 75.2% | 75.2% |  | 95% | ❌ 20 pts to go |
| P06M | 167 | 0.6% | 0.6% |  | n/a | no target |
| P06T | 2435 | 83.3% | 83.3% |  | n/a | no target |
| P06 | 163 | 75.5% | 75.5% |  | n/a | no target |
| P07 | 249 | 76.7% | 76.7% |  | n/a | no target |
| P08 | 3037 | 84.9% | 85.0% |  | n/a | no target |
| P09 | 369 | 98.9% | 98.9% |  | 100% | 🟡 1 pts to go |
| P10 | 2590 | 98.4% | 98.4% |  | n/a | no target |
| P11 | 498 | 89.6% | 89.6% |  | n/a | no target |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50788 | 0.0% | 0.0% |  | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 3.3% | 3.3% |  | n/a | no target |
| P01_GOLD | 582 | 69.6% | 69.6% |  | 100% | ❌ 30 pts to go |
| P02 | 369 | 71.5% | 71.8% |  | 100% | ❌ 28 pts to go |
| P03 | 225 | 68.0% | 68.0% |  | n/a | no target |
| P04 | 1615 | 57.9% | 57.9% |  | 95% | ❌ 37 pts to go |
| P05 | 379 | 14.0% | 14.0% |  | 70% | ❌ 56 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2435 | 0.2% | 0.2% |  | n/a | no target |
| P06 | 163 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 249 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 95.7% | 95.7% |  | 100% | 🟡 4 pts to go |
| P10 | 2590 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 498 | 24.1% | 24.1% |  | n/a | no target |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50788 | 0.0% | 0.0% |  | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 1.1% | 1.1% |  | n/a | no target · rows from a source that publishes bids: 3 rows, 33.3% filled |
| P01_GOLD | 582 | 18.4% | 18.4% |  | 60% | ❌ 42 pts to go · rows from a source that publishes bids: 356 rows, 30.1% filled |
| P02 | 369 | 14.1% | 14.1% |  | n/a | no target · rows from a source that publishes bids: 268 rows, 19.4% filled |
| P03 | 225 | 15.1% | 15.1% |  | n/a | no target · rows from a source that publishes bids: 139 rows, 24.5% filled |
| P04 | 1615 | 3.5% | 3.5% |  | n/a | no target · rows from a source that publishes bids: 900 rows, 6.3% filled |
| P05 | 379 | 3.4% | 3.4% |  | n/a | no target · rows from a source that publishes bids: 48 rows, 27.1% filled |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2435 | 0.1% | 0.1% |  | n/a | no target · rows from a source that publishes bids: 4 rows, 50.0% filled |
| P06 | 163 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 249 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 3.3% | 3.3% |  | n/a | no target · rows from a source that publishes bids: 355 rows, 3.4% filled |
| P10 | 2590 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 498 | 3.0% | 3.0% |  | n/a | no target · rows from a source that publishes bids: 111 rows, 13.5% filled |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target · rows from a source that publishes bids: 21 rows, 0.0% filled |
| P13 | 50788 | 0.0% | 0.0% |  | n/a | no target |

## 6. history

### `average_contract_duration_days`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 100.0% |  | n/a | no target |
| P01T | 92 | 0.0% | 96.7% |  | n/a | no target |
| P01_GOLD | 582 | 40.5% | 67.7% |  | 90% | ❌ 50 pts to go |
| P02 | 369 | 55.6% | 80.5% |  | 90% | ❌ 34 pts to go |
| P03 | 225 | 39.1% | 64.4% |  | 90% | ❌ 51 pts to go |
| P04 | 1615 | 42.6% | 82.9% |  | 90% | ❌ 47 pts to go |
| P05 | 379 | 0.0% | 82.1% |  | 90% | ❌ 90 pts to go |
| P06M | 167 | 0.0% | 100.0% |  | n/a | no target |
| P06T | 2435 | 0.0% | 99.8% |  | n/a | no target |
| P06 | 163 | 0.0% | 100.0% |  | n/a | no target |
| P07 | 249 | 0.0% | 100.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 100.0% |  | n/a | no target |
| P09 | 369 | 0.0% | 1.4% |  | 90% | ❌ 90 pts to go |
| P10 | 2590 | 0.0% | 100.0% |  | n/a | no target |
| P11 | 498 | 14.7% | 88.4% |  | n/a | no target |
| P12 | 21 | 0.0% | 100.0% |  | n/a | no target |
| P13 | 50788 | 0.0% | 100.0% |  | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 100.0% |  | n/a | no target |
| P01T | 92 | 0.0% | 96.7% |  | n/a | no target |
| P01_GOLD | 582 | 27.1% | 54.3% |  | 90% | ❌ 63 pts to go |
| P02 | 369 | 58.8% | 83.7% |  | n/a | no target |
| P03 | 225 | 28.0% | 53.3% |  | n/a | no target |
| P04 | 1615 | 49.5% | 89.8% |  | n/a | no target |
| P05 | 379 | 0.3% | 82.3% |  | n/a | no target |
| P06M | 167 | 0.0% | 100.0% |  | n/a | no target |
| P06T | 2435 | 0.0% | 99.8% |  | n/a | no target |
| P06 | 163 | 0.0% | 100.0% |  | n/a | no target |
| P07 | 249 | 0.0% | 100.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 100.0% |  | n/a | no target |
| P09 | 369 | 45.8% | 47.2% |  | n/a | no target |
| P10 | 2590 | 0.0% | 100.0% |  | n/a | no target |
| P11 | 498 | 13.9% | 87.6% |  | n/a | no target |
| P12 | 21 | 0.0% | 100.0% |  | n/a | no target |
| P13 | 50788 | 0.0% | 100.0% |  | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 100.0% |  | n/a | no target |
| P01T | 92 | 2.2% | 98.9% |  | n/a | no target |
| P01_GOLD | 582 | 54.1% | 81.3% |  | 95% | ❌ 41 pts to go |
| P02 | 369 | 66.1% | 91.1% |  | n/a | no target |
| P03 | 225 | 57.8% | 83.1% |  | n/a | no target |
| P04 | 1615 | 50.2% | 90.5% |  | n/a | no target |
| P05 | 379 | 4.7% | 86.8% |  | n/a | no target |
| P06M | 167 | 0.0% | 100.0% |  | n/a | no target |
| P06T | 2435 | 0.0% | 99.8% |  | n/a | no target |
| P06 | 163 | 0.0% | 100.0% |  | n/a | no target |
| P07 | 249 | 0.0% | 100.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 100.0% |  | n/a | no target |
| P09 | 369 | 69.1% | 70.5% |  | n/a | no target |
| P10 | 2590 | 0.0% | 100.0% |  | n/a | no target |
| P11 | 498 | 14.3% | 88.0% |  | n/a | no target |
| P12 | 21 | 0.0% | 100.0% |  | n/a | no target |
| P13 | 50788 | 0.0% | 100.0% |  | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01T | 92 | 98.9% | 98.9% |  | 100% | 🟡 1 pts to go |
| P01_GOLD | 582 | 99.8% | 99.8% |  | 100% | 🟡 0 pts to go |
| P02 | 369 | 100.0% | 100.0% |  | 100% | ✅ met |
| P03 | 225 | 99.6% | 99.6% |  | 100% | 🟡 0 pts to go |
| P04 | 1615 | 100.0% | 100.0% |  | 100% | ✅ met |
| P05 | 379 | 99.7% | 99.7% |  | 100% | 🟡 0 pts to go |
| P06M | 167 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06T | 2435 | 99.8% | 99.8% |  | 100% | 🟡 0 pts to go |
| P06 | 163 | 98.2% | 98.2% |  | 100% | 🟡 2 pts to go |
| P07 | 249 | 98.4% | 98.4% |  | 100% | 🟡 2 pts to go |
| P08 | 3037 | 100.0% | 100.0% |  | 100% | ✅ met |
| P09 | 369 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2590 | 99.9% | 99.9% |  | 100% | 🟡 0 pts to go |
| P11 | 498 | 99.8% | 99.8% |  | 100% | 🟡 0 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50788 | 100.0% | 100.0% |  | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01T | 92 | 98.9% | 98.9% |  | 100% | 🟡 1 pts to go |
| P01_GOLD | 582 | 99.8% | 99.8% |  | 100% | 🟡 0 pts to go |
| P02 | 369 | 100.0% | 100.0% |  | 100% | ✅ met |
| P03 | 225 | 99.6% | 99.6% |  | 100% | 🟡 0 pts to go |
| P04 | 1615 | 100.0% | 100.0% |  | 100% | ✅ met |
| P05 | 379 | 99.7% | 99.7% |  | 100% | 🟡 0 pts to go |
| P06M | 167 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06T | 2435 | 99.8% | 99.8% |  | 100% | 🟡 0 pts to go |
| P06 | 163 | 98.2% | 98.2% |  | 100% | 🟡 2 pts to go |
| P07 | 249 | 98.4% | 98.4% |  | 100% | 🟡 2 pts to go |
| P08 | 3037 | 100.0% | 100.0% |  | 100% | ✅ met |
| P09 | 369 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2590 | 99.9% | 99.9% |  | 100% | 🟡 0 pts to go |
| P11 | 498 | 99.8% | 99.8% |  | 100% | 🟡 0 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50788 | 100.0% | 100.0% |  | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01T | 92 | 98.9% | 98.9% |  | 100% | 🟡 1 pts to go |
| P01_GOLD | 582 | 99.8% | 99.8% |  | 100% | 🟡 0 pts to go |
| P02 | 369 | 100.0% | 100.0% |  | 100% | ✅ met |
| P03 | 225 | 99.6% | 99.6% |  | 100% | 🟡 0 pts to go |
| P04 | 1615 | 100.0% | 100.0% |  | 100% | ✅ met |
| P05 | 379 | 99.7% | 99.7% |  | 100% | 🟡 0 pts to go |
| P06M | 167 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06T | 2435 | 99.8% | 99.8% |  | 100% | 🟡 0 pts to go |
| P06 | 163 | 98.2% | 98.2% |  | 100% | 🟡 2 pts to go |
| P07 | 249 | 98.4% | 98.4% |  | 100% | 🟡 2 pts to go |
| P08 | 3037 | 100.0% | 100.0% |  | 100% | ✅ met |
| P09 | 369 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2590 | 99.9% | 99.9% |  | 100% | 🟡 0 pts to go |
| P11 | 498 | 99.8% | 99.8% |  | 100% | 🟡 0 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50788 | 100.0% | 100.0% |  | 100% | ✅ met |


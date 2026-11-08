# Coverage vs the downstream team's targets — 2026-11-08

Benchmarks (field × package with a numeric target): **72 of 438 met** (16.4%); 53 within 10 points; 313 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 20, P01T 92, P01_GOLD 581, P02 368, P03 224, P04 1618, P05 379, P06M 167, P06T 2435, P06 163, P07 249, P08 3037, P09 369, P10 2590, P11 498, P12 21, P13 50788

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 25.0% | 7 | reference to quote (PO / contract / vendor id) (20 rows) |
| P01T | 92 | 0.0% | 25.0% | 7 | reference to quote (PO / contract / vendor id) (87 rows) |
| P01_GOLD | 581 | 5.0% | 54.6% | 9 | buyer tax status (304 rows) |
| P02 | 368 | 0.5% | 36.1% | 8 | PO rule (344 rows) |
| P03 | 224 | 0.4% | 20.5% | 8 | payment terms (177 rows) |
| P04 | 1618 | 0.0% | 19.7% | 7 | PO rule (1587 rows) |
| P05 | 379 | 0.3% | 4.2% | 6 | payment terms (342 rows) |
| P06M | 167 | 0.0% | 0.6% | 6 | reference to quote (PO / contract / vendor id) (167 rows) |
| P06T | 2435 | 0.0% | 0.5% | 5 | reference to quote (PO / contract / vendor id) (2433 rows) |
| P06 | 163 | 0.0% | 3.7% | 5 | reference to quote (PO / contract / vendor id) (163 rows) |
| P07 | 249 | 0.0% | 0.0% | 5 | reference to quote (PO / contract / vendor id) (249 rows) |
| P08 | 3037 | 0.0% | 0.0% | 5 | reference to quote (PO / contract / vendor id) (3037 rows) |
| P09 | 369 | 0.0% | 35.0% | 8 | payment terms (351 rows) |
| P10 | 2590 | 0.0% | 0.2% | 4 | reference to quote (PO / contract / vendor id) (2588 rows) |
| P11 | 498 | 0.0% | 6.8% | 4 | PO rule (482 rows) |
| P12 | 21 | 0.0% | 14.3% | 7 | reference to quote (PO / contract / vendor id) (21 rows) |
| P13 | 50788 | 0.0% | 0.0% | 5 | reference to quote (PO / contract / vendor id) (50788 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 20 | 5 | 2 | 13 | 0 | 0 | 73 |
| P01T | 92 | 16 | 43 | 33 | 0 | 0 | 77 |
| P01_GOLD | 581 | 117 | 237 | 227 | 0 | 0 | 78 |
| P02 | 368 | 0 | 46 | 322 | 0 | 0 | 63 |
| P03 | 224 | 0 | 0 | 215 | 9 | 0 | 51 |
| P04 | 1618 | 0 | 0 | 1558 | 60 | 0 | 50 |
| P05 | 379 | 9 | 26 | 325 | 19 | 0 | 48 |
| P06M | 167 | 0 | 1 | 157 | 9 | 0 | 48 |
| P06T | 2435 | 0 | 12 | 2142 | 281 | 0 | 48 |
| P06 | 163 | 13 | 31 | 119 | 0 | 0 | 69 |
| P07 | 249 | 0 | 10 | 214 | 25 | 0 | 51 |
| P08 | 3037 | 0 | 0 | 2251 | 786 | 0 | 40 |
| P09 | 369 | 4 | 9 | 355 | 1 | 0 | 50 |
| P10 | 2590 | 3 | 11 | 1845 | 731 | 0 | 40 |
| P11 | 498 | 0 | 0 | 0 | 0 | 498 | 25 |
| P12 | 21 | 1 | 1 | 19 | 0 | 0 | 53 |
| P13 | 50788 | 5 | 26 | 40872 | 9885 | 0 | 43 |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 15 | 0 | 0 | 0 | 0 | 1 | 1 | 12 | 13 | 6 |
| P01T | 76 | 0 | 0 | 0 | 1 | 4 | 4 | 35 | 43 | 58 |
| P01_GOLD | 464 | 0 | 0 | 0 | 1 | 82 | 40 | 230 | 255 | 260 |
| P02 | 368 | 0 | 368 | 0 | 0 | 31 | 13 | 344 | 331 | 208 |
| P03 | 224 | 0 | 224 | 0 | 1 | 40 | 13 | 164 | 190 | 85 |
| P04 | 1618 | 0 | 1618 | 0 | 1 | 338 | 127 | 1587 | 1568 | 982 |
| P05 | 370 | 0 | 316 | 0 | 3 | 91 | 54 | 322 | 345 | 238 |
| P06M | 167 | 0 | 167 | 0 | 0 | 19 | 47 | 161 | 164 | 94 |
| P06T | 2435 | 0 | 2435 | 0 | 18 | 865 | 485 | 2400 | 2369 | 1913 |
| P06 | 150 | 0 | 0 | 0 | 3 | 71 | 47 | 89 | 124 | 41 |
| P07 | 249 | 0 | 249 | 0 | 5 | 118 | 72 | 208 | 226 | 119 |
| P08 | 3037 | 0 | 3037 | 0 | 19 | 1917 | 1041 | 2994 | 2990 | 2067 |
| P09 | 365 | 0 | 346 | 0 | 2 | 64 | 1 | 348 | 355 | 278 |
| P10 | 2587 | 0 | 2535 | 0 | 21 | 1753 | 915 | 2552 | 2556 | 1866 |
| P11 | 498 | 498 | 461 | 0 | 5 | 358 | 235 | 482 | 487 | 322 |
| P12 | 20 | 0 | 16 | 0 | 0 | 4 | 0 | 19 | 17 | 16 |
| P13 | 50783 | 0 | 50477 | 0 | 460 | 26105 | 12641 | 50711 | 50659 | 40182 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 10150 |
| buyer_address | P13 | 75.0% | 95% | 10143 |
| ap_system_hint | P13 | 0.4% | 20% | 9957 |
| buyer_phone | P13 | 79.0% | 95% | 8123 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 7581 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 7549 |
| buyer_payment_method_preference | P13 | 0.9% | 15% | 7157 |
| buyer_legal_name_as_published | P13 | 48.6% | 60% | 5790 |
| buyer_logo_url | P13 | 83.9% | 95% | 5647 |
| buyer_bn_as_published | P13 | 21.5% | 30% | 4305 |
| buyer_legal_name_as_published | P08 | 36.9% | 75% | 1158 |
| buyer_legal_name_as_published | P10 | 32.3% | 70% | 976 |
| buyer_address | P08 | 65.6% | 95% | 893 |
| vendor_emails | P08 | 47.0% | 75% | 851 |
| buyer_address | P10 | 64.4% | 95% | 794 |
| average_contract_duration_days | P04 | 42.6% | 90% | 768 |
| invoice_reference_hint | P08 | 0.0% | 25% | 760 |
| vendor_emails | P10 | 50.7% | 80% | 758 |
| buyer_bn_as_published | P08 | 10.5% | 35% | 744 |
| vendor_registered_address | P10 | 42.4% | 70% | 714 |
| vendor_logo_url | P04 | 42.7% | 85% | 685 |
| invoice_reference_hint | P10 | 0.1% | 25% | 646 |
| solicitation_or_tender_number | P04 | 10.2% | 50% | 644 |
| buyer_phone | P08 | 74.5% | 95% | 622 |
| po_required_as_published | P04 | 1.9% | 40% | 617 |
| vendor_phone | P08 | 64.8% | 85% | 613 |
| buyer_phone | P10 | 71.4% | 95% | 611 |
| vendor_emails | P04 | 32.4% | 70% | 608 |
| buyer_ap_cycle_published | P08 | 0.1% | 20% | 604 |
| contract_description | P04 | 57.9% | 95% | 601 |
| payment_terms_as_published | P04 | 3.1% | 40% | 598 |
| end_date | P04 | 53.8% | 90% | 586 |
| buyer_vendor_id | P04 | 4.3% | 40% | 578 |
| ap_system_hint | P08 | 1.2% | 20% | 573 |
| records_with_this_vendor | P04 | 59.7% | 95% | 572 |
| currency | P04 | 60.1% | 95% | 566 |
| vendor_neq | P04 | 60.3% | 95% | 563 |
| ap_phone | P04 | 50.3% | 85% | 562 |
| commodity_codes | P04 | 51.2% | 85% | 547 |
| buyer_bn_as_published | P10 | 8.9% | 30% | 547 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | 50% | ❌ 50 pts to go |
| P01T | 92 | 5.4% | 6.5% |  | 50% | ❌ 45 pts to go |
| P01_GOLD | 581 | 77.3% | 85.7% |  | 95% | ❌ 18 pts to go |
| P02 | 368 | 75.8% | 78.5% |  | 95% | ❌ 19 pts to go |
| P03 | 224 | 77.7% | 87.5% |  | 95% | ❌ 17 pts to go |
| P04 | 1618 | 66.2% | 69.2% |  | 90% | ❌ 24 pts to go |
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
| P13 | 50788 | 0.0% | 0.2% |  | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | 10% | 🟡 10 pts to go |
| P01_GOLD | 581 | 6.4% | 6.4% |  | 50% | ❌ 44 pts to go |
| P02 | 368 | 8.2% | 8.2% |  | 50% | ❌ 42 pts to go |
| P03 | 224 | 1.3% | 1.3% |  | 40% | ❌ 39 pts to go |
| P04 | 1618 | 1.2% | 1.2% |  | 30% | ❌ 29 pts to go |
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
| P01_GOLD | 581 | 46.1% | 46.1% |  | 85% | ❌ 39 pts to go |
| P02 | 368 | 62.5% | 62.5% |  | 90% | ❌ 28 pts to go |
| P03 | 224 | 45.5% | 45.5% |  | 85% | ❌ 40 pts to go |
| P04 | 1618 | 61.2% | 61.2% |  | 85% | ❌ 24 pts to go |
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
| P01_GOLD | 581 | 38.7% | 38.7% |  | 80% | ❌ 41 pts to go |
| P02 | 368 | 22.6% | 22.6% |  | 60% | ❌ 37 pts to go |
| P03 | 224 | 41.1% | 41.1% |  | 80% | ❌ 39 pts to go |
| P04 | 1618 | 10.2% | 10.2% |  | 50% | ❌ 40 pts to go |
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
| P01_GOLD | 581 | 44.2% | 44.2% |  | 85% | ❌ 41 pts to go |
| P02 | 368 | 54.1% | 54.1% |  | 90% | ❌ 36 pts to go |
| P03 | 224 | 50.9% | 50.9% |  | 85% | ❌ 34 pts to go |
| P04 | 1618 | 52.7% | 52.7% |  | 85% | ❌ 32 pts to go |
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
| P01_GOLD | 581 | 13.4% | 13.4% |  | 60% | ❌ 47 pts to go |
| P02 | 368 | 7.6% | 7.6% |  | 50% | ❌ 42 pts to go |
| P03 | 224 | 10.3% | 10.3% |  | 50% | ❌ 40 pts to go |
| P04 | 1618 | 4.3% | 4.3% |  | 40% | ❌ 36 pts to go |
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
| P01_GOLD | 581 | 36.3% | 36.3% |  | 80% | ❌ 44 pts to go |
| P02 | 368 | 59.2% | 59.2% |  | 90% | ❌ 31 pts to go |
| P03 | 224 | 37.1% | 37.1% |  | 80% | ❌ 43 pts to go |
| P04 | 1618 | 51.2% | 51.2% |  | 85% | ❌ 34 pts to go |
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
| P01_GOLD | 581 | 8.6% | 8.6% |  | 50% | ❌ 41 pts to go |
| P02 | 368 | 8.2% | 8.2% |  | 50% | ❌ 42 pts to go |
| P03 | 224 | 2.2% | 2.2% |  | 30% | ❌ 28 pts to go |
| P04 | 1618 | 1.1% | 1.1% |  | 30% | ❌ 29 pts to go |
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
| P01_GOLD | 581 | 72.8% | 100.0% |  | 100% | ❌ 27 pts to go |
| P02 | 368 | 75.0% | 100.0% |  | 100% | ❌ 25 pts to go |
| P03 | 224 | 75.0% | 100.0% |  | 100% | ❌ 25 pts to go |
| P04 | 1618 | 59.7% | 100.0% |  | 95% | ❌ 35 pts to go |
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
| P01_GOLD | 581 | 79.0% | 79.0% |  | 90% | ❌ 11 pts to go |
| P02 | 368 | 65.5% | 65.5% |  | 85% | ❌ 20 pts to go |
| P03 | 224 | 80.8% | 80.8% |  | 90% | 🟡 9 pts to go |
| P04 | 1618 | 54.1% | 54.1% |  | 75% | ❌ 21 pts to go |
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
| P01_GOLD | 581 | 75.9% | 75.9% |  | 95% | ❌ 19 pts to go |
| P02 | 368 | 81.8% | 81.8% |  | 95% | ❌ 13 pts to go |
| P03 | 224 | 77.2% | 77.2% |  | 95% | ❌ 18 pts to go |
| P04 | 1618 | 78.7% | 78.7% |  | 95% | ❌ 16 pts to go |
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
| P01_GOLD | 581 | 49.9% | 49.9% |  | 60% | ❌ 10 pts to go |
| P02 | 368 | 63.3% | 63.3% |  | 60% | ✅ met |
| P03 | 224 | 57.1% | 57.1% |  | 60% | 🟡 3 pts to go |
| P04 | 1618 | 53.6% | 53.6% |  | 55% | 🟡 1 pts to go |
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
| P01_GOLD | 581 | 33.4% | 33.4% |  | 70% | ❌ 37 pts to go |
| P02 | 368 | 41.8% | 41.8% |  | 70% | ❌ 28 pts to go |
| P03 | 224 | 38.8% | 38.8% |  | 70% | ❌ 31 pts to go |
| P04 | 1618 | 33.2% | 33.2% |  | 65% | ❌ 32 pts to go |
| P05 | 379 | 16.6% | 16.6% |  | 60% | ❌ 43 pts to go |
| P06M | 167 | 6.6% | 6.6% |  | n/a | no target |
| P06T | 2435 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 163 | 58.9% | 58.9% |  | 40% | ✅ met |
| P07 | 249 | 65.5% | 65.5% |  | 85% | ❌ 20 pts to go |
| P08 | 3037 | 64.8% | 64.8% |  | 85% | ❌ 20 pts to go |
| P09 | 369 | 52.3% | 52.3% |  | 85% | ❌ 33 pts to go |
| P10 | 2590 | 65.1% | 65.1% |  | 85% | ❌ 20 pts to go |
| P11 | 498 | 48.0% | 48.0% |  | 75% | ❌ 27 pts to go |
| P12 | 21 | 4.8% | 4.8% |  | n/a | no target |
| P13 | 50788 | 100.0% | 100.0% |  | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 50.0% | 50.0% |  | n/a | no target |
| P01T | 92 | 10.9% | 10.9% |  | n/a | no target |
| P01_GOLD | 581 | 86.4% | 86.4% |  | 90% | 🟡 4 pts to go |
| P02 | 368 | 80.4% | 80.4% |  | 90% | 🟡 10 pts to go |
| P03 | 224 | 82.6% | 82.6% |  | 90% | 🟡 7 pts to go |
| P04 | 1618 | 62.1% | 62.1% |  | 85% | ❌ 23 pts to go |
| P05 | 379 | 43.8% | 43.8% |  | 70% | ❌ 26 pts to go |
| P06M | 167 | 26.3% | 26.3% |  | n/a | no target |
| P06T | 2435 | 2.5% | 2.5% |  | n/a | no target |
| P06 | 163 | 97.5% | 97.5% |  | 50% | ✅ met |
| P07 | 249 | 96.8% | 96.8% |  | 100% | 🟡 3 pts to go |
| P08 | 3037 | 96.0% | 96.0% |  | 100% | 🟡 4 pts to go |
| P09 | 369 | 81.3% | 81.3% |  | 100% | ❌ 19 pts to go |
| P10 | 2590 | 100.0% | 100.0% |  | 100% | ✅ met |
| P11 | 498 | 88.0% | 88.0% |  | 100% | ❌ 12 pts to go |
| P12 | 21 | 42.9% | 42.9% |  | n/a | no target |
| P13 | 50788 | 100.0% | 100.0% |  | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 35.0% | 35.0% |  | n/a | no target |
| P01T | 92 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 581 | 36.8% | 36.8% |  | 70% | ❌ 33 pts to go |
| P02 | 368 | 44.8% | 44.8% |  | 75% | ❌ 30 pts to go |
| P03 | 224 | 42.0% | 42.0% |  | 75% | ❌ 33 pts to go |
| P04 | 1618 | 32.4% | 32.4% |  | 70% | ❌ 38 pts to go |
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
| P01_GOLD | 581 | 49.2% | 49.2% |  | 90% | ❌ 41 pts to go |
| P02 | 368 | 57.6% | 57.6% |  | 90% | ❌ 32 pts to go |
| P03 | 224 | 54.9% | 54.9% |  | 90% | ❌ 35 pts to go |
| P04 | 1618 | 42.7% | 42.7% |  | 85% | ❌ 42 pts to go |
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
| P01_GOLD | 581 | 49.1% | 49.1% |  | 95% | ❌ 46 pts to go · QC vendors: 49 rows, 98.0% filled |
| P02 | 368 | 66.8% | 66.8% |  | 95% | ❌ 28 pts to go · QC vendors: 92 rows, 100.0% filled |
| P03 | 224 | 54.9% | 54.9% |  | 95% | ❌ 40 pts to go · QC vendors: 16 rows, 100.0% filled |
| P04 | 1618 | 60.3% | 60.3% |  | 95% | ❌ 35 pts to go · QC vendors: 450 rows, 98.7% filled |
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
| P01_GOLD | 581 | 85.7% | 85.7% |  | 100% | ❌ 14 pts to go · vendors with a registry record: 498 rows, 100.0% filled |
| P02 | 368 | 88.3% | 88.3% |  | 100% | ❌ 12 pts to go · vendors with a registry record: 325 rows, 100.0% filled |
| P03 | 224 | 87.5% | 87.5% |  | 100% | ❌ 12 pts to go · vendors with a registry record: 196 rows, 100.0% filled |
| P04 | 1618 | 81.4% | 81.4% |  | 100% | ❌ 19 pts to go · vendors with a registry record: 1317 rows, 100.0% filled |
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
| P01_GOLD | 581 | 85.9% | 85.9% |  | 95% | 🟡 9 pts to go |
| P02 | 368 | 91.6% | 91.6% |  | 95% | 🟡 3 pts to go |
| P03 | 224 | 82.1% | 82.1% |  | 85% | 🟡 3 pts to go |
| P04 | 1618 | 79.1% | 79.1% |  | 90% | ❌ 11 pts to go |
| P05 | 379 | 76.0% | 76.0% |  | 75% | ✅ met |
| P06M | 167 | 88.6% | 88.6% |  | n/a | no target |
| P06T | 2435 | 64.5% | 64.5% |  | n/a | no target |
| P06 | 163 | 56.4% | 56.4% |  | 80% | ❌ 24 pts to go |
| P07 | 249 | 52.6% | 52.6% |  | 80% | ❌ 27 pts to go |
| P08 | 3037 | 36.9% | 36.9% |  | 75% | ❌ 38 pts to go |
| P09 | 369 | 82.7% | 82.7% |  | 95% | ❌ 12 pts to go |
| P10 | 2590 | 32.3% | 32.3% |  | 70% | ❌ 38 pts to go |
| P11 | 498 | 28.1% | 28.1% |  | 65% | ❌ 37 pts to go |
| P12 | 21 | 81.0% | 81.0% |  | 80% | ✅ met |
| P13 | 50788 | 48.6% | 48.6% |  | 60% | ❌ 11 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 40.0% | 40.0% |  | 50% | 🟡 10 pts to go |
| P01T | 92 | 20.7% | 20.7% |  | n/a | no target |
| P01_GOLD | 581 | 20.5% | 20.5% |  | 40% | ❌ 20 pts to go |
| P02 | 368 | 20.7% | 20.7% |  | 40% | ❌ 19 pts to go |
| P03 | 224 | 26.8% | 26.8% |  | 40% | ❌ 13 pts to go |
| P04 | 1618 | 27.4% | 27.4% |  | 40% | ❌ 13 pts to go |
| P05 | 379 | 23.2% | 23.2% |  | 25% | 🟡 2 pts to go |
| P06M | 167 | 24.6% | 24.6% |  | n/a | no target |
| P06T | 2435 | 30.9% | 30.9% |  | n/a | no target |
| P06 | 163 | 9.8% | 9.8% |  | 35% | ❌ 25 pts to go |
| P07 | 249 | 10.0% | 10.0% |  | 35% | ❌ 25 pts to go |
| P08 | 3037 | 10.5% | 10.5% |  | 35% | ❌ 24 pts to go |
| P09 | 369 | 17.9% | 17.9% |  | n/a | no target |
| P10 | 2590 | 8.9% | 8.9% |  | 30% | ❌ 21 pts to go |
| P11 | 498 | 9.6% | 9.6% |  | n/a | no target |
| P12 | 21 | 19.0% | 19.0% |  | n/a | no target |
| P13 | 50788 | 21.5% | 21.5% |  | 30% | 🟡 8 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 95.0% | 95.0% |  | 100% | 🟡 5 pts to go |
| P01T | 92 | 93.5% | 93.5% |  | 100% | 🟡 6 pts to go |
| P01_GOLD | 581 | 89.3% | 89.3% |  | 100% | ❌ 11 pts to go |
| P02 | 368 | 95.7% | 95.7% |  | 100% | 🟡 4 pts to go |
| P03 | 224 | 94.2% | 94.2% |  | 100% | 🟡 6 pts to go |
| P04 | 1618 | 91.1% | 91.1% |  | 100% | 🟡 9 pts to go |
| P05 | 379 | 84.7% | 84.7% |  | 100% | ❌ 15 pts to go |
| P06M | 167 | 71.3% | 71.3% |  | n/a | no target |
| P06T | 2435 | 80.0% | 80.0% |  | n/a | no target |
| P06 | 163 | 67.5% | 67.5% |  | 95% | ❌ 28 pts to go |
| P07 | 249 | 69.9% | 69.9% |  | 95% | ❌ 25 pts to go |
| P08 | 3037 | 65.6% | 65.6% |  | 95% | ❌ 29 pts to go |
| P09 | 369 | 98.4% | 98.4% |  | 100% | 🟡 2 pts to go |
| P10 | 2590 | 64.4% | 64.4% |  | 95% | ❌ 31 pts to go |
| P11 | 498 | 37.8% | 37.8% |  | 80% | ❌ 42 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50788 | 75.0% | 75.0% |  | 95% | ❌ 20 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 90.0% | 90.0% |  | n/a | no target |
| P01T | 92 | 80.4% | 80.4% |  | n/a | no target |
| P01_GOLD | 581 | 69.7% | 69.7% |  | 90% | ❌ 20 pts to go |
| P02 | 368 | 78.0% | 78.0% |  | 95% | ❌ 17 pts to go |
| P03 | 224 | 74.6% | 74.6% |  | 95% | ❌ 20 pts to go |
| P04 | 1618 | 85.4% | 85.4% |  | 95% | 🟡 10 pts to go |
| P05 | 379 | 74.9% | 74.9% |  | 90% | ❌ 15 pts to go |
| P06M | 167 | 83.8% | 83.8% |  | n/a | no target |
| P06T | 2435 | 77.2% | 77.2% |  | n/a | no target |
| P06 | 163 | 64.4% | 64.4% |  | 95% | ❌ 31 pts to go |
| P07 | 249 | 65.1% | 65.1% |  | 90% | ❌ 25 pts to go |
| P08 | 3037 | 74.5% | 74.5% |  | 95% | ❌ 20 pts to go |
| P09 | 369 | 89.7% | 89.7% |  | 100% | ❌ 10 pts to go |
| P10 | 2590 | 71.4% | 71.4% |  | 95% | ❌ 24 pts to go |
| P11 | 498 | 27.7% | 27.7% |  | 75% | ❌ 47 pts to go |
| P12 | 21 | 85.7% | 85.7% |  | n/a | no target |
| P13 | 50788 | 79.0% | 79.0% |  | 95% | ❌ 16 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 80.0% | 80.0% |  | n/a | no target |
| P01T | 92 | 91.3% | 91.3% |  | 95% | 🟡 4 pts to go |
| P01_GOLD | 581 | 68.7% | 68.7% |  | 90% | ❌ 21 pts to go |
| P02 | 368 | 78.0% | 78.0% |  | 95% | ❌ 17 pts to go |
| P03 | 224 | 70.5% | 70.5% |  | 95% | ❌ 24 pts to go |
| P04 | 1618 | 63.3% | 63.3% |  | 90% | ❌ 27 pts to go |
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
| P13 | 50788 | 83.9% | 83.9% |  | 95% | ❌ 11 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 15.0% | 15.0% |  | n/a | no target |
| P01T | 92 | 19.6% | 19.6% |  | n/a | no target |
| P01_GOLD | 581 | 10.3% | 10.3% |  | 25% | ❌ 15 pts to go |
| P02 | 368 | 20.7% | 20.7% |  | 40% | ❌ 19 pts to go |
| P03 | 224 | 2.7% | 2.7% |  | 20% | ❌ 17 pts to go |
| P04 | 1618 | 1.2% | 1.2% |  | 20% | ❌ 19 pts to go |
| P05 | 379 | 1.6% | 1.6% |  | 15% | ❌ 13 pts to go |
| P06M | 167 | 1.8% | 1.8% |  | n/a | no target |
| P06T | 2435 | 0.9% | 0.9% |  | n/a | no target |
| P06 | 163 | 4.9% | 4.9% |  | n/a | no target |
| P07 | 249 | 6.0% | 6.0% |  | n/a | no target |
| P08 | 3037 | 0.2% | 0.2% |  | n/a | no target |
| P09 | 369 | 5.7% | 5.7% |  | n/a | no target |
| P10 | 2590 | 0.5% | 0.5% |  | n/a | no target |
| P11 | 498 | 1.2% | 1.2% |  | n/a | no target |
| P12 | 21 | 4.8% | 4.8% |  | n/a | no target |
| P13 | 50788 | 0.2% | 0.2% |  | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 40.0% | 40.0% |  | n/a | no target |
| P01T | 92 | 38.0% | 38.0% |  | 70% | ❌ 32 pts to go |
| P01_GOLD | 581 | 44.9% | 44.9% |  | 80% | ❌ 35 pts to go |
| P02 | 368 | 68.2% | 68.2% |  | 90% | ❌ 22 pts to go |
| P03 | 224 | 21.0% | 21.0% |  | 60% | ❌ 39 pts to go |
| P04 | 1618 | 50.3% | 50.3% |  | 85% | ❌ 35 pts to go |
| P05 | 379 | 12.7% | 12.7% |  | 50% | ❌ 37 pts to go |
| P06M | 167 | 6.0% | 6.0% |  | n/a | no target |
| P06T | 2435 | 2.3% | 2.3% |  | n/a | no target |
| P06 | 163 | 18.4% | 18.4% |  | n/a | no target |
| P07 | 249 | 19.3% | 19.3% |  | n/a | no target |
| P08 | 3037 | 0.5% | 0.5% |  | n/a | no target |
| P09 | 369 | 81.0% | 81.0% |  | 95% | ❌ 14 pts to go |
| P10 | 2590 | 3.1% | 3.1% |  | n/a | no target |
| P11 | 498 | 33.7% | 33.7% |  | n/a | no target |
| P12 | 21 | 33.3% | 33.3% |  | n/a | no target |
| P13 | 50788 | 0.9% | 0.9% |  | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 5.0% | 5.0% |  | n/a | no target |
| P01T | 92 | 18.5% | 18.5% |  | n/a | no target |
| P01_GOLD | 581 | 33.9% | 33.9% |  | 70% | ❌ 36 pts to go |
| P02 | 368 | 44.8% | 44.8% |  | 75% | ❌ 30 pts to go |
| P03 | 224 | 21.0% | 21.0% |  | 55% | ❌ 34 pts to go |
| P04 | 1618 | 49.8% | 49.8% |  | 75% | ❌ 25 pts to go |
| P05 | 379 | 10.8% | 10.8% |  | 50% | ❌ 39 pts to go |
| P06M | 167 | 1.8% | 1.8% |  | n/a | no target |
| P06T | 2435 | 1.1% | 1.1% |  | n/a | no target |
| P06 | 163 | 10.4% | 10.4% |  | n/a | no target |
| P07 | 249 | 10.4% | 10.4% |  | n/a | no target |
| P08 | 3037 | 0.5% | 0.5% |  | n/a | no target |
| P09 | 369 | 77.2% | 77.2% |  | 95% | ❌ 18 pts to go |
| P10 | 2590 | 1.8% | 1.8% |  | n/a | no target |
| P11 | 498 | 33.5% | 33.5% |  | n/a | no target |
| P12 | 21 | 19.0% | 19.0% |  | n/a | no target |
| P13 | 50788 | 0.6% | 0.6% |  | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 15.0% | 15.0% |  | n/a | no target |
| P01T | 92 | 16.3% | 16.3% |  | n/a | no target |
| P01_GOLD | 581 | 53.5% | 53.7% |  | 80% | ❌ 26 pts to go |
| P02 | 368 | 46.2% | 46.2% |  | 75% | ❌ 29 pts to go |
| P03 | 224 | 31.7% | 31.7% |  | 70% | ❌ 38 pts to go |
| P04 | 1618 | 36.7% | 36.7% |  | 70% | ❌ 33 pts to go |
| P05 | 379 | 13.5% | 13.5% |  | 50% | ❌ 36 pts to go |
| P06M | 167 | 0.6% | 0.6% |  | n/a | no target |
| P06T | 2435 | 0.8% | 0.8% |  | n/a | no target |
| P06 | 163 | 21.5% | 21.5% |  | n/a | no target |
| P07 | 249 | 4.0% | 4.0% |  | n/a | no target |
| P08 | 3037 | 0.8% | 0.8% |  | n/a | no target |
| P09 | 369 | 41.7% | 41.7% |  | 80% | ❌ 38 pts to go |
| P10 | 2590 | 1.4% | 1.4% |  | n/a | no target |
| P11 | 498 | 18.9% | 18.9% |  | n/a | no target |
| P12 | 21 | 33.3% | 33.3% |  | n/a | no target |
| P13 | 50788 | 0.3% | 0.3% |  | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 35.0% | 35.0% |  | n/a | no target |
| P01T | 92 | 53.3% | 53.3% |  | 60% | 🟡 7 pts to go |
| P01_GOLD | 581 | 56.1% | 56.1% |  | 70% | ❌ 14 pts to go |
| P02 | 368 | 10.1% | 10.1% |  | 50% | ❌ 40 pts to go |
| P03 | 224 | 15.2% | 15.2% |  | 55% | ❌ 40 pts to go |
| P04 | 1618 | 3.1% | 3.1% |  | 40% | ❌ 37 pts to go |
| P05 | 379 | 9.0% | 9.0% |  | 40% | ❌ 31 pts to go |
| P06M | 167 | 1.8% | 1.8% |  | n/a | no target |
| P06T | 2435 | 2.7% | 2.7% |  | n/a | no target |
| P06 | 163 | 23.9% | 23.9% |  | n/a | no target |
| P07 | 249 | 9.2% | 9.2% |  | n/a | no target |
| P08 | 3037 | 1.5% | 1.5% |  | n/a | no target |
| P09 | 369 | 3.8% | 3.8% |  | n/a | no target |
| P10 | 2590 | 1.3% | 1.3% |  | n/a | no target |
| P11 | 498 | 2.2% | 2.2% |  | n/a | no target |
| P12 | 21 | 19.0% | 19.0% |  | n/a | no target |
| P13 | 50788 | 0.3% | 0.3% |  | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 40.0% | 40.0% |  | n/a | no target |
| P01T | 92 | 62.0% | 62.0% |  | 65% | 🟡 3 pts to go |
| P01_GOLD | 581 | 60.4% | 60.4% |  | 70% | 🟡 10 pts to go |
| P02 | 368 | 6.5% | 6.5% |  | 50% | ❌ 44 pts to go |
| P03 | 224 | 26.8% | 26.8% |  | 60% | ❌ 33 pts to go |
| P04 | 1618 | 1.9% | 1.9% |  | 40% | ❌ 38 pts to go |
| P05 | 379 | 15.0% | 15.0% |  | 45% | ❌ 30 pts to go |
| P06M | 167 | 3.6% | 3.6% |  | n/a | no target |
| P06T | 2435 | 1.4% | 1.4% |  | n/a | no target |
| P06 | 163 | 45.4% | 45.4% |  | n/a | no target |
| P07 | 249 | 16.5% | 16.5% |  | n/a | no target |
| P08 | 3037 | 1.4% | 1.4% |  | n/a | no target |
| P09 | 369 | 5.7% | 5.7% |  | n/a | no target |
| P10 | 2590 | 1.5% | 1.5% |  | n/a | no target |
| P11 | 498 | 3.2% | 3.2% |  | n/a | no target |
| P12 | 21 | 9.5% | 9.5% |  | n/a | no target |
| P13 | 50788 | 0.2% | 0.2% |  | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 10.0% | 10.0% |  | n/a | no target |
| P01T | 92 | 34.8% | 34.8% |  | n/a | no target |
| P01_GOLD | 581 | 37.7% | 37.7% |  | 50% | ❌ 12 pts to go |
| P02 | 368 | 15.5% | 15.5% |  | n/a | no target |
| P03 | 224 | 49.1% | 49.1% |  | 60% | ❌ 11 pts to go |
| P04 | 1618 | 8.5% | 8.5% |  | n/a | no target |
| P05 | 379 | 12.4% | 12.4% |  | n/a | no target |
| P06M | 167 | 3.0% | 3.0% |  | n/a | no target |
| P06T | 2435 | 1.6% | 1.6% |  | n/a | no target |
| P06 | 163 | 31.9% | 31.9% |  | n/a | no target |
| P07 | 249 | 16.9% | 16.9% |  | n/a | no target |
| P08 | 3037 | 1.1% | 1.1% |  | n/a | no target |
| P09 | 369 | 8.1% | 8.1% |  | n/a | no target |
| P10 | 2590 | 1.9% | 1.9% |  | n/a | no target |
| P11 | 498 | 4.8% | 4.8% |  | n/a | no target |
| P12 | 21 | 9.5% | 9.5% |  | n/a | no target |
| P13 | 50788 | 0.4% | 0.4% |  | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 20.0% | 20.0% |  | 15% | ✅ met |
| P01T | 92 | 23.9% | 23.9% |  | 15% | ✅ met |
| P01_GOLD | 581 | 26.7% | 26.7% |  | 40% | ❌ 13 pts to go |
| P02 | 368 | 7.3% | 7.3% |  | 25% | ❌ 18 pts to go |
| P03 | 224 | 9.4% | 9.4% |  | 25% | ❌ 16 pts to go |
| P04 | 1618 | 1.2% | 1.2% |  | 15% | ❌ 14 pts to go |
| P05 | 379 | 5.8% | 5.8% |  | 15% | 🟡 9 pts to go |
| P06M | 167 | 3.6% | 3.6% |  | 15% | ❌ 11 pts to go |
| P06T | 2435 | 0.9% | 0.9% |  | 15% | ❌ 14 pts to go |
| P06 | 163 | 9.2% | 9.2% |  | 15% | 🟡 6 pts to go |
| P07 | 249 | 4.8% | 4.8% |  | 15% | ❌ 10 pts to go |
| P08 | 3037 | 1.0% | 1.0% |  | 15% | ❌ 14 pts to go |
| P09 | 369 | 0.8% | 0.8% |  | 15% | ❌ 14 pts to go |
| P10 | 2590 | 1.3% | 1.3% |  | 15% | ❌ 14 pts to go |
| P11 | 498 | 0.6% | 0.6% |  | 15% | ❌ 14 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P13 | 50788 | 0.9% | 0.9% |  | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P01T | 92 | 25.0% | 25.0% |  | 25% | ✅ met |
| P01_GOLD | 581 | 18.1% | 18.1% |  | 25% | 🟡 7 pts to go |
| P02 | 368 | 5.2% | 5.2% |  | 15% | 🟡 10 pts to go |
| P03 | 224 | 4.0% | 4.0% |  | 15% | ❌ 11 pts to go |
| P04 | 1618 | 0.6% | 0.6% |  | 15% | ❌ 14 pts to go |
| P05 | 379 | 8.7% | 8.7% |  | 15% | 🟡 6 pts to go |
| P06M | 167 | 1.2% | 1.2% |  | 15% | ❌ 14 pts to go |
| P06T | 2435 | 0.6% | 0.6% |  | 15% | ❌ 14 pts to go |
| P06 | 163 | 8.0% | 8.0% |  | 15% | 🟡 7 pts to go |
| P07 | 249 | 4.4% | 4.4% |  | 15% | ❌ 11 pts to go |
| P08 | 3037 | 0.4% | 0.4% |  | 15% | ❌ 15 pts to go |
| P09 | 369 | 0.3% | 0.3% |  | 15% | ❌ 15 pts to go |
| P10 | 2590 | 0.5% | 0.5% |  | 15% | ❌ 14 pts to go |
| P11 | 498 | 1.4% | 1.4% |  | 15% | ❌ 14 pts to go |
| P12 | 21 | 14.3% | 14.3% |  | 15% | 🟡 1 pts to go |
| P13 | 50788 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P01T | 92 | 6.5% | 6.5% |  | 20% | ❌ 14 pts to go |
| P01_GOLD | 581 | 3.8% | 3.8% |  | 20% | ❌ 16 pts to go |
| P02 | 368 | 0.3% | 0.3% |  | 20% | ❌ 20 pts to go |
| P03 | 224 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P04 | 1618 | 0.1% | 0.1% |  | 20% | ❌ 20 pts to go |
| P05 | 379 | 0.8% | 0.8% |  | 20% | ❌ 19 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P06T | 2435 | 0.1% | 0.1% |  | 20% | ❌ 20 pts to go |
| P06 | 163 | 3.7% | 3.7% |  | 20% | ❌ 16 pts to go |
| P07 | 249 | 0.4% | 0.4% |  | 20% | ❌ 20 pts to go |
| P08 | 3037 | 0.1% | 0.1% |  | 20% | ❌ 20 pts to go |
| P09 | 369 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P10 | 2590 | 0.2% | 0.2% |  | 20% | ❌ 20 pts to go |
| P11 | 498 | 0.2% | 0.2% |  | 20% | ❌ 20 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P13 | 50788 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 5.0% | 5.0% |  | 15% | 🟡 10 pts to go |
| P01T | 92 | 6.5% | 6.5% |  | 15% | 🟡 8 pts to go |
| P01_GOLD | 581 | 5.7% | 5.7% |  | 15% | 🟡 9 pts to go |
| P02 | 368 | 1.1% | 1.1% |  | 15% | ❌ 14 pts to go |
| P03 | 224 | 3.6% | 3.6% |  | 15% | ❌ 11 pts to go |
| P04 | 1618 | 0.5% | 0.5% |  | 15% | ❌ 14 pts to go |
| P05 | 379 | 0.8% | 0.8% |  | 15% | ❌ 14 pts to go |
| P06M | 167 | 0.6% | 0.6% |  | 15% | ❌ 14 pts to go |
| P06T | 2435 | 0.2% | 0.2% |  | 15% | ❌ 15 pts to go |
| P06 | 163 | 4.3% | 4.3% |  | 15% | ❌ 11 pts to go |
| P07 | 249 | 0.8% | 0.8% |  | 15% | ❌ 14 pts to go |
| P08 | 3037 | 0.3% | 0.3% |  | 15% | ❌ 15 pts to go |
| P09 | 369 | 0.3% | 0.3% |  | 15% | ❌ 15 pts to go |
| P10 | 2590 | 0.3% | 0.3% |  | 15% | ❌ 15 pts to go |
| P11 | 498 | 0.2% | 0.2% |  | 15% | ❌ 15 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P13 | 50788 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 10.0% | 10.0% |  | 20% | 🟡 10 pts to go |
| P01T | 92 | 23.9% | 23.9% |  | 40% | ❌ 16 pts to go |
| P01_GOLD | 581 | 17.9% | 17.9% |  | 40% | ❌ 22 pts to go |
| P02 | 368 | 5.7% | 5.7% |  | 20% | ❌ 14 pts to go |
| P03 | 224 | 11.2% | 11.2% |  | 35% | ❌ 24 pts to go |
| P04 | 1618 | 4.6% | 4.6% |  | 20% | ❌ 15 pts to go |
| P05 | 379 | 6.1% | 6.1% |  | 20% | ❌ 14 pts to go |
| P06M | 167 | 3.0% | 3.0% |  | 20% | ❌ 17 pts to go |
| P06T | 2435 | 1.4% | 1.4% |  | 20% | ❌ 19 pts to go |
| P06 | 163 | 25.8% | 25.8% |  | 20% | ✅ met |
| P07 | 249 | 11.6% | 11.6% |  | 20% | 🟡 8 pts to go |
| P08 | 3037 | 1.2% | 1.2% |  | 20% | ❌ 19 pts to go |
| P09 | 369 | 10.0% | 10.0% |  | 20% | 🟡 10 pts to go |
| P10 | 2590 | 1.6% | 1.6% |  | 20% | ❌ 18 pts to go |
| P11 | 498 | 3.6% | 3.6% |  | 20% | ❌ 16 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P13 | 50788 | 0.4% | 0.4% |  | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 92 | 1.1% | 1.1% |  | n/a | no target |
| P01_GOLD | 581 | 70.7% | 70.7% |  | 95% | ❌ 24 pts to go |
| P02 | 368 | 74.2% | 74.2% |  | 95% | ❌ 21 pts to go |
| P03 | 224 | 63.8% | 63.8% |  | 90% | ❌ 26 pts to go |
| P04 | 1618 | 58.7% | 58.7% |  | 85% | ❌ 26 pts to go |
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
| P01_GOLD | 581 | 74.4% | 74.4% |  | 100% | ❌ 26 pts to go |
| P02 | 368 | 77.7% | 77.7% |  | 100% | ❌ 22 pts to go |
| P03 | 224 | 71.0% | 71.0% |  | n/a | no target |
| P04 | 1618 | 60.1% | 60.1% |  | 95% | ❌ 35 pts to go |
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
| P01_GOLD | 581 | 52.8% | 52.8% |  | 85% | ❌ 32 pts to go |
| P02 | 368 | 65.2% | 65.2% |  | 90% | ❌ 25 pts to go |
| P03 | 224 | 52.2% | 52.2% |  | 85% | ❌ 33 pts to go |
| P04 | 1618 | 63.9% | 63.9% |  | 90% | ❌ 26 pts to go |
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
| P01_GOLD | 581 | 53.9% | 53.9% |  | 85% | ❌ 31 pts to go |
| P02 | 368 | 60.6% | 60.6% |  | 90% | ❌ 29 pts to go |
| P03 | 224 | 52.7% | 52.7% |  | 85% | ❌ 32 pts to go |
| P04 | 1618 | 53.8% | 53.8% |  | 90% | ❌ 36 pts to go |
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
| P01_GOLD | 581 | 82.1% | 82.1% |  | 100% | ❌ 18 pts to go |
| P02 | 368 | 80.4% | 80.4% |  | 100% | ❌ 20 pts to go |
| P03 | 224 | 86.6% | 86.6% |  | n/a | no target |
| P04 | 1618 | 71.6% | 71.6% |  | 95% | ❌ 23 pts to go |
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
| P01_GOLD | 581 | 69.5% | 69.5% |  | 100% | ❌ 30 pts to go |
| P02 | 368 | 71.5% | 71.7% |  | 100% | ❌ 28 pts to go |
| P03 | 224 | 68.3% | 68.3% |  | n/a | no target |
| P04 | 1618 | 57.9% | 57.9% |  | 95% | ❌ 37 pts to go |
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
| P01_GOLD | 581 | 18.6% | 18.6% |  | 60% | ❌ 41 pts to go · rows from a source that publishes bids: 355 rows, 30.4% filled |
| P02 | 368 | 14.1% | 14.1% |  | n/a | no target · rows from a source that publishes bids: 267 rows, 19.5% filled |
| P03 | 224 | 15.2% | 15.2% |  | n/a | no target · rows from a source that publishes bids: 139 rows, 24.5% filled |
| P04 | 1618 | 3.6% | 3.6% |  | n/a | no target · rows from a source that publishes bids: 903 rows, 6.4% filled |
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
| P01_GOLD | 581 | 40.6% | 67.8% |  | 90% | ❌ 49 pts to go |
| P02 | 368 | 55.4% | 80.4% |  | 90% | ❌ 35 pts to go |
| P03 | 224 | 39.3% | 64.3% |  | 90% | ❌ 51 pts to go |
| P04 | 1618 | 42.6% | 82.9% |  | 90% | ❌ 47 pts to go |
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
| P01_GOLD | 581 | 27.2% | 54.4% |  | 90% | ❌ 63 pts to go |
| P02 | 368 | 58.4% | 83.4% |  | n/a | no target |
| P03 | 224 | 28.1% | 53.1% |  | n/a | no target |
| P04 | 1618 | 49.6% | 89.9% |  | n/a | no target |
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
| P01_GOLD | 581 | 54.2% | 81.4% |  | 95% | ❌ 41 pts to go |
| P02 | 368 | 65.8% | 90.8% |  | n/a | no target |
| P03 | 224 | 58.0% | 83.0% |  | n/a | no target |
| P04 | 1618 | 50.2% | 90.5% |  | n/a | no target |
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
| P01T | 92 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01_GOLD | 581 | 100.0% | 100.0% |  | 100% | ✅ met |
| P02 | 368 | 100.0% | 100.0% |  | 100% | ✅ met |
| P03 | 224 | 100.0% | 100.0% |  | 100% | ✅ met |
| P04 | 1618 | 100.0% | 100.0% |  | 100% | ✅ met |
| P05 | 379 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06M | 167 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06T | 2435 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06 | 163 | 100.0% | 100.0% |  | 100% | ✅ met |
| P07 | 249 | 100.0% | 100.0% |  | 100% | ✅ met |
| P08 | 3037 | 100.0% | 100.0% |  | 100% | ✅ met |
| P09 | 369 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2590 | 100.0% | 100.0% |  | 100% | ✅ met |
| P11 | 498 | 100.0% | 100.0% |  | 100% | ✅ met |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50788 | 100.0% | 100.0% |  | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01T | 92 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01_GOLD | 581 | 100.0% | 100.0% |  | 100% | ✅ met |
| P02 | 368 | 100.0% | 100.0% |  | 100% | ✅ met |
| P03 | 224 | 100.0% | 100.0% |  | 100% | ✅ met |
| P04 | 1618 | 100.0% | 100.0% |  | 100% | ✅ met |
| P05 | 379 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06M | 167 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06T | 2435 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06 | 163 | 100.0% | 100.0% |  | 100% | ✅ met |
| P07 | 249 | 100.0% | 100.0% |  | 100% | ✅ met |
| P08 | 3037 | 100.0% | 100.0% |  | 100% | ✅ met |
| P09 | 369 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2590 | 100.0% | 100.0% |  | 100% | ✅ met |
| P11 | 498 | 100.0% | 100.0% |  | 100% | ✅ met |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50788 | 100.0% | 100.0% |  | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01T | 92 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01_GOLD | 581 | 100.0% | 100.0% |  | 100% | ✅ met |
| P02 | 368 | 100.0% | 100.0% |  | 100% | ✅ met |
| P03 | 224 | 100.0% | 100.0% |  | 100% | ✅ met |
| P04 | 1618 | 100.0% | 100.0% |  | 100% | ✅ met |
| P05 | 379 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06M | 167 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06T | 2435 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06 | 163 | 100.0% | 100.0% |  | 100% | ✅ met |
| P07 | 249 | 100.0% | 100.0% |  | 100% | ✅ met |
| P08 | 3037 | 100.0% | 100.0% |  | 100% | ✅ met |
| P09 | 369 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2590 | 100.0% | 100.0% |  | 100% | ✅ met |
| P11 | 498 | 100.0% | 100.0% |  | 100% | ✅ met |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50788 | 100.0% | 100.0% |  | 100% | ✅ met |


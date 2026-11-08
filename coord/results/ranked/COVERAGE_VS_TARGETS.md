# Coverage vs the downstream team's targets — 2026-11-08

Benchmarks (field × package with a numeric target): **51 of 438 met** (11.6%); 55 within 10 points; 332 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 20, P01T 91, P01_GOLD 583, P02 368, P03 225, P04 1615, P05 378, P06M 167, P06T 2431, P06 161, P07 248, P08 3037, P09 369, P10 2588, P11 499, P12 21, P13 50789

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% | 5 | reference to quote (PO / contract / vendor id) (20 rows) |
| P01T | 91 | 0.0% | 1.1% | 6 | currency (91 rows) |
| P01_GOLD | 583 | 0.5% | 19.4% | 7 | buyer tax status (540 rows) |
| P02 | 368 | 0.0% | 6.2% | 7 | PO rule (365 rows) |
| P03 | 225 | 0.0% | 3.6% | 7 | buyer tax status (219 rows) |
| P04 | 1615 | 0.0% | 1.1% | 7 | PO rule (1608 rows) |
| P05 | 378 | 0.0% | 0.5% | 5 | payment terms (364 rows) |
| P06M | 167 | 0.0% | 0.0% | 4 | reference to quote (PO / contract / vendor id) (167 rows) |
| P06T | 2431 | 0.0% | 0.0% | 4 | currency (2431 rows) |
| P06 | 161 | 0.0% | 0.0% | 5 | reference to quote (PO / contract / vendor id) (161 rows) |
| P07 | 248 | 0.0% | 0.0% | 4 | reference to quote (PO / contract / vendor id) (248 rows) |
| P08 | 3037 | 0.0% | 0.0% | 4 | reference to quote (PO / contract / vendor id) (3037 rows) |
| P09 | 369 | 0.0% | 0.5% | 7 | buyer tax status (368 rows) |
| P10 | 2588 | 0.0% | 0.0% | 4 | currency (2588 rows) |
| P11 | 499 | 0.0% | 0.4% | 3 | buyer tax status (494 rows) |
| P12 | 21 | 0.0% | 0.0% | 6 | reference to quote (PO / contract / vendor id) (21 rows) |
| P13 | 50789 | 0.0% | 0.0% | 4 | reference to quote (PO / contract / vendor id) (50789 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 20 | 2 | 2 | 16 | 0 | 0 | 71 |
| P01T | 91 | 2 | 27 | 62 | 0 | 0 | 70 |
| P01_GOLD | 583 | 38 | 150 | 395 | 0 | 0 | 72 |
| P02 | 368 | 0 | 13 | 355 | 0 | 0 | 60 |
| P03 | 225 | 0 | 0 | 216 | 9 | 0 | 49 |
| P04 | 1615 | 0 | 0 | 1547 | 68 | 0 | 47 |
| P05 | 378 | 3 | 20 | 324 | 31 | 0 | 46 |
| P06M | 167 | 0 | 1 | 150 | 16 | 0 | 46 |
| P06T | 2431 | 0 | 1 | 2085 | 345 | 0 | 41 |
| P06 | 161 | 7 | 27 | 127 | 0 | 0 | 66 |
| P07 | 248 | 0 | 3 | 218 | 27 | 0 | 49 |
| P08 | 3037 | 0 | 0 | 2235 | 802 | 0 | 38 |
| P09 | 369 | 4 | 5 | 359 | 1 | 0 | 50 |
| P10 | 2588 | 2 | 5 | 1849 | 732 | 0 | 38 |
| P11 | 499 | 0 | 0 | 0 | 0 | 499 | 23 |
| P12 | 21 | 0 | 0 | 21 | 0 | 0 | 51 |
| P13 | 50789 | 1 | 14 | 39217 | 11557 | 0 | 38 |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 18 | 0 | 0 | 2 | 0 | 2 | 1 | 16 | 16 | 6 |
| P01T | 89 | 0 | 0 | 4 | 0 | 7 | 4 | 63 | 77 | 58 |
| P01_GOLD | 545 | 0 | 0 | 79 | 0 | 91 | 42 | 384 | 463 | 260 |
| P02 | 368 | 0 | 368 | 49 | 0 | 38 | 14 | 365 | 356 | 209 |
| P03 | 225 | 0 | 225 | 36 | 1 | 44 | 13 | 197 | 212 | 84 |
| P04 | 1615 | 0 | 1615 | 160 | 1 | 439 | 132 | 1608 | 1605 | 980 |
| P05 | 375 | 0 | 315 | 26 | 2 | 125 | 62 | 348 | 366 | 234 |
| P06M | 167 | 0 | 167 | 11 | 0 | 34 | 50 | 165 | 166 | 94 |
| P06T | 2431 | 0 | 2431 | 88 | 15 | 1167 | 522 | 2423 | 2417 | 1905 |
| P06 | 154 | 0 | 0 | 26 | 1 | 71 | 45 | 104 | 138 | 40 |
| P07 | 248 | 0 | 248 | 18 | 3 | 122 | 80 | 231 | 239 | 116 |
| P08 | 3037 | 0 | 3037 | 215 | 19 | 1950 | 1076 | 3029 | 3023 | 1960 |
| P09 | 365 | 0 | 346 | 64 | 2 | 86 | 1 | 355 | 359 | 277 |
| P10 | 2586 | 0 | 2533 | 152 | 19 | 1757 | 932 | 2567 | 2574 | 1773 |
| P11 | 499 | 499 | 462 | 34 | 6 | 365 | 236 | 491 | 497 | 307 |
| P12 | 21 | 0 | 16 | 4 | 0 | 6 | 0 | 20 | 19 | 16 |
| P13 | 50788 | 0 | 50477 | 316 | 460 | 35844 | 13018 | 50717 | 50667 | 40171 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_legal_name_as_published | P13 | 29.4% | 60% | 15529 |
| buyer_address | P13 | 74.3% | 95% | 10523 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 10155 |
| ap_system_hint | P13 | 0.3% | 20% | 9986 |
| buyer_logo_url | P13 | 76.3% | 95% | 9498 |
| buyer_phone | P13 | 76.9% | 95% | 9173 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 7589 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 7563 |
| buyer_payment_method_preference | P13 | 0.6% | 15% | 7292 |
| buyer_bn_as_published | P13 | 17.6% | 30% | 6283 |
| vendor_registered_address | P10 | 17.9% | 70% | 1348 |
| vendor_registered_address | P08 | 29.1% | 70% | 1241 |
| buyer_legal_name_as_published | P08 | 35.8% | 75% | 1191 |
| buyer_legal_name_as_published | P10 | 32.1% | 70% | 981 |
| buyer_address | P08 | 64.5% | 95% | 928 |
| buyer_bn_as_published | P08 | 6.5% | 35% | 865 |
| vendor_emails | P08 | 47.0% | 75% | 851 |
| buyer_address | P10 | 63.6% | 95% | 812 |
| average_contract_duration_days | P04 | 42.6% | 90% | 766 |
| invoice_reference_hint | P08 | 0.0% | 25% | 760 |
| vendor_emails | P10 | 50.8% | 80% | 757 |
| vendor_logo_url | P04 | 42.7% | 85% | 683 |
| vendor_bn9 | P08 | 27.7% | 50% | 679 |
| solicitation_or_tender_number | P04 | 10.0% | 50% | 646 |
| invoice_reference_hint | P10 | 0.1% | 25% | 645 |
| po_required_as_published | P04 | 0.4% | 40% | 639 |
| payment_terms_as_published | P04 | 0.6% | 40% | 636 |
| buyer_bn_as_published | P10 | 5.6% | 30% | 631 |
| vendor_phone | P08 | 64.5% | 85% | 624 |
| buyer_phone | P08 | 74.5% | 95% | 622 |
| buyer_phone | P10 | 71.4% | 95% | 612 |
| vendor_emails | P04 | 32.4% | 70% | 607 |
| buyer_ap_cycle_published | P08 | 0.1% | 20% | 606 |
| contract_description | P04 | 57.9% | 95% | 600 |
| end_date | P04 | 53.1% | 90% | 596 |
| currency | P04 | 58.5% | 95% | 590 |
| ap_system_hint | P08 | 0.9% | 20% | 582 |
| ap_phone | P04 | 49.2% | 85% | 578 |
| buyer_vendor_id | P04 | 4.3% | 40% | 576 |
| records_with_this_vendor | P04 | 59.7% | 95% | 571 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | 50% | ❌ 50 pts to go |
| P01T | 91 | 5.5% | 6.6% |  | 50% | ❌ 44 pts to go |
| P01_GOLD | 583 | 77.2% | 85.6% |  | 95% | ❌ 18 pts to go |
| P02 | 368 | 76.1% | 78.8% |  | 95% | ❌ 19 pts to go |
| P03 | 225 | 77.8% | 87.6% |  | 95% | ❌ 17 pts to go |
| P04 | 1615 | 66.1% | 69.2% |  | 90% | ❌ 24 pts to go |
| P05 | 378 | 32.5% | 36.2% |  | 70% | ❌ 38 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2431 | 0.2% | 0.2% |  | n/a | no target |
| P06 | 161 | 0.0% | 0.0% |  | 30% | ❌ 30 pts to go |
| P07 | 248 | 0.0% | 0.0% |  | 30% | ❌ 30 pts to go |
| P08 | 3037 | 0.0% | 0.0% |  | 25% | ❌ 25 pts to go |
| P09 | 369 | 98.4% | 99.2% |  | 100% | 🟡 2 pts to go |
| P10 | 2588 | 0.1% | 1.0% |  | 25% | ❌ 25 pts to go |
| P11 | 499 | 24.8% | 28.5% |  | 60% | ❌ 35 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50789 | 0.0% | 0.0% |  | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 91 | 0.0% | 0.0% |  | 10% | 🟡 10 pts to go |
| P01_GOLD | 583 | 6.5% | 6.5% |  | 50% | ❌ 44 pts to go |
| P02 | 368 | 7.9% | 7.9% |  | 50% | ❌ 42 pts to go |
| P03 | 225 | 1.3% | 1.3% |  | 40% | ❌ 39 pts to go |
| P04 | 1615 | 1.1% | 1.1% |  | 30% | ❌ 29 pts to go |
| P05 | 378 | 0.3% | 0.3% |  | 20% | ❌ 20 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2431 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 161 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 248 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 0.5% | 0.5% |  | 50% | ❌ 50 pts to go |
| P10 | 2588 | 0.1% | 0.1% |  | n/a | no target |
| P11 | 499 | 1.4% | 1.4% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50789 | 0.0% | 0.0% |  | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 91 | 4.4% | 4.4% |  | 50% | ❌ 46 pts to go |
| P01_GOLD | 583 | 45.6% | 45.6% |  | 85% | ❌ 39 pts to go |
| P02 | 368 | 62.8% | 62.8% |  | 90% | ❌ 27 pts to go |
| P03 | 225 | 45.8% | 45.8% |  | 85% | ❌ 39 pts to go |
| P04 | 1615 | 61.2% | 61.2% |  | 85% | ❌ 24 pts to go |
| P05 | 378 | 22.0% | 22.0% |  | 60% | ❌ 38 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2431 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 161 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 248 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 87.0% | 87.0% |  | 100% | ❌ 13 pts to go |
| P10 | 2588 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 499 | 18.4% | 18.4% |  | 60% | ❌ 42 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50789 | 0.0% | 0.0% |  | n/a | no target |

### `solicitation_or_tender_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 91 | 2.2% | 2.2% |  | 30% | ❌ 28 pts to go |
| P01_GOLD | 583 | 38.1% | 38.1% |  | 80% | ❌ 42 pts to go |
| P02 | 368 | 22.6% | 22.6% |  | 60% | ❌ 37 pts to go |
| P03 | 225 | 40.9% | 40.9% |  | 80% | ❌ 39 pts to go |
| P04 | 1615 | 10.0% | 10.0% |  | 50% | ❌ 40 pts to go |
| P05 | 378 | 12.4% | 12.4% |  | 40% | ❌ 28 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2431 | 0.2% | 0.2% |  | n/a | no target |
| P06 | 161 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 248 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 11.1% | 11.1% |  | 50% | ❌ 39 pts to go |
| P10 | 2588 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 499 | 11.6% | 11.6% |  | 40% | ❌ 28 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50789 | 0.0% | 0.0% |  | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 91 | 3.3% | 3.3% |  | n/a | no target |
| P01_GOLD | 583 | 44.3% | 44.3% |  | 85% | ❌ 41 pts to go |
| P02 | 368 | 54.3% | 54.3% |  | 90% | ❌ 36 pts to go |
| P03 | 225 | 50.7% | 50.7% |  | 85% | ❌ 34 pts to go |
| P04 | 1615 | 52.6% | 52.6% |  | 85% | ❌ 32 pts to go |
| P05 | 378 | 14.8% | 14.8% |  | 50% | ❌ 35 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2431 | 0.1% | 0.1% |  | n/a | no target |
| P06 | 161 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 248 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 90.8% | 90.8% |  | 100% | 🟡 9 pts to go |
| P10 | 2588 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 499 | 18.6% | 18.6% |  | 60% | ❌ 41 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50789 | 0.0% | 0.0% |  | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 91 | 2.2% | 2.2% |  | n/a | no target |
| P01_GOLD | 583 | 13.6% | 13.6% |  | 60% | ❌ 46 pts to go |
| P02 | 368 | 7.3% | 7.3% |  | 50% | ❌ 43 pts to go |
| P03 | 225 | 10.2% | 10.2% |  | 50% | ❌ 40 pts to go |
| P04 | 1615 | 4.3% | 4.3% |  | 40% | ❌ 36 pts to go |
| P05 | 378 | 1.3% | 1.3% |  | 20% | ❌ 19 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2431 | 0.1% | 0.1% |  | n/a | no target |
| P06 | 161 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 248 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 2.4% | 2.4% |  | 50% | ❌ 48 pts to go |
| P10 | 2588 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 499 | 4.8% | 4.8% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50789 | 0.0% | 0.0% |  | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 91 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 583 | 36.4% | 36.4% |  | 80% | ❌ 44 pts to go |
| P02 | 368 | 59.5% | 59.5% |  | 90% | ❌ 30 pts to go |
| P03 | 225 | 36.9% | 36.9% |  | 80% | ❌ 43 pts to go |
| P04 | 1615 | 51.2% | 51.2% |  | 85% | ❌ 34 pts to go |
| P05 | 378 | 5.3% | 5.3% |  | 50% | ❌ 45 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2431 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 161 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 248 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 75.9% | 75.9% |  | 95% | ❌ 19 pts to go |
| P10 | 2588 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 499 | 15.8% | 15.8% |  | 50% | ❌ 34 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50789 | 0.0% | 0.0% |  | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 91 | 1.1% | 1.1% |  | n/a | no target |
| P01_GOLD | 583 | 8.7% | 8.7% |  | 50% | ❌ 41 pts to go |
| P02 | 368 | 7.9% | 7.9% |  | 50% | ❌ 42 pts to go |
| P03 | 225 | 2.2% | 2.2% |  | 30% | ❌ 28 pts to go |
| P04 | 1615 | 1.1% | 1.1% |  | 30% | ❌ 29 pts to go |
| P05 | 378 | 0.0% | 0.0% |  | n/a | no target |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2431 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 161 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 248 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 0.3% | 0.3% |  | n/a | no target |
| P10 | 2588 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 499 | 1.4% | 1.4% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50789 | 0.0% | 0.0% |  | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 100.0% |  | n/a | no target |
| P01T | 91 | 3.3% | 100.0% |  | 60% | ❌ 57 pts to go |
| P01_GOLD | 583 | 72.7% | 100.0% |  | 100% | ❌ 27 pts to go |
| P02 | 368 | 75.3% | 100.0% |  | 100% | ❌ 25 pts to go |
| P03 | 225 | 74.7% | 100.0% |  | 100% | ❌ 25 pts to go |
| P04 | 1615 | 59.7% | 100.0% |  | 95% | ❌ 35 pts to go |
| P05 | 378 | 18.0% | 100.0% |  | 70% | ❌ 52 pts to go |
| P06M | 167 | 0.0% | 100.0% |  | n/a | no target |
| P06T | 2431 | 0.2% | 100.0% |  | n/a | no target |
| P06 | 161 | 0.0% | 100.0% |  | 50% | ❌ 50 pts to go |
| P07 | 248 | 0.0% | 100.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 100.0% |  | n/a | no target |
| P09 | 369 | 98.6% | 100.0% |  | 100% | 🟡 1 pts to go |
| P10 | 2588 | 0.0% | 100.0% |  | n/a | no target |
| P11 | 499 | 26.3% | 100.0% |  | 70% | ❌ 44 pts to go |
| P12 | 21 | 0.0% | 100.0% |  | n/a | no target |
| P13 | 50789 | 0.0% | 0.0% |  | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 85.0% | 85.0% |  | 70% | ✅ met |
| P01T | 91 | 80.2% | 80.2% |  | 60% | ✅ met |
| P01_GOLD | 583 | 78.9% | 78.9% |  | 90% | ❌ 11 pts to go |
| P02 | 368 | 64.9% | 64.9% |  | 85% | ❌ 20 pts to go |
| P03 | 225 | 80.9% | 80.9% |  | 90% | 🟡 9 pts to go |
| P04 | 1615 | 53.9% | 53.9% |  | 75% | ❌ 21 pts to go |
| P05 | 378 | 52.6% | 52.6% |  | 50% | ✅ met |
| P06M | 167 | 70.1% | 70.1% |  | n/a | no target |
| P06T | 2431 | 60.4% | 60.4% |  | n/a | no target |
| P06 | 161 | 44.1% | 44.1% |  | 40% | ✅ met |
| P07 | 248 | 36.7% | 36.7% |  | 50% | ❌ 13 pts to go |
| P08 | 3037 | 27.7% | 27.7% |  | 50% | ❌ 22 pts to go |
| P09 | 369 | 53.7% | 53.7% |  | 80% | ❌ 26 pts to go |
| P10 | 2588 | 25.0% | 25.0% |  | 40% | ❌ 15 pts to go |
| P11 | 499 | 37.1% | 37.1% |  | 60% | ❌ 23 pts to go |
| P12 | 21 | 47.6% | 47.6% |  | 85% | ❌ 37 pts to go |
| P13 | 50789 | 91.7% | 91.7% |  | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 35.0% | 35.0% |  | n/a | no target |
| P01T | 91 | 62.6% | 62.6% |  | n/a | no target |
| P01_GOLD | 583 | 75.0% | 75.0% |  | 95% | ❌ 20 pts to go |
| P02 | 368 | 80.4% | 80.4% |  | 95% | ❌ 15 pts to go |
| P03 | 225 | 77.3% | 77.3% |  | 95% | ❌ 18 pts to go |
| P04 | 1615 | 78.1% | 78.1% |  | 95% | ❌ 17 pts to go |
| P05 | 378 | 52.9% | 52.9% |  | 70% | ❌ 17 pts to go |
| P06M | 167 | 6.6% | 6.6% |  | n/a | no target |
| P06T | 2431 | 75.3% | 75.3% |  | n/a | no target |
| P06 | 161 | 50.3% | 50.3% |  | 80% | ❌ 30 pts to go |
| P07 | 248 | 46.8% | 46.8% |  | 70% | ❌ 23 pts to go |
| P08 | 3037 | 29.1% | 29.1% |  | 70% | ❌ 41 pts to go |
| P09 | 369 | 88.1% | 88.1% |  | 100% | ❌ 12 pts to go |
| P10 | 2588 | 17.9% | 17.9% |  | 70% | ❌ 52 pts to go |
| P11 | 499 | 37.9% | 37.9% |  | 75% | ❌ 37 pts to go |
| P12 | 21 | 85.7% | 85.7% |  | n/a | no target |
| P13 | 50789 | 0.0% | 0.0% |  | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 35.0% | 35.0% |  | n/a | no target |
| P01T | 91 | 19.8% | 19.8% |  | n/a | no target |
| P01_GOLD | 583 | 50.1% | 50.1% |  | 60% | 🟡 10 pts to go |
| P02 | 368 | 63.0% | 63.0% |  | 60% | ✅ met |
| P03 | 225 | 56.9% | 56.9% |  | 60% | 🟡 3 pts to go |
| P04 | 1615 | 53.6% | 53.6% |  | 55% | 🟡 1 pts to go |
| P05 | 378 | 23.5% | 23.5% |  | 50% | ❌ 26 pts to go |
| P06M | 167 | 13.2% | 13.2% |  | n/a | no target |
| P06T | 2431 | 53.5% | 53.5% |  | n/a | no target |
| P06 | 161 | 49.1% | 49.1% |  | n/a | no target |
| P07 | 248 | 43.5% | 43.5% |  | 55% | ❌ 12 pts to go |
| P08 | 3037 | 43.6% | 43.6% |  | 50% | 🟡 6 pts to go |
| P09 | 369 | 71.5% | 71.5% |  | 70% | ✅ met |
| P10 | 2588 | 49.0% | 49.0% |  | 55% | 🟡 6 pts to go |
| P11 | 499 | 41.3% | 41.3% |  | 50% | 🟡 9 pts to go |
| P12 | 21 | 85.7% | 85.7% |  | n/a | no target |
| P13 | 50789 | 0.0% | 0.0% |  | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 35.0% | 35.0% |  | n/a | no target |
| P01T | 91 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 583 | 33.3% | 33.3% |  | 70% | ❌ 37 pts to go |
| P02 | 368 | 42.1% | 42.1% |  | 70% | ❌ 28 pts to go |
| P03 | 225 | 38.7% | 38.7% |  | 70% | ❌ 31 pts to go |
| P04 | 1615 | 33.2% | 33.2% |  | 65% | ❌ 32 pts to go |
| P05 | 378 | 16.7% | 16.7% |  | 60% | ❌ 43 pts to go |
| P06M | 167 | 6.6% | 6.6% |  | n/a | no target |
| P06T | 2431 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 161 | 59.0% | 59.0% |  | 40% | ✅ met |
| P07 | 248 | 65.3% | 65.3% |  | 85% | ❌ 20 pts to go |
| P08 | 3037 | 64.5% | 64.5% |  | 85% | ❌ 20 pts to go |
| P09 | 369 | 52.3% | 52.3% |  | 85% | ❌ 33 pts to go |
| P10 | 2588 | 65.1% | 65.1% |  | 85% | ❌ 20 pts to go |
| P11 | 499 | 47.9% | 47.9% |  | 75% | ❌ 27 pts to go |
| P12 | 21 | 4.8% | 4.8% |  | n/a | no target |
| P13 | 50789 | 100.0% | 100.0% |  | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 45.0% | 45.0% |  | n/a | no target |
| P01T | 91 | 11.0% | 11.0% |  | n/a | no target |
| P01_GOLD | 583 | 85.4% | 85.4% |  | 90% | 🟡 5 pts to go |
| P02 | 368 | 81.2% | 81.2% |  | 90% | 🟡 9 pts to go |
| P03 | 225 | 86.7% | 86.7% |  | 90% | 🟡 3 pts to go |
| P04 | 1615 | 60.6% | 60.6% |  | 85% | ❌ 24 pts to go |
| P05 | 378 | 34.7% | 34.7% |  | 70% | ❌ 35 pts to go |
| P06M | 167 | 10.2% | 10.2% |  | n/a | no target |
| P06T | 2431 | 2.6% | 2.6% |  | n/a | no target |
| P06 | 161 | 96.9% | 96.9% |  | 50% | ✅ met |
| P07 | 248 | 94.4% | 94.4% |  | 100% | 🟡 6 pts to go |
| P08 | 3037 | 92.9% | 92.9% |  | 100% | 🟡 7 pts to go |
| P09 | 369 | 80.2% | 80.2% |  | 100% | ❌ 20 pts to go |
| P10 | 2588 | 100.0% | 100.0% |  | 100% | ✅ met |
| P11 | 499 | 85.2% | 85.2% |  | 100% | ❌ 15 pts to go |
| P12 | 21 | 38.1% | 38.1% |  | n/a | no target |
| P13 | 50789 | 100.0% | 100.0% |  | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 35.0% | 35.0% |  | n/a | no target |
| P01T | 91 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 583 | 36.7% | 36.7% |  | 70% | ❌ 33 pts to go |
| P02 | 368 | 45.1% | 45.1% |  | 75% | ❌ 30 pts to go |
| P03 | 225 | 41.8% | 41.8% |  | 75% | ❌ 33 pts to go |
| P04 | 1615 | 32.4% | 32.4% |  | 70% | ❌ 38 pts to go |
| P05 | 378 | 14.0% | 14.0% |  | 55% | ❌ 41 pts to go |
| P06M | 167 | 6.6% | 6.6% |  | n/a | no target |
| P06T | 2431 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 161 | 40.4% | 40.4% |  | n/a | no target |
| P07 | 248 | 35.9% | 35.9% |  | 70% | ❌ 34 pts to go |
| P08 | 3037 | 47.0% | 47.0% |  | 75% | ❌ 28 pts to go |
| P09 | 369 | 52.8% | 52.8% |  | 85% | ❌ 32 pts to go |
| P10 | 2588 | 50.8% | 50.8% |  | 80% | ❌ 29 pts to go |
| P11 | 499 | 36.3% | 36.3% |  | 70% | ❌ 34 pts to go |
| P12 | 21 | 19.0% | 19.0% |  | n/a | no target |
| P13 | 50789 | 0.0% | 0.0% |  | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 35.0% | 35.0% |  | n/a | no target |
| P01T | 91 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 583 | 49.1% | 49.1% |  | 90% | ❌ 41 pts to go |
| P02 | 368 | 57.9% | 57.9% |  | 90% | ❌ 32 pts to go |
| P03 | 225 | 54.7% | 54.7% |  | 90% | ❌ 35 pts to go |
| P04 | 1615 | 42.7% | 42.7% |  | 85% | ❌ 42 pts to go |
| P05 | 378 | 22.8% | 22.8% |  | 75% | ❌ 52 pts to go |
| P06M | 167 | 6.6% | 6.6% |  | n/a | no target |
| P06T | 2431 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 161 | 87.6% | 87.6% |  | n/a | no target |
| P07 | 248 | 87.9% | 87.9% |  | 100% | ❌ 12 pts to go |
| P08 | 3037 | 85.3% | 85.3% |  | 100% | ❌ 15 pts to go |
| P09 | 369 | 58.8% | 58.8% |  | n/a | no target |
| P10 | 2588 | 87.6% | 87.6% |  | 100% | ❌ 12 pts to go |
| P11 | 499 | 64.1% | 64.1% |  | n/a | no target |
| P12 | 21 | 14.3% | 14.3% |  | n/a | no target |
| P13 | 50789 | 0.0% | 0.0% |  | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 91 | 19.8% | 19.8% |  | n/a | no target · QC vendors: 1 rows, 0.0% filled |
| P01_GOLD | 583 | 46.8% | 46.8% |  | 95% | ❌ 48 pts to go · QC vendors: 46 rows, 87.0% filled |
| P02 | 368 | 66.6% | 66.6% |  | 95% | ❌ 28 pts to go · QC vendors: 91 rows, 100.0% filled |
| P03 | 225 | 53.8% | 53.8% |  | 95% | ❌ 41 pts to go · QC vendors: 16 rows, 87.5% filled |
| P04 | 1615 | 59.7% | 59.7% |  | 95% | ❌ 35 pts to go · QC vendors: 446 rows, 97.3% filled |
| P05 | 378 | 11.1% | 11.1% |  | n/a | no target · QC vendors: 20 rows, 80.0% filled |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2431 | 53.5% | 53.5% |  | n/a | no target · QC vendors: 4 rows, 0.0% filled |
| P06 | 161 | 21.7% | 21.7% |  | n/a | no target · QC vendors: 14 rows, 92.9% filled |
| P07 | 248 | 16.9% | 16.9% |  | n/a | no target · QC vendors: 23 rows, 91.3% filled |
| P08 | 3037 | 23.4% | 23.4% |  | n/a | no target · QC vendors: 438 rows, 99.8% filled |
| P09 | 369 | 81.8% | 81.8% |  | 95% | ❌ 13 pts to go · QC vendors: 153 rows, 100.0% filled |
| P10 | 2588 | 15.5% | 15.5% |  | n/a | no target · QC vendors: 241 rows, 90.5% filled |
| P11 | 499 | 26.3% | 26.3% |  | n/a | no target · QC vendors: 65 rows, 95.4% filled |
| P12 | 21 | 71.4% | 71.4% |  | n/a | no target · QC vendors: 3 rows, 100.0% filled |
| P13 | 50789 | 0.0% | 0.0% |  | n/a | no target |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 91 | 46.2% | 46.2% |  | n/a | no target · vendors with a registry record: 42 rows, 100.0% filled |
| P01_GOLD | 583 | 84.6% | 84.6% |  | 100% | ❌ 15 pts to go · vendors with a registry record: 493 rows, 100.0% filled |
| P02 | 368 | 87.8% | 87.8% |  | 100% | ❌ 12 pts to go · vendors with a registry record: 323 rows, 100.0% filled |
| P03 | 225 | 87.6% | 87.6% |  | 100% | ❌ 12 pts to go · vendors with a registry record: 197 rows, 100.0% filled |
| P04 | 1615 | 80.8% | 80.8% |  | 100% | ❌ 19 pts to go · vendors with a registry record: 1305 rows, 100.0% filled |
| P05 | 378 | 58.2% | 58.2% |  | n/a | no target · vendors with a registry record: 220 rows, 100.0% filled |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2431 | 74.0% | 74.0% |  | n/a | no target · vendors with a registry record: 1799 rows, 100.0% filled |
| P06 | 161 | 51.6% | 51.6% |  | n/a | no target · vendors with a registry record: 83 rows, 100.0% filled |
| P07 | 248 | 47.6% | 47.6% |  | n/a | no target · vendors with a registry record: 118 rows, 100.0% filled |
| P08 | 3037 | 30.0% | 30.0% |  | n/a | no target · vendors with a registry record: 910 rows, 100.0% filled |
| P09 | 369 | 91.3% | 91.3% |  | n/a | no target · vendors with a registry record: 337 rows, 100.0% filled |
| P10 | 2588 | 18.4% | 18.4% |  | n/a | no target · vendors with a registry record: 477 rows, 100.0% filled |
| P11 | 499 | 41.7% | 41.7% |  | n/a | no target · vendors with a registry record: 208 rows, 100.0% filled |
| P12 | 21 | 71.4% | 71.4% |  | n/a | no target · vendors with a registry record: 15 rows, 100.0% filled |
| P13 | 50789 | 0.0% | 0.0% |  | n/a | no target |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 90.0% | 90.0% |  | 90% | ✅ met |
| P01T | 91 | 92.3% | 92.3% |  | 90% | ✅ met |
| P01_GOLD | 583 | 84.4% | 84.4% |  | 95% | ❌ 11 pts to go |
| P02 | 368 | 89.7% | 89.7% |  | 95% | 🟡 5 pts to go |
| P03 | 225 | 80.4% | 80.4% |  | 85% | 🟡 5 pts to go |
| P04 | 1615 | 72.8% | 72.8% |  | 90% | ❌ 17 pts to go |
| P05 | 378 | 66.9% | 66.9% |  | 75% | 🟡 8 pts to go |
| P06M | 167 | 79.6% | 79.6% |  | n/a | no target |
| P06T | 2431 | 52.0% | 52.0% |  | n/a | no target |
| P06 | 161 | 55.9% | 55.9% |  | 80% | ❌ 24 pts to go |
| P07 | 248 | 50.8% | 50.8% |  | 80% | ❌ 29 pts to go |
| P08 | 3037 | 35.8% | 35.8% |  | 75% | ❌ 39 pts to go |
| P09 | 369 | 76.7% | 76.7% |  | 95% | ❌ 18 pts to go |
| P10 | 2588 | 32.1% | 32.1% |  | 70% | ❌ 38 pts to go |
| P11 | 499 | 26.9% | 26.9% |  | 65% | ❌ 38 pts to go |
| P12 | 21 | 71.4% | 71.4% |  | 80% | 🟡 9 pts to go |
| P13 | 50789 | 29.4% | 29.4% |  | 60% | ❌ 31 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 40.0% | 40.0% |  | 50% | 🟡 10 pts to go |
| P01T | 91 | 15.4% | 15.4% |  | n/a | no target |
| P01_GOLD | 583 | 17.2% | 17.2% |  | 40% | ❌ 23 pts to go |
| P02 | 368 | 19.0% | 19.0% |  | 40% | ❌ 21 pts to go |
| P03 | 225 | 25.3% | 25.3% |  | 40% | ❌ 15 pts to go |
| P04 | 1615 | 22.9% | 22.9% |  | 40% | ❌ 17 pts to go |
| P05 | 378 | 12.2% | 12.2% |  | 25% | ❌ 13 pts to go |
| P06M | 167 | 13.2% | 13.2% |  | n/a | no target |
| P06T | 2431 | 11.0% | 11.0% |  | n/a | no target |
| P06 | 161 | 7.5% | 7.5% |  | 35% | ❌ 28 pts to go |
| P07 | 248 | 6.5% | 6.5% |  | 35% | ❌ 28 pts to go |
| P08 | 3037 | 6.5% | 6.5% |  | 35% | ❌ 28 pts to go |
| P09 | 369 | 17.1% | 17.1% |  | n/a | no target |
| P10 | 2588 | 5.6% | 5.6% |  | 30% | ❌ 24 pts to go |
| P11 | 499 | 9.0% | 9.0% |  | n/a | no target |
| P12 | 21 | 19.0% | 19.0% |  | n/a | no target |
| P13 | 50789 | 17.6% | 17.6% |  | 30% | ❌ 12 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 95.0% | 95.0% |  | 100% | 🟡 5 pts to go |
| P01T | 91 | 93.4% | 93.4% |  | 100% | 🟡 7 pts to go |
| P01_GOLD | 583 | 89.0% | 89.0% |  | 100% | ❌ 11 pts to go |
| P02 | 368 | 95.4% | 95.4% |  | 100% | 🟡 5 pts to go |
| P03 | 225 | 94.2% | 94.2% |  | 100% | 🟡 6 pts to go |
| P04 | 1615 | 90.8% | 90.8% |  | 100% | 🟡 9 pts to go |
| P05 | 378 | 82.5% | 82.5% |  | 100% | ❌ 18 pts to go |
| P06M | 167 | 69.5% | 69.5% |  | n/a | no target |
| P06T | 2431 | 78.4% | 78.4% |  | n/a | no target |
| P06 | 161 | 68.3% | 68.3% |  | 95% | ❌ 27 pts to go |
| P07 | 248 | 66.5% | 66.5% |  | 95% | ❌ 28 pts to go |
| P08 | 3037 | 64.5% | 64.5% |  | 95% | ❌ 30 pts to go |
| P09 | 369 | 98.4% | 98.4% |  | 100% | 🟡 2 pts to go |
| P10 | 2588 | 63.6% | 63.6% |  | 95% | ❌ 31 pts to go |
| P11 | 499 | 37.7% | 37.7% |  | 80% | ❌ 42 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50789 | 74.3% | 74.3% |  | 95% | ❌ 21 pts to go |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 90.0% | 90.0% |  | n/a | no target |
| P01T | 91 | 80.2% | 80.2% |  | n/a | no target |
| P01_GOLD | 583 | 69.6% | 69.6% |  | 90% | ❌ 20 pts to go |
| P02 | 368 | 78.3% | 78.3% |  | 95% | ❌ 17 pts to go |
| P03 | 225 | 74.7% | 74.7% |  | 95% | ❌ 20 pts to go |
| P04 | 1615 | 85.4% | 85.4% |  | 95% | 🟡 10 pts to go |
| P05 | 378 | 74.9% | 74.9% |  | 90% | ❌ 15 pts to go |
| P06M | 167 | 83.8% | 83.8% |  | n/a | no target |
| P06T | 2431 | 77.3% | 77.3% |  | n/a | no target |
| P06 | 161 | 64.6% | 64.6% |  | 95% | ❌ 30 pts to go |
| P07 | 248 | 64.9% | 64.9% |  | 90% | ❌ 25 pts to go |
| P08 | 3037 | 74.5% | 74.5% |  | 95% | ❌ 20 pts to go |
| P09 | 369 | 89.7% | 89.7% |  | 100% | ❌ 10 pts to go |
| P10 | 2588 | 71.4% | 71.4% |  | 95% | ❌ 24 pts to go |
| P11 | 499 | 27.5% | 27.5% |  | 75% | ❌ 48 pts to go |
| P12 | 21 | 85.7% | 85.7% |  | n/a | no target |
| P13 | 50789 | 76.9% | 76.9% |  | 95% | ❌ 18 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 80.0% | 80.0% |  | n/a | no target |
| P01T | 91 | 91.2% | 91.2% |  | 95% | 🟡 4 pts to go |
| P01_GOLD | 583 | 68.8% | 68.8% |  | 90% | ❌ 21 pts to go |
| P02 | 368 | 77.7% | 77.7% |  | 95% | ❌ 17 pts to go |
| P03 | 225 | 70.2% | 70.2% |  | 95% | ❌ 25 pts to go |
| P04 | 1615 | 63.3% | 63.3% |  | 90% | ❌ 27 pts to go |
| P05 | 378 | 78.6% | 78.6% |  | 95% | ❌ 16 pts to go |
| P06M | 167 | 84.4% | 84.4% |  | n/a | no target |
| P06T | 2431 | 93.7% | 93.7% |  | n/a | no target |
| P06 | 161 | 88.8% | 88.8% |  | 100% | ❌ 11 pts to go |
| P07 | 248 | 87.1% | 87.1% |  | 100% | ❌ 13 pts to go |
| P08 | 3037 | 90.2% | 90.2% |  | 100% | 🟡 10 pts to go |
| P09 | 369 | 53.1% | 53.1% |  | n/a | no target |
| P10 | 2588 | 89.3% | 89.3% |  | 100% | ❌ 11 pts to go |
| P11 | 499 | 31.7% | 31.7% |  | 80% | ❌ 48 pts to go |
| P12 | 21 | 61.9% | 61.9% |  | n/a | no target |
| P13 | 50789 | 76.3% | 76.3% |  | 95% | ❌ 19 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 15.0% | 15.0% |  | n/a | no target |
| P01T | 91 | 9.9% | 9.9% |  | n/a | no target |
| P01_GOLD | 583 | 5.5% | 5.5% |  | 25% | ❌ 20 pts to go |
| P02 | 368 | 19.8% | 19.8% |  | 40% | ❌ 20 pts to go |
| P03 | 225 | 0.9% | 0.9% |  | 20% | ❌ 19 pts to go |
| P04 | 1615 | 0.8% | 0.8% |  | 20% | ❌ 19 pts to go |
| P05 | 378 | 0.8% | 0.8% |  | 15% | ❌ 14 pts to go |
| P06M | 167 | 1.8% | 1.8% |  | n/a | no target |
| P06T | 2431 | 0.1% | 0.1% |  | n/a | no target |
| P06 | 161 | 2.5% | 2.5% |  | n/a | no target |
| P07 | 248 | 4.4% | 4.4% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 5.4% | 5.4% |  | n/a | no target |
| P10 | 2588 | 0.3% | 0.3% |  | n/a | no target |
| P11 | 499 | 0.4% | 0.4% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50789 | 0.1% | 0.1% |  | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 40.0% | 40.0% |  | n/a | no target |
| P01T | 91 | 38.5% | 38.5% |  | 70% | ❌ 32 pts to go |
| P01_GOLD | 583 | 45.1% | 45.1% |  | 80% | ❌ 35 pts to go |
| P02 | 368 | 66.6% | 66.6% |  | 90% | ❌ 23 pts to go |
| P03 | 225 | 20.0% | 20.0% |  | 60% | ❌ 40 pts to go |
| P04 | 1615 | 49.2% | 49.2% |  | 85% | ❌ 36 pts to go |
| P05 | 378 | 12.7% | 12.7% |  | 50% | ❌ 37 pts to go |
| P06M | 167 | 5.4% | 5.4% |  | n/a | no target |
| P06T | 2431 | 2.3% | 2.3% |  | n/a | no target |
| P06 | 161 | 18.6% | 18.6% |  | n/a | no target |
| P07 | 248 | 19.4% | 19.4% |  | n/a | no target |
| P08 | 3037 | 0.5% | 0.5% |  | n/a | no target |
| P09 | 369 | 81.0% | 81.0% |  | 95% | ❌ 14 pts to go |
| P10 | 2588 | 3.1% | 3.1% |  | n/a | no target |
| P11 | 499 | 33.3% | 33.3% |  | n/a | no target |
| P12 | 21 | 33.3% | 33.3% |  | n/a | no target |
| P13 | 50789 | 0.9% | 0.9% |  | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 5.0% | 5.0% |  | n/a | no target |
| P01T | 91 | 18.7% | 18.7% |  | n/a | no target |
| P01_GOLD | 583 | 34.0% | 34.0% |  | 70% | ❌ 36 pts to go |
| P02 | 368 | 39.9% | 39.9% |  | 75% | ❌ 35 pts to go |
| P03 | 225 | 20.0% | 20.0% |  | 55% | ❌ 35 pts to go |
| P04 | 1615 | 48.5% | 48.5% |  | 75% | ❌ 26 pts to go |
| P05 | 378 | 10.8% | 10.8% |  | 50% | ❌ 39 pts to go |
| P06M | 167 | 1.8% | 1.8% |  | n/a | no target |
| P06T | 2431 | 1.1% | 1.1% |  | n/a | no target |
| P06 | 161 | 10.6% | 10.6% |  | n/a | no target |
| P07 | 248 | 10.5% | 10.5% |  | n/a | no target |
| P08 | 3037 | 0.5% | 0.5% |  | n/a | no target |
| P09 | 369 | 77.2% | 77.2% |  | 95% | ❌ 18 pts to go |
| P10 | 2588 | 1.8% | 1.8% |  | n/a | no target |
| P11 | 499 | 32.7% | 32.7% |  | n/a | no target |
| P12 | 21 | 19.0% | 19.0% |  | n/a | no target |
| P13 | 50789 | 0.6% | 0.6% |  | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 15.0% | 15.0% |  | n/a | no target |
| P01T | 91 | 6.6% | 6.6% |  | n/a | no target |
| P01_GOLD | 583 | 48.0% | 48.0% |  | 80% | ❌ 32 pts to go |
| P02 | 368 | 41.3% | 41.3% |  | 75% | ❌ 34 pts to go |
| P03 | 225 | 25.3% | 25.3% |  | 70% | ❌ 45 pts to go |
| P04 | 1615 | 35.4% | 35.4% |  | 70% | ❌ 35 pts to go |
| P05 | 378 | 11.1% | 11.1% |  | 50% | ❌ 39 pts to go |
| P06M | 167 | 0.6% | 0.6% |  | n/a | no target |
| P06T | 2431 | 0.6% | 0.6% |  | n/a | no target |
| P06 | 161 | 16.1% | 16.1% |  | n/a | no target |
| P07 | 248 | 1.6% | 1.6% |  | n/a | no target |
| P08 | 3037 | 0.4% | 0.4% |  | n/a | no target |
| P09 | 369 | 40.9% | 40.9% |  | 80% | ❌ 39 pts to go |
| P10 | 2588 | 1.0% | 1.0% |  | n/a | no target |
| P11 | 499 | 16.8% | 16.8% |  | n/a | no target |
| P12 | 21 | 33.3% | 33.3% |  | n/a | no target |
| P13 | 50789 | 0.3% | 0.3% |  | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 20.0% | 20.0% |  | n/a | no target |
| P01T | 91 | 15.4% | 15.4% |  | 60% | ❌ 45 pts to go |
| P01_GOLD | 583 | 20.6% | 20.6% |  | 70% | ❌ 49 pts to go |
| P02 | 368 | 3.3% | 3.3% |  | 50% | ❌ 47 pts to go |
| P03 | 225 | 5.8% | 5.8% |  | 55% | ❌ 49 pts to go |
| P04 | 1615 | 0.6% | 0.6% |  | 40% | ❌ 39 pts to go |
| P05 | 378 | 3.2% | 3.2% |  | 40% | ❌ 37 pts to go |
| P06M | 167 | 0.6% | 0.6% |  | n/a | no target |
| P06T | 2431 | 0.6% | 0.6% |  | n/a | no target |
| P06 | 161 | 14.3% | 14.3% |  | n/a | no target |
| P07 | 248 | 3.6% | 3.6% |  | n/a | no target |
| P08 | 3037 | 0.5% | 0.5% |  | n/a | no target |
| P09 | 369 | 2.7% | 2.7% |  | n/a | no target |
| P10 | 2588 | 0.5% | 0.5% |  | n/a | no target |
| P11 | 499 | 0.4% | 0.4% |  | n/a | no target |
| P12 | 21 | 9.5% | 9.5% |  | n/a | no target |
| P13 | 50789 | 0.2% | 0.2% |  | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 20.0% | 20.0% |  | n/a | no target |
| P01T | 91 | 30.8% | 30.8% |  | 65% | ❌ 34 pts to go |
| P01_GOLD | 583 | 34.1% | 34.1% |  | 70% | ❌ 36 pts to go |
| P02 | 368 | 0.8% | 0.8% |  | 50% | ❌ 49 pts to go |
| P03 | 225 | 12.4% | 12.4% |  | 60% | ❌ 48 pts to go |
| P04 | 1615 | 0.4% | 0.4% |  | 40% | ❌ 40 pts to go |
| P05 | 378 | 7.9% | 7.9% |  | 45% | ❌ 37 pts to go |
| P06M | 167 | 1.2% | 1.2% |  | n/a | no target |
| P06T | 2431 | 0.3% | 0.3% |  | n/a | no target |
| P06 | 161 | 35.4% | 35.4% |  | n/a | no target |
| P07 | 248 | 6.9% | 6.9% |  | n/a | no target |
| P08 | 3037 | 0.3% | 0.3% |  | n/a | no target |
| P09 | 369 | 3.8% | 3.8% |  | n/a | no target |
| P10 | 2588 | 0.8% | 0.8% |  | n/a | no target |
| P11 | 499 | 1.6% | 1.6% |  | n/a | no target |
| P12 | 21 | 4.8% | 4.8% |  | n/a | no target |
| P13 | 50789 | 0.1% | 0.1% |  | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 10.0% | 10.0% |  | n/a | no target |
| P01T | 91 | 19.8% | 19.8% |  | n/a | no target |
| P01_GOLD | 583 | 17.8% | 17.8% |  | 50% | ❌ 32 pts to go |
| P02 | 368 | 5.2% | 5.2% |  | n/a | no target |
| P03 | 225 | 34.7% | 34.7% |  | 60% | ❌ 25 pts to go |
| P04 | 1615 | 4.6% | 4.6% |  | n/a | no target |
| P05 | 378 | 7.9% | 7.9% |  | n/a | no target |
| P06M | 167 | 2.4% | 2.4% |  | n/a | no target |
| P06T | 2431 | 0.9% | 0.9% |  | n/a | no target |
| P06 | 161 | 18.0% | 18.0% |  | n/a | no target |
| P07 | 248 | 11.7% | 11.7% |  | n/a | no target |
| P08 | 3037 | 0.5% | 0.5% |  | n/a | no target |
| P09 | 369 | 6.5% | 6.5% |  | n/a | no target |
| P10 | 2588 | 1.4% | 1.4% |  | n/a | no target |
| P11 | 499 | 1.6% | 1.6% |  | n/a | no target |
| P12 | 21 | 4.8% | 4.8% |  | n/a | no target |
| P13 | 50789 | 0.4% | 0.4% |  | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 5.0% | 5.0% |  | 15% | 🟡 10 pts to go |
| P01T | 91 | 4.4% | 4.4% |  | 15% | ❌ 11 pts to go |
| P01_GOLD | 583 | 10.5% | 10.5% |  | 40% | ❌ 30 pts to go |
| P02 | 368 | 1.4% | 1.4% |  | 25% | ❌ 24 pts to go |
| P03 | 225 | 4.0% | 4.0% |  | 25% | ❌ 21 pts to go |
| P04 | 1615 | 0.8% | 0.8% |  | 15% | ❌ 14 pts to go |
| P05 | 378 | 2.1% | 2.1% |  | 15% | ❌ 13 pts to go |
| P06M | 167 | 2.4% | 2.4% |  | 15% | ❌ 13 pts to go |
| P06T | 2431 | 0.7% | 0.7% |  | 15% | ❌ 14 pts to go |
| P06 | 161 | 5.6% | 5.6% |  | 15% | 🟡 9 pts to go |
| P07 | 248 | 2.4% | 2.4% |  | 15% | ❌ 13 pts to go |
| P08 | 3037 | 0.8% | 0.8% |  | 15% | ❌ 14 pts to go |
| P09 | 369 | 0.3% | 0.3% |  | 15% | ❌ 15 pts to go |
| P10 | 2588 | 0.9% | 0.9% |  | 15% | ❌ 14 pts to go |
| P11 | 499 | 0.2% | 0.2% |  | 15% | ❌ 15 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P13 | 50789 | 0.6% | 0.6% |  | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P01T | 91 | 7.7% | 7.7% |  | 25% | ❌ 17 pts to go |
| P01_GOLD | 583 | 7.4% | 7.4% |  | 25% | ❌ 18 pts to go |
| P02 | 368 | 2.7% | 2.7% |  | 15% | ❌ 12 pts to go |
| P03 | 225 | 2.7% | 2.7% |  | 15% | ❌ 12 pts to go |
| P04 | 1615 | 0.5% | 0.5% |  | 15% | ❌ 14 pts to go |
| P05 | 378 | 3.7% | 3.7% |  | 15% | ❌ 11 pts to go |
| P06M | 167 | 0.6% | 0.6% |  | 15% | ❌ 14 pts to go |
| P06T | 2431 | 0.5% | 0.5% |  | 15% | ❌ 14 pts to go |
| P06 | 161 | 3.7% | 3.7% |  | 15% | ❌ 11 pts to go |
| P07 | 248 | 2.0% | 2.0% |  | 15% | ❌ 13 pts to go |
| P08 | 3037 | 0.2% | 0.2% |  | 15% | ❌ 15 pts to go |
| P09 | 369 | 0.3% | 0.3% |  | 15% | ❌ 15 pts to go |
| P10 | 2588 | 0.2% | 0.2% |  | 15% | ❌ 15 pts to go |
| P11 | 499 | 1.0% | 1.0% |  | 15% | ❌ 14 pts to go |
| P12 | 21 | 9.5% | 9.5% |  | 15% | 🟡 6 pts to go |
| P13 | 50789 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P01T | 91 | 3.3% | 3.3% |  | 20% | ❌ 17 pts to go |
| P01_GOLD | 583 | 1.4% | 1.4% |  | 20% | ❌ 19 pts to go |
| P02 | 368 | 0.3% | 0.3% |  | 20% | ❌ 20 pts to go |
| P03 | 225 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P04 | 1615 | 0.1% | 0.1% |  | 20% | ❌ 20 pts to go |
| P05 | 378 | 0.5% | 0.5% |  | 20% | ❌ 20 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P06T | 2431 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P06 | 161 | 1.9% | 1.9% |  | 20% | ❌ 18 pts to go |
| P07 | 248 | 0.4% | 0.4% |  | 20% | ❌ 20 pts to go |
| P08 | 3037 | 0.1% | 0.1% |  | 20% | ❌ 20 pts to go |
| P09 | 369 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P10 | 2588 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P11 | 499 | 0.2% | 0.2% |  | 20% | ❌ 20 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P13 | 50789 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P01T | 91 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P01_GOLD | 583 | 1.2% | 1.2% |  | 15% | ❌ 14 pts to go |
| P02 | 368 | 0.3% | 0.3% |  | 15% | ❌ 15 pts to go |
| P03 | 225 | 0.9% | 0.9% |  | 15% | ❌ 14 pts to go |
| P04 | 1615 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |
| P05 | 378 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P06T | 2431 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |
| P06 | 161 | 1.2% | 1.2% |  | 15% | ❌ 14 pts to go |
| P07 | 248 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P08 | 3037 | 0.2% | 0.2% |  | 15% | ❌ 15 pts to go |
| P09 | 369 | 0.3% | 0.3% |  | 15% | ❌ 15 pts to go |
| P10 | 2588 | 0.2% | 0.2% |  | 15% | ❌ 15 pts to go |
| P11 | 499 | 0.2% | 0.2% |  | 15% | ❌ 15 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | 15% | ❌ 15 pts to go |
| P13 | 50789 | 0.1% | 0.1% |  | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 10.0% | 10.0% |  | 20% | 🟡 10 pts to go |
| P01T | 91 | 16.5% | 16.5% |  | 40% | ❌ 24 pts to go |
| P01_GOLD | 583 | 11.8% | 11.8% |  | 40% | ❌ 28 pts to go |
| P02 | 368 | 4.9% | 4.9% |  | 20% | ❌ 15 pts to go |
| P03 | 225 | 10.2% | 10.2% |  | 35% | ❌ 25 pts to go |
| P04 | 1615 | 4.3% | 4.3% |  | 20% | ❌ 16 pts to go |
| P05 | 378 | 5.0% | 5.0% |  | 20% | ❌ 15 pts to go |
| P06M | 167 | 2.4% | 2.4% |  | 20% | ❌ 18 pts to go |
| P06T | 2431 | 1.2% | 1.2% |  | 20% | ❌ 19 pts to go |
| P06 | 161 | 18.0% | 18.0% |  | 20% | 🟡 2 pts to go |
| P07 | 248 | 9.7% | 9.7% |  | 20% | ❌ 10 pts to go |
| P08 | 3037 | 0.9% | 0.9% |  | 20% | ❌ 19 pts to go |
| P09 | 369 | 9.5% | 9.5% |  | 20% | ❌ 10 pts to go |
| P10 | 2588 | 1.4% | 1.4% |  | 20% | ❌ 19 pts to go |
| P11 | 499 | 2.0% | 2.0% |  | 20% | ❌ 18 pts to go |
| P12 | 21 | 0.0% | 0.0% |  | 20% | ❌ 20 pts to go |
| P13 | 50789 | 0.3% | 0.3% |  | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 91 | 1.1% | 1.1% |  | n/a | no target |
| P01_GOLD | 583 | 68.4% | 68.4% |  | 95% | ❌ 27 pts to go |
| P02 | 368 | 74.2% | 74.2% |  | 95% | ❌ 21 pts to go |
| P03 | 225 | 63.6% | 63.6% |  | 90% | ❌ 26 pts to go |
| P04 | 1615 | 57.0% | 57.0% |  | 85% | ❌ 28 pts to go |
| P05 | 378 | 34.4% | 34.4% |  | 75% | ❌ 41 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2431 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 161 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 248 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 90.8% | 90.8% |  | 100% | 🟡 9 pts to go |
| P10 | 2588 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 499 | 21.8% | 21.8% |  | 60% | ❌ 38 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50789 | 0.0% | 0.0% |  | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 91 | 0.0% | 0.0% |  | n/a | no target |
| P01_GOLD | 583 | 72.6% | 72.6% |  | 100% | ❌ 27 pts to go |
| P02 | 368 | 77.7% | 77.7% |  | 100% | ❌ 22 pts to go |
| P03 | 225 | 70.7% | 70.7% |  | n/a | no target |
| P04 | 1615 | 58.5% | 58.5% |  | 95% | ❌ 36 pts to go |
| P05 | 378 | 30.7% | 30.7% |  | 80% | ❌ 49 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2431 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 161 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 248 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 93.5% | 93.5% |  | 100% | 🟡 6 pts to go |
| P10 | 2588 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 499 | 23.2% | 23.2% |  | n/a | no target |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50789 | 0.0% | 0.0% |  | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 91 | 1.1% | 1.1% |  | n/a | no target |
| P01_GOLD | 583 | 52.3% | 52.3% |  | 85% | ❌ 33 pts to go |
| P02 | 368 | 65.5% | 65.5% |  | 90% | ❌ 24 pts to go |
| P03 | 225 | 52.0% | 52.0% |  | 85% | ❌ 33 pts to go |
| P04 | 1615 | 63.5% | 63.5% |  | 90% | ❌ 26 pts to go |
| P05 | 378 | 35.4% | 35.4% |  | 75% | ❌ 40 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2431 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 161 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 248 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 85.4% | 85.4% |  | 95% | 🟡 10 pts to go |
| P10 | 2588 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 499 | 21.2% | 21.2% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50789 | 0.0% | 0.0% |  | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 91 | 1.1% | 1.1% |  | n/a | no target |
| P01_GOLD | 583 | 52.8% | 52.8% |  | 85% | ❌ 32 pts to go |
| P02 | 368 | 60.9% | 60.9% |  | 90% | ❌ 29 pts to go |
| P03 | 225 | 52.4% | 52.4% |  | 85% | ❌ 33 pts to go |
| P04 | 1615 | 53.1% | 53.1% |  | 90% | ❌ 37 pts to go |
| P05 | 378 | 42.3% | 42.3% |  | 75% | ❌ 33 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2431 | 0.0% | 0.0% |  | n/a | no target |
| P06 | 161 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 248 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 0.3% | 0.3% |  | 95% | ❌ 95 pts to go |
| P10 | 2588 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 499 | 17.4% | 17.4% |  | n/a | no target |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target |
| P13 | 50789 | 0.0% | 0.0% |  | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 91 | 76.9% | 76.9% |  | n/a | no target |
| P01_GOLD | 583 | 82.0% | 82.0% |  | 100% | ❌ 18 pts to go |
| P02 | 368 | 80.7% | 80.7% |  | 100% | ❌ 19 pts to go |
| P03 | 225 | 86.2% | 86.2% |  | n/a | no target |
| P04 | 1615 | 71.6% | 71.6% |  | 95% | ❌ 23 pts to go |
| P05 | 378 | 75.4% | 75.4% |  | 95% | ❌ 20 pts to go |
| P06M | 167 | 0.6% | 0.6% |  | n/a | no target |
| P06T | 2431 | 83.3% | 83.3% |  | n/a | no target |
| P06 | 161 | 75.2% | 75.2% |  | n/a | no target |
| P07 | 248 | 77.0% | 77.0% |  | n/a | no target |
| P08 | 3037 | 84.9% | 85.0% |  | n/a | no target |
| P09 | 369 | 98.9% | 98.9% |  | 100% | 🟡 1 pts to go |
| P10 | 2588 | 98.4% | 98.4% |  | n/a | no target |
| P11 | 499 | 89.6% | 89.6% |  | n/a | no target |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50789 | 0.0% | 0.0% |  | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 91 | 3.3% | 3.3% |  | n/a | no target |
| P01_GOLD | 583 | 69.5% | 69.5% |  | 100% | ❌ 30 pts to go |
| P02 | 368 | 71.7% | 72.0% |  | 100% | ❌ 28 pts to go |
| P03 | 225 | 68.0% | 68.0% |  | n/a | no target |
| P04 | 1615 | 57.9% | 57.9% |  | 95% | ❌ 37 pts to go |
| P05 | 378 | 14.0% | 14.0% |  | 70% | ❌ 56 pts to go |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2431 | 0.2% | 0.2% |  | n/a | no target |
| P06 | 161 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 248 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 95.7% | 95.7% |  | 100% | 🟡 4 pts to go |
| P10 | 2588 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 499 | 24.0% | 24.0% |  | n/a | no target |
| P12 | 21 | 100.0% | 100.0% |  | n/a | no target |
| P13 | 50789 | 0.0% | 0.0% |  | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 0.0% |  | n/a | no target |
| P01T | 91 | 1.1% | 1.1% |  | n/a | no target · rows from a source that publishes bids: 3 rows, 33.3% filled |
| P01_GOLD | 583 | 18.4% | 18.4% |  | 60% | ❌ 42 pts to go · rows from a source that publishes bids: 356 rows, 30.1% filled |
| P02 | 368 | 14.1% | 14.1% |  | n/a | no target · rows from a source that publishes bids: 268 rows, 19.4% filled |
| P03 | 225 | 15.1% | 15.1% |  | n/a | no target · rows from a source that publishes bids: 139 rows, 24.5% filled |
| P04 | 1615 | 3.5% | 3.5% |  | n/a | no target · rows from a source that publishes bids: 900 rows, 6.3% filled |
| P05 | 378 | 3.4% | 3.4% |  | n/a | no target · rows from a source that publishes bids: 48 rows, 27.1% filled |
| P06M | 167 | 0.0% | 0.0% |  | n/a | no target |
| P06T | 2431 | 0.1% | 0.1% |  | n/a | no target · rows from a source that publishes bids: 4 rows, 50.0% filled |
| P06 | 161 | 0.0% | 0.0% |  | n/a | no target |
| P07 | 248 | 0.0% | 0.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 0.0% |  | n/a | no target |
| P09 | 369 | 3.3% | 3.3% |  | n/a | no target · rows from a source that publishes bids: 355 rows, 3.4% filled |
| P10 | 2588 | 0.0% | 0.0% |  | n/a | no target |
| P11 | 499 | 3.0% | 3.0% |  | n/a | no target · rows from a source that publishes bids: 111 rows, 13.5% filled |
| P12 | 21 | 0.0% | 0.0% |  | n/a | no target · rows from a source that publishes bids: 21 rows, 0.0% filled |
| P13 | 50789 | 0.0% | 0.0% |  | n/a | no target |

## 6. history

### `average_contract_duration_days`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 100.0% |  | n/a | no target |
| P01T | 91 | 0.0% | 96.7% |  | n/a | no target |
| P01_GOLD | 583 | 40.5% | 67.8% |  | 90% | ❌ 50 pts to go |
| P02 | 368 | 55.7% | 80.4% |  | 90% | ❌ 34 pts to go |
| P03 | 225 | 39.1% | 64.4% |  | 90% | ❌ 51 pts to go |
| P04 | 1615 | 42.6% | 82.9% |  | 90% | ❌ 47 pts to go |
| P05 | 378 | 0.0% | 82.0% |  | 90% | ❌ 90 pts to go |
| P06M | 167 | 0.0% | 100.0% |  | n/a | no target |
| P06T | 2431 | 0.0% | 99.8% |  | n/a | no target |
| P06 | 161 | 0.0% | 100.0% |  | n/a | no target |
| P07 | 248 | 0.0% | 100.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 100.0% |  | n/a | no target |
| P09 | 369 | 0.0% | 1.4% |  | 90% | ❌ 90 pts to go |
| P10 | 2588 | 0.0% | 100.0% |  | n/a | no target |
| P11 | 499 | 14.6% | 88.4% |  | n/a | no target |
| P12 | 21 | 0.0% | 100.0% |  | n/a | no target |
| P13 | 50789 | 0.0% | 100.0% |  | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 100.0% |  | n/a | no target |
| P01T | 91 | 0.0% | 96.7% |  | n/a | no target |
| P01_GOLD | 583 | 27.1% | 54.4% |  | 90% | ❌ 63 pts to go |
| P02 | 368 | 59.0% | 83.7% |  | n/a | no target |
| P03 | 225 | 28.0% | 53.3% |  | n/a | no target |
| P04 | 1615 | 49.5% | 89.8% |  | n/a | no target |
| P05 | 378 | 0.3% | 82.3% |  | n/a | no target |
| P06M | 167 | 0.0% | 100.0% |  | n/a | no target |
| P06T | 2431 | 0.0% | 99.8% |  | n/a | no target |
| P06 | 161 | 0.0% | 100.0% |  | n/a | no target |
| P07 | 248 | 0.0% | 100.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 100.0% |  | n/a | no target |
| P09 | 369 | 45.8% | 47.2% |  | n/a | no target |
| P10 | 2588 | 0.0% | 100.0% |  | n/a | no target |
| P11 | 499 | 13.8% | 87.6% |  | n/a | no target |
| P12 | 21 | 0.0% | 100.0% |  | n/a | no target |
| P13 | 50789 | 0.0% | 100.0% |  | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 0.0% | 100.0% |  | n/a | no target |
| P01T | 91 | 2.2% | 98.9% |  | n/a | no target |
| P01_GOLD | 583 | 54.0% | 81.3% |  | 95% | ❌ 41 pts to go |
| P02 | 368 | 66.3% | 91.0% |  | n/a | no target |
| P03 | 225 | 57.8% | 83.1% |  | n/a | no target |
| P04 | 1615 | 50.2% | 90.5% |  | n/a | no target |
| P05 | 378 | 4.8% | 86.8% |  | n/a | no target |
| P06M | 167 | 0.0% | 100.0% |  | n/a | no target |
| P06T | 2431 | 0.0% | 99.8% |  | n/a | no target |
| P06 | 161 | 0.0% | 100.0% |  | n/a | no target |
| P07 | 248 | 0.0% | 100.0% |  | n/a | no target |
| P08 | 3037 | 0.0% | 100.0% |  | n/a | no target |
| P09 | 369 | 69.1% | 70.5% |  | n/a | no target |
| P10 | 2588 | 0.0% | 100.0% |  | n/a | no target |
| P11 | 499 | 14.2% | 88.0% |  | n/a | no target |
| P12 | 21 | 0.0% | 100.0% |  | n/a | no target |
| P13 | 50789 | 0.0% | 100.0% |  | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01T | 91 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01_GOLD | 583 | 100.0% | 100.0% |  | 100% | ✅ met |
| P02 | 368 | 100.0% | 100.0% |  | 100% | ✅ met |
| P03 | 225 | 99.6% | 99.6% |  | 100% | 🟡 0 pts to go |
| P04 | 1615 | 100.0% | 100.0% |  | 100% | ✅ met |
| P05 | 378 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06M | 167 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06T | 2431 | 99.9% | 99.9% |  | 100% | 🟡 0 pts to go |
| P06 | 161 | 99.4% | 99.4% |  | 100% | 🟡 1 pts to go |
| P07 | 248 | 99.2% | 99.2% |  | 100% | 🟡 1 pts to go |
| P08 | 3037 | 100.0% | 100.0% |  | 100% | ✅ met |
| P09 | 369 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2588 | 100.0% | 100.0% |  | 100% | ✅ met |
| P11 | 499 | 99.6% | 99.6% |  | 100% | 🟡 0 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50789 | 100.0% | 100.0% |  | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01T | 91 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01_GOLD | 583 | 100.0% | 100.0% |  | 100% | ✅ met |
| P02 | 368 | 100.0% | 100.0% |  | 100% | ✅ met |
| P03 | 225 | 99.6% | 99.6% |  | 100% | 🟡 0 pts to go |
| P04 | 1615 | 100.0% | 100.0% |  | 100% | ✅ met |
| P05 | 378 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06M | 167 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06T | 2431 | 99.9% | 99.9% |  | 100% | 🟡 0 pts to go |
| P06 | 161 | 99.4% | 99.4% |  | 100% | 🟡 1 pts to go |
| P07 | 248 | 99.2% | 99.2% |  | 100% | 🟡 1 pts to go |
| P08 | 3037 | 100.0% | 100.0% |  | 100% | ✅ met |
| P09 | 369 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2588 | 100.0% | 100.0% |  | 100% | ✅ met |
| P11 | 499 | 99.6% | 99.6% |  | 100% | 🟡 0 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50789 | 100.0% | 100.0% |  | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 20 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01T | 91 | 100.0% | 100.0% |  | 100% | ✅ met |
| P01_GOLD | 583 | 100.0% | 100.0% |  | 100% | ✅ met |
| P02 | 368 | 100.0% | 100.0% |  | 100% | ✅ met |
| P03 | 225 | 99.6% | 99.6% |  | 100% | 🟡 0 pts to go |
| P04 | 1615 | 100.0% | 100.0% |  | 100% | ✅ met |
| P05 | 378 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06M | 167 | 100.0% | 100.0% |  | 100% | ✅ met |
| P06T | 2431 | 99.9% | 99.9% |  | 100% | 🟡 0 pts to go |
| P06 | 161 | 99.4% | 99.4% |  | 100% | 🟡 1 pts to go |
| P07 | 248 | 99.2% | 99.2% |  | 100% | 🟡 1 pts to go |
| P08 | 3037 | 100.0% | 100.0% |  | 100% | ✅ met |
| P09 | 369 | 100.0% | 100.0% |  | 100% | ✅ met |
| P10 | 2588 | 100.0% | 100.0% |  | 100% | ✅ met |
| P11 | 499 | 99.6% | 99.6% |  | 100% | 🟡 0 pts to go |
| P12 | 21 | 100.0% | 100.0% |  | 100% | ✅ met |
| P13 | 50789 | 100.0% | 100.0% |  | 100% | ✅ met |


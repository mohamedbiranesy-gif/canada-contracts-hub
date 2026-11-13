# Coverage vs the downstream team's targets — 2026-11-13

Benchmarks (field × package with a numeric target): **90 of 438 met** (20.5%); 64 within 10 points; 284 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 377, P01T 210, P01_GOLD 653, P02 490, P03 277, P04 4847, P05 429, P06M 28880, P06T 55820, P06 258, P07 790, P08 29531, P09 276, P10R 0, P10 2069, P11 1812, P12 11, P13 196420

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 377 | 0.0% | 10.6% | 7 | vendor GST/HST number (356 rows) |
| P01T | 210 | 1.0% | 33.3% | 8 | payment terms (166 rows) |
| P01_GOLD | 653 | 23.3% | 68.8% | 9 | payment terms (249 rows) |
| P02 | 490 | 7.1% | 52.7% | 9 | PO rule (379 rows) |
| P03 | 277 | 14.1% | 53.8% | 9 | PO rule (144 rows) |
| P04 | 4847 | 1.0% | 12.6% | 7 | PO rule (4647 rows) |
| P05 | 429 | 0.9% | 17.0% | 7 | payment terms (358 rows) |
| P06M | 28880 | 0.0% | 2.5% | 7 | PO rule (28497 rows) |
| P06T | 55820 | 0.1% | 13.4% | 7 | PO rule (55491 rows) |
| P06 | 258 | 0.0% | 9.7% | 6 | reference to quote (PO / contract / vendor id) (241 rows) |
| P07 | 790 | 0.0% | 2.9% | 6 | PO rule (751 rows) |
| P08 | 29531 | 0.0% | 1.5% | 6 | PO rule (29278 rows) |
| P09 | 276 | 1.4% | 42.0% | 8 | payment terms (257 rows) |
| P10 | 2069 | 0.0% | 1.2% | 5 | reference to quote (PO / contract / vendor id) (2069 rows) |
| P11 | 1812 | 0.1% | 7.9% | 6 | PO rule (1746 rows) |
| P12 | 11 | 0.0% | 36.4% | 8 | PO rule (11 rows) |
| P13 | 196420 | 0.0% | 0.3% | 6 | reference to quote (PO / contract / vendor id) (196420 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 377 | 11 | 68 | 298 | 0 | 0 | 66 |
| P01T | 210 | 26 | 32 | 152 | 0 | 0 | 66 |
| P01_GOLD | 653 | 254 | 169 | 230 | 0 | 0 | 81 |
| P02 | 490 | 0 | 191 | 299 | 0 | 0 | 66 |
| P03 | 277 | 0 | 0 | 265 | 12 | 0 | 57 |
| P04 | 4847 | 0 | 0 | 4181 | 666 | 0 | 46 |
| P05 | 429 | 14 | 29 | 373 | 13 | 0 | 51 |
| P06M | 28880 | 0 | 19 | 28809 | 52 | 0 | 46 |
| P06T | 55820 | 0 | 27 | 38355 | 17438 | 0 | 38 |
| P06 | 258 | 15 | 32 | 211 | 0 | 0 | 66 |
| P07 | 790 | 0 | 20 | 752 | 18 | 0 | 55 |
| P08 | 29531 | 0 | 0 | 26735 | 2796 | 0 | 46 |
| P09 | 276 | 5 | 10 | 260 | 1 | 0 | 53 |
| P10 | 2069 | 2 | 10 | 1404 | 653 | 0 | 41 |
| P11 | 1812 | 7 | 13 | 37 | 0 | 1755 | 23 |
| P12 | 11 | 0 | 0 | 11 | 0 | 0 | 51 |
| P13 | 196420 | 12 | 64 | 196331 | 13 | 0 | 38 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 377 | 280 | 74.3% | tax treatment (69) |
| P01T | 210 | 126 | 60.0% | bill-to legal name and address (68) |
| P01_GOLD | 653 | 491 | 75.2% | bill-to legal name and address (94) |
| P02 | 490 | 332 | 67.8% | the buyer's PO / reference rule (85) |
| P03 | 277 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (277) |
| P04 | 4847 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (4847) |
| P05 | 429 | 45 | 10.5% | a confirmed invoicing / AP or finance channel (341) |
| P06M | 28880 | 317 | 1.1% | a confirmed invoicing / AP or finance channel (28483) |
| P06T | 55820 | 326 | 0.6% | a confirmed invoicing / AP or finance channel (55059) |
| P06 | 258 | 44 | 17.1% | the buyer's PO / reference rule (115) |
| P07 | 790 | 48 | 6.1% | the buyer's PO / reference rule (324) |
| P08 | 29531 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (29531) |
| P09 | 276 | 39 | 14.1% | a confirmed invoicing / AP or finance channel (226) |
| P10 | 2069 | 5 | 0.2% | a confirmed invoicing / AP or finance channel (1995) |
| P11 | 1812 | 19 | 1.0% | a confirmed invoicing / AP or finance channel (1755) |
| P12 | 11 | 2 | 18.2% | a confirmed invoicing / AP or finance channel (9) |
| P13 | 196420 | 43 | 0.0% | a confirmed invoicing / AP or finance channel (193977) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 377 | 9 | 2.4% | 7 | 0 | the vendor's GST/HST number (BN9) (356) |
| P01T | 210 | 83 | 39.5% | 3 | 0 | the vendor's GST/HST number (BN9) (77) |
| P01_GOLD | 653 | 409 | 62.6% | 11 | 0 | the vendor's GST/HST number (BN9) (167) |
| P02 | 490 | 215 | 43.9% | 22 | 0 | the vendor's GST/HST number (BN9) (225) |
| P03 | 277 | 17 | 6.1% | 0 | 132 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (108) |
| P04 | 4847 | 43 | 0.9% | 7 | 913 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3826) |
| P05 | 429 | 21 | 4.9% | 8 | 128 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (204) |
| P06M | 28880 | 8 | 0.0% | 14 | 702 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (27678) |
| P06T | 55820 | 358 | 0.6% | 14 | 18217 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (36762) |
| P06 | 258 | 20 | 7.8% | 51 | 0 | the vendor's GST/HST number (BN9) (118) |
| P07 | 790 | 16 | 2.0% | 137 | 37 | the vendor's GST/HST number (BN9) (387) |
| P08 | 29531 | 4 | 0.0% | 13 | 7287 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (22184) |
| P09 | 276 | 36 | 13.0% | 0 | 107 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (107) |
| P10 | 2069 | 5 | 0.2% | 14 | 291 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1683) |
| P11 | 1812 | 7 | 0.4% | 2 | 0 | a confirmed invoicing / AP or finance channel (1739) |
| P12 | 11 | 1 | 9.1% | 0 | 5 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (4) |
| P13 | 196420 | 22 | 0.0% | 1152 | 76812 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (116985) |
| **all** | 323150 | 1274 | 0.4% | 1455 | 104631 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 366 | 0 | 0 | 0 | 273 | 9 | 0 | 314 | 333 | 0 |
| P01T | 184 | 0 | 0 | 0 | 118 | 62 | 28 | 155 | 167 | 2 |
| P01_GOLD | 399 | 0 | 0 | 0 | 39 | 76 | 30 | 227 | 264 | 2 |
| P02 | 490 | 0 | 490 | 0 | 59 | 58 | 14 | 379 | 306 | 2 |
| P03 | 277 | 0 | 277 | 0 | 28 | 45 | 27 | 144 | 152 | 2 |
| P04 | 4847 | 0 | 4847 | 0 | 2692 | 1507 | 1013 | 4647 | 4407 | 33 |
| P05 | 415 | 0 | 362 | 0 | 87 | 100 | 40 | 345 | 360 | 7 |
| P06M | 28880 | 0 | 28880 | 0 | 22627 | 1461 | 130 | 28497 | 28239 | 20 |
| P06T | 55820 | 0 | 55820 | 0 | 50182 | 34772 | 22583 | 55491 | 55025 | 392 |
| P06 | 243 | 0 | 0 | 0 | 132 | 71 | 42 | 191 | 214 | 4 |
| P07 | 790 | 0 | 790 | 0 | 536 | 306 | 100 | 751 | 751 | 5 |
| P08 | 29531 | 0 | 29531 | 0 | 23359 | 12737 | 4312 | 29278 | 28922 | 187 |
| P09 | 271 | 0 | 252 | 0 | 12 | 68 | 1 | 246 | 259 | 7 |
| P10 | 2067 | 0 | 2037 | 0 | 1074 | 1114 | 949 | 2006 | 1968 | 16 |
| P11 | 1805 | 1755 | 1710 | 0 | 932 | 1223 | 548 | 1746 | 1741 | 21 |
| P12 | 11 | 0 | 10 | 0 | 0 | 3 | 0 | 11 | 11 | 2 |
| P13 | 196408 | 0 | 195963 | 0 | 166387 | 118313 | 19 | 196074 | 195206 | 70 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_phone | P13 | 57.6% | 95% | 73387 |
| buyer_logo_url | P13 | 73.2% | 95% | 42736 |
| buyer_legal_name_as_published | P13 | 39.8% | 60% | 39745 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 39227 |
| ap_system_hint | P13 | 0.3% | 20% | 38662 |
| buyer_bn_as_published | P13 | 10.6% | 30% | 38102 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 29304 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 29262 |
| buyer_payment_method_preference | P13 | 0.6% | 15% | 28332 |
| vendor_registered_address | P08 | 31.8% | 70% | 11274 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 11149 |
| ap_system_hint | P06T | 0.6% | 20% | 10830 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 8277 |
| buyer_tax_exempt_status | P06T | 0.2% | 15% | 8265 |
| buyer_payment_method_preference | P06T | 0.7% | 15% | 7998 |
| buyer_phone | P08 | 70.9% | 95% | 7121 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 5895 |
| buyer_ap_cycle_published | P06M | 0.0% | 20% | 5762 |
| ap_system_hint | P08 | 0.8% | 20% | 5683 |
| vendor_emails | P08 | 55.9% | 75% | 5644 |
| ap_system_hint | P06M | 0.9% | 20% | 5509 |
| buyer_legal_name_as_published | P08 | 56.9% | 75% | 5355 |
| vendor_bn9 | P08 | 32.3% | 50% | 5238 |
| vendor_phone | P08 | 67.7% | 85% | 5121 |
| vendor_trading_name | P08 | 34.0% | 50% | 4725 |
| buyer_esignature_preference | P08 | 0.3% | 15% | 4332 |
| buyer_tax_exempt_status | P08 | 0.3% | 15% | 4327 |
| buyer_payment_method_preference | P08 | 0.6% | 15% | 4252 |
| buyer_esignature_preference | P06M | 0.3% | 15% | 4234 |
| buyer_tax_exempt_status | P06M | 0.6% | 15% | 4172 |
| buyer_payment_method_preference | P06M | 0.8% | 15% | 4108 |
| invoice_reference_hint | P08 | 12.1% | 25% | 3803 |
| buyer_bn_as_published | P08 | 22.6% | 35% | 3664 |
| average_contract_duration_days | P04 | 14.6% | 90% | 3657 |
| currency | P04 | 20.9% | 95% | 3590 |
| ap_phone | P04 | 15.0% | 85% | 3395 |
| commodity_codes | P04 | 16.5% | 85% | 3322 |
| award_or_notice_id | P04 | 18.4% | 85% | 3226 |
| contract_value | P04 | 20.6% | 85% | 3122 |
| invoice_mailing_address | P04 | 15.0% | 75% | 2910 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 94.4% | 94.4% | +1.2 | 50% | ✅ met |
| P01T | 210 | 94.8% | 94.8% | -0.8 | 50% | ✅ met |
| P01_GOLD | 653 | 92.2% | 94.6% | +0.0 | 95% | 🟡 3 pts to go |
| P02 | 490 | 75.7% | 77.1% | +0.7 | 95% | ❌ 19 pts to go |
| P03 | 277 | 82.3% | 85.6% | +0.7 | 95% | ❌ 13 pts to go |
| P04 | 4847 | 43.4% | 44.7% | +11.6 | 90% | ❌ 47 pts to go |
| P05 | 429 | 40.3% | 43.4% | +0.7 | 70% | ❌ 30 pts to go |
| P06M | 28880 | 93.7% | 93.7% | +0.5 | n/a | no target |
| P06T | 55820 | 99.5% | 99.5% | +0.2 | n/a | no target |
| P06 | 258 | 32.2% | 32.2% | -3.2 | 30% | ✅ met |
| P07 | 790 | 13.9% | 13.9% | -0.3 | 30% | ❌ 16 pts to go |
| P08 | 29531 | 12.1% | 12.1% | -0.1 | 25% | ❌ 13 pts to go |
| P09 | 276 | 98.9% | 99.6% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2069 | 3.0% | 3.0% | -0.3 | 25% | ❌ 22 pts to go |
| P11 | 1812 | 55.0% | 55.7% | +0.7 | 60% | 🟡 5 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 196420 | 99.6% | 99.6% | +0.0 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 210 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 653 | 5.7% | 5.7% | +0.0 | 50% | ❌ 44 pts to go |
| P02 | 490 | 5.5% | 5.5% | -0.7 | 50% | ❌ 44 pts to go |
| P03 | 277 | 1.8% | 1.8% | -0.1 | 40% | ❌ 38 pts to go |
| P04 | 4847 | 0.5% | 0.5% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 429 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 28880 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55820 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 258 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 790 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29531 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10 | 2069 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1812 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 196420 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 92.0% | 92.0% | +2.4 | n/a | no target |
| P01T | 210 | 78.1% | 78.1% | -1.8 | 50% | ✅ met |
| P01_GOLD | 653 | 68.9% | 68.9% | +1.6 | 85% | ❌ 16 pts to go |
| P02 | 490 | 67.1% | 67.1% | +0.9 | 90% | ❌ 23 pts to go |
| P03 | 277 | 62.1% | 62.1% | +1.6 | 85% | ❌ 23 pts to go |
| P04 | 4847 | 41.4% | 41.4% | +12.3 | 85% | ❌ 44 pts to go |
| P05 | 429 | 31.0% | 31.0% | +1.1 | 60% | ❌ 29 pts to go |
| P06M | 28880 | 93.5% | 93.5% | +0.5 | n/a | no target |
| P06T | 55820 | 99.4% | 99.4% | +0.2 | n/a | no target |
| P06 | 258 | 6.6% | 6.6% | +0.2 | n/a | no target |
| P07 | 790 | 9.0% | 9.0% | -0.1 | n/a | no target |
| P08 | 29531 | 11.3% | 11.3% | +0.0 | n/a | no target |
| P09 | 276 | 95.7% | 95.7% | +0.1 | 100% | 🟡 4 pts to go |
| P10 | 2069 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1812 | 52.2% | 52.2% | +0.7 | 60% | 🟡 8 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 196420 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 210 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 653 | 49.3% | 49.3% | -2.4 | 80% | ❌ 31 pts to go |
| P02 | 490 | 55.1% | 55.1% | -3.0 | 60% | 🟡 5 pts to go |
| P03 | 277 | 48.4% | 48.4% | -2.0 | 80% | ❌ 32 pts to go |
| P04 | 4847 | 17.7% | 17.7% | -6.3 | 50% | ❌ 32 pts to go |
| P05 | 429 | 13.8% | 13.8% | +1.2 | 40% | ❌ 26 pts to go |
| P06M | 28880 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55820 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 258 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 790 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29531 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 81.2% | 81.2% | +0.1 | 50% | ✅ met |
| P10 | 2069 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1812 | 3.3% | 3.3% | +0.0 | 40% | ❌ 37 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 196420 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 210 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 653 | 58.5% | 58.5% | -2.4 | 85% | ❌ 26 pts to go |
| P02 | 490 | 55.3% | 55.3% | -2.8 | 90% | ❌ 35 pts to go |
| P03 | 277 | 56.7% | 56.7% | -2.7 | 85% | ❌ 28 pts to go |
| P04 | 4847 | 18.4% | 18.4% | -6.5 | 85% | ❌ 67 pts to go |
| P05 | 429 | 21.4% | 21.4% | +1.0 | 50% | ❌ 29 pts to go |
| P06M | 28880 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55820 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 258 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 790 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29531 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 2069 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1812 | 3.6% | 3.6% | +0.0 | 60% | ❌ 56 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 196420 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 210 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 653 | 12.3% | 12.3% | -0.3 | 60% | ❌ 48 pts to go |
| P02 | 490 | 6.5% | 6.5% | -0.8 | 50% | ❌ 44 pts to go |
| P03 | 277 | 8.3% | 8.3% | -0.3 | 50% | ❌ 42 pts to go |
| P04 | 4847 | 1.4% | 1.4% | -0.5 | 40% | ❌ 39 pts to go |
| P05 | 429 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 28880 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55820 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 258 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 790 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29531 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 3.6% | 3.6% | +0.0 | 50% | ❌ 46 pts to go |
| P10 | 2069 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1812 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 196420 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 210 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 653 | 34.3% | 34.3% | -1.6 | 80% | ❌ 46 pts to go |
| P02 | 490 | 50.0% | 50.0% | -3.0 | 90% | ❌ 40 pts to go |
| P03 | 277 | 32.5% | 32.5% | -1.3 | 80% | ❌ 48 pts to go |
| P04 | 4847 | 16.5% | 16.5% | -5.7 | 85% | ❌ 68 pts to go |
| P05 | 429 | 7.7% | 7.7% | +1.3 | 50% | ❌ 42 pts to go |
| P06M | 28880 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55820 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 258 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 790 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29531 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 73.2% | 73.2% | +0.1 | 95% | ❌ 22 pts to go |
| P10 | 2069 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1812 | 2.6% | 2.6% | +0.0 | 50% | ❌ 47 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 196420 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 210 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 653 | 8.0% | 8.0% | -0.1 | 50% | ❌ 42 pts to go |
| P02 | 490 | 5.3% | 5.3% | -0.9 | 50% | ❌ 45 pts to go |
| P03 | 277 | 2.5% | 2.5% | -0.1 | 30% | ❌ 28 pts to go |
| P04 | 4847 | 0.4% | 0.4% | -0.2 | 30% | ❌ 30 pts to go |
| P05 | 429 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 28880 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55820 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 258 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 790 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29531 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P10 | 2069 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1812 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 196420 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 210 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 653 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 490 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 277 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4847 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 429 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 28880 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 55820 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 258 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 790 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 29531 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2069 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1812 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 196420 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 5.6% | 5.6% | -0.8 | 70% | ❌ 64 pts to go |
| P01T | 210 | 55.7% | 55.7% | -4.6 | 60% | 🟡 4 pts to go |
| P01_GOLD | 653 | 72.1% | 72.1% | -2.7 | 90% | ❌ 18 pts to go |
| P02 | 490 | 51.6% | 51.6% | -2.7 | 85% | ❌ 33 pts to go |
| P03 | 277 | 63.5% | 63.5% | -3.4 | 90% | ❌ 26 pts to go |
| P04 | 4847 | 28.3% | 28.3% | -9.9 | 75% | ❌ 47 pts to go |
| P05 | 429 | 54.8% | 54.8% | +0.1 | 50% | ✅ met |
| P06M | 28880 | 3.0% | 3.0% | +0.1 | n/a | no target |
| P06T | 55820 | 64.9% | 64.9% | +0.4 | n/a | no target |
| P06 | 258 | 42.2% | 42.2% | +0.1 | 40% | ✅ met |
| P07 | 790 | 32.4% | 32.4% | +0.3 | 50% | ❌ 18 pts to go |
| P08 | 29531 | 32.3% | 32.3% | +1.7 | 50% | ❌ 18 pts to go |
| P09 | 276 | 56.5% | 56.5% | -0.2 | 80% | ❌ 24 pts to go |
| P10 | 2069 | 38.7% | 38.7% | -0.1 | 40% | 🟡 1 pts to go |
| P11 | 1812 | 53.7% | 53.7% | -0.9 | 60% | 🟡 6 pts to go |
| P12 | 11 | 54.5% | 54.5% | +9.0 | 85% | ❌ 30 pts to go |
| P13 | 196420 | 44.4% | 44.4% | -0.4 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 43.2% | 43.2% | -3.4 | n/a | no target |
| P01T | 210 | 56.2% | 56.2% | -3.6 | n/a | no target |
| P01_GOLD | 653 | 74.1% | 74.1% | +1.2 | 95% | ❌ 21 pts to go |
| P02 | 490 | 74.7% | 74.7% | +0.1 | 95% | ❌ 20 pts to go |
| P03 | 277 | 70.4% | 70.4% | +0.9 | 95% | ❌ 25 pts to go |
| P04 | 4847 | 54.1% | 54.1% | +1.0 | 95% | ❌ 41 pts to go |
| P05 | 429 | 58.7% | 58.7% | +0.6 | 70% | ❌ 11 pts to go |
| P06M | 28880 | 39.7% | 39.7% | -1.6 | n/a | no target |
| P06T | 55820 | 68.4% | 68.4% | +0.9 | n/a | no target |
| P06 | 258 | 38.4% | 38.4% | +0.2 | 80% | ❌ 42 pts to go |
| P07 | 790 | 31.5% | 31.5% | +0.5 | 70% | ❌ 38 pts to go |
| P08 | 29531 | 31.8% | 31.8% | +2.1 | 70% | ❌ 38 pts to go |
| P09 | 276 | 86.2% | 86.2% | +0.0 | 100% | ❌ 14 pts to go |
| P10 | 2069 | 39.2% | 39.2% | +0.0 | 70% | ❌ 31 pts to go |
| P11 | 1812 | 58.6% | 58.6% | +0.0 | 75% | ❌ 16 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 196420 | 40.0% | 40.0% | -0.2 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 21.8% | 21.8% | -0.3 | n/a | no target |
| P01T | 210 | 59.0% | 59.0% | -6.5 | n/a | no target |
| P01_GOLD | 653 | 50.8% | 50.8% | +2.0 | 60% | 🟡 9 pts to go |
| P02 | 490 | 58.0% | 58.0% | +2.2 | 60% | 🟡 2 pts to go |
| P03 | 277 | 54.2% | 54.2% | +1.9 | 60% | 🟡 6 pts to go |
| P04 | 4847 | 54.2% | 54.2% | +11.6 | 55% | 🟡 1 pts to go |
| P05 | 429 | 23.5% | 23.5% | +0.8 | 50% | ❌ 26 pts to go |
| P06M | 28880 | 11.1% | 11.1% | +1.6 | n/a | no target |
| P06T | 55820 | 70.0% | 70.0% | +2.1 | n/a | no target |
| P06 | 258 | 50.0% | 50.0% | +1.4 | n/a | no target |
| P07 | 790 | 39.5% | 39.5% | -0.1 | 55% | ❌ 16 pts to go |
| P08 | 29531 | 34.0% | 34.0% | +1.0 | 50% | ❌ 16 pts to go |
| P09 | 276 | 72.1% | 72.1% | +0.1 | 70% | ✅ met |
| P10 | 2069 | 47.6% | 47.6% | -0.5 | 55% | 🟡 7 pts to go |
| P11 | 1812 | 59.3% | 59.3% | +0.1 | 50% | ✅ met |
| P12 | 11 | 90.9% | 90.9% | +0.0 | n/a | no target |
| P13 | 196420 | 3.0% | 3.0% | -0.2 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 25.7% | 25.7% | -7.6 | n/a | no target |
| P01T | 210 | 77.1% | 77.1% | -2.4 | n/a | no target |
| P01_GOLD | 653 | 48.4% | 48.4% | -2.0 | 70% | ❌ 22 pts to go |
| P02 | 490 | 54.7% | 54.7% | -2.1 | 70% | ❌ 15 pts to go |
| P03 | 277 | 48.4% | 48.4% | -2.0 | 70% | ❌ 22 pts to go |
| P04 | 4847 | 49.6% | 49.6% | -5.3 | 65% | ❌ 15 pts to go |
| P05 | 429 | 29.6% | 29.6% | +0.5 | 60% | ❌ 30 pts to go |
| P06M | 28880 | 24.4% | 24.4% | -3.0 | n/a | no target |
| P06T | 55820 | 87.0% | 87.0% | +4.3 | n/a | no target |
| P06 | 258 | 72.1% | 72.1% | +2.8 | 40% | ✅ met |
| P07 | 790 | 66.8% | 66.8% | +1.8 | 85% | ❌ 18 pts to go |
| P08 | 29531 | 67.7% | 67.7% | +3.7 | 85% | ❌ 17 pts to go |
| P09 | 276 | 56.2% | 56.2% | -0.2 | 85% | ❌ 29 pts to go |
| P10 | 2069 | 65.5% | 65.5% | -0.6 | 85% | ❌ 20 pts to go |
| P11 | 1812 | 68.5% | 68.5% | +0.4 | 75% | 🟡 6 pts to go |
| P12 | 11 | 36.4% | 36.4% | +0.0 | n/a | no target |
| P13 | 196420 | 91.5% | 91.5% | -0.3 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 30.2% | 30.2% | -7.6 | n/a | no target |
| P01T | 210 | 98.1% | 98.1% | -0.2 | n/a | no target |
| P01_GOLD | 653 | 75.3% | 75.3% | -3.3 | 90% | ❌ 15 pts to go |
| P02 | 490 | 78.6% | 78.6% | -3.2 | 90% | ❌ 11 pts to go |
| P03 | 277 | 81.6% | 81.6% | -3.7 | 90% | 🟡 8 pts to go |
| P04 | 4847 | 71.2% | 71.2% | -11.6 | 85% | ❌ 14 pts to go |
| P05 | 429 | 44.8% | 44.8% | +0.3 | 70% | ❌ 25 pts to go |
| P06M | 28880 | 30.0% | 30.0% | -3.0 | n/a | no target |
| P06T | 55820 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 258 | 99.2% | 99.2% | -0.1 | 50% | ✅ met |
| P07 | 790 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P08 | 29531 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P09 | 276 | 77.5% | 77.5% | -0.3 | 100% | ❌ 22 pts to go |
| P10 | 2069 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1812 | 97.5% | 97.5% | -0.5 | 100% | 🟡 2 pts to go |
| P12 | 11 | 54.5% | 54.5% | +0.0 | n/a | no target |
| P13 | 196420 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 13.8% | 13.8% | -2.3 | n/a | no target |
| P01T | 210 | 53.8% | 53.8% | -6.0 | n/a | no target |
| P01_GOLD | 653 | 41.8% | 41.8% | -1.6 | 70% | ❌ 28 pts to go |
| P02 | 490 | 45.1% | 45.1% | -2.1 | 75% | ❌ 30 pts to go |
| P03 | 277 | 43.3% | 43.3% | -1.4 | 75% | ❌ 32 pts to go |
| P04 | 4847 | 35.4% | 35.4% | -3.3 | 70% | ❌ 35 pts to go |
| P05 | 429 | 21.9% | 21.9% | +0.6 | 55% | ❌ 33 pts to go |
| P06M | 28880 | 6.6% | 6.6% | +0.7 | n/a | no target |
| P06T | 55820 | 42.3% | 42.3% | -5.1 | n/a | no target |
| P06 | 258 | 51.9% | 51.9% | +0.8 | n/a | no target |
| P07 | 790 | 53.5% | 53.5% | +0.8 | 70% | ❌ 16 pts to go |
| P08 | 29531 | 55.9% | 55.9% | +1.1 | 75% | ❌ 19 pts to go |
| P09 | 276 | 46.7% | 46.7% | -0.2 | 85% | ❌ 38 pts to go |
| P10 | 2069 | 44.6% | 44.6% | +0.2 | 80% | ❌ 35 pts to go |
| P11 | 1812 | 51.6% | 51.6% | -1.7 | 70% | ❌ 18 pts to go |
| P12 | 11 | 27.3% | 27.3% | +0.0 | n/a | no target |
| P13 | 196420 | 5.7% | 5.7% | +0.2 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 29.2% | 29.2% | -8.6 | n/a | no target |
| P01T | 210 | 95.7% | 95.7% | -0.8 | n/a | no target |
| P01_GOLD | 653 | 69.8% | 69.8% | -3.1 | 90% | ❌ 20 pts to go |
| P02 | 490 | 73.5% | 73.5% | -3.2 | 90% | ❌ 16 pts to go |
| P03 | 277 | 78.3% | 78.3% | -3.7 | 90% | ❌ 12 pts to go |
| P04 | 4847 | 67.0% | 67.0% | -10.7 | 85% | ❌ 18 pts to go |
| P05 | 429 | 43.4% | 43.4% | +0.5 | 75% | ❌ 32 pts to go |
| P06M | 28880 | 29.1% | 29.1% | -3.8 | n/a | no target |
| P06T | 55820 | 97.8% | 97.8% | -0.5 | n/a | no target |
| P06 | 258 | 92.2% | 92.2% | +2.2 | n/a | no target |
| P07 | 790 | 94.3% | 94.3% | +2.6 | 100% | 🟡 6 pts to go |
| P08 | 29531 | 92.8% | 92.8% | +5.5 | 100% | 🟡 7 pts to go |
| P09 | 276 | 66.3% | 66.3% | -0.2 | n/a | no target |
| P10 | 2069 | 90.1% | 90.1% | -0.2 | 100% | 🟡 10 pts to go |
| P11 | 1812 | 90.2% | 90.2% | +0.0 | n/a | no target |
| P12 | 11 | 54.5% | 54.5% | +0.0 | n/a | no target |
| P13 | 196420 | 69.7% | 69.7% | -0.1 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 33.4% | 33.4% | -3.5 | n/a | no target · QC vendors: 57 rows, 100.0% filled |
| P01T | 210 | 21.9% | 21.9% | +2.2 | n/a | no target · QC vendors: 34 rows, 88.2% filled |
| P01_GOLD | 653 | 45.5% | 45.5% | +2.0 | 95% | ❌ 50 pts to go · QC vendors: 49 rows, 98.0% filled |
| P02 | 490 | 57.6% | 57.6% | +1.6 | 95% | ❌ 37 pts to go · QC vendors: 111 rows, 100.0% filled |
| P03 | 277 | 44.8% | 44.8% | +1.9 | 95% | ❌ 50 pts to go · QC vendors: 19 rows, 100.0% filled |
| P04 | 4847 | 39.0% | 39.0% | +6.6 | 95% | ❌ 56 pts to go · QC vendors: 598 rows, 97.8% filled |
| P05 | 429 | 14.9% | 14.9% | +0.9 | n/a | no target · QC vendors: 38 rows, 100.0% filled |
| P06M | 28880 | 35.4% | 35.4% | -2.1 | n/a | no target · QC vendors: 7497 rows, 99.9% filled |
| P06T | 55820 | 37.7% | 37.7% | +7.1 | n/a | no target · QC vendors: 21433 rows, 96.1% filled |
| P06 | 258 | 7.0% | 7.0% | -0.1 | n/a | no target · QC vendors: 12 rows, 66.7% filled |
| P07 | 790 | 6.7% | 6.7% | -0.2 | n/a | no target · QC vendors: 45 rows, 77.8% filled |
| P08 | 29531 | 7.1% | 7.1% | +0.1 | n/a | no target · QC vendors: 1799 rows, 92.7% filled |
| P09 | 276 | 73.6% | 73.6% | +0.1 | 95% | ❌ 21 pts to go · QC vendors: 100 rows, 100.0% filled |
| P10 | 2069 | 15.8% | 15.8% | +0.1 | n/a | no target · QC vendors: 200 rows, 92.5% filled |
| P11 | 1812 | 20.7% | 20.7% | +1.1 | n/a | no target · QC vendors: 323 rows, 94.1% filled |
| P12 | 11 | 81.8% | 81.8% | +0.0 | n/a | no target · QC vendors: 2 rows, 100.0% filled |
| P13 | 196420 | 22.3% | 22.3% | +0.1 | n/a | no target · QC vendors: 43783 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 42.7% | 42.7% | -3.5 | n/a | no target · vendors with a registry record: 161 rows, 100.0% filled |
| P01T | 210 | 56.2% | 56.2% | -3.6 | n/a | no target · vendors with a registry record: 118 rows, 100.0% filled |
| P01_GOLD | 653 | 81.8% | 81.8% | +0.9 | 100% | ❌ 18 pts to go · vendors with a registry record: 534 rows, 100.0% filled |
| P02 | 490 | 78.4% | 78.4% | +0.0 | 100% | ❌ 22 pts to go · vendors with a registry record: 384 rows, 100.0% filled |
| P03 | 277 | 78.7% | 78.7% | +0.5 | 100% | ❌ 21 pts to go · vendors with a registry record: 218 rows, 100.0% filled |
| P04 | 4847 | 54.7% | 54.7% | +0.7 | 100% | ❌ 45 pts to go · vendors with a registry record: 2652 rows, 100.0% filled |
| P05 | 429 | 63.2% | 63.2% | +0.4 | n/a | no target · vendors with a registry record: 271 rows, 100.0% filled |
| P06M | 28880 | 39.6% | 39.6% | -1.6 | n/a | no target · vendors with a registry record: 11447 rows, 100.0% filled |
| P06T | 55820 | 68.4% | 68.4% | +0.8 | n/a | no target · vendors with a registry record: 38198 rows, 100.0% filled |
| P06 | 258 | 39.1% | 39.1% | -0.2 | n/a | no target · vendors with a registry record: 101 rows, 100.0% filled |
| P07 | 790 | 32.2% | 32.2% | +0.4 | n/a | no target · vendors with a registry record: 254 rows, 100.0% filled |
| P08 | 29531 | 31.9% | 31.9% | +1.9 | n/a | no target · vendors with a registry record: 9415 rows, 100.0% filled |
| P09 | 276 | 89.5% | 89.5% | +0.0 | n/a | no target · vendors with a registry record: 247 rows, 100.0% filled |
| P10 | 2069 | 40.1% | 40.1% | +0.0 | n/a | no target · vendors with a registry record: 829 rows, 100.0% filled |
| P11 | 1812 | 59.4% | 59.4% | +0.1 | n/a | no target · vendors with a registry record: 1076 rows, 100.0% filled |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 11 rows, 100.0% filled |
| P13 | 196420 | 40.0% | 40.0% | -0.2 | n/a | no target · vendors with a registry record: 78589 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 97.6% | 97.6% | +1.2 | 90% | ✅ met |
| P01T | 210 | 70.5% | 70.5% | -0.2 | 90% | ❌ 20 pts to go |
| P01_GOLD | 653 | 88.4% | 88.4% | +1.0 | 95% | 🟡 7 pts to go |
| P02 | 490 | 88.2% | 88.2% | +0.0 | 95% | 🟡 7 pts to go |
| P03 | 277 | 83.8% | 83.8% | +0.7 | 85% | 🟡 1 pts to go |
| P04 | 4847 | 68.9% | 68.9% | +4.4 | 90% | ❌ 21 pts to go |
| P05 | 429 | 76.7% | 76.7% | -1.3 | 75% | ✅ met |
| P06M | 28880 | 94.9% | 94.9% | +1.1 | n/a | no target |
| P06T | 55820 | 37.7% | 37.7% | +0.8 | n/a | no target |
| P06 | 258 | 72.5% | 72.5% | +1.4 | 80% | 🟡 8 pts to go |
| P07 | 790 | 61.3% | 61.4% | +3.1 | 80% | ❌ 19 pts to go |
| P08 | 29531 | 56.9% | 56.9% | +5.0 | 75% | ❌ 18 pts to go |
| P09 | 276 | 75.4% | 75.4% | -0.2 | 95% | ❌ 20 pts to go |
| P10 | 2069 | 46.2% | 46.2% | -0.6 | 70% | ❌ 24 pts to go |
| P11 | 1812 | 32.5% | 32.5% | +0.7 | 65% | ❌ 32 pts to go |
| P12 | 11 | 72.7% | 72.7% | +0.0 | 80% | 🟡 7 pts to go |
| P13 | 196420 | 39.8% | 39.8% | -5.8 | 60% | ❌ 20 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 14.6% | 14.6% | -3.9 | 50% | ❌ 35 pts to go |
| P01T | 210 | 16.2% | 16.2% | +0.0 | n/a | no target |
| P01_GOLD | 653 | 19.1% | 19.1% | -0.7 | 40% | ❌ 21 pts to go |
| P02 | 490 | 19.2% | 19.2% | -0.7 | 40% | ❌ 21 pts to go |
| P03 | 277 | 19.5% | 19.5% | -0.8 | 40% | ❌ 20 pts to go |
| P04 | 4847 | 14.0% | 14.0% | -2.3 | 40% | ❌ 26 pts to go |
| P05 | 429 | 21.0% | 21.0% | +0.1 | 25% | 🟡 4 pts to go |
| P06M | 28880 | 20.1% | 20.1% | -0.3 | n/a | no target |
| P06T | 55820 | 10.1% | 10.1% | +2.6 | n/a | no target |
| P06 | 258 | 20.9% | 20.9% | +3.4 | 35% | ❌ 14 pts to go |
| P07 | 790 | 22.9% | 22.9% | +3.8 | 35% | ❌ 12 pts to go |
| P08 | 29531 | 22.6% | 22.6% | +4.9 | 35% | ❌ 12 pts to go |
| P09 | 276 | 16.7% | 16.7% | +0.0 | n/a | no target |
| P10 | 2069 | 9.3% | 9.3% | +2.2 | 30% | ❌ 21 pts to go |
| P11 | 1812 | 9.6% | 9.6% | +3.1 | n/a | no target |
| P12 | 11 | 18.2% | 18.2% | +0.0 | n/a | no target |
| P13 | 196420 | 10.6% | 10.6% | -1.9 | 30% | ❌ 19 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 210 | 85.2% | 85.2% | +0.0 | 100% | ❌ 15 pts to go |
| P01_GOLD | 653 | 91.7% | 91.7% | +0.6 | 100% | 🟡 8 pts to go |
| P02 | 490 | 96.7% | 96.7% | +0.1 | 100% | 🟡 3 pts to go |
| P03 | 277 | 89.5% | 89.5% | +0.0 | 100% | ❌ 10 pts to go |
| P04 | 4847 | 78.7% | 78.7% | +6.2 | 100% | ❌ 21 pts to go |
| P05 | 429 | 90.0% | 90.0% | +0.0 | 100% | 🟡 10 pts to go |
| P06M | 28880 | 99.5% | 99.5% | +0.1 | n/a | no target |
| P06T | 55820 | 59.5% | 59.5% | +0.8 | n/a | no target |
| P06 | 258 | 82.2% | 82.2% | +0.1 | 95% | ❌ 13 pts to go |
| P07 | 790 | 87.1% | 87.1% | +1.7 | 95% | 🟡 8 pts to go |
| P08 | 29531 | 85.4% | 85.4% | +0.9 | 95% | 🟡 10 pts to go |
| P09 | 276 | 96.4% | 96.4% | +0.0 | 100% | 🟡 4 pts to go |
| P10 | 2069 | 54.0% | 54.1% | -0.6 | 95% | ❌ 41 pts to go |
| P11 | 1812 | 61.6% | 61.6% | +0.7 | 80% | ❌ 18 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 196420 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 70.3% | 70.3% | -0.8 | n/a | no target |
| P01T | 210 | 71.9% | 71.9% | -2.3 | n/a | no target |
| P01_GOLD | 653 | 73.0% | 73.0% | -0.2 | 90% | ❌ 17 pts to go |
| P02 | 490 | 77.3% | 77.3% | -1.1 | 95% | ❌ 18 pts to go |
| P03 | 277 | 73.6% | 73.6% | -0.5 | 95% | ❌ 21 pts to go |
| P04 | 4847 | 69.5% | 69.5% | +0.0 | 95% | ❌ 26 pts to go |
| P05 | 429 | 71.6% | 71.6% | -0.9 | 90% | ❌ 18 pts to go |
| P06M | 28880 | 73.6% | 73.6% | -3.1 | n/a | no target |
| P06T | 55820 | 58.5% | 58.5% | -0.1 | n/a | no target |
| P06 | 258 | 70.2% | 70.2% | +4.8 | 95% | ❌ 25 pts to go |
| P07 | 790 | 67.8% | 67.8% | +8.1 | 90% | ❌ 22 pts to go |
| P08 | 29531 | 70.9% | 70.9% | +12.3 | 95% | ❌ 24 pts to go |
| P09 | 276 | 85.5% | 85.5% | -0.3 | 100% | ❌ 14 pts to go |
| P10 | 2069 | 53.3% | 53.3% | -0.5 | 95% | ❌ 42 pts to go |
| P11 | 1812 | 33.0% | 33.0% | +2.3 | 75% | ❌ 42 pts to go |
| P12 | 11 | 81.8% | 81.8% | +0.0 | n/a | no target |
| P13 | 196420 | 57.6% | 57.6% | -10.3 | 95% | ❌ 37 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 82.8% | 82.8% | -0.7 | n/a | no target |
| P01T | 210 | 90.0% | 90.0% | -1.7 | 95% | 🟡 5 pts to go |
| P01_GOLD | 653 | 85.1% | 85.1% | +0.1 | 90% | 🟡 5 pts to go |
| P02 | 490 | 90.6% | 90.6% | -0.4 | 95% | 🟡 4 pts to go |
| P03 | 277 | 84.1% | 84.1% | +0.3 | 95% | ❌ 11 pts to go |
| P04 | 4847 | 90.4% | 90.4% | -1.2 | 90% | ✅ met |
| P05 | 429 | 92.5% | 92.5% | +0.1 | 95% | 🟡 2 pts to go |
| P06M | 28880 | 85.5% | 85.5% | +0.2 | n/a | no target |
| P06T | 55820 | 87.3% | 87.3% | +2.7 | n/a | no target |
| P06 | 258 | 93.0% | 93.0% | +7.6 | 100% | 🟡 7 pts to go |
| P07 | 790 | 94.7% | 94.7% | +11.1 | 100% | 🟡 5 pts to go |
| P08 | 29531 | 95.0% | 95.0% | +17.2 | 100% | 🟡 5 pts to go |
| P09 | 276 | 73.9% | 73.9% | -0.3 | n/a | no target |
| P10 | 2069 | 94.2% | 94.2% | -0.2 | 100% | 🟡 6 pts to go |
| P11 | 1812 | 55.5% | 55.5% | +4.4 | 80% | ❌ 24 pts to go |
| P12 | 11 | 90.9% | 90.9% | +0.0 | n/a | no target |
| P13 | 196420 | 73.2% | 73.2% | -7.6 | 95% | ❌ 22 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 2.4% | 2.4% | -0.8 | n/a | no target |
| P01T | 210 | 9.5% | 9.5% | +0.8 | n/a | no target |
| P01_GOLD | 653 | 13.6% | 13.6% | -0.4 | 25% | ❌ 11 pts to go |
| P02 | 490 | 23.7% | 23.7% | -1.1 | 40% | ❌ 16 pts to go |
| P03 | 277 | 8.7% | 8.7% | -0.3 | 20% | ❌ 11 pts to go |
| P04 | 4847 | 2.4% | 2.4% | -0.9 | 20% | ❌ 18 pts to go |
| P05 | 429 | 3.0% | 3.0% | -0.3 | 15% | ❌ 12 pts to go |
| P06M | 28880 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06T | 55820 | 0.3% | 0.3% | +0.1 | n/a | no target |
| P06 | 258 | 5.0% | 5.0% | -0.4 | n/a | no target |
| P07 | 790 | 8.0% | 8.0% | +0.1 | n/a | no target |
| P08 | 29531 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 276 | 7.2% | 7.2% | -0.4 | n/a | no target |
| P10 | 2069 | 0.8% | 0.8% | +0.0 | n/a | no target |
| P11 | 1812 | 0.7% | 0.7% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 196420 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 11.9% | 11.9% | -4.2 | n/a | no target |
| P01T | 210 | 18.1% | 18.1% | -1.1 | 70% | ❌ 52 pts to go |
| P01_GOLD | 653 | 40.7% | 40.7% | -1.4 | 80% | ❌ 39 pts to go |
| P02 | 490 | 54.7% | 54.7% | -2.6 | 90% | ❌ 35 pts to go |
| P03 | 277 | 18.1% | 18.1% | -1.1 | 60% | ❌ 42 pts to go |
| P04 | 4847 | 15.0% | 15.0% | -5.2 | 85% | ❌ 70 pts to go |
| P05 | 429 | 11.0% | 11.0% | -0.1 | 50% | ❌ 39 pts to go |
| P06M | 28880 | 0.5% | 0.5% | -0.1 | n/a | no target |
| P06T | 55820 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P06 | 258 | 13.2% | 13.2% | +0.0 | n/a | no target |
| P07 | 790 | 9.5% | 9.5% | +0.4 | n/a | no target |
| P08 | 29531 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P09 | 276 | 72.1% | 72.1% | +0.1 | 95% | ❌ 23 pts to go |
| P10 | 2069 | 1.4% | 1.4% | -0.2 | n/a | no target |
| P11 | 1812 | 12.6% | 12.6% | -0.4 | n/a | no target |
| P12 | 11 | 27.3% | 27.3% | +0.0 | n/a | no target |
| P13 | 196420 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 4.5% | 4.5% | -1.1 | n/a | no target |
| P01T | 210 | 11.0% | 11.0% | +1.8 | n/a | no target |
| P01_GOLD | 653 | 32.5% | 32.5% | -1.3 | 70% | ❌ 38 pts to go |
| P02 | 490 | 37.3% | 37.3% | -1.4 | 75% | ❌ 38 pts to go |
| P03 | 277 | 18.1% | 18.1% | -1.1 | 55% | ❌ 37 pts to go |
| P04 | 4847 | 15.0% | 15.0% | -5.2 | 75% | ❌ 60 pts to go |
| P05 | 429 | 10.3% | 10.3% | +0.1 | 50% | ❌ 40 pts to go |
| P06M | 28880 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06T | 55820 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 258 | 5.4% | 5.4% | -0.3 | n/a | no target |
| P07 | 790 | 4.8% | 4.8% | +0.2 | n/a | no target |
| P08 | 29531 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 276 | 68.8% | 68.8% | +0.1 | 95% | ❌ 26 pts to go |
| P10 | 2069 | 0.7% | 0.7% | -0.1 | n/a | no target |
| P11 | 1812 | 12.4% | 12.4% | -0.4 | n/a | no target |
| P12 | 11 | 18.2% | 18.2% | +0.0 | n/a | no target |
| P13 | 196420 | 0.1% | 0.1% | -0.1 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 5.3% | 5.3% | -2.3 | n/a | no target |
| P01T | 210 | 8.6% | 8.6% | -0.1 | n/a | no target |
| P01_GOLD | 653 | 54.8% | 55.0% | -2.3 | 80% | ❌ 25 pts to go |
| P02 | 490 | 43.3% | 43.5% | -2.0 | 75% | ❌ 32 pts to go |
| P03 | 277 | 33.9% | 33.9% | -2.2 | 70% | ❌ 36 pts to go |
| P04 | 4847 | 14.8% | 15.0% | -5.1 | 70% | ❌ 55 pts to go |
| P05 | 429 | 13.8% | 13.8% | -0.2 | 50% | ❌ 36 pts to go |
| P06M | 28880 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06T | 55820 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06 | 258 | 12.8% | 12.8% | -0.4 | n/a | no target |
| P07 | 790 | 1.0% | 1.0% | -0.1 | n/a | no target |
| P08 | 29531 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P09 | 276 | 46.7% | 47.1% | -0.2 | 80% | ❌ 33 pts to go |
| P10 | 2069 | 1.1% | 1.1% | +0.0 | n/a | no target |
| P11 | 1812 | 4.4% | 4.4% | -0.1 | n/a | no target |
| P12 | 11 | 36.4% | 36.4% | +0.0 | n/a | no target |
| P13 | 196420 | 0.1% | 0.1% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 11.7% | 11.7% | -3.2 | n/a | no target |
| P01T | 210 | 20.5% | 20.5% | +1.3 | 60% | ❌ 40 pts to go |
| P01_GOLD | 653 | 59.6% | 59.6% | -2.6 | 70% | ❌ 10 pts to go |
| P02 | 490 | 37.6% | 37.6% | -1.9 | 50% | ❌ 12 pts to go |
| P03 | 277 | 45.1% | 45.1% | -2.6 | 55% | 🟡 10 pts to go |
| P04 | 4847 | 9.1% | 9.1% | -3.4 | 40% | ❌ 31 pts to go |
| P05 | 429 | 16.1% | 16.1% | -0.5 | 40% | ❌ 24 pts to go |
| P06M | 28880 | 2.2% | 2.2% | -0.6 | n/a | no target |
| P06T | 55820 | 1.4% | 1.4% | -0.1 | n/a | no target |
| P06 | 258 | 17.1% | 17.1% | -1.1 | n/a | no target |
| P07 | 790 | 4.9% | 4.9% | +0.0 | n/a | no target |
| P08 | 29531 | 2.1% | 2.1% | +0.0 | n/a | no target |
| P09 | 276 | 6.2% | 6.2% | +0.4 | n/a | no target |
| P10 | 2069 | 4.9% | 4.9% | -0.2 | n/a | no target |
| P11 | 1812 | 3.9% | 3.9% | -0.1 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 196420 | 0.6% | 0.6% | -0.1 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 16.7% | 16.7% | -5.0 | n/a | no target |
| P01T | 210 | 26.2% | 26.2% | -1.7 | 65% | ❌ 39 pts to go |
| P01_GOLD | 653 | 65.2% | 65.2% | -3.4 | 70% | 🟡 5 pts to go |
| P02 | 490 | 22.7% | 22.7% | -1.0 | 50% | ❌ 27 pts to go |
| P03 | 277 | 48.0% | 48.0% | -2.4 | 60% | ❌ 12 pts to go |
| P04 | 4847 | 4.1% | 4.1% | -1.5 | 40% | ❌ 36 pts to go |
| P05 | 429 | 19.6% | 19.6% | -0.3 | 45% | ❌ 25 pts to go |
| P06M | 28880 | 1.3% | 1.3% | -0.4 | n/a | no target |
| P06T | 55820 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06 | 258 | 26.0% | 26.0% | -3.3 | n/a | no target |
| P07 | 790 | 4.9% | 4.9% | -0.2 | n/a | no target |
| P08 | 29531 | 0.9% | 0.9% | +0.0 | n/a | no target |
| P09 | 276 | 10.9% | 10.9% | +0.0 | n/a | no target |
| P10 | 2069 | 3.0% | 3.0% | -0.3 | n/a | no target |
| P11 | 1812 | 3.6% | 3.6% | +0.0 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 196420 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 10.1% | 10.1% | -1.9 | n/a | no target |
| P01T | 210 | 13.3% | 13.3% | +0.6 | n/a | no target |
| P01_GOLD | 653 | 47.9% | 47.9% | -2.3 | 50% | 🟡 2 pts to go |
| P02 | 490 | 35.9% | 35.9% | -1.7 | n/a | no target |
| P03 | 277 | 48.4% | 48.4% | -2.4 | 60% | ❌ 12 pts to go |
| P04 | 4847 | 9.3% | 9.3% | -3.5 | n/a | no target |
| P05 | 429 | 15.2% | 15.2% | +0.0 | n/a | no target |
| P06M | 28880 | 0.6% | 0.6% | -0.2 | n/a | no target |
| P06T | 55820 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 258 | 18.6% | 18.6% | -1.8 | n/a | no target |
| P07 | 790 | 5.1% | 5.1% | -0.6 | n/a | no target |
| P08 | 29531 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P09 | 276 | 20.7% | 20.7% | +0.0 | n/a | no target |
| P10 | 2069 | 2.2% | 2.2% | -0.3 | n/a | no target |
| P11 | 1812 | 2.5% | 2.5% | -0.2 | n/a | no target |
| P12 | 11 | 18.2% | 18.2% | +0.0 | n/a | no target |
| P13 | 196420 | 0.1% | 0.1% | -0.1 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 6.6% | 6.6% | -2.2 | 15% | 🟡 8 pts to go |
| P01T | 210 | 12.9% | 12.9% | +0.2 | 15% | 🟡 2 pts to go |
| P01_GOLD | 653 | 33.4% | 33.4% | -1.7 | 40% | 🟡 7 pts to go |
| P02 | 490 | 11.6% | 11.8% | -0.6 | 25% | ❌ 13 pts to go |
| P03 | 277 | 15.5% | 15.5% | -1.0 | 25% | 🟡 10 pts to go |
| P04 | 4847 | 2.1% | 2.1% | -0.6 | 15% | ❌ 13 pts to go |
| P05 | 429 | 6.3% | 6.3% | -0.3 | 15% | 🟡 9 pts to go |
| P06M | 28880 | 0.8% | 0.8% | +0.0 | 15% | ❌ 14 pts to go |
| P06T | 55820 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P06 | 258 | 8.5% | 8.5% | -0.8 | 15% | 🟡 6 pts to go |
| P07 | 790 | 3.4% | 3.4% | +0.0 | 15% | ❌ 12 pts to go |
| P08 | 29531 | 0.6% | 0.6% | +0.1 | 15% | ❌ 14 pts to go |
| P09 | 276 | 1.1% | 1.1% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2069 | 1.4% | 1.4% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 1812 | 1.2% | 1.2% | +0.0 | 15% | ❌ 14 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 196420 | 0.6% | 0.6% | +0.0 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 4.8% | 4.8% | -0.8 | 15% | ❌ 10 pts to go |
| P01T | 210 | 11.4% | 11.4% | +0.5 | 25% | ❌ 14 pts to go |
| P01_GOLD | 653 | 27.9% | 27.9% | -1.0 | 25% | ✅ met |
| P02 | 490 | 24.1% | 24.1% | -1.3 | 15% | ✅ met |
| P03 | 277 | 20.6% | 20.6% | -1.2 | 15% | ✅ met |
| P04 | 4847 | 3.0% | 3.0% | -1.0 | 15% | ❌ 12 pts to go |
| P05 | 429 | 11.4% | 11.4% | +0.0 | 15% | 🟡 4 pts to go |
| P06M | 28880 | 0.6% | 0.6% | +0.0 | 15% | ❌ 14 pts to go |
| P06T | 55820 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 258 | 7.0% | 7.0% | -0.1 | 15% | 🟡 8 pts to go |
| P07 | 790 | 1.6% | 1.6% | -0.2 | 15% | ❌ 13 pts to go |
| P08 | 29531 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 276 | 1.4% | 1.4% | -0.1 | 15% | ❌ 14 pts to go |
| P10 | 2069 | 1.5% | 1.5% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 1812 | 1.8% | 1.8% | +0.0 | 15% | ❌ 13 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 196420 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 1.1% | 1.1% | -0.5 | 20% | ❌ 19 pts to go |
| P01T | 210 | 3.3% | 3.3% | +0.2 | 20% | ❌ 17 pts to go |
| P01_GOLD | 653 | 4.1% | 4.1% | -0.2 | 20% | ❌ 16 pts to go |
| P02 | 490 | 1.4% | 1.4% | -0.1 | 20% | ❌ 19 pts to go |
| P03 | 277 | 1.4% | 1.4% | -0.5 | 20% | ❌ 19 pts to go |
| P04 | 4847 | 0.6% | 0.6% | -0.1 | 20% | ❌ 19 pts to go |
| P05 | 429 | 0.9% | 0.9% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 28880 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 55820 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 258 | 1.2% | 1.2% | -0.2 | 20% | ❌ 19 pts to go |
| P07 | 790 | 0.3% | 0.3% | +0.1 | 20% | ❌ 20 pts to go |
| P08 | 29531 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 276 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2069 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1812 | 0.1% | 0.1% | +0.0 | 20% | ❌ 20 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 196420 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 1.1% | 1.1% | -0.5 | 15% | ❌ 14 pts to go |
| P01T | 210 | 2.4% | 2.4% | -0.7 | 15% | ❌ 13 pts to go |
| P01_GOLD | 653 | 10.4% | 10.4% | -0.1 | 15% | 🟡 5 pts to go |
| P02 | 490 | 10.4% | 10.4% | -1.1 | 15% | 🟡 5 pts to go |
| P03 | 277 | 19.9% | 19.9% | -0.8 | 15% | ✅ met |
| P04 | 4847 | 1.8% | 1.8% | -0.6 | 15% | ❌ 13 pts to go |
| P05 | 429 | 2.8% | 2.8% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 28880 | 0.3% | 0.3% | -0.1 | 15% | ❌ 15 pts to go |
| P06T | 55820 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 258 | 3.9% | 3.9% | +0.0 | 15% | ❌ 11 pts to go |
| P07 | 790 | 1.3% | 1.3% | +0.1 | 15% | ❌ 14 pts to go |
| P08 | 29531 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 276 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2069 | 1.1% | 1.1% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 1812 | 0.8% | 0.8% | +0.0 | 15% | ❌ 14 pts to go |
| P12 | 11 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 196420 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 11.1% | 11.1% | -1.3 | 20% | 🟡 9 pts to go |
| P01T | 210 | 14.3% | 14.3% | +0.8 | 40% | ❌ 26 pts to go |
| P01_GOLD | 653 | 44.7% | 44.7% | -1.9 | 40% | ✅ met |
| P02 | 490 | 41.4% | 41.4% | -1.8 | 20% | ✅ met |
| P03 | 277 | 46.9% | 46.9% | -1.6 | 35% | ✅ met |
| P04 | 4847 | 11.1% | 11.1% | -3.8 | 20% | 🟡 9 pts to go |
| P05 | 429 | 15.6% | 15.6% | +0.0 | 20% | 🟡 4 pts to go |
| P06M | 28880 | 0.9% | 0.9% | -0.1 | 20% | ❌ 19 pts to go |
| P06T | 55820 | 0.6% | 0.6% | +0.0 | 20% | ❌ 19 pts to go |
| P06 | 258 | 19.4% | 19.4% | -1.7 | 20% | 🟡 1 pts to go |
| P07 | 790 | 5.7% | 5.7% | -0.4 | 20% | ❌ 14 pts to go |
| P08 | 29531 | 0.8% | 0.8% | +0.0 | 20% | ❌ 19 pts to go |
| P09 | 276 | 21.0% | 21.0% | -0.1 | 20% | ✅ met |
| P10 | 2069 | 3.5% | 3.5% | -0.3 | 20% | ❌ 16 pts to go |
| P11 | 1812 | 3.0% | 3.0% | -0.2 | 20% | ❌ 17 pts to go |
| P12 | 11 | 9.1% | 9.1% | +0.0 | 20% | ❌ 11 pts to go |
| P13 | 196420 | 0.3% | 0.3% | -0.1 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 12.7% | 12.7% | -5.4 | n/a | no target |
| P01T | 210 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 653 | 68.9% | 68.9% | -2.7 | 95% | ❌ 26 pts to go |
| P02 | 490 | 62.9% | 62.9% | -3.3 | 95% | ❌ 32 pts to go |
| P03 | 277 | 55.2% | 55.2% | -2.7 | 90% | ❌ 35 pts to go |
| P04 | 4847 | 20.6% | 20.6% | -5.9 | 85% | ❌ 64 pts to go |
| P05 | 429 | 39.4% | 39.4% | +0.5 | 75% | ❌ 36 pts to go |
| P06M | 28880 | 23.8% | 23.8% | -4.3 | n/a | no target |
| P06T | 55820 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 258 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 790 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29531 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 89.1% | 89.1% | +0.0 | 100% | ❌ 11 pts to go |
| P10 | 2069 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1812 | 3.9% | 3.9% | +0.1 | 60% | ❌ 56 pts to go |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 196420 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 12.7% | 12.7% | -5.4 | n/a | no target |
| P01T | 210 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 653 | 70.8% | 70.8% | -2.7 | 100% | ❌ 29 pts to go |
| P02 | 490 | 64.7% | 64.7% | -3.5 | 100% | ❌ 35 pts to go |
| P03 | 277 | 57.8% | 57.8% | -2.7 | n/a | no target |
| P04 | 4847 | 20.9% | 20.9% | -6.1 | 95% | ❌ 74 pts to go |
| P05 | 429 | 35.2% | 35.2% | +0.6 | 80% | ❌ 45 pts to go |
| P06M | 28880 | 23.8% | 23.8% | -4.3 | n/a | no target |
| P06T | 55820 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 258 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 790 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29531 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 91.7% | 91.7% | +0.1 | 100% | 🟡 8 pts to go |
| P10 | 2069 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1812 | 4.1% | 4.1% | +0.1 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 196420 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 82.0% | 82.0% | -2.3 | n/a | no target |
| P01T | 210 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 653 | 54.1% | 54.1% | +1.8 | 85% | ❌ 31 pts to go |
| P02 | 490 | 60.4% | 60.4% | +1.2 | 90% | ❌ 30 pts to go |
| P03 | 277 | 46.6% | 46.6% | +2.6 | 85% | ❌ 38 pts to go |
| P04 | 4847 | 37.5% | 37.5% | +8.4 | 90% | ❌ 52 pts to go |
| P05 | 429 | 33.1% | 33.1% | +0.2 | 75% | ❌ 42 pts to go |
| P06M | 28880 | 81.9% | 81.9% | -2.4 | n/a | no target |
| P06T | 55820 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 258 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 790 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29531 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 81.9% | 81.9% | +0.1 | 95% | ❌ 13 pts to go |
| P10 | 2069 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1812 | 3.8% | 3.8% | +0.5 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 196420 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 54.4% | 54.4% | -11.5 | n/a | no target |
| P01T | 210 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 653 | 53.8% | 53.8% | +1.8 | 85% | ❌ 31 pts to go |
| P02 | 490 | 55.1% | 55.1% | +1.7 | 90% | ❌ 35 pts to go |
| P03 | 277 | 46.9% | 46.9% | +2.5 | 85% | ❌ 38 pts to go |
| P04 | 4847 | 33.2% | 33.2% | +8.6 | 90% | ❌ 57 pts to go |
| P05 | 429 | 42.0% | 42.0% | -0.7 | 75% | ❌ 33 pts to go |
| P06M | 28880 | 63.1% | 63.1% | -6.1 | n/a | no target |
| P06T | 55820 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 258 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 790 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29531 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 0.4% | 0.4% | +0.0 | 95% | ❌ 95 pts to go |
| P10 | 2069 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1812 | 3.0% | 3.0% | +0.5 | n/a | no target |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 196420 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 96.8% | 96.8% | +1.6 | n/a | no target |
| P01T | 210 | 95.7% | 95.7% | -0.4 | n/a | no target |
| P01_GOLD | 653 | 86.1% | 86.2% | +0.6 | 100% | ❌ 14 pts to go |
| P02 | 490 | 78.0% | 78.0% | +0.4 | 100% | ❌ 22 pts to go |
| P03 | 277 | 92.4% | 92.4% | -0.1 | n/a | no target |
| P04 | 4847 | 53.4% | 53.4% | +2.8 | 95% | ❌ 42 pts to go |
| P05 | 429 | 77.6% | 77.6% | +0.3 | 95% | ❌ 17 pts to go |
| P06M | 28880 | 99.4% | 99.4% | +0.1 | n/a | no target |
| P06T | 55820 | 97.9% | 97.9% | +3.4 | n/a | no target |
| P06 | 258 | 21.3% | 21.3% | +0.9 | n/a | no target |
| P07 | 790 | 10.4% | 10.4% | +0.2 | n/a | no target |
| P08 | 29531 | 4.6% | 4.6% | +0.1 | n/a | no target |
| P09 | 276 | 98.2% | 98.2% | +0.0 | 100% | 🟡 2 pts to go |
| P10 | 2069 | 70.9% | 70.9% | +0.3 | n/a | no target |
| P11 | 1812 | 70.1% | 70.1% | +0.3 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 196420 | 99.6% | 99.6% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 96.8% | 96.8% | +1.6 | n/a | no target |
| P01T | 210 | 95.7% | 95.7% | -0.4 | n/a | no target |
| P01_GOLD | 653 | 89.1% | 89.3% | +0.4 | 100% | ❌ 11 pts to go |
| P02 | 490 | 79.2% | 79.2% | +0.4 | 100% | ❌ 21 pts to go |
| P03 | 277 | 93.1% | 93.1% | -0.1 | n/a | no target |
| P04 | 4847 | 55.9% | 55.9% | +1.9 | 95% | ❌ 39 pts to go |
| P05 | 429 | 89.7% | 89.7% | +0.4 | 70% | ✅ met |
| P06M | 28880 | 99.4% | 99.4% | +0.1 | n/a | no target |
| P06T | 55820 | 97.9% | 97.9% | +3.4 | n/a | no target |
| P06 | 258 | 21.3% | 21.3% | +0.9 | n/a | no target |
| P07 | 790 | 10.4% | 10.4% | +0.2 | n/a | no target |
| P08 | 29531 | 4.6% | 4.6% | +0.1 | n/a | no target |
| P09 | 276 | 98.2% | 98.2% | +0.0 | 100% | 🟡 2 pts to go |
| P10 | 2069 | 70.9% | 70.9% | +0.3 | n/a | no target |
| P11 | 1812 | 70.2% | 70.2% | +0.3 | n/a | no target |
| P12 | 11 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 196420 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 210 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 653 | 16.4% | 16.4% | -0.5 | 60% | ❌ 44 pts to go · rows from a source that publishes bids: 368 rows, 29.1% filled |
| P02 | 490 | 9.6% | 9.6% | -1.1 | n/a | no target · rows from a source that publishes bids: 294 rows, 16.0% filled |
| P03 | 277 | 13.4% | 13.4% | -0.5 | n/a | no target · rows from a source that publishes bids: 143 rows, 25.9% filled |
| P04 | 4847 | 1.3% | 1.3% | -0.4 | n/a | no target · rows from a source that publishes bids: 884 rows, 6.9% filled |
| P05 | 429 | 2.6% | 2.6% | +0.0 | n/a | no target · rows from a source that publishes bids: 60 rows, 18.3% filled |
| P06M | 28880 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55820 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 258 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 790 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29531 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 276 | 4.3% | 4.3% | -0.1 | n/a | no target · rows from a source that publishes bids: 263 rows, 4.6% filled |
| P10 | 2069 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1812 | 0.4% | 0.4% | +0.0 | n/a | no target · rows from a source that publishes bids: 68 rows, 11.8% filled |
| P12 | 11 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 11 rows, 0.0% filled |
| P13 | 196420 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 210 | 0.0% | 97.6% | +0.0 | n/a | no target |
| P01_GOLD | 653 | 51.1% | 82.7% | -2.3 | 90% | ❌ 39 pts to go |
| P02 | 490 | 50.8% | 87.8% | -2.6 | 90% | ❌ 39 pts to go |
| P03 | 277 | 44.0% | 80.9% | -1.9 | 90% | ❌ 46 pts to go |
| P04 | 4847 | 14.6% | 94.8% | -5.0 | 90% | ❌ 75 pts to go |
| P05 | 429 | 0.0% | 81.1% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 28880 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 55820 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 258 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 790 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 29531 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 276 | 2.9% | 4.7% | +0.0 | 90% | ❌ 87 pts to go |
| P10 | 2069 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1812 | 2.2% | 97.6% | +0.1 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 196420 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 210 | 1.0% | 98.6% | +0.1 | n/a | no target |
| P01_GOLD | 653 | 25.1% | 56.7% | -1.4 | 90% | ❌ 65 pts to go |
| P02 | 490 | 49.6% | 86.5% | -2.8 | n/a | no target |
| P03 | 277 | 24.2% | 61.0% | -1.0 | n/a | no target |
| P04 | 4847 | 15.8% | 96.0% | -5.6 | n/a | no target |
| P05 | 429 | 0.5% | 81.6% | +0.0 | n/a | no target |
| P06M | 28880 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 55820 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 258 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 790 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 29531 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 276 | 40.6% | 42.4% | +0.2 | n/a | no target |
| P10 | 2069 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1812 | 2.3% | 97.7% | +0.1 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 196420 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 210 | 2.4% | 100.0% | +0.2 | n/a | no target |
| P01_GOLD | 653 | 50.1% | 81.6% | -1.9 | 95% | ❌ 45 pts to go |
| P02 | 490 | 55.3% | 92.2% | -2.8 | n/a | no target |
| P03 | 277 | 48.0% | 84.8% | -2.4 | n/a | no target |
| P04 | 4847 | 16.3% | 96.5% | -5.9 | n/a | no target |
| P05 | 429 | 5.1% | 86.2% | +0.1 | n/a | no target |
| P06M | 28880 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 55820 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 258 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 790 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 29531 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 276 | 59.8% | 61.6% | -0.6 | n/a | no target |
| P10 | 2069 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1812 | 2.3% | 97.8% | -0.1 | n/a | no target |
| P12 | 11 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 196420 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 210 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 653 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 490 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 277 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4847 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 429 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 28880 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 55820 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 258 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 790 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 29531 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2069 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1812 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 196420 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 210 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 653 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 490 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 277 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4847 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 429 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 28880 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 55820 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 258 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 790 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 29531 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2069 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1812 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 196420 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 377 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 210 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 653 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 490 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 277 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4847 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 429 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 28880 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 55820 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 258 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 790 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 29531 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 276 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2069 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1812 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 11 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 196420 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |


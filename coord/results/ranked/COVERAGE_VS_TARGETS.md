# Coverage vs the downstream team's targets — 2026-11-13

Benchmarks (field × package with a numeric target): **90 of 438 met** (20.5%); 65 within 10 points; 283 further away.
A cell counts as filled only when it carries a value: blank, `not_published`, `not_found_yet` and label-only cells ("no identifier published …", "no dataset record …", "0 in the contract dataset …") do not count; the DNS checks count when checked. `any` = share of non-blank cells incl. such labels. Δ = change since the previous build in `coord/results/coverage_history.csv`.
Rows per package: P01M 420, P01T 206, P01_GOLD 657, P02 486, P03 275, P04 4816, P05 428, P06M 30514, P06T 55144, P06 249, P07 780, P08 29302, P09 278, P10R 0, P10 2052, P11 1813, P12 10, P13 202744

## Invoice-grade readiness (the row as an invoice header: bill-to, submit-to, references, terms, tax, vendor identity, follow-up)

| package | rows | all 11 elements | ≥ 9 of 11 | median elements | most-missing element |
|---|---|---|---|---|---|
| P01M | 420 | 0.0% | 9.5% | 7 | vendor GST/HST number (398 rows) |
| P01T | 206 | 1.0% | 32.5% | 8 | payment terms (162 rows) |
| P01_GOLD | 657 | 23.4% | 68.9% | 9 | payment terms (247 rows) |
| P02 | 486 | 7.4% | 52.7% | 9 | PO rule (378 rows) |
| P03 | 275 | 14.2% | 54.5% | 9 | payment terms (143 rows) |
| P04 | 4816 | 1.0% | 12.8% | 7 | PO rule (4617 rows) |
| P05 | 428 | 0.9% | 16.8% | 7 | payment terms (357 rows) |
| P06M | 30514 | 0.0% | 2.4% | 7 | PO rule (30129 rows) |
| P06T | 55144 | 0.1% | 13.4% | 7 | PO rule (54825 rows) |
| P06 | 249 | 0.0% | 9.2% | 6 | reference to quote (PO / contract / vendor id) (232 rows) |
| P07 | 780 | 0.0% | 2.9% | 6 | PO rule (745 rows) |
| P08 | 29302 | 0.0% | 1.5% | 6 | PO rule (29054 rows) |
| P09 | 278 | 1.4% | 42.1% | 8 | payment terms (258 rows) |
| P10 | 2052 | 0.0% | 1.2% | 5 | reference to quote (PO / contract / vendor id) (2052 rows) |
| P11 | 1813 | 0.1% | 7.9% | 6 | PO rule (1748 rows) |
| P12 | 10 | 0.0% | 40.0% | 8 | PO rule (10 rows) |
| P13 | 202744 | 0.0% | 0.3% | 6 | reference to quote (PO / contract / vendor id) (202744 rows) |

## AP grade (how stringently the row's accounts-payable data meets what an invoice needs; A = invoicing mailbox referee-confirmed on the buyer's own domain with MX, legal name, address, PO rule and terms all published, no penalties)

| package | rows | A | B | C | D | E | median ap_score |
|---|---|---|---|---|---|---|---|
| P01M | 420 | 11 | 71 | 338 | 0 | 0 | 66 |
| P01T | 206 | 26 | 33 | 147 | 0 | 0 | 66 |
| P01_GOLD | 657 | 256 | 172 | 229 | 0 | 0 | 81 |
| P02 | 486 | 0 | 188 | 298 | 0 | 0 | 66 |
| P03 | 275 | 0 | 0 | 263 | 12 | 0 | 57 |
| P04 | 4816 | 0 | 0 | 4155 | 661 | 0 | 46 |
| P05 | 428 | 16 | 28 | 371 | 13 | 0 | 51 |
| P06M | 30514 | 0 | 20 | 30449 | 45 | 0 | 46 |
| P06T | 55144 | 0 | 26 | 38046 | 17072 | 0 | 38 |
| P06 | 249 | 15 | 33 | 201 | 0 | 0 | 67 |
| P07 | 780 | 0 | 17 | 745 | 18 | 0 | 55 |
| P08 | 29302 | 0 | 0 | 26577 | 2725 | 0 | 46 |
| P09 | 278 | 5 | 10 | 262 | 1 | 0 | 53 |
| P10 | 2052 | 2 | 10 | 1390 | 650 | 0 | 41 |
| P11 | 1813 | 7 | 12 | 39 | 0 | 1755 | 23 |
| P12 | 10 | 0 | 0 | 10 | 0 | 0 | 54 |
| P13 | 202744 | 12 | 66 | 202653 | 13 | 0 | 38 |

### AP payability (confirmed channel + bill-to legal name and address + the buyer's reference rule + tax treatment known)

| package | rows | payable today | % | most common gap |
|---|---|---|---|---|
| P01M | 420 | 305 | 72.6% | tax treatment (83) |
| P01T | 206 | 124 | 60.2% | bill-to legal name and address (67) |
| P01_GOLD | 657 | 493 | 75.0% | bill-to legal name and address (97) |
| P02 | 486 | 329 | 67.7% | the buyer's PO / reference rule (84) |
| P03 | 275 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (275) |
| P04 | 4816 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (4816) |
| P05 | 428 | 45 | 10.5% | a confirmed invoicing / AP or finance channel (340) |
| P06M | 30514 | 335 | 1.1% | a confirmed invoicing / AP or finance channel (30089) |
| P06T | 55144 | 325 | 0.6% | a confirmed invoicing / AP or finance channel (54392) |
| P06 | 249 | 45 | 18.1% | the buyer's PO / reference rule (107) |
| P07 | 780 | 47 | 6.0% | the buyer's PO / reference rule (322) |
| P08 | 29302 | 0 | 0.0% | a confirmed invoicing / AP or finance channel (29302) |
| P09 | 278 | 39 | 14.0% | a confirmed invoicing / AP or finance channel (228) |
| P10 | 2052 | 5 | 0.2% | a confirmed invoicing / AP or finance channel (1978) |
| P11 | 1813 | 19 | 1.0% | a confirmed invoicing / AP or finance channel (1755) |
| P12 | 10 | 2 | 20.0% | a confirmed invoicing / AP or finance channel (8) |
| P13 | 202744 | 43 | 0.0% | a confirmed invoicing / AP or finance channel (200233) |

### Pay on sight (an invoice generated from the row would clear AP: confirmed invoicing / AP or finance channel, bill-to legal name + address, vendor legal name + GST/HST number + remit-to address, tax treatment and currency known — published or labelled-derived; the buyer's reference rule is reported separately)

| package | rows | pay on sight | % | + reference rule not published | routed (general inbox only) | most common gap |
|---|---|---|---|---|---|---|
| P01M | 420 | 9 | 2.1% | 7 | 0 | the vendor's GST/HST number (BN9) (397) |
| P01T | 206 | 81 | 39.3% | 2 | 0 | the vendor's GST/HST number (BN9) (77) |
| P01_GOLD | 657 | 412 | 62.7% | 11 | 0 | the vendor's GST/HST number (BN9) (168) |
| P02 | 486 | 213 | 43.8% | 22 | 0 | the vendor's GST/HST number (BN9) (222) |
| P03 | 275 | 18 | 6.5% | 0 | 133 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (106) |
| P04 | 4816 | 42 | 0.9% | 7 | 906 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3805) |
| P05 | 428 | 20 | 4.7% | 8 | 128 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (204) |
| P06M | 30514 | 9 | 0.0% | 14 | 723 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (29261) |
| P06T | 55144 | 360 | 0.7% | 15 | 18579 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (35732) |
| P06 | 249 | 19 | 7.6% | 46 | 0 | the vendor's GST/HST number (BN9) (117) |
| P07 | 780 | 16 | 2.1% | 136 | 36 | the vendor's GST/HST number (BN9) (385) |
| P08 | 29302 | 4 | 0.0% | 13 | 7262 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (21982) |
| P09 | 278 | 36 | 12.9% | 0 | 108 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (108) |
| P10 | 2052 | 5 | 0.2% | 14 | 286 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (1671) |
| P11 | 1813 | 7 | 0.4% | 3 | 0 | a confirmed invoicing / AP or finance channel (1739) |
| P12 | 10 | 1 | 10.0% | 0 | 5 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (3) |
| P13 | 202744 | 22 | 0.0% | 1197 | 80003 | an invoicing / AP or finance mailbox (only a purchasing / general inbo (120047) |
| **all** | 330174 | 1274 | 0.4% | 1495 | 108169 | |

### What still blocks grade A (rows per missing element; a row counts under every element it lacks)

| package | rows not A | referee confirmation of the mailbox | an invoicing / AP mailbox (not finance / procurement / general) | a mailbox on the buyer's own domain | MX record for the mailbox domain | published bill-to legal name | invoice / billing address | published PO rule | published payment terms | clear the penalty |
|---|---|---|---|---|---|---|---|---|---|---|
| P01M | 409 | 0 | 0 | 0 | 306 | 10 | 1 | 354 | 376 | 1 |
| P01T | 180 | 0 | 0 | 0 | 115 | 61 | 28 | 150 | 163 | 2 |
| P01_GOLD | 401 | 0 | 0 | 0 | 39 | 78 | 31 | 224 | 262 | 3 |
| P02 | 486 | 0 | 486 | 0 | 60 | 57 | 14 | 378 | 305 | 2 |
| P03 | 275 | 0 | 275 | 0 | 28 | 46 | 25 | 142 | 152 | 2 |
| P04 | 4816 | 0 | 4816 | 0 | 2670 | 1490 | 1001 | 4617 | 4367 | 31 |
| P05 | 412 | 0 | 360 | 0 | 87 | 100 | 40 | 344 | 359 | 7 |
| P06M | 30514 | 0 | 30514 | 0 | 24086 | 1755 | 137 | 30129 | 29869 | 19 |
| P06T | 55144 | 0 | 55144 | 0 | 49605 | 34363 | 22058 | 54825 | 54359 | 384 |
| P06 | 234 | 0 | 0 | 0 | 128 | 69 | 41 | 182 | 206 | 4 |
| P07 | 780 | 0 | 780 | 0 | 530 | 304 | 97 | 745 | 742 | 5 |
| P08 | 29302 | 0 | 29302 | 0 | 23187 | 12666 | 4167 | 29054 | 28700 | 187 |
| P09 | 273 | 0 | 254 | 0 | 12 | 69 | 1 | 248 | 260 | 7 |
| P10 | 2050 | 0 | 2020 | 0 | 1059 | 1109 | 945 | 1989 | 1952 | 17 |
| P11 | 1806 | 1755 | 1710 | 0 | 929 | 1224 | 537 | 1748 | 1742 | 21 |
| P12 | 10 | 0 | 9 | 0 | 0 | 2 | 0 | 10 | 10 | 1 |
| P13 | 202732 | 0 | 202267 | 0 | 172304 | 123262 | 19 | 202383 | 201466 | 70 |

## Where the work is (largest gaps in rows still needed)

| field | package | now | target | rows needed |
|---|---|---|---|---|
| buyer_phone | P13 | 56.8% | 95% | 77529 |
| buyer_logo_url | P13 | 72.4% | 95% | 45881 |
| buyer_legal_name_as_published | P13 | 39.2% | 60% | 42165 |
| buyer_ap_cycle_published | P13 | 0.0% | 20% | 40492 |
| ap_system_hint | P13 | 0.3% | 20% | 39918 |
| buyer_bn_as_published | P13 | 10.4% | 30% | 39805 |
| buyer_esignature_preference | P13 | 0.1% | 15% | 30245 |
| buyer_tax_exempt_status | P13 | 0.1% | 15% | 30204 |
| buyer_payment_method_preference | P13 | 0.6% | 15% | 29257 |
| vendor_registered_address | P08 | 31.8% | 70% | 11186 |
| buyer_ap_cycle_published | P06T | 0.0% | 20% | 11014 |
| ap_system_hint | P06T | 0.6% | 20% | 10700 |
| buyer_esignature_preference | P06T | 0.2% | 15% | 8179 |
| buyer_tax_exempt_status | P06T | 0.2% | 15% | 8168 |
| buyer_payment_method_preference | P06T | 0.7% | 15% | 7907 |
| buyer_phone | P08 | 70.9% | 95% | 7059 |
| buyer_ap_cycle_published | P06M | 0.0% | 20% | 6089 |
| buyer_ap_cycle_published | P08 | 0.0% | 20% | 5849 |
| ap_system_hint | P06M | 0.9% | 20% | 5827 |
| ap_system_hint | P08 | 0.8% | 20% | 5641 |
| vendor_emails | P08 | 55.9% | 75% | 5609 |
| buyer_legal_name_as_published | P08 | 56.8% | 75% | 5341 |
| vendor_bn9 | P08 | 32.3% | 50% | 5188 |
| vendor_phone | P08 | 67.7% | 85% | 5077 |
| vendor_trading_name | P08 | 33.9% | 50% | 4708 |
| buyer_esignature_preference | P06M | 0.3% | 15% | 4480 |
| buyer_tax_exempt_status | P06M | 0.5% | 15% | 4417 |
| buyer_payment_method_preference | P06M | 0.7% | 15% | 4352 |
| buyer_esignature_preference | P08 | 0.3% | 15% | 4301 |
| buyer_tax_exempt_status | P08 | 0.3% | 15% | 4296 |
| buyer_payment_method_preference | P08 | 0.6% | 15% | 4218 |
| invoice_reference_hint | P08 | 12.2% | 25% | 3761 |
| buyer_bn_as_published | P08 | 22.5% | 35% | 3651 |
| average_contract_duration_days | P04 | 14.7% | 90% | 3628 |
| currency | P04 | 21.0% | 95% | 3563 |
| ap_phone | P04 | 15.9% | 85% | 3328 |
| commodity_codes | P04 | 16.5% | 85% | 3298 |
| award_or_notice_id | P04 | 18.5% | 85% | 3203 |
| contract_value | P04 | 20.7% | 85% | 3098 |
| invoice_mailing_address | P04 | 15.9% | 75% | 2846 |

## 1. identifiers

### `invoice_reference_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 94.5% | 94.5% | +1.3 | 50% | ✅ met |
| P01T | 206 | 95.1% | 95.1% | -0.5 | 50% | ✅ met |
| P01_GOLD | 657 | 92.2% | 94.5% | +0.0 | 95% | 🟡 3 pts to go |
| P02 | 486 | 75.7% | 77.2% | +0.7 | 95% | ❌ 19 pts to go |
| P03 | 275 | 82.5% | 85.8% | +0.9 | 95% | ❌ 12 pts to go |
| P04 | 4816 | 43.6% | 45.0% | +11.8 | 90% | ❌ 46 pts to go |
| P05 | 428 | 40.2% | 43.2% | +0.6 | 70% | ❌ 30 pts to go |
| P06M | 30514 | 93.9% | 93.9% | +0.7 | n/a | no target |
| P06T | 55144 | 99.5% | 99.5% | +0.2 | n/a | no target |
| P06 | 249 | 33.3% | 33.3% | -2.1 | 30% | ✅ met |
| P07 | 780 | 13.5% | 13.5% | -0.7 | 30% | ❌ 16 pts to go |
| P08 | 29302 | 12.2% | 12.2% | +0.0 | 25% | ❌ 13 pts to go |
| P09 | 278 | 98.9% | 99.6% | +0.0 | 100% | 🟡 1 pts to go |
| P10 | 2052 | 3.1% | 3.1% | -0.2 | 25% | ❌ 22 pts to go |
| P11 | 1813 | 54.9% | 55.7% | +0.6 | 60% | 🟡 5 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 202744 | 99.6% | 99.6% | +0.0 | 0% by design | — leave (by design) |

### `po_number_as_published`

> ceiling: a purchase-order number exists only where the buyer publishes PO-level data (Montréal, Laval, Toronto open data so far) or the record itself carries one; most sources publish awards, not POs — the target cannot be reached from public data for most buyers

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 206 | 0.0% | 0.0% | +0.0 | 10% | 🟡 10 pts to go |
| P01_GOLD | 657 | 5.6% | 5.6% | -0.1 | 50% | ❌ 44 pts to go |
| P02 | 486 | 5.3% | 5.3% | -0.9 | 50% | ❌ 45 pts to go |
| P03 | 275 | 1.8% | 1.8% | -0.1 | 40% | ❌ 38 pts to go |
| P04 | 4816 | 0.5% | 0.5% | -0.1 | 30% | ❌ 30 pts to go |
| P05 | 428 | 0.2% | 0.2% | +0.0 | 20% | ❌ 20 pts to go |
| P06M | 30514 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55144 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 249 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 780 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29302 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 0.7% | 0.7% | +0.0 | 50% | ❌ 49 pts to go |
| P10 | 2052 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1813 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 202744 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_or_agreement_number`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 92.4% | 92.4% | +2.8 | n/a | no target |
| P01T | 206 | 77.7% | 77.7% | -2.2 | 50% | ✅ met |
| P01_GOLD | 657 | 68.3% | 68.3% | +1.0 | 85% | ❌ 17 pts to go |
| P02 | 486 | 67.5% | 67.5% | +1.3 | 90% | ❌ 22 pts to go |
| P03 | 275 | 62.5% | 62.5% | +2.0 | 85% | ❌ 22 pts to go |
| P04 | 4816 | 41.6% | 41.6% | +12.5 | 85% | ❌ 43 pts to go |
| P05 | 428 | 30.8% | 30.8% | +0.9 | 60% | ❌ 29 pts to go |
| P06M | 30514 | 93.7% | 93.7% | +0.7 | n/a | no target |
| P06T | 55144 | 99.4% | 99.4% | +0.2 | n/a | no target |
| P06 | 249 | 6.8% | 6.8% | +0.4 | n/a | no target |
| P07 | 780 | 9.0% | 9.0% | -0.1 | n/a | no target |
| P08 | 29302 | 11.3% | 11.3% | +0.0 | n/a | no target |
| P09 | 278 | 95.7% | 95.7% | +0.1 | 100% | 🟡 4 pts to go |
| P10 | 2052 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1813 | 52.2% | 52.2% | +0.7 | 60% | 🟡 8 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 202744 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `solicitation_or_tender_number`

> ceiling: SEAO's 'numero' is the organisation's own reference for the notice (SEAO data dictionary) and is reported here; sources that publish awards under a tender number only (bids&tenders, SaskTenders, BC) also carry it as the contract reference, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 206 | 0.0% | 0.0% | +0.0 | 30% | ❌ 30 pts to go |
| P01_GOLD | 657 | 49.3% | 49.3% | -2.4 | 80% | ❌ 31 pts to go |
| P02 | 486 | 55.6% | 55.6% | -2.5 | 60% | 🟡 4 pts to go |
| P03 | 275 | 48.4% | 48.4% | -2.0 | 80% | ❌ 32 pts to go |
| P04 | 4816 | 17.8% | 17.8% | -6.2 | 50% | ❌ 32 pts to go |
| P05 | 428 | 13.6% | 13.6% | +1.0 | 40% | ❌ 26 pts to go |
| P06M | 30514 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55144 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 249 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 780 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29302 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 81.3% | 81.3% | +0.2 | 50% | ✅ met |
| P10 | 2052 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1813 | 3.3% | 3.3% | +0.0 | 40% | ❌ 37 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 202744 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `award_or_notice_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 206 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 657 | 58.4% | 58.4% | -2.5 | 85% | ❌ 27 pts to go |
| P02 | 486 | 55.8% | 55.8% | -2.3 | 90% | ❌ 34 pts to go |
| P03 | 275 | 56.7% | 56.7% | -2.7 | 85% | ❌ 28 pts to go |
| P04 | 4816 | 18.5% | 18.5% | -6.4 | 85% | ❌ 66 pts to go |
| P05 | 428 | 21.3% | 21.3% | +0.9 | 50% | ❌ 29 pts to go |
| P06M | 30514 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55144 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 249 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 780 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29302 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 97.1% | 97.1% | +0.0 | 100% | 🟡 3 pts to go |
| P10 | 2052 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1813 | 3.7% | 3.7% | +0.1 | 60% | ❌ 56 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 202744 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_vendor_id`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 206 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 657 | 12.5% | 12.5% | -0.1 | 60% | ❌ 48 pts to go |
| P02 | 486 | 6.6% | 6.6% | -0.7 | 50% | ❌ 43 pts to go |
| P03 | 275 | 8.4% | 8.4% | -0.2 | 50% | ❌ 42 pts to go |
| P04 | 4816 | 1.4% | 1.4% | -0.5 | 40% | ❌ 39 pts to go |
| P05 | 428 | 0.7% | 0.7% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 30514 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55144 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 249 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 780 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29302 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 3.2% | 3.2% | -0.4 | 50% | ❌ 47 pts to go |
| P10 | 2052 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1813 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 202744 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `commodity_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 206 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 657 | 34.4% | 34.4% | -1.5 | 80% | ❌ 46 pts to go |
| P02 | 486 | 50.2% | 50.2% | -2.8 | 90% | ❌ 40 pts to go |
| P03 | 275 | 32.7% | 32.7% | -1.1 | 80% | ❌ 47 pts to go |
| P04 | 4816 | 16.5% | 16.5% | -5.7 | 85% | ❌ 68 pts to go |
| P05 | 428 | 7.5% | 7.5% | +1.1 | 50% | ❌ 42 pts to go |
| P06M | 30514 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55144 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 249 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 780 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29302 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 73.7% | 73.7% | +0.6 | 95% | ❌ 21 pts to go |
| P10 | 2052 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1813 | 2.7% | 2.7% | +0.1 | 50% | ❌ 47 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 202744 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `buyer_org_codes`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 206 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 657 | 7.9% | 7.9% | -0.2 | 50% | ❌ 42 pts to go |
| P02 | 486 | 5.3% | 5.3% | -0.9 | 50% | ❌ 45 pts to go |
| P03 | 275 | 2.5% | 2.5% | -0.1 | 30% | ❌ 28 pts to go |
| P04 | 4816 | 0.4% | 0.4% | -0.2 | 30% | ❌ 30 pts to go |
| P05 | 428 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06M | 30514 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55144 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 249 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 780 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29302 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P10 | 2052 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1813 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 202744 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `records_with_this_vendor`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 206 | 100.0% | 100.0% | +0.0 | 60% | ✅ met |
| P01_GOLD | 657 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 486 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 275 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4816 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |
| P05 | 428 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P06M | 30514 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 55144 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 249 | 100.0% | 100.0% | +0.0 | 50% | ✅ met |
| P07 | 780 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 29302 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 278 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2052 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1813 | 100.0% | 100.0% | +0.0 | 70% | ✅ met |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 202744 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 2. vendor

### `vendor_bn9`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 5.2% | 5.2% | -1.2 | 70% | ❌ 65 pts to go |
| P01T | 206 | 54.9% | 54.9% | -5.4 | 60% | 🟡 5 pts to go |
| P01_GOLD | 657 | 72.1% | 72.1% | -2.7 | 90% | ❌ 18 pts to go |
| P02 | 486 | 51.9% | 51.9% | -2.4 | 85% | ❌ 33 pts to go |
| P03 | 275 | 63.6% | 63.6% | -3.3 | 90% | ❌ 26 pts to go |
| P04 | 4816 | 28.2% | 28.2% | -10.0 | 75% | ❌ 47 pts to go |
| P05 | 428 | 54.7% | 54.7% | +0.0 | 50% | ✅ met |
| P06M | 30514 | 2.9% | 2.9% | +0.0 | n/a | no target |
| P06T | 55144 | 65.1% | 65.1% | +0.6 | n/a | no target |
| P06 | 249 | 41.8% | 41.8% | -0.3 | 40% | ✅ met |
| P07 | 780 | 32.7% | 32.7% | +0.6 | 50% | ❌ 17 pts to go |
| P08 | 29302 | 32.3% | 32.3% | +1.7 | 50% | ❌ 18 pts to go |
| P09 | 278 | 56.5% | 56.5% | -0.2 | 80% | ❌ 24 pts to go |
| P10 | 2052 | 38.7% | 38.7% | -0.1 | 40% | 🟡 1 pts to go |
| P11 | 1813 | 53.7% | 53.7% | -0.9 | 60% | 🟡 6 pts to go |
| P12 | 10 | 60.0% | 60.0% | +14.5 | 85% | ❌ 25 pts to go |
| P13 | 202744 | 44.7% | 44.7% | -0.1 | 0% by design | — leave (by design) |

### `vendor_registered_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 41.9% | 41.9% | -4.7 | n/a | no target |
| P01T | 206 | 55.3% | 55.3% | -4.5 | n/a | no target |
| P01_GOLD | 657 | 73.8% | 73.8% | +0.9 | 95% | ❌ 21 pts to go |
| P02 | 486 | 75.3% | 75.3% | +0.7 | 95% | ❌ 20 pts to go |
| P03 | 275 | 70.5% | 70.5% | +1.0 | 95% | ❌ 24 pts to go |
| P04 | 4816 | 54.2% | 54.2% | +1.1 | 95% | ❌ 41 pts to go |
| P05 | 428 | 58.6% | 58.6% | +0.5 | 70% | ❌ 11 pts to go |
| P06M | 30514 | 38.9% | 38.9% | -2.4 | n/a | no target |
| P06T | 55144 | 68.6% | 68.6% | +1.1 | n/a | no target |
| P06 | 249 | 38.2% | 38.2% | +0.0 | 80% | ❌ 42 pts to go |
| P07 | 780 | 31.7% | 31.7% | +0.7 | 70% | ❌ 38 pts to go |
| P08 | 29302 | 31.8% | 31.8% | +2.1 | 70% | ❌ 38 pts to go |
| P09 | 278 | 86.7% | 86.7% | +0.5 | 100% | ❌ 13 pts to go |
| P10 | 2052 | 39.2% | 39.2% | +0.0 | 70% | ❌ 31 pts to go |
| P11 | 1813 | 58.6% | 58.6% | +0.0 | 75% | ❌ 16 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 202744 | 40.4% | 40.4% | +0.2 | n/a | no target |

### `vendor_trading_name`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 22.4% | 22.4% | +0.3 | n/a | no target |
| P01T | 206 | 58.7% | 58.7% | -6.8 | n/a | no target |
| P01_GOLD | 657 | 50.7% | 50.7% | +1.9 | 60% | 🟡 9 pts to go |
| P02 | 486 | 58.4% | 58.4% | +2.6 | 60% | 🟡 2 pts to go |
| P03 | 275 | 54.5% | 54.5% | +2.2 | 60% | 🟡 6 pts to go |
| P04 | 4816 | 54.2% | 54.2% | +11.6 | 55% | 🟡 1 pts to go |
| P05 | 428 | 23.6% | 23.6% | +0.9 | 50% | ❌ 26 pts to go |
| P06M | 30514 | 11.2% | 11.2% | +1.7 | n/a | no target |
| P06T | 55144 | 70.2% | 70.2% | +2.3 | n/a | no target |
| P06 | 249 | 50.6% | 50.6% | +2.0 | n/a | no target |
| P07 | 780 | 39.5% | 39.5% | -0.1 | 55% | ❌ 16 pts to go |
| P08 | 29302 | 33.9% | 33.9% | +0.9 | 50% | ❌ 16 pts to go |
| P09 | 278 | 72.7% | 72.7% | +0.7 | 70% | ✅ met |
| P10 | 2052 | 47.7% | 47.7% | -0.4 | 55% | 🟡 7 pts to go |
| P11 | 1813 | 59.5% | 59.5% | +0.3 | 50% | ✅ met |
| P12 | 10 | 90.0% | 90.0% | -0.9 | n/a | no target |
| P13 | 202744 | 3.0% | 3.0% | -0.2 | n/a | no target |

### `vendor_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 24.3% | 24.3% | -9.0 | n/a | no target |
| P01T | 206 | 76.7% | 76.7% | -2.8 | n/a | no target |
| P01_GOLD | 657 | 48.1% | 48.1% | -2.3 | 70% | ❌ 22 pts to go |
| P02 | 486 | 54.9% | 54.9% | -1.9 | 70% | ❌ 15 pts to go |
| P03 | 275 | 48.4% | 48.4% | -2.0 | 70% | ❌ 22 pts to go |
| P04 | 4816 | 49.5% | 49.5% | -5.4 | 65% | ❌ 16 pts to go |
| P05 | 428 | 29.7% | 29.7% | +0.6 | 60% | ❌ 30 pts to go |
| P06M | 30514 | 23.6% | 23.6% | -3.8 | n/a | no target |
| P06T | 55144 | 87.0% | 87.0% | +4.3 | n/a | no target |
| P06 | 249 | 70.7% | 70.7% | +1.4 | 40% | ✅ met |
| P07 | 780 | 66.9% | 66.9% | +1.9 | 85% | ❌ 18 pts to go |
| P08 | 29302 | 67.7% | 67.7% | +3.7 | 85% | ❌ 17 pts to go |
| P09 | 278 | 56.5% | 56.5% | +0.1 | 85% | ❌ 28 pts to go |
| P10 | 2052 | 65.2% | 65.2% | -0.9 | 85% | ❌ 20 pts to go |
| P11 | 1813 | 68.7% | 68.7% | +0.6 | 75% | 🟡 6 pts to go |
| P12 | 10 | 40.0% | 40.0% | +3.6 | n/a | no target |
| P13 | 202744 | 90.9% | 90.9% | -0.9 | 60% | ✅ met |

### `vendor_website`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 29.0% | 29.0% | -8.8 | n/a | no target |
| P01T | 206 | 98.1% | 98.1% | -0.2 | n/a | no target |
| P01_GOLD | 657 | 75.3% | 75.3% | -3.3 | 90% | ❌ 15 pts to go |
| P02 | 486 | 78.6% | 78.6% | -3.2 | 90% | ❌ 11 pts to go |
| P03 | 275 | 81.5% | 81.5% | -3.8 | 90% | 🟡 8 pts to go |
| P04 | 4816 | 71.0% | 71.0% | -11.8 | 85% | ❌ 14 pts to go |
| P05 | 428 | 44.9% | 44.9% | +0.4 | 70% | ❌ 25 pts to go |
| P06M | 30514 | 29.5% | 29.5% | -3.5 | n/a | no target |
| P06T | 55144 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P06 | 249 | 99.2% | 99.2% | -0.1 | 50% | ✅ met |
| P07 | 780 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P08 | 29302 | 99.9% | 99.9% | +0.0 | 100% | 🟡 0 pts to go |
| P09 | 278 | 78.1% | 78.1% | +0.3 | 100% | ❌ 22 pts to go |
| P10 | 2052 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1813 | 97.5% | 97.5% | -0.5 | 100% | 🟡 2 pts to go |
| P12 | 10 | 60.0% | 60.0% | +5.5 | n/a | no target |
| P13 | 202744 | 100.0% | 100.0% | +0.0 | n/a | no target |

### `vendor_emails`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 13.8% | 13.8% | -2.3 | n/a | no target |
| P01T | 206 | 53.9% | 53.9% | -5.9 | n/a | no target |
| P01_GOLD | 657 | 41.2% | 41.2% | -2.2 | 70% | ❌ 29 pts to go |
| P02 | 486 | 45.7% | 45.7% | -1.5 | 75% | ❌ 29 pts to go |
| P03 | 275 | 43.6% | 43.6% | -1.1 | 75% | ❌ 31 pts to go |
| P04 | 4816 | 35.3% | 35.3% | -3.4 | 70% | ❌ 35 pts to go |
| P05 | 428 | 22.0% | 22.0% | +0.7 | 55% | ❌ 33 pts to go |
| P06M | 30514 | 6.7% | 6.7% | +0.8 | n/a | no target |
| P06T | 55144 | 42.0% | 42.0% | -5.4 | n/a | no target |
| P06 | 249 | 51.8% | 51.8% | +0.7 | n/a | no target |
| P07 | 780 | 53.8% | 53.8% | +1.1 | 70% | ❌ 16 pts to go |
| P08 | 29302 | 55.9% | 55.9% | +1.1 | 75% | ❌ 19 pts to go |
| P09 | 278 | 47.5% | 47.5% | +0.6 | 85% | ❌ 38 pts to go |
| P10 | 2052 | 44.4% | 44.4% | +0.0 | 80% | ❌ 36 pts to go |
| P11 | 1813 | 51.7% | 51.7% | -1.6 | 70% | ❌ 18 pts to go |
| P12 | 10 | 30.0% | 30.0% | +2.7 | n/a | no target |
| P13 | 202744 | 5.9% | 5.9% | +0.4 | n/a | no target |

### `vendor_logo_url`

> ceiling: needs the vendor's website first; sites that block automated readers (robots.txt / 403) are never read

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 27.6% | 27.6% | -10.2 | n/a | no target |
| P01T | 206 | 96.1% | 96.1% | -0.4 | n/a | no target |
| P01_GOLD | 657 | 69.9% | 69.9% | -3.0 | 90% | ❌ 20 pts to go |
| P02 | 486 | 73.5% | 73.5% | -3.2 | 90% | ❌ 16 pts to go |
| P03 | 275 | 78.2% | 78.2% | -3.8 | 90% | ❌ 12 pts to go |
| P04 | 4816 | 66.8% | 66.8% | -10.9 | 85% | ❌ 18 pts to go |
| P05 | 428 | 43.5% | 43.5% | +0.6 | 75% | ❌ 32 pts to go |
| P06M | 30514 | 28.6% | 28.6% | -4.3 | n/a | no target |
| P06T | 55144 | 97.8% | 97.8% | -0.5 | n/a | no target |
| P06 | 249 | 92.0% | 92.0% | +2.0 | n/a | no target |
| P07 | 780 | 94.4% | 94.4% | +2.7 | 100% | 🟡 6 pts to go |
| P08 | 29302 | 92.8% | 92.8% | +5.5 | 100% | 🟡 7 pts to go |
| P09 | 278 | 66.5% | 66.5% | +0.0 | n/a | no target |
| P10 | 2052 | 90.0% | 90.0% | -0.3 | 100% | 🟡 10 pts to go |
| P11 | 1813 | 90.2% | 90.2% | +0.0 | n/a | no target |
| P12 | 10 | 60.0% | 60.0% | +5.5 | n/a | no target |
| P13 | 202744 | 69.5% | 69.5% | -0.3 | n/a | no target |

### `vendor_neq`

> ceiling: only Québec-registered vendors have an NEQ; the share of QC vendors is reported next to the rate

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 32.1% | 32.1% | -4.8 | n/a | no target · QC vendors: 55 rows, 100.0% filled |
| P01T | 206 | 22.3% | 22.3% | +2.6 | n/a | no target · QC vendors: 34 rows, 88.2% filled |
| P01_GOLD | 657 | 45.1% | 45.1% | +1.6 | 95% | ❌ 50 pts to go · QC vendors: 48 rows, 97.9% filled |
| P02 | 486 | 58.0% | 58.0% | +2.0 | 95% | ❌ 37 pts to go · QC vendors: 111 rows, 100.0% filled |
| P03 | 275 | 44.7% | 44.7% | +1.8 | 95% | ❌ 50 pts to go · QC vendors: 18 rows, 100.0% filled |
| P04 | 4816 | 39.1% | 39.1% | +6.7 | 95% | ❌ 56 pts to go · QC vendors: 594 rows, 97.8% filled |
| P05 | 428 | 14.7% | 14.7% | +0.7 | n/a | no target · QC vendors: 38 rows, 100.0% filled |
| P06M | 30514 | 34.6% | 34.6% | -2.9 | n/a | no target · QC vendors: 7651 rows, 99.9% filled |
| P06T | 55144 | 38.1% | 38.1% | +7.5 | n/a | no target · QC vendors: 21402 rows, 96.2% filled |
| P06 | 249 | 7.2% | 7.2% | +0.1 | n/a | no target · QC vendors: 11 rows, 63.6% filled |
| P07 | 780 | 6.8% | 6.8% | -0.1 | n/a | no target · QC vendors: 44 rows, 79.5% filled |
| P08 | 29302 | 7.1% | 7.1% | +0.1 | n/a | no target · QC vendors: 1779 rows, 92.8% filled |
| P09 | 278 | 74.1% | 74.1% | +0.6 | 95% | ❌ 21 pts to go · QC vendors: 102 rows, 100.0% filled |
| P10 | 2052 | 15.9% | 15.9% | +0.2 | n/a | no target · QC vendors: 201 rows, 92.5% filled |
| P11 | 1813 | 20.7% | 20.7% | +1.1 | n/a | no target · QC vendors: 323 rows, 94.1% filled |
| P12 | 10 | 80.0% | 80.0% | -1.8 | n/a | no target · QC vendors: 2 rows, 100.0% filled |
| P13 | 202744 | 21.9% | 21.9% | -0.3 | n/a | no target · QC vendors: 44462 rows, 100.0% filled |

### `vendor_years_in_business`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 41.7% | 41.7% | -4.5 | n/a | no target · vendors with a registry record: 175 rows, 100.0% filled |
| P01T | 206 | 55.3% | 55.3% | -4.5 | n/a | no target · vendors with a registry record: 114 rows, 100.0% filled |
| P01_GOLD | 657 | 81.6% | 81.6% | +0.7 | 100% | ❌ 18 pts to go · vendors with a registry record: 536 rows, 100.0% filled |
| P02 | 486 | 78.8% | 78.8% | +0.4 | 100% | ❌ 21 pts to go · vendors with a registry record: 383 rows, 100.0% filled |
| P03 | 275 | 78.9% | 78.9% | +0.7 | 100% | ❌ 21 pts to go · vendors with a registry record: 217 rows, 100.0% filled |
| P04 | 4816 | 54.8% | 54.8% | +0.8 | 100% | ❌ 45 pts to go · vendors with a registry record: 2638 rows, 100.0% filled |
| P05 | 428 | 63.1% | 63.1% | +0.3 | n/a | no target · vendors with a registry record: 270 rows, 100.0% filled |
| P06M | 30514 | 38.9% | 38.9% | -2.3 | n/a | no target · vendors with a registry record: 11871 rows, 100.0% filled |
| P06T | 55144 | 68.6% | 68.6% | +1.0 | n/a | no target · vendors with a registry record: 37854 rows, 100.0% filled |
| P06 | 249 | 39.0% | 39.0% | -0.3 | n/a | no target · vendors with a registry record: 97 rows, 100.0% filled |
| P07 | 780 | 32.3% | 32.3% | +0.5 | n/a | no target · vendors with a registry record: 252 rows, 100.0% filled |
| P08 | 29302 | 31.9% | 31.9% | +1.9 | n/a | no target · vendors with a registry record: 9340 rows, 100.0% filled |
| P09 | 278 | 89.9% | 89.9% | +0.4 | n/a | no target · vendors with a registry record: 250 rows, 100.0% filled |
| P10 | 2052 | 40.1% | 40.1% | +0.0 | n/a | no target · vendors with a registry record: 823 rows, 100.0% filled |
| P11 | 1813 | 59.3% | 59.3% | +0.0 | n/a | no target · vendors with a registry record: 1076 rows, 100.0% filled |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target · vendors with a registry record: 10 rows, 100.0% filled |
| P13 | 202744 | 40.4% | 40.4% | +0.2 | n/a | no target · vendors with a registry record: 81956 rows, 100.0% filled |

## 3. buyer

### `buyer_legal_name_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 97.6% | 97.6% | +1.2 | 90% | ✅ met |
| P01T | 206 | 70.4% | 70.4% | -0.3 | 90% | ❌ 20 pts to go |
| P01_GOLD | 657 | 88.1% | 88.1% | +0.7 | 95% | 🟡 7 pts to go |
| P02 | 486 | 88.3% | 88.3% | +0.1 | 95% | 🟡 7 pts to go |
| P03 | 275 | 83.3% | 83.3% | +0.2 | 85% | 🟡 2 pts to go |
| P04 | 4816 | 69.1% | 69.1% | +4.6 | 90% | ❌ 21 pts to go |
| P05 | 428 | 76.6% | 76.6% | -1.4 | 75% | ✅ met |
| P06M | 30514 | 94.2% | 94.3% | +0.4 | n/a | no target |
| P06T | 55144 | 37.7% | 37.7% | +0.8 | n/a | no target |
| P06 | 249 | 72.3% | 72.3% | +1.2 | 80% | 🟡 8 pts to go |
| P07 | 780 | 61.0% | 61.2% | +2.8 | 80% | ❌ 19 pts to go |
| P08 | 29302 | 56.8% | 56.8% | +4.9 | 75% | ❌ 18 pts to go |
| P09 | 278 | 75.2% | 75.2% | -0.4 | 95% | ❌ 20 pts to go |
| P10 | 2052 | 46.0% | 46.0% | -0.8 | 70% | ❌ 24 pts to go |
| P11 | 1813 | 32.5% | 32.5% | +0.7 | 65% | ❌ 32 pts to go |
| P12 | 10 | 80.0% | 80.0% | +7.3 | 80% | ✅ met |
| P13 | 202744 | 39.2% | 39.2% | -6.4 | 60% | ❌ 21 pts to go |

### `buyer_bn_as_published`

> ceiling: a buyer's BN is public only where the buyer prints it or a public dataset carries it (CRA charities, federal grants & contributions recipients, business registries for corporations); municipalities rarely publish theirs

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 13.8% | 13.8% | -4.7 | 50% | ❌ 36 pts to go |
| P01T | 206 | 16.5% | 16.5% | +0.3 | n/a | no target |
| P01_GOLD | 657 | 18.9% | 18.9% | -0.9 | 40% | ❌ 21 pts to go |
| P02 | 486 | 19.3% | 19.3% | -0.6 | 40% | ❌ 21 pts to go |
| P03 | 275 | 19.6% | 19.6% | -0.7 | 40% | ❌ 20 pts to go |
| P04 | 4816 | 14.0% | 14.0% | -2.3 | 40% | ❌ 26 pts to go |
| P05 | 428 | 21.0% | 21.0% | +0.1 | 25% | 🟡 4 pts to go |
| P06M | 30514 | 19.1% | 19.1% | -1.3 | n/a | no target |
| P06T | 55144 | 9.9% | 9.9% | +2.4 | n/a | no target |
| P06 | 249 | 20.5% | 20.5% | +3.0 | 35% | ❌ 14 pts to go |
| P07 | 780 | 22.8% | 22.8% | +3.7 | 35% | ❌ 12 pts to go |
| P08 | 29302 | 22.5% | 22.5% | +4.8 | 35% | ❌ 12 pts to go |
| P09 | 278 | 16.5% | 16.5% | -0.2 | n/a | no target |
| P10 | 2052 | 9.2% | 9.2% | +2.1 | 30% | ❌ 21 pts to go |
| P11 | 1813 | 9.5% | 9.5% | +3.0 | n/a | no target |
| P12 | 10 | 20.0% | 20.0% | +1.8 | n/a | no target |
| P13 | 202744 | 10.4% | 10.4% | -2.1 | 30% | ❌ 20 pts to go |

### `buyer_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 99.8% | 99.8% | -0.2 | 100% | 🟡 0 pts to go |
| P01T | 206 | 85.0% | 85.0% | -0.2 | 100% | ❌ 15 pts to go |
| P01_GOLD | 657 | 91.5% | 91.5% | +0.4 | 100% | 🟡 8 pts to go |
| P02 | 486 | 96.7% | 96.7% | +0.1 | 100% | 🟡 3 pts to go |
| P03 | 275 | 89.8% | 89.8% | +0.3 | 100% | ❌ 10 pts to go |
| P04 | 4816 | 78.8% | 78.8% | +6.3 | 100% | ❌ 21 pts to go |
| P05 | 428 | 90.0% | 90.0% | +0.0 | 100% | 🟡 10 pts to go |
| P06M | 30514 | 99.6% | 99.6% | +0.2 | n/a | no target |
| P06T | 55144 | 60.0% | 60.0% | +1.3 | n/a | no target |
| P06 | 249 | 81.9% | 81.9% | -0.2 | 95% | ❌ 13 pts to go |
| P07 | 780 | 87.3% | 87.3% | +1.9 | 95% | 🟡 8 pts to go |
| P08 | 29302 | 85.8% | 85.8% | +1.3 | 95% | 🟡 9 pts to go |
| P09 | 278 | 96.4% | 96.4% | +0.0 | 100% | 🟡 4 pts to go |
| P10 | 2052 | 53.8% | 53.9% | -0.8 | 95% | ❌ 41 pts to go |
| P11 | 1813 | 61.9% | 61.9% | +1.0 | 80% | ❌ 18 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 202744 | 100.0% | 100.0% | +0.0 | 95% | ✅ met |

### `buyer_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 65.7% | 65.7% | -5.4 | n/a | no target |
| P01T | 206 | 71.8% | 71.8% | -2.4 | n/a | no target |
| P01_GOLD | 657 | 73.2% | 73.2% | +0.0 | 90% | ❌ 17 pts to go |
| P02 | 486 | 77.4% | 77.4% | -1.0 | 95% | ❌ 18 pts to go |
| P03 | 275 | 74.2% | 74.2% | +0.1 | 95% | ❌ 21 pts to go |
| P04 | 4816 | 69.6% | 69.6% | +0.1 | 95% | ❌ 25 pts to go |
| P05 | 428 | 71.5% | 71.5% | -1.0 | 90% | ❌ 18 pts to go |
| P06M | 30514 | 70.5% | 70.6% | -6.2 | n/a | no target |
| P06T | 55144 | 58.3% | 58.3% | -0.3 | n/a | no target |
| P06 | 249 | 70.7% | 70.7% | +5.3 | 95% | ❌ 24 pts to go |
| P07 | 780 | 67.7% | 67.7% | +8.0 | 90% | ❌ 22 pts to go |
| P08 | 29302 | 70.9% | 70.9% | +12.3 | 95% | ❌ 24 pts to go |
| P09 | 278 | 86.0% | 86.0% | +0.2 | 100% | ❌ 14 pts to go |
| P10 | 2052 | 53.2% | 53.2% | -0.6 | 95% | ❌ 42 pts to go |
| P11 | 1813 | 32.9% | 32.9% | +2.2 | 75% | ❌ 42 pts to go |
| P12 | 10 | 80.0% | 80.0% | -1.8 | n/a | no target |
| P13 | 202744 | 56.8% | 56.8% | -11.1 | 95% | ❌ 38 pts to go |

### `buyer_logo_url`

> ceiling: sites that block automated readers (robots.txt / 403) are never read; an og:image that looks like a photo is labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 77.6% | 77.6% | -5.9 | n/a | no target |
| P01T | 206 | 90.3% | 90.3% | -1.4 | 95% | 🟡 5 pts to go |
| P01_GOLD | 657 | 85.2% | 85.2% | +0.2 | 90% | 🟡 5 pts to go |
| P02 | 486 | 90.3% | 90.3% | -0.7 | 95% | 🟡 5 pts to go |
| P03 | 275 | 84.4% | 84.4% | +0.6 | 95% | ❌ 11 pts to go |
| P04 | 4816 | 90.4% | 90.4% | -1.2 | 90% | ✅ met |
| P05 | 428 | 92.5% | 92.5% | +0.1 | 95% | 🟡 2 pts to go |
| P06M | 30514 | 82.0% | 82.0% | -3.3 | n/a | no target |
| P06T | 55144 | 87.2% | 87.2% | +2.6 | n/a | no target |
| P06 | 249 | 92.8% | 92.8% | +7.4 | 100% | 🟡 7 pts to go |
| P07 | 780 | 94.6% | 94.6% | +11.0 | 100% | 🟡 5 pts to go |
| P08 | 29302 | 95.0% | 95.0% | +17.2 | 100% | 🟡 5 pts to go |
| P09 | 278 | 74.1% | 74.1% | -0.1 | n/a | no target |
| P10 | 2052 | 94.2% | 94.2% | -0.2 | 100% | 🟡 6 pts to go |
| P11 | 1813 | 55.4% | 55.4% | +4.3 | 80% | ❌ 25 pts to go |
| P12 | 10 | 90.0% | 90.0% | -0.9 | n/a | no target |
| P13 | 202744 | 72.4% | 72.4% | -8.4 | 95% | ❌ 23 pts to go |

## 4. AP

### `ap_contact_name_as_published`

> ceiling: owner 2026-11-08: the AP contact person the organisation itself names on its AP / finance page is allowed (name + role phrase, quoted); mailboxes stay organisational; many bodies publish no AP person

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 2.6% | 2.6% | -0.6 | n/a | no target |
| P01T | 206 | 9.2% | 9.2% | +0.5 | n/a | no target |
| P01_GOLD | 657 | 13.2% | 13.2% | -0.8 | 25% | ❌ 12 pts to go |
| P02 | 486 | 23.9% | 23.9% | -0.9 | 40% | ❌ 16 pts to go |
| P03 | 275 | 8.4% | 8.4% | -0.6 | 20% | ❌ 12 pts to go |
| P04 | 4816 | 2.7% | 2.7% | -0.6 | 20% | ❌ 17 pts to go |
| P05 | 428 | 3.3% | 3.3% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 30514 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06T | 55144 | 0.3% | 0.3% | +0.1 | n/a | no target |
| P06 | 249 | 5.2% | 5.2% | -0.2 | n/a | no target |
| P07 | 780 | 8.1% | 8.1% | +0.2 | n/a | no target |
| P08 | 29302 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P09 | 278 | 7.9% | 7.9% | +0.3 | n/a | no target |
| P10 | 2052 | 0.8% | 0.8% | +0.0 | n/a | no target |
| P11 | 1813 | 0.7% | 0.7% | +0.0 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 202744 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `ap_phone`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 11.2% | 11.2% | -4.9 | n/a | no target |
| P01T | 206 | 18.0% | 18.0% | -1.2 | 70% | ❌ 52 pts to go |
| P01_GOLD | 657 | 41.9% | 41.9% | -0.2 | 80% | ❌ 38 pts to go |
| P02 | 486 | 55.1% | 55.1% | -2.2 | 90% | ❌ 35 pts to go |
| P03 | 275 | 18.5% | 18.5% | -0.7 | 60% | ❌ 42 pts to go |
| P04 | 4816 | 15.9% | 15.9% | -4.3 | 85% | ❌ 69 pts to go |
| P05 | 428 | 11.7% | 11.7% | +0.6 | 50% | ❌ 38 pts to go |
| P06M | 30514 | 0.5% | 0.5% | -0.1 | n/a | no target |
| P06T | 55144 | 0.5% | 0.5% | +0.0 | n/a | no target |
| P06 | 249 | 13.3% | 13.3% | +0.1 | n/a | no target |
| P07 | 780 | 9.6% | 9.6% | +0.5 | n/a | no target |
| P08 | 29302 | 0.4% | 0.4% | -0.1 | n/a | no target |
| P09 | 278 | 74.8% | 74.8% | +2.8 | 95% | ❌ 20 pts to go |
| P10 | 2052 | 1.5% | 1.5% | -0.1 | n/a | no target |
| P11 | 1813 | 13.1% | 13.1% | +0.1 | n/a | no target |
| P12 | 10 | 30.0% | 30.0% | +2.7 | n/a | no target |
| P13 | 202744 | 0.3% | 0.3% | +0.0 | n/a | no target |

### `invoice_mailing_address`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 4.0% | 4.0% | -1.6 | n/a | no target |
| P01T | 206 | 11.2% | 11.2% | +2.0 | n/a | no target |
| P01_GOLD | 657 | 33.2% | 33.2% | -0.6 | 70% | ❌ 37 pts to go |
| P02 | 486 | 37.7% | 37.7% | -1.0 | 75% | ❌ 37 pts to go |
| P03 | 275 | 18.9% | 18.9% | -0.3 | 55% | ❌ 36 pts to go |
| P04 | 4816 | 15.9% | 15.9% | -4.3 | 75% | ❌ 59 pts to go |
| P05 | 428 | 10.7% | 10.7% | +0.5 | 50% | ❌ 39 pts to go |
| P06M | 30514 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06T | 55144 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 249 | 5.6% | 5.6% | -0.1 | n/a | no target |
| P07 | 780 | 4.9% | 4.9% | +0.3 | n/a | no target |
| P08 | 29302 | 0.1% | 0.1% | -0.1 | n/a | no target |
| P09 | 278 | 71.6% | 71.6% | +2.9 | 95% | ❌ 23 pts to go |
| P10 | 2052 | 0.7% | 0.7% | -0.1 | n/a | no target |
| P11 | 1813 | 13.0% | 13.0% | +0.2 | n/a | no target |
| P12 | 10 | 20.0% | 20.0% | +1.8 | n/a | no target |
| P13 | 202744 | 0.1% | 0.1% | -0.1 | n/a | no target |

### `invoicing_requirements`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 5.2% | 5.2% | -2.4 | n/a | no target |
| P01T | 206 | 8.7% | 8.7% | +0.0 | n/a | no target |
| P01_GOLD | 657 | 55.7% | 55.9% | -1.4 | 80% | ❌ 24 pts to go |
| P02 | 486 | 43.4% | 43.6% | -1.9 | 75% | ❌ 32 pts to go |
| P03 | 275 | 35.6% | 35.6% | -0.5 | 70% | ❌ 34 pts to go |
| P04 | 4816 | 15.8% | 16.1% | -4.1 | 70% | ❌ 54 pts to go |
| P05 | 428 | 14.3% | 14.3% | +0.3 | 50% | ❌ 36 pts to go |
| P06M | 30514 | 0.2% | 0.2% | -0.1 | n/a | no target |
| P06T | 55144 | 0.2% | 0.2% | +0.0 | n/a | no target |
| P06 | 249 | 12.9% | 12.9% | -0.3 | n/a | no target |
| P07 | 780 | 1.0% | 1.0% | -0.1 | n/a | no target |
| P08 | 29302 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P09 | 278 | 48.2% | 48.9% | +1.3 | 80% | ❌ 32 pts to go |
| P10 | 2052 | 1.1% | 1.1% | +0.0 | n/a | no target |
| P11 | 1813 | 4.5% | 4.5% | +0.0 | n/a | no target |
| P12 | 10 | 30.0% | 30.0% | -6.4 | n/a | no target |
| P13 | 202744 | 0.1% | 0.1% | +0.0 | n/a | no target |

### `payment_terms_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 10.5% | 10.5% | -4.4 | n/a | no target |
| P01T | 206 | 20.9% | 20.9% | +1.7 | 60% | ❌ 39 pts to go |
| P01_GOLD | 657 | 60.1% | 60.1% | -2.1 | 70% | 🟡 10 pts to go |
| P02 | 486 | 37.2% | 37.2% | -2.3 | 50% | ❌ 13 pts to go |
| P03 | 275 | 44.7% | 44.7% | -3.0 | 55% | ❌ 10 pts to go |
| P04 | 4816 | 9.3% | 9.3% | -3.2 | 40% | ❌ 31 pts to go |
| P05 | 428 | 16.1% | 16.1% | -0.5 | 40% | ❌ 24 pts to go |
| P06M | 30514 | 2.1% | 2.1% | -0.7 | n/a | no target |
| P06T | 55144 | 1.4% | 1.4% | -0.1 | n/a | no target |
| P06 | 249 | 17.3% | 17.3% | -0.9 | n/a | no target |
| P07 | 780 | 4.9% | 4.9% | +0.0 | n/a | no target |
| P08 | 29302 | 2.1% | 2.1% | +0.0 | n/a | no target |
| P09 | 278 | 6.5% | 6.5% | +0.7 | n/a | no target |
| P10 | 2052 | 4.9% | 4.9% | -0.2 | n/a | no target |
| P11 | 1813 | 3.9% | 3.9% | -0.1 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 202744 | 0.6% | 0.6% | -0.1 | n/a | no target |

### `po_required_as_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 15.7% | 15.7% | -6.0 | n/a | no target |
| P01T | 206 | 27.2% | 27.2% | -0.7 | 65% | ❌ 38 pts to go |
| P01_GOLD | 657 | 65.9% | 65.9% | -2.7 | 70% | 🟡 4 pts to go |
| P02 | 486 | 22.2% | 22.2% | -1.5 | 50% | ❌ 28 pts to go |
| P03 | 275 | 48.4% | 48.4% | -2.0 | 60% | ❌ 12 pts to go |
| P04 | 4816 | 4.1% | 4.1% | -1.5 | 40% | ❌ 36 pts to go |
| P05 | 428 | 19.6% | 19.6% | -0.3 | 45% | ❌ 25 pts to go |
| P06M | 30514 | 1.3% | 1.3% | -0.4 | n/a | no target |
| P06T | 55144 | 0.6% | 0.6% | +0.0 | n/a | no target |
| P06 | 249 | 26.9% | 26.9% | -2.4 | n/a | no target |
| P07 | 780 | 4.5% | 4.5% | -0.6 | n/a | no target |
| P08 | 29302 | 0.8% | 0.8% | -0.1 | n/a | no target |
| P09 | 278 | 10.8% | 10.8% | -0.1 | n/a | no target |
| P10 | 2052 | 3.1% | 3.1% | -0.2 | n/a | no target |
| P11 | 1813 | 3.6% | 3.6% | +0.0 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 202744 | 0.2% | 0.2% | +0.0 | n/a | no target |

### `invoice_portal_url`

> ceiling: only portals the buyer names on its own pages; informational tax-authority links are not portals

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 9.8% | 9.8% | -2.2 | n/a | no target |
| P01T | 206 | 14.1% | 14.1% | +1.4 | n/a | no target |
| P01_GOLD | 657 | 47.8% | 47.8% | -2.4 | 50% | 🟡 2 pts to go |
| P02 | 486 | 36.4% | 36.4% | -1.2 | n/a | no target |
| P03 | 275 | 49.1% | 49.1% | -1.7 | 60% | ❌ 11 pts to go |
| P04 | 4816 | 9.3% | 9.3% | -3.5 | n/a | no target |
| P05 | 428 | 15.2% | 15.2% | +0.0 | n/a | no target |
| P06M | 30514 | 0.6% | 0.6% | -0.2 | n/a | no target |
| P06T | 55144 | 0.3% | 0.3% | +0.0 | n/a | no target |
| P06 | 249 | 18.5% | 18.5% | -1.9 | n/a | no target |
| P07 | 780 | 4.9% | 4.9% | -0.8 | n/a | no target |
| P08 | 29302 | 0.4% | 0.4% | +0.0 | n/a | no target |
| P09 | 278 | 20.9% | 20.9% | +0.2 | n/a | no target |
| P10 | 2052 | 2.2% | 2.2% | -0.3 | n/a | no target |
| P11 | 1813 | 2.5% | 2.5% | -0.2 | n/a | no target |
| P12 | 10 | 20.0% | 20.0% | +1.8 | n/a | no target |
| P13 | 202744 | 0.1% | 0.1% | -0.1 | n/a | no target |

### `buyer_payment_method_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 6.0% | 6.0% | -2.8 | 15% | 🟡 9 pts to go |
| P01T | 206 | 13.6% | 13.6% | +0.9 | 15% | 🟡 1 pts to go |
| P01_GOLD | 657 | 33.6% | 33.6% | -1.5 | 40% | 🟡 6 pts to go |
| P02 | 486 | 11.5% | 11.7% | -0.7 | 25% | ❌ 14 pts to go |
| P03 | 275 | 15.3% | 15.3% | -1.2 | 25% | 🟡 10 pts to go |
| P04 | 4816 | 2.2% | 2.2% | -0.5 | 15% | ❌ 13 pts to go |
| P05 | 428 | 6.3% | 6.3% | -0.3 | 15% | 🟡 9 pts to go |
| P06M | 30514 | 0.7% | 0.7% | -0.1 | 15% | ❌ 14 pts to go |
| P06T | 55144 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P06 | 249 | 9.2% | 9.2% | -0.1 | 15% | 🟡 6 pts to go |
| P07 | 780 | 3.5% | 3.5% | +0.1 | 15% | ❌ 12 pts to go |
| P08 | 29302 | 0.6% | 0.6% | +0.1 | 15% | ❌ 14 pts to go |
| P09 | 278 | 1.1% | 1.1% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2052 | 1.3% | 1.3% | -0.1 | 15% | ❌ 14 pts to go |
| P11 | 1813 | 1.2% | 1.2% | +0.0 | 15% | ❌ 14 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 202744 | 0.6% | 0.6% | +0.0 | 15% | ❌ 14 pts to go |

### `buyer_tax_exempt_status`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 4.0% | 4.0% | -1.6 | 15% | ❌ 11 pts to go |
| P01T | 206 | 11.7% | 11.7% | +0.8 | 25% | ❌ 13 pts to go |
| P01_GOLD | 657 | 27.5% | 27.5% | -1.4 | 25% | ✅ met |
| P02 | 486 | 24.3% | 24.3% | -1.1 | 15% | ✅ met |
| P03 | 275 | 21.5% | 21.5% | -0.3 | 15% | ✅ met |
| P04 | 4816 | 3.0% | 3.0% | -1.0 | 15% | ❌ 12 pts to go |
| P05 | 428 | 11.4% | 11.4% | +0.0 | 15% | 🟡 4 pts to go |
| P06M | 30514 | 0.5% | 0.5% | -0.1 | 15% | ❌ 14 pts to go |
| P06T | 55144 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 249 | 6.8% | 6.8% | -0.3 | 15% | 🟡 8 pts to go |
| P07 | 780 | 1.7% | 1.7% | -0.1 | 15% | ❌ 13 pts to go |
| P08 | 29302 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 278 | 1.4% | 1.4% | -0.1 | 15% | ❌ 14 pts to go |
| P10 | 2052 | 1.6% | 1.6% | +0.0 | 15% | ❌ 13 pts to go |
| P11 | 1813 | 1.8% | 1.8% | +0.0 | 15% | ❌ 13 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 202744 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `buyer_ap_cycle_published`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 1.2% | 1.2% | -0.4 | 20% | ❌ 19 pts to go |
| P01T | 206 | 3.4% | 3.4% | +0.3 | 20% | ❌ 17 pts to go |
| P01_GOLD | 657 | 4.1% | 4.1% | -0.2 | 20% | ❌ 16 pts to go |
| P02 | 486 | 1.4% | 1.4% | -0.1 | 20% | ❌ 19 pts to go |
| P03 | 275 | 1.5% | 1.5% | -0.4 | 20% | ❌ 18 pts to go |
| P04 | 4816 | 0.6% | 0.6% | -0.1 | 20% | ❌ 19 pts to go |
| P05 | 428 | 0.9% | 0.9% | +0.0 | 20% | ❌ 19 pts to go |
| P06M | 30514 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06T | 55144 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P06 | 249 | 1.6% | 1.6% | +0.2 | 20% | ❌ 18 pts to go |
| P07 | 780 | 0.3% | 0.3% | +0.1 | 20% | ❌ 20 pts to go |
| P08 | 29302 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P09 | 278 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P10 | 2052 | 0.3% | 0.3% | +0.0 | 20% | ❌ 20 pts to go |
| P11 | 1813 | 0.1% | 0.1% | +0.0 | 20% | ❌ 20 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |
| P13 | 202744 | 0.0% | 0.0% | +0.0 | 20% | ❌ 20 pts to go |

### `buyer_esignature_preference`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 1.0% | 1.0% | -0.6 | 15% | ❌ 14 pts to go |
| P01T | 206 | 2.4% | 2.4% | -0.7 | 15% | ❌ 13 pts to go |
| P01_GOLD | 657 | 10.2% | 10.2% | -0.3 | 15% | 🟡 5 pts to go |
| P02 | 486 | 10.5% | 10.5% | -1.0 | 15% | 🟡 4 pts to go |
| P03 | 275 | 20.4% | 20.4% | -0.3 | 15% | ✅ met |
| P04 | 4816 | 1.8% | 1.8% | -0.6 | 15% | ❌ 13 pts to go |
| P05 | 428 | 2.8% | 2.8% | +0.0 | 15% | ❌ 12 pts to go |
| P06M | 30514 | 0.3% | 0.3% | -0.1 | 15% | ❌ 15 pts to go |
| P06T | 55144 | 0.2% | 0.2% | +0.0 | 15% | ❌ 15 pts to go |
| P06 | 249 | 4.0% | 4.0% | +0.1 | 15% | ❌ 11 pts to go |
| P07 | 780 | 1.3% | 1.3% | +0.1 | 15% | ❌ 14 pts to go |
| P08 | 29302 | 0.3% | 0.3% | +0.0 | 15% | ❌ 15 pts to go |
| P09 | 278 | 0.7% | 0.7% | +0.0 | 15% | ❌ 14 pts to go |
| P10 | 2052 | 1.1% | 1.1% | +0.0 | 15% | ❌ 14 pts to go |
| P11 | 1813 | 0.7% | 0.7% | -0.1 | 15% | ❌ 14 pts to go |
| P12 | 10 | 0.0% | 0.0% | +0.0 | 15% | ❌ 15 pts to go |
| P13 | 202744 | 0.1% | 0.1% | +0.0 | 15% | ❌ 15 pts to go |

### `ap_system_hint`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 11.0% | 11.0% | -1.4 | 20% | 🟡 9 pts to go |
| P01T | 206 | 15.0% | 15.0% | +1.5 | 40% | ❌ 25 pts to go |
| P01_GOLD | 657 | 44.3% | 44.3% | -2.3 | 40% | ✅ met |
| P02 | 486 | 42.0% | 42.0% | -1.2 | 20% | ✅ met |
| P03 | 275 | 47.3% | 47.3% | -1.2 | 35% | ✅ met |
| P04 | 4816 | 11.0% | 11.0% | -3.9 | 20% | 🟡 9 pts to go |
| P05 | 428 | 15.7% | 15.7% | +0.1 | 20% | 🟡 4 pts to go |
| P06M | 30514 | 0.9% | 0.9% | -0.1 | 20% | ❌ 19 pts to go |
| P06T | 55144 | 0.6% | 0.6% | +0.0 | 20% | ❌ 19 pts to go |
| P06 | 249 | 18.9% | 18.9% | -2.2 | 20% | 🟡 1 pts to go |
| P07 | 780 | 5.4% | 5.4% | -0.7 | 20% | ❌ 15 pts to go |
| P08 | 29302 | 0.8% | 0.8% | +0.0 | 20% | ❌ 19 pts to go |
| P09 | 278 | 21.2% | 21.2% | +0.1 | 20% | ✅ met |
| P10 | 2052 | 3.6% | 3.6% | -0.2 | 20% | ❌ 16 pts to go |
| P11 | 1813 | 3.1% | 3.1% | -0.1 | 20% | ❌ 17 pts to go |
| P12 | 10 | 10.0% | 10.0% | +0.9 | 20% | 🟡 10 pts to go |
| P13 | 202744 | 0.3% | 0.3% | -0.1 | 20% | ❌ 20 pts to go |

## 5. contract

### `contract_value`

> ceiling: rows proven by a lobbying filing, a news release, an auditor appointment, a customer story or a vendor's client list have no contract value by nature (≈17 % of P01 Gold); bids&tenders awards now carry the awarded bidder's submitted price when no award value was published

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 11.2% | 11.2% | -6.9 | n/a | no target |
| P01T | 206 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 657 | 68.9% | 68.9% | -2.7 | 95% | ❌ 26 pts to go |
| P02 | 486 | 63.0% | 63.0% | -3.2 | 95% | ❌ 32 pts to go |
| P03 | 275 | 55.3% | 55.3% | -2.6 | 90% | ❌ 35 pts to go |
| P04 | 4816 | 20.7% | 20.7% | -5.8 | 85% | ❌ 64 pts to go |
| P05 | 428 | 39.3% | 39.3% | +0.4 | 75% | ❌ 36 pts to go |
| P06M | 30514 | 23.0% | 23.0% | -5.1 | n/a | no target |
| P06T | 55144 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 249 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 780 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29302 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 89.6% | 89.6% | +0.5 | 100% | ❌ 10 pts to go |
| P10 | 2052 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1813 | 4.0% | 4.0% | +0.2 | 60% | ❌ 56 pts to go |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 202744 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `currency`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 11.2% | 11.2% | -6.9 | n/a | no target |
| P01T | 206 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 657 | 70.6% | 70.6% | -2.9 | 100% | ❌ 29 pts to go |
| P02 | 486 | 64.8% | 64.8% | -3.4 | 100% | ❌ 35 pts to go |
| P03 | 275 | 57.8% | 57.8% | -2.7 | n/a | no target |
| P04 | 4816 | 21.0% | 21.0% | -6.0 | 95% | ❌ 74 pts to go |
| P05 | 428 | 35.0% | 35.0% | +0.4 | 80% | ❌ 45 pts to go |
| P06M | 30514 | 23.0% | 23.0% | -5.1 | n/a | no target |
| P06T | 55144 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 249 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 780 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29302 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 92.1% | 92.1% | +0.5 | 100% | 🟡 8 pts to go |
| P10 | 2052 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1813 | 4.1% | 4.1% | +0.1 | n/a | no target |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 202744 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `start_date`

> ceiling: most award notices publish an award date, not a start date; start_date carries the signature date when the source gives one, labelled

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 82.1% | 82.1% | -2.2 | n/a | no target |
| P01T | 206 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 657 | 54.2% | 54.2% | +1.9 | 85% | ❌ 31 pts to go |
| P02 | 486 | 60.3% | 60.3% | +1.1 | 90% | ❌ 30 pts to go |
| P03 | 275 | 46.9% | 46.9% | +2.9 | 85% | ❌ 38 pts to go |
| P04 | 4816 | 37.7% | 37.7% | +8.6 | 90% | ❌ 52 pts to go |
| P05 | 428 | 32.9% | 32.9% | +0.0 | 75% | ❌ 42 pts to go |
| P06M | 30514 | 82.0% | 82.0% | -2.3 | n/a | no target |
| P06T | 55144 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 249 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 780 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29302 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 82.4% | 82.4% | +0.6 | 95% | ❌ 13 pts to go |
| P10 | 2052 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1813 | 3.9% | 3.9% | +0.6 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 202744 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `end_date`

> ceiling: an inferred end (award date + published duration) is labelled as such; sources without a duration leave end_date empty — the honest ceiling. P09 is BY DEFINITION the rows whose end date is not published (older SEAO contracts with no closing notice): its end_date / duration targets cannot be met without inventing a date

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 54.3% | 54.3% | -11.6 | n/a | no target |
| P01T | 206 | 0.5% | 0.5% | +0.1 | n/a | no target |
| P01_GOLD | 657 | 53.9% | 53.9% | +1.9 | 85% | ❌ 31 pts to go |
| P02 | 486 | 54.3% | 54.3% | +0.9 | 90% | ❌ 36 pts to go |
| P03 | 275 | 46.9% | 46.9% | +2.5 | 85% | ❌ 38 pts to go |
| P04 | 4816 | 33.5% | 33.5% | +8.9 | 90% | ❌ 56 pts to go |
| P05 | 428 | 42.1% | 42.1% | -0.6 | 75% | ❌ 33 pts to go |
| P06M | 30514 | 63.1% | 63.1% | -6.1 | n/a | no target |
| P06T | 55144 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 249 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 780 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29302 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 0.4% | 0.4% | +0.0 | 95% | ❌ 95 pts to go |
| P10 | 2052 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1813 | 3.0% | 3.0% | +0.5 | n/a | no target |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P13 | 202744 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `contract_title`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 97.1% | 97.1% | +1.9 | n/a | no target |
| P01T | 206 | 95.6% | 95.6% | -0.5 | n/a | no target |
| P01_GOLD | 657 | 85.8% | 86.0% | +0.3 | 100% | ❌ 14 pts to go |
| P02 | 486 | 78.2% | 78.2% | +0.6 | 100% | ❌ 22 pts to go |
| P03 | 275 | 92.4% | 92.4% | -0.1 | n/a | no target |
| P04 | 4816 | 53.6% | 53.6% | +3.0 | 95% | ❌ 41 pts to go |
| P05 | 428 | 77.6% | 77.6% | +0.3 | 95% | ❌ 17 pts to go |
| P06M | 30514 | 99.5% | 99.5% | +0.2 | n/a | no target |
| P06T | 55144 | 97.9% | 97.9% | +3.4 | n/a | no target |
| P06 | 249 | 20.9% | 20.9% | +0.5 | n/a | no target |
| P07 | 780 | 10.3% | 10.3% | +0.1 | n/a | no target |
| P08 | 29302 | 4.6% | 4.6% | +0.1 | n/a | no target |
| P09 | 278 | 98.2% | 98.2% | +0.0 | 100% | 🟡 2 pts to go |
| P10 | 2052 | 71.1% | 71.1% | +0.5 | n/a | no target |
| P11 | 1813 | 70.0% | 70.0% | +0.2 | n/a | no target |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 202744 | 99.6% | 99.6% | +0.0 | n/a | no target |

### `contract_description`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 97.1% | 97.1% | +1.9 | n/a | no target |
| P01T | 206 | 95.6% | 95.6% | -0.5 | n/a | no target |
| P01_GOLD | 657 | 88.9% | 89.0% | +0.2 | 100% | ❌ 11 pts to go |
| P02 | 486 | 79.4% | 79.4% | +0.6 | 100% | ❌ 21 pts to go |
| P03 | 275 | 93.1% | 93.1% | -0.1 | n/a | no target |
| P04 | 4816 | 56.1% | 56.1% | +2.1 | 95% | ❌ 39 pts to go |
| P05 | 428 | 89.7% | 89.7% | +0.4 | 70% | ✅ met |
| P06M | 30514 | 99.5% | 99.5% | +0.2 | n/a | no target |
| P06T | 55144 | 97.9% | 97.9% | +3.4 | n/a | no target |
| P06 | 249 | 20.9% | 20.9% | +0.5 | n/a | no target |
| P07 | 780 | 10.3% | 10.3% | +0.1 | n/a | no target |
| P08 | 29302 | 4.6% | 4.6% | +0.1 | n/a | no target |
| P09 | 278 | 98.2% | 98.2% | +0.0 | 100% | 🟡 2 pts to go |
| P10 | 2052 | 71.1% | 71.1% | +0.5 | n/a | no target |
| P11 | 1813 | 70.0% | 70.0% | +0.1 | n/a | no target |
| P12 | 10 | 100.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 202744 | 0.0% | 0.0% | +0.0 | n/a | no target |

### `number_of_bids`

> ceiling: published by some portals only (bids&tenders submission lists, Biddingo bidder lists); federal proactive disclosure does not publish bid counts

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01T | 206 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P01_GOLD | 657 | 16.1% | 16.1% | -0.8 | 60% | ❌ 44 pts to go · rows from a source that publishes bids: 368 rows, 28.8% filled |
| P02 | 486 | 9.9% | 9.9% | -0.8 | n/a | no target · rows from a source that publishes bids: 294 rows, 16.3% filled |
| P03 | 275 | 13.1% | 13.1% | -0.8 | n/a | no target · rows from a source that publishes bids: 142 rows, 25.4% filled |
| P04 | 4816 | 1.3% | 1.3% | -0.4 | n/a | no target · rows from a source that publishes bids: 882 rows, 7.0% filled |
| P05 | 428 | 2.6% | 2.6% | +0.0 | n/a | no target · rows from a source that publishes bids: 59 rows, 18.6% filled |
| P06M | 30514 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06T | 55144 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P06 | 249 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P07 | 780 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P08 | 29302 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P09 | 278 | 4.0% | 4.0% | -0.4 | n/a | no target · rows from a source that publishes bids: 265 rows, 4.2% filled |
| P10 | 2052 | 0.0% | 0.0% | +0.0 | n/a | no target |
| P11 | 1813 | 0.4% | 0.4% | +0.0 | n/a | no target · rows from a source that publishes bids: 69 rows, 11.6% filled |
| P12 | 10 | 0.0% | 0.0% | +0.0 | n/a | no target · rows from a source that publishes bids: 10 rows, 0.0% filled |
| P13 | 202744 | 0.0% | 0.0% | +0.0 | n/a | no target |

## 6. history

### `average_contract_duration_days`

> ceiling: needs two dates (or a published term) on the buyer's records; P09 rows (end date unpublished by definition) and buyers whose sources publish award dates only have no honest duration

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 206 | 0.0% | 97.6% | +0.0 | n/a | no target |
| P01_GOLD | 657 | 51.1% | 83.0% | -2.3 | 90% | ❌ 39 pts to go |
| P02 | 486 | 50.2% | 87.0% | -3.2 | 90% | ❌ 40 pts to go |
| P03 | 275 | 44.0% | 80.7% | -1.9 | 90% | ❌ 46 pts to go |
| P04 | 4816 | 14.7% | 94.8% | -4.9 | 90% | ❌ 75 pts to go |
| P05 | 428 | 0.0% | 81.3% | +0.0 | 90% | ❌ 90 pts to go |
| P06M | 30514 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 55144 | 0.0% | 99.9% | +0.0 | n/a | no target |
| P06 | 249 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 780 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 29302 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 278 | 2.9% | 4.7% | +0.0 | 90% | ❌ 87 pts to go |
| P10 | 2052 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1813 | 2.2% | 97.6% | +0.1 | n/a | no target |
| P12 | 10 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 202744 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `commodity_distribution_top3`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 206 | 1.0% | 98.5% | +0.1 | n/a | no target |
| P01_GOLD | 657 | 25.3% | 57.1% | -1.2 | 90% | ❌ 65 pts to go |
| P02 | 486 | 49.6% | 86.4% | -2.8 | n/a | no target |
| P03 | 275 | 24.4% | 61.1% | -0.8 | n/a | no target |
| P04 | 4816 | 15.8% | 96.0% | -5.6 | n/a | no target |
| P05 | 428 | 0.5% | 81.8% | +0.0 | n/a | no target |
| P06M | 30514 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 55144 | 0.1% | 99.9% | +0.0 | n/a | no target |
| P06 | 249 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 780 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 29302 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 278 | 41.0% | 42.8% | +0.6 | n/a | no target |
| P10 | 2052 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1813 | 2.3% | 97.7% | +0.1 | n/a | no target |
| P12 | 10 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 202744 | 0.0% | 100.0% | +0.0 | n/a | no target |

### `year_over_year_spend_trend`

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P01T | 206 | 2.4% | 100.0% | +0.2 | n/a | no target |
| P01_GOLD | 657 | 50.1% | 81.9% | -1.9 | 95% | ❌ 45 pts to go |
| P02 | 486 | 55.1% | 92.0% | -3.0 | n/a | no target |
| P03 | 275 | 48.0% | 84.7% | -2.4 | n/a | no target |
| P04 | 4816 | 16.4% | 96.5% | -5.8 | n/a | no target |
| P05 | 428 | 5.1% | 86.4% | +0.1 | n/a | no target |
| P06M | 30514 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P06T | 55144 | 0.1% | 100.0% | +0.0 | n/a | no target |
| P06 | 249 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P07 | 780 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P08 | 29302 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P09 | 278 | 60.4% | 62.2% | +0.0 | n/a | no target |
| P10 | 2052 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P11 | 1813 | 2.4% | 97.8% | +0.0 | n/a | no target |
| P12 | 10 | 0.0% | 100.0% | +0.0 | n/a | no target |
| P13 | 202744 | 0.0% | 100.0% | +0.0 | n/a | no target |

## 7. mail security

### `mta_sts`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 206 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 657 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 486 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 275 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4816 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 428 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 30514 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 55144 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 249 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 780 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 29302 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 278 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2052 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1813 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 202744 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `tls_rpt`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 206 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 657 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 486 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 275 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4816 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 428 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 30514 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 55144 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 249 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 780 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 29302 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 278 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2052 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1813 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 202744 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |

### `bimi`

> ceiling: DNS-only check; 'no record' counts as checked

| package | rows | now (values) | any (incl. labels) | Δ | target | status |
|---|---|---|---|---|---|---|
| P01M | 420 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01T | 206 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P01_GOLD | 657 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P02 | 486 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P03 | 275 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P04 | 4816 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P05 | 428 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06M | 30514 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06T | 55144 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P06 | 249 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P07 | 780 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P08 | 29302 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P09 | 278 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P10 | 2052 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P11 | 1813 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P12 | 10 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |
| P13 | 202744 | 100.0% | 100.0% | +0.0 | 100% | ✅ met |


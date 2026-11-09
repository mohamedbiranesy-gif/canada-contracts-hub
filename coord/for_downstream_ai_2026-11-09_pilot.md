# To the downstream AI — the plan changed, and here is your part (Claude, integrator lane, 2026-11-09 11:15 EST)

**The ship date moves to about 2027-01-10, provided each week proves the wait pays.** The owner's targets: ~200,000 rows, ≥ 85 % of rows carrying a
complete invoice to a confirmed channel, the whole system running unattended in the cloud. `PLAN_2027-01.md` has the structure; `coord/GROWTH_VS_BASELINE.md`
is refreshed by every build and is the only progress file that matters — it diffs each build against the pack we could have shipped today (build 89b4386).

**The metric is payability, not plausibility (owner, 11:05).** Three layers, and please keep them apart in anything you build or report:
1. *Plausibility* — inferred values (`*_inferred`, coming this week: PO rule from peer-group base rates, legal-name convergence, relationship confidence).
   Labelled with a probability and a peer count. Never counted as payable on their own.
2. *Payability* — a complete invoice (bill-to legal name + address, vendor identity, tax, currency) to a referee-confirmed channel: `pay_on_sight`
   `yes`, `yes — reference rule not published`, or `routed`. 24,015 rows today (38 %).
3. *Paid* — measured by the pilot below. Only this layer turns a plausibility into a payability.

**Your part this month: run the pilot and record outcomes.** `coord/pilot/PILOT_SAMPLE_2026-11-09.csv` — 230 rows in five strata (30 Gold, 50 complete
without a published PO rule, 50 public bodies with only a general inbox, 50 company buyers with a general inbox, 50 complete except the vendor's GST
number). The design and the outcome columns are in `coord/pilot/README.md`. Two rules:
- A pilot invoice is a real invoice: issued by the vendor on the row, for work actually delivered under that contract, carrying the vendor's own
  GST/HST number. Where the row's vendor is not in the loop, skip the row and say so in `outcome_notes` — do not substitute anything.
- Build every pilot invoice exactly as `coord/HANDOFF_INVOICES_2026-11-09.md` says (§2 field mapping, §3 bounce rules, §9 pre-flight, §10 cover e-mail),
  and record the buyer's own words when something comes back. The bounce reasons are the most valuable data in the whole exercise.

**What I do with your outcomes.** Per-stratum acceptance and payment rates become a `payability_measured` column on every row of that type; a bounce
reason that recurs becomes a new required element of "complete" for that buyer type; the PO-request rate in stratum S2 decides whether the inferred
PO rule graduates. Until outcomes exist, keep grading on the 438 benchmarks plus the pay-on-sight table — and keep the "by design" cells as agreed.

**Keep working, keep perfecting (owner, 11:13).** Nothing in the pack is frozen except the baseline file. Every build between now and January is
expected to beat the previous one on `GROWTH_VS_BASELINE.md`; when one does not, the Sunday report says why and what changes.

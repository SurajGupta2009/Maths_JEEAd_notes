# Source Audit — Chapter 11: Probability & Statistics

## Sources reviewed

- `notes/Probability/Probability.md` — all 1033 lines reviewed before
  authoring: six theory chapters, worked examples, Olympiad frontier and
  appendix.
- `notes/Probability/Probability — Paper.md` and `… — Solutions.md` identified
  as companion practice sources; no practice-paper text was copied into the
  notes.
- Official JEE Advanced syllabus coverage includes probability and descriptive
  statistics (mean, median, mode, mean deviation, grouped/ungrouped variance
  and SD, and random-variable mean/variance).

## Source gap

The repository Probability module contains substantial probability,
random-variable, distribution and Olympiad material, but **does not contain a
dedicated treatment of the official descriptive-statistics list**. The mean,
median, mode, mean-deviation, variance/SD and grouped-data material is therefore
authored here from standard definitions and syllabus scope; grouped-data
interpolations are expressly presented as estimates, not exact recovery of raw
data.

## Independent verification performed

`scripts/math_checks.py`: **221 targeted checks** (script output), including
two-dice counts, complements, card/committee counts, conditional probability,
without-replacement draws, total probability and Bayes; random-variable mean,
second moment and variance; binomial total mass/mean/variance for multiple
$n,p$ pairs; geometric expectation checks; ungrouped and frequency-table
statistics, variance identity and affine scaling; grouped class-mark
mean/variance/mean deviation and median/mode estimates; ballot theorem by
listing orderings; birthday probability; coupon-collector expectation;
consecutive-head recurrence; derangement value and biased gambler's-ruin
recurrence. Numeric/simulation evidence in the source was not treated as proof.

## Corrections and conventions

- A first draft of the authored derangements example misstated $D_3$ as 4;
  the recurrence and inclusion–exclusion check caught it before export. The
  correct count is $D_3=2$ (probability $1/3$); content and test were corrected.
- No numerical source error was identified among source examples used in the
  authored probability sheets and independently checked.
- The source's probability treatment is supplemented, not silently treated as
  a statistics source; this gap is recorded above and on the sheets.
- Conditional probabilities explicitly require a positive conditioning-event
  probability; Bayes requires a partition; binomial requires independent
  constant-probability trials; geometric waiting time states its support
  convention.
- General optional-stopping claims are not used. The fair gambler's-ruin
  argument is limited to finite barriers and absorption.

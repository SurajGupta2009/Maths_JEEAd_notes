# Chapter 11 — Probability & Statistics

Explanatory handwritten-style short notes, generated from editable source in
`content/` with the shared renderer. **Part I (JEE): 5 sheets; Part II
(Olympiad extensions): 2 sheets.**

## Coverage

- **Part I — JEE Main + Advanced:** finite sample spaces, equally likely
  outcomes and complements; addition and conditional probability; independence,
  total probability and Bayes; discrete random variables, expectation and
  variance; binomial and geometric waiting models (with conditions); mean,
  median, mode and mean deviation; grouped/ungrouped variance and standard
  deviation; class-mark estimates and grouped median/mode interpolation.
- **Part II — Olympiad/specialised extensions:** geometric probability,
  Bertrand ballot, birthday collisions; state recurrences, memorylessness,
  coupon collector, runs, gambler's ruin, derangements and averaging.

A source gap is made explicit: the repository has a complete probability
module, but no standalone descriptive-statistics chapter. Statistics content
was authored from syllabus scope and standard definitions; grouped-data
estimates are labelled as estimates.

## Files

`JEE/` and `Olympiad/` contain numbered sheets; `exports/` contains three PNG
ZIPs and three bookmarked A4 PDFs (combined PDF puts JEE first). `index.html`
is the gallery; `manifest.json` records pagination. `content/*.md` is editable;
`scripts/` contains render/export/layout/numeric checks. See `SCOPE.md`,
`SOURCE-AUDIT.md`, and `PRINTING.txt`.

## Rebuild

```bash
python3 scripts/render.py && python3 scripts/export.py && python3 scripts/check.py
python3 scripts/math_checks.py
```

## Reading order

Follow the `LESSON n / total` ribbons; read down the left column, then down the right column, and continue to the next sheet. This sequence follows the chapter’s prerequisite path.

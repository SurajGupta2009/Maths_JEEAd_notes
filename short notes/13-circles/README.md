# Chapter 13 — Circles

Explanatory handwritten-style notes generated from the editable Markdown in
`content/`. **Part I: 5 JEE sheets; Part II: 2 Olympiad sheets.** Scope is
mapped to the official Advanced 2026 circle bullets, including parametric
equations and line intersections; power/radical-axis methods are identified as
useful applications.

## Coverage

- **Part I — JEE core and close applications:** standard/general forms and
  real-radius cases; circles through data and diameter endpoints; angular and
  rational parametrization; secant/tangent/no-hit classification and chord
  length; tangent, normal, power, tangent length and chord of contact; radical
  axis/centre and two-circle position.
- **Part II — Olympiad extensions:** coaxal families, inversion, Simson's line
  and Ptolemy, with exact hypotheses and source-data corrections. These are
  topic-linked extensions, not a complete IOQM course.

## Files and rebuild

- `JEE/`, `Olympiad/` — independently numbered PNG sheets.
- `exports/` — three PNG ZIPs and three bookmarked A4 PDFs (combined puts JEE
  first); `index.html` — gallery; `manifest.json` — build manifest.
- `content/*.md` — source lessons; `scripts/` — render, export, delivery and
  mathematical checks.
- `SCOPE.md`, `SOURCE-AUDIT.md`, `PRINTING.txt` — scope, source review and print
  setup.

```bash
python3 scripts/render.py && python3 scripts/export.py && python3 scripts/check.py
python3 scripts/math_checks.py
```

## Reading order

Follow the `LESSON n / total` markers. Read top-to-bottom in the left column,
then top-to-bottom in the right column, then continue to the next sheet. The
lesson sequence goes circle forms → parametrization → line intersection →
tangents/power → radical axes.

## Audit boundary

The syllabus comparison in `SOURCE-AUDIT.md` is anchored to the official JEE
Advanced 2026 syllabus. Part I is intended for overlapping JEE Main + Advanced
preparation, but this is not a separate exhaustive JEE Main crosswalk. Read
`SCOPE.md` for what is core and what is a useful derivation; no complete IOQM
coverage is claimed.

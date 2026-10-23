# Chapter 12 — Straight Lines & Locus

Explanatory handwritten-style notes generated from the editable Markdown in
`content/`. **Part I: 7 JEE sheets; Part II: 2 Olympiad sheets.** The official
Advanced 2026 line/triangle-centre bullets are mapped in `SCOPE.md`; derived
locus methods and line-pair machinery are labelled as applications rather than
invented syllabus bullets.

## Coverage

- **Part I — JEE core and close applications:** coordinate distance, section
  and translation; line forms, angles, distance and perpendicular feet; line
  pencils, concurrency and normalized bisectors; centroid, circumcentre,
  orthocentre and incentre; equidistance and Apollonius loci; homogeneous pairs
  of lines as a useful derived tool.
- **Part II — Olympiad extensions:** Euler-line ratios, the nine-point circle
  with a coordinate proof pattern, and further locus reasoning. These are
  relevant extensions only; this chapter is not a full IOQM geometry course.

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
lesson sequence goes coordinates → lines → centres → loci.

## Audit boundary

The syllabus comparison in `SOURCE-AUDIT.md` is anchored to the official JEE
Advanced 2026 syllabus. Part I is intended for overlapping JEE Main + Advanced
preparation, but this is not a separate exhaustive JEE Main crosswalk. Read
`SCOPE.md` for what is core and what is a useful derivation; no complete IOQM
coverage is claimed.

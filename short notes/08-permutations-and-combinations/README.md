# Chapter 8 — Permutations & Combinations

Handwritten-style, teacher-style explanatory notes generated from editable Markdown. This expanded edition includes a dedicated visual-methods lesson and uses one continuous top-to-bottom reading stream on every sheet.

## Current edition

- **Part I — JEE Main + Advanced:** 17 sheets across 8 source lessons in `JEE/`.
- **Part II — Olympiad / extensions:** 4 sheets across 3 source lessons in `Olympiad/`.
- **Visual expansion:** `jee-90-visual-methods.md` adds 5 editable figures; the chapter has 6 diagram blocks in total.
- **Page geometry:** 2480×3508 px A4 portrait PNGs at nominal 300 DPI, with ink kept inside the safe margins.

## Downloads

| Artifact | File |
|---|---|
| Combined PNG ZIP (JEE first) | [`exports/08-permutations-and-combinations-combined-sheets.zip`](exports/08-permutations-and-combinations-combined-sheets.zip) |
| JEE PNG ZIP | [`exports/08-permutations-and-combinations-JEE-sheets.zip`](exports/08-permutations-and-combinations-JEE-sheets.zip) |
| Olympiad PNG ZIP | [`exports/08-permutations-and-combinations-Olympiad-sheets.zip`](exports/08-permutations-and-combinations-Olympiad-sheets.zip) |
| Combined bookmarked PDF (JEE first) | [`exports/08-permutations-and-combinations-combined.pdf`](exports/08-permutations-and-combinations-combined.pdf) |
| JEE bookmarked PDF | [`exports/08-permutations-and-combinations-JEE.pdf`](exports/08-permutations-and-combinations-JEE.pdf) |
| Olympiad bookmarked PDF | [`exports/08-permutations-and-combinations-Olympiad-extensions.pdf`](exports/08-permutations-and-combinations-Olympiad-extensions.pdf) |
| Browser gallery | [`index.html`](index.html) |

## Source lessons and page ranges

### Part I — JEE

- `jee-01.md` — Permutations & Combinations — The Two Rules, the Complement, and What Counting Means (**JEE 1–2**).
- `jee-02.md` — Permutations — nPr, Factorials, and Arrangements with Identical Objects (**JEE 3**).
- `jee-03.md` — Circular Permutations and Restriction Methods — Bundle, Gap, Relative Order (**JEE 4–5**).
- `jee-04.md` — Combinations — nCr, Pascal, Hockey-Stick, and Restricted Selections (**JEE 6–7**).
- `jee-05.md` — Stars and Bars, Compositions, Multisets, and Bounded Distributions (**JEE 8**).
- `jee-06.md` — Inclusion–Exclusion and Derangements — Counting 'None of the Bad Things' (**JEE 9–10**).
- `jee-07.md` — Pigeonhole, Recurrence Counting, and the Chapter Recap (**JEE 11–12**).
- `jee-90-visual-methods.md` — Visual Counting Lab — Decisions, Paths, Distributions and Overlap (**JEE 13–17**).

### Part II — Olympiad / extensions

- `olympiad-01.md` — Extension — Lattice Paths, Reflection, Catalan Numbers, and the Ballot Theorem (**Olympiad 1**).
- `olympiad-02.md` — Extension — Burnside's Lemma and Pólya Enumeration: Counting Up to Symmetry (**Olympiad 2**).
- `olympiad-03.md` — Extension — Partitions, Stirling Numbers, and Extremal Set Families (**Olympiad 3–4**).

## Editable sources and visual builders

Every sheet is authored in `content/*.md` using frontmatter, prose, display mathematics, callout boxes, JSON diagram specifications, and optional `<!-- pagebreak -->` markers. Lessons start on fresh sheets; long lessons continue automatically without shrinking or clipping prose. Figures remain editable in the source rather than being external screenshots.

## Reproducible build and verification

```bash
python3 -m pip install -r ../_engine/requirements.txt  # once
python3 scripts/render.py       # Markdown -> PNG sheets + manifest.json
python3 scripts/export.py       # 3 ZIPs + 3 bookmarked PDFs + gallery
python3 scripts/math_checks.py  # independent exact/numeric worked-example checks
python3 scripts/check.py        # formula, font, PNG, manifest, export and link gates
```

The mathematical suites include targeted checks for the visual-methods examples. The delivery suite checks formula parsing, glyph fallback, A4 dimensions and DPI, complete safe-border ink scans, manifest ordering, ZIP integrity, PDF page counts and bookmarks, documentation, and local gallery links. These reproducible checks supplement—rather than claim to replace—mathematical and visual review.

## Reading order, scope and printing

Follow the `LESSON n / total` ribbons and read straight down each sheet, then continue on the next sheet. Continuation sheets retain the lesson title and add `(cont.)`. See [`SCOPE.md`](SCOPE.md) for syllabus/extension boundaries, [`SOURCE-AUDIT.md`](SOURCE-AUDIT.md) for source and convention notes, and [`PRINTING.txt`](PRINTING.txt) for A4 **Fit** printing instructions.

Body and heading handwriting uses **Kalam** with DejaVu fallback; mathematics uses matplotlib mathtext. Fonts and their libre licences are in `../_assets/fonts/` and the shared asset documentation.

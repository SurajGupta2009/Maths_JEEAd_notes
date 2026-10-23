# Chapter 11 — Probability & Statistics

Handwritten-style, teacher-style explanatory notes generated from editable Markdown. This expanded edition includes a dedicated visual-methods lesson and uses one continuous top-to-bottom reading stream on every sheet.

## Current edition

- **Part I — JEE Main + Advanced:** 15 sheets across 9 source lessons in `JEE/`.
- **Part II — Olympiad / extensions:** 4 sheets across 3 source lessons in `Olympiad/`.
- **Visual expansion:** `jee-90-visual-methods.md` adds 5 editable figures; the chapter has 5 diagram blocks in total.
- **Page geometry:** 2480×3508 px A4 portrait PNGs at nominal 300 DPI, with ink kept inside the safe margins.

## Downloads

| Artifact | File |
|---|---|
| Combined PNG ZIP (JEE first) | [`exports/11-probability-and-statistics-combined-sheets.zip`](exports/11-probability-and-statistics-combined-sheets.zip) |
| JEE PNG ZIP | [`exports/11-probability-and-statistics-JEE-sheets.zip`](exports/11-probability-and-statistics-JEE-sheets.zip) |
| Olympiad PNG ZIP | [`exports/11-probability-and-statistics-Olympiad-sheets.zip`](exports/11-probability-and-statistics-Olympiad-sheets.zip) |
| Combined bookmarked PDF (JEE first) | [`exports/11-probability-and-statistics-combined.pdf`](exports/11-probability-and-statistics-combined.pdf) |
| JEE bookmarked PDF | [`exports/11-probability-and-statistics-JEE.pdf`](exports/11-probability-and-statistics-JEE.pdf) |
| Olympiad bookmarked PDF | [`exports/11-probability-and-statistics-Olympiad-extensions.pdf`](exports/11-probability-and-statistics-Olympiad-extensions.pdf) |
| Browser gallery | [`index.html`](index.html) |

## Source lessons and page ranges

### Part I — JEE

- `jee-01.md` — Probability Foundations — Spaces, Events, Complements (**JEE 1**).
- `jee-02.md` — Addition Rule, Counting, Conditional Probability (**JEE 2–3**).
- `jee-03.md` — Independence, Total Probability, Bayes (**JEE 4**).
- `jee-04.md` — Random Variables — Mean and Variance (**JEE 5**).
- `jee-05.md` — Binomial and Geometric Models (**JEE 6**).
- `jee-06.md` — Descriptive Statistics I — Centre & Deviation (**JEE 7–8**).
- `jee-07.md` — Descriptive Statistics II — Spread & Grouping (**JEE 9–10**).
- `jee-08.md` — Probability and Statistics — Mixed Strategy, Assumptions (**JEE 11**).
- `jee-90-visual-methods.md` — Visual Probability and Statistics Lab — Trees, Distributions and Spread (**JEE 12–15**).

### Part II — Olympiad / extensions

- `olympiad-01.md` — Geometric Probability, Ballot, Birthday (**Olympiad 1**).
- `olympiad-02.md` — Recursions, Memorylessness, Coupon Collector (**Olympiad 2**).
- `olympiad-03.md` — Gambler's Ruin, Derangements, Averaging (**Olympiad 3–4**).

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

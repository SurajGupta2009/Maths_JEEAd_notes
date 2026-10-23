# Chapter 9 — Binomial Theorem

Handwritten-style, teacher-style explanatory notes generated from editable Markdown. This expanded edition includes a dedicated visual-methods lesson and uses one continuous top-to-bottom reading stream on every sheet.

## Current edition

- **Part I — JEE Main + Advanced:** 11 sheets across 5 source lessons in `JEE/`.
- **Part II — Olympiad / extensions:** 3 sheets across 2 source lessons in `Olympiad/`.
- **Visual expansion:** `jee-90-visual-methods.md` adds 5 editable figures; the chapter has 5 diagram blocks in total.
- **Page geometry:** 2480×3508 px A4 portrait PNGs at nominal 300 DPI, with ink kept inside the safe margins.

## Downloads

| Artifact | File |
|---|---|
| Combined PNG ZIP (JEE first) | [`exports/09-binomial-theorem-combined-sheets.zip`](exports/09-binomial-theorem-combined-sheets.zip) |
| JEE PNG ZIP | [`exports/09-binomial-theorem-JEE-sheets.zip`](exports/09-binomial-theorem-JEE-sheets.zip) |
| Olympiad PNG ZIP | [`exports/09-binomial-theorem-Olympiad-sheets.zip`](exports/09-binomial-theorem-Olympiad-sheets.zip) |
| Combined bookmarked PDF (JEE first) | [`exports/09-binomial-theorem-combined.pdf`](exports/09-binomial-theorem-combined.pdf) |
| JEE bookmarked PDF | [`exports/09-binomial-theorem-JEE.pdf`](exports/09-binomial-theorem-JEE.pdf) |
| Olympiad bookmarked PDF | [`exports/09-binomial-theorem-Olympiad-extensions.pdf`](exports/09-binomial-theorem-Olympiad-extensions.pdf) |
| Browser gallery | [`index.html`](index.html) |

## Source lessons and page ranges

### Part I — JEE

- `jee-01.md` — Binomial Theorem — What (a+b)ⁿ Counts, the General Term, Middle Terms (**JEE 1–2**).
- `jee-02.md` — Coefficient Machinery — Multinomials, Counting Terms, Greatest Coefficients (**JEE 3**).
- `jee-03.md` — Three Identity Engines — Substitution, Calculus, and Coefficient Extraction (**JEE 4**).
- `jee-04.md` — Greatest Terms, Truncation Inequalities, and the Binomial as a Sieve (**JEE 5–6**).
- `jee-90-visual-methods.md` — Visual Binomial Lab — Pascal Rows, Term Tracking and Greatest Terms (**JEE 7–11**).

### Part II — Olympiad / extensions

- `olympiad-01.md` — Extension — The General Binomial Series: Negative and Fractional Indices, Validity, Approximation (**Olympiad 1–2**).
- `olympiad-02.md` — Extension — Divisibility, Prime Rows, Lucas, and Finite Differences (**Olympiad 3**).

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

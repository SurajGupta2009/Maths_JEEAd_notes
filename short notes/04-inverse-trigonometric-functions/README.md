# Chapter 4 — Inverse Trigonometric Functions

Handwritten-style, teacher-style explanatory notes generated from editable Markdown. This expanded edition includes a dedicated visual-methods lesson and uses one continuous top-to-bottom reading stream on every sheet.

## Current edition

- **Part I — JEE Main + Advanced:** 28 sheets across 7 source lessons in `JEE/`.
- **Part II — Olympiad / extensions:** 9 sheets across 3 source lessons in `Olympiad/`.
- **Visual expansion:** `jee-90-visual-methods.md` adds 5 editable figures; the chapter has 11 diagram blocks in total.
- **Page geometry:** 2480×3508 px A4 portrait PNGs at nominal 300 DPI, with ink kept inside the safe margins.

## Downloads

| Artifact | File |
|---|---|
| Combined PNG ZIP (JEE first) | [`exports/04-inverse-trigonometric-functions-combined-sheets.zip`](exports/04-inverse-trigonometric-functions-combined-sheets.zip) |
| JEE PNG ZIP | [`exports/04-inverse-trigonometric-functions-JEE-sheets.zip`](exports/04-inverse-trigonometric-functions-JEE-sheets.zip) |
| Olympiad PNG ZIP | [`exports/04-inverse-trigonometric-functions-Olympiad-sheets.zip`](exports/04-inverse-trigonometric-functions-Olympiad-sheets.zip) |
| Combined bookmarked PDF (JEE first) | [`exports/04-inverse-trigonometric-functions-combined.pdf`](exports/04-inverse-trigonometric-functions-combined.pdf) |
| JEE bookmarked PDF | [`exports/04-inverse-trigonometric-functions-JEE.pdf`](exports/04-inverse-trigonometric-functions-JEE.pdf) |
| Olympiad bookmarked PDF | [`exports/04-inverse-trigonometric-functions-Olympiad-extensions.pdf`](exports/04-inverse-trigonometric-functions-Olympiad-extensions.pdf) |
| Browser gallery | [`index.html`](index.html) |

## Source lessons and page ranges

### Part I — JEE

- `jee-01.md` — Inverse Trigonometric Functions — Why Branches, the Six Principal Inverses (**JEE 1–4**).
- `jee-02.md` — sin⁻¹(sin x) and Companions — Reading Angles Off the Branch (**JEE 5–8**).
- `jee-03.md` — tan⁻¹ Addition Formulas — With Their Branch Conditions (**JEE 9–12**).
- `jee-04.md` — sin⁻¹ and cos⁻¹ Addition Formulas + the Simplification Toolkit (**JEE 13–15**).
- `jee-05.md` — Equations, Inequalities and Parameters — Domain First, Injectivity Second (**JEE 16–18**).
- `jee-06.md` — Recap Toolkit — Every Formula of the Chapter on One Page (**JEE 19–22**).
- `jee-90-visual-methods.md` — Visual Inverse-Trigonometry Lab — Branches, Graphs and Safe Identities (**JEE 23–28**).

### Part II — Olympiad / extensions

- `olympiad-01.md` — Extension — Piecewise Masters: f(x) = sin⁻¹(sin x) + cos⁻¹(cos x) and Siblings (**Olympiad 1–3**).
- `olympiad-02.md` — Extension — Telescoping Arctan Series and Sums (**Olympiad 4–6**).
- `olympiad-03.md` — Extension — Hidden-Structure Identities and Constraint Problems (**Olympiad 7–9**).

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

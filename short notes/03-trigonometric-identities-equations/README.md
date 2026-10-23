# Chapter 3 — Trigonometric Identities & Equations (handwritten-style short notes)

Handwritten-style, teacher-style explanatory notes generated from editable Markdown. This expanded edition includes a dedicated visual-methods lesson and uses one continuous top-to-bottom reading stream on every sheet.

## Current edition

- **Part I — JEE Main + Advanced:** 23 sheets across 10 source lessons in `JEE/`.
- **Part II — Olympiad / extensions:** 8 sheets across 4 source lessons in `Olympiad/`.
- **Visual expansion:** `jee-90-visual-methods.md` adds 4 editable figures; the chapter has 9 diagram blocks in total.
- **Page geometry:** 2480×3508 px A4 portrait PNGs at nominal 300 DPI, with ink kept inside the safe margins.

## Downloads

| Artifact | File |
|---|---|
| Combined PNG ZIP (JEE first) | [`exports/03-trigonometric-identities-equations-combined-sheets.zip`](exports/03-trigonometric-identities-equations-combined-sheets.zip) |
| JEE PNG ZIP | [`exports/03-trigonometric-identities-equations-JEE-sheets.zip`](exports/03-trigonometric-identities-equations-JEE-sheets.zip) |
| Olympiad PNG ZIP | [`exports/03-trigonometric-identities-equations-Olympiad-sheets.zip`](exports/03-trigonometric-identities-equations-Olympiad-sheets.zip) |
| Combined bookmarked PDF (JEE first) | [`exports/03-trigonometric-identities-equations-combined.pdf`](exports/03-trigonometric-identities-equations-combined.pdf) |
| JEE bookmarked PDF | [`exports/03-trigonometric-identities-equations-JEE.pdf`](exports/03-trigonometric-identities-equations-JEE.pdf) |
| Olympiad bookmarked PDF | [`exports/03-trigonometric-identities-equations-Olympiad-extensions.pdf`](exports/03-trigonometric-identities-equations-Olympiad-extensions.pdf) |
| Browser gallery | [`index.html`](index.html) |

## Source lessons and page ranges

### Part I — JEE

- `jee-01.md` — Trigonometry — Ratios, the Unit Circle, Fundamental Identities (**JEE 1–2**).
- `jee-02.md` — Signs by Quadrant, Allied Angles, Standard Values (**JEE 3–5**).
- `jee-03.md` — Compound Angles — the Four Formulae and How to Own Them (**JEE 6–7**).
- `jee-04.md` — Multiple & Submultiple Angles — Double, Triple, Half, Power Reduction (**JEE 8–9**).
- `jee-05.md` — Transformation Formulae — Products ↔ Sums (**JEE 10–11**).
- `jee-06.md` — Trigonometric Equations I — Principal and General Solutions (**JEE 12–13**).
- `jee-07.md` — Trigonometric Equations II — Factorise, Combine, Filter (**JEE 14–15**).
- `jee-08.md` — Conditional Identities — When $A + B + C = \pi$ (**JEE 16–17**).
- `jee-09.md` — Chapter Recap — Identities & Equations Toolkit (**JEE 18–19**).
- `jee-90-visual-methods.md` — Visual Trigonometry Lab — Unit Circle, Graphs and General Solutions (**JEE 20–23**).

### Part II — Olympiad / extensions

- `olympiad-01.md` — Olympiad Extensions — the Weierstrass Substitution (**Olympiad 1–2**).
- `olympiad-02.md` — Olympiad Extensions — Products of Sines & Cosines from Roots of Unity (**Olympiad 3–4**).
- `olympiad-03.md` — Olympiad Extensions — Trig Series (Telescoping) and Square Sums (**Olympiad 5–6**).
- `olympiad-04.md` — Specialised Toolkit — Triangle Formulae & Derived Special Values (**Olympiad 7–8**).

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

# Chapter 14 — Conic Sections

Handwritten-style, teacher-style explanatory notes generated from editable Markdown. The chapter covers parabola, ellipse and hyperbola in one continuous top-to-bottom reading stream, with exact worked examples and a dedicated visual conic lab.

## Current edition

- **Part I — JEE Main + Advanced:** 29 sheets across 10 source lessons in `JEE/`.
- **Part II — Olympiad / extensions:** 6 sheets across 3 source lessons in `Olympiad/`.
- **Total:** 35 A4 sheets and 20 editable diagram blocks.
- **Visual expansion:** `jee-90-visual-methods.md` adds 6 figures on focal chords, auxiliary-circle squashing, exact ellipse focal segments, asymptote-parallel intersections, pole–polar incidence and problem selection.
- **Mathematical verification:** 233 exact/rational, numerical and editable-figure assertions in `scripts/math_checks.py`.
- **Page geometry:** 2480×3508 px A4 portrait PNGs at nominal 300 DPI, with ink kept inside the safe margins.

## Downloads

| Artifact | File |
|---|---|
| Combined PNG ZIP (JEE first) | [`exports/14-conic-sections-combined-sheets.zip`](exports/14-conic-sections-combined-sheets.zip) |
| JEE PNG ZIP | [`exports/14-conic-sections-JEE-sheets.zip`](exports/14-conic-sections-JEE-sheets.zip) |
| Olympiad PNG ZIP | [`exports/14-conic-sections-Olympiad-sheets.zip`](exports/14-conic-sections-Olympiad-sheets.zip) |
| Combined bookmarked PDF (JEE first) | [`exports/14-conic-sections-combined.pdf`](exports/14-conic-sections-combined.pdf) |
| JEE bookmarked PDF | [`exports/14-conic-sections-JEE.pdf`](exports/14-conic-sections-JEE.pdf) |
| Olympiad bookmarked PDF | [`exports/14-conic-sections-Olympiad-extensions.pdf`](exports/14-conic-sections-Olympiad-extensions.pdf) |
| Browser gallery | [`index.html`](index.html) |

## Source lessons and page ranges

### Part I — JEE

- `jee-01.md` — The Conic Family — Focus, Directrix and Eccentricity (**JEE 1–3**).
- `jee-02.md` — Parabola — Anatomy, Parameters and Focal Chords (**JEE 4–6**).
- `jee-03.md` — Parabola — Tangents, Normals and Reflection (**JEE 7–9**).
- `jee-04.md` — Ellipse — Focal Geometry and the Eccentric Angle (**JEE 10–11**).
- `jee-05.md` — Ellipse — Tangents, Focal Chords and Director Circle (**JEE 12–14**).
- `jee-06.md` — Hyperbola — Branches, Asymptotes and Conjugate (**JEE 15–17**).
- `jee-07.md` — Hyperbola — Tangents, Normals and the Rectangular Form (**JEE 18–19**).
- `jee-08.md` — The Unified Toolkit — Tangents, Contacts and Midpoint Chords (**JEE 20–21**).
- `jee-09.md` — Pole, Polar and Mixed Conic Strategy (**JEE 22–23**).
- `jee-90-visual-methods.md` — Visual Conic Lab (**JEE 24–29**).

### Part II — Olympiad / extensions

- `olympiad-01.md` — Reflection Properties and Confocal Conics (**Olympiad 1–2**).
- `olympiad-02.md` — Rectangular Hyperbola and Triangle Geometry (**Olympiad 3–4**).
- `olympiad-03.md` — The General Second-Degree Conic (**Olympiad 5–6**).

## Editable sources and visual builders

Every sheet is authored in `content/*.md` using frontmatter, prose, display mathematics, callout boxes, JSON diagram specifications, and optional `<!-- pagebreak -->` markers. Lessons start on fresh sheets; long lessons continue automatically without shrinking or clipping prose. Figures remain editable in the source rather than being external screenshots. The shared geometry builder supports parabolas, ellipses, hyperbolas, rectangular hyperbolas and standalone labels in addition to the existing diagram types.

## Reproducible build and verification

```bash
python3 -m pip install -r ../_engine/requirements.txt  # once
python3 scripts/render.py       # Markdown -> PNG sheets + manifest.json
python3 scripts/export.py       # 3 ZIPs + 3 bookmarked PDFs + gallery
python3 scripts/math_checks.py  # 233 independent mathematical checks
python3 scripts/check.py        # formula, font, PNG, manifest, export and link gates
```

The mathematical suite checks standard forms, parameters, focal distances, chord and tangent equations, normal cubics, director circles, exact focal chords, midpoint root sums, pole–polar incidence, confocal orthogonality, the rectangular-hyperbola orthocentre, and general-conic invariants. It includes the visual lab and an opposite-branch hyperbola countercheck. These targeted checks supplement—not replace—proofs and visual review.

The delivery suite checks formula parsing, glyph fallback, A4 dimensions and DPI, complete safe-border ink scans, running-header fit, manifest ordering, ZIP integrity, PDF page counts and bookmarks, documentation, and local gallery links.

## Reading order, scope and printing

Follow the `LESSON n / total` ribbons and read straight down each sheet, then continue on the next sheet. Continuation sheets retain the lesson title and add `(cont.)`. See [`SCOPE.md`](SCOPE.md) for syllabus/extension boundaries, [`SOURCE-AUDIT.md`](SOURCE-AUDIT.md) for source and convention notes, and [`PRINTING.txt`](PRINTING.txt) for A4 **Fit** printing instructions.

Body and heading handwriting uses **Kalam** with DejaVu fallback; mathematics uses matplotlib mathtext. Fonts and their libre licences are in `../_assets/fonts/` and the shared asset documentation.

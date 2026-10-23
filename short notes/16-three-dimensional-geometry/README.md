# Chapter 16 — Three-Dimensional Geometry

Handwritten-style, teacher-style explanatory notes generated from editable Markdown. The chapter covers coordinates and direction in space, lines, planes, angles, distances, feet and reflections in one continuous top-to-bottom reading stream, with exact worked examples and a dedicated visual 3D geometry lab.

## Current edition

- **Part I — JEE Main + Advanced:** 25 sheets across 10 source lessons in `JEE/`.
- **Part II — Olympiad / extensions:** 13 sheets across 5 source lessons in `Olympiad/`.
- **Total:** 38 A4 sheets and 22 editable diagram blocks, including 19 configurable 3D figures.
- **Visual expansion:** `jee-90-visual-methods.md` adds 6 sheets with five exact 3D constructions, a problem-selection workflow and a formula-selection table.
- **Mathematical verification:** 200 exact/rational, numerical, visual-lab and editable-figure assertions in `scripts/math_checks.py`.
- **Page geometry:** 2480×3508 px A4 portrait PNGs at nominal 300 DPI, with ink kept inside the safe margins.

## Downloads

| Artifact | File |
|---|---|
| Combined PNG ZIP (JEE first) | [`exports/16-three-dimensional-geometry-combined-sheets.zip`](exports/16-three-dimensional-geometry-combined-sheets.zip) |
| JEE PNG ZIP | [`exports/16-three-dimensional-geometry-JEE-sheets.zip`](exports/16-three-dimensional-geometry-JEE-sheets.zip) |
| Olympiad PNG ZIP | [`exports/16-three-dimensional-geometry-Olympiad-sheets.zip`](exports/16-three-dimensional-geometry-Olympiad-sheets.zip) |
| Combined bookmarked PDF (JEE first) | [`exports/16-three-dimensional-geometry-combined.pdf`](exports/16-three-dimensional-geometry-combined.pdf) |
| JEE bookmarked PDF | [`exports/16-three-dimensional-geometry-JEE.pdf`](exports/16-three-dimensional-geometry-JEE.pdf) |
| Olympiad bookmarked PDF | [`exports/16-three-dimensional-geometry-Olympiad-extensions.pdf`](exports/16-three-dimensional-geometry-Olympiad-extensions.pdf) |
| Browser gallery | [`index.html`](index.html) |

## Source lessons and page ranges

### Part I — JEE

- `jee-01.md` — Coordinates and Direction in Space (**JEE 1–2**).
- `jee-02.md` — Lines in Space — Vector and Cartesian Forms (**JEE 3–5**).
- `jee-03.md` — Line Relationships — Angles, Intersection and Coplanarity (**JEE 6–7**).
- `jee-04.md` — Foot, Image and Distance to a Line (**JEE 8–9**).
- `jee-05.md` — Skew Lines and the Common Perpendicular (**JEE 10–11**).
- `jee-06.md` — Planes — Normal, Intercept and Three-Point Forms (**JEE 12–13**).
- `jee-07.md` — Angles Between Lines and Planes (**JEE 14–15**).
- `jee-08.md` — Plane Distances, Feet and Reflections (**JEE 16–17**).
- `jee-09.md` — Pencils, Bisector Planes and Mixed Strategy (**JEE 18–19**).
- `jee-90-visual-methods.md` — Visual 3D Geometry Lab (**JEE 20–25**).

### Part II — Olympiad / extensions

- `olympiad-01.md` — Extension I — Sphere Foundations (**Olympiad 1–3**).
- `olympiad-02.md` — Extension II — Sphere Sections and Tangent Planes (**Olympiad 4–5**).
- `olympiad-03.md` — Extension III — Radical Planes, Polars and Orthogonality (**Olympiad 6–8**).
- `olympiad-04.md` — Extension IV — Inspheres and the Monge Point (**Olympiad 9–11**).
- `olympiad-05.md` — Extension V — Spherical Geometry & Tetrahedra (**Olympiad 12–13**).

## Editable sources and visual builders

Every sheet is authored in `content/*.md` using frontmatter, prose, display mathematics, callout boxes, JSON diagram specifications, and optional `<!-- pagebreak -->` markers. Lessons start on fresh sheets; long lessons continue automatically without shrinking or clipping prose. Figures remain editable in the source rather than being external screenshots.

In addition to the shared geometry, table and flow builders, the registered `vector3d` builder supports labelled arrows, points, segments, polygons, parallelepipeds, plane patches, spheres and circles/arcs in 3D. Axis ranges, view angles, basis vectors, transparency and viewport zoom remain configurable. The mathematical suite reads the actual JSON figures and checks selected coordinates, plane incidence, sphere distances, circle bases and rounded geometric data.

## Reproducible build and verification

```bash
python3 -m pip install -r ../_engine/requirements.txt  # once
python3 scripts/render.py       # Markdown -> PNG sheets + manifest.json
python3 scripts/export.py       # 3 ZIPs + 3 bookmarked PDFs + gallery
python3 scripts/math_checks.py  # 200 independent mathematical/figure checks
python3 scripts/check.py        # formula, font, PNG, manifest, export and link gates
```

The mathematical suite checks direction cosines, projections, every printed line/plane example, coplanarity, both skew-line feet, distances and reflections, pencils and bisectors, sphere equations and sections, radical/polar constructions, the tangent cone, the insphere, all six Monge midplanes, regular-tetrahedron measurements and spherical excess. It also tests the editable figure inventory and the six-page visual lab. These checks supplement—not replace—proofs and native-size visual review.

The delivery suite checks formula parsing, glyph fallback, A4 dimensions and DPI, complete safe-border ink scans, running-header fit, manifest ordering, ZIP integrity, PDF page counts and bookmarks, documentation, and local gallery links.

## Reading order, scope and printing

Follow the `LESSON n / total` ribbons and read straight down each sheet, then continue on the next sheet. Continuation sheets retain the lesson title and add `(cont.)`. See [`SCOPE.md`](SCOPE.md) for the official/extension boundaries, [`SOURCE-AUDIT.md`](SOURCE-AUDIT.md) for source corrections and convention notes, and [`PRINTING.txt`](PRINTING.txt) for A4 **Fit** printing instructions.

Body and heading handwriting uses **Kalam** with DejaVu fallback; mathematics uses matplotlib mathtext. Fonts and their libre licences are in `../_assets/fonts/` and the shared asset documentation.

---
title: "Diagrams — SVG + Mermaid Catalog"
aliases: ["Diagrams", "Figures"]
module: "docs"
type: catalog
tags: [diagrams, svg, mermaid]
created: 2026-09-27
---

# Diagrams — SVG + Mermaid Catalog

> Every diagram lives as an SVG in the module's `notes/<Module>/assets/fig-XX.svg`
> and is augmented with a Mermaid flowchart for native GitHub/Obsidian rendering.

**Inventory: 18 modules · 43 SVG figures · 27 Mermaid flowcharts.** Every SVG on
disk is referenced by at least one note, and every image link resolves — both
facts are enforced by `python3 tools/verify-md.py`.

| Module | SVG figures | Mermaid |
|---|---|---|
| PnC | 11 | 12 |
| Complex Numbers | 4 | 3 |
| Conic Sections | 1 | 6 |
| Applications of Derivatives | 2 | 2 |
| Binomial Theorem | 1 | 3 |
| Differential Equations | 2 | 1 |
| 3D-Geometry | 2 | 0 |
| Coordinate Geometry — Lines & Circles | 2 | 0 |
| Differentiation & Methods | 1 | 0 |
| Inequalities | 2 | 0 |
| Integration | 2 | 0 |
| Limits & Continuity | 1 | 0 |
| Matrices & Determinants | 2 | 0 |
| Probability | 2 | 0 |
| Quadratic Equations | 2 | 0 |
| Sequences & Series | 2 | 0 |
| Trigonometry | 2 | 0 |
| Vectors | 2 | 0 |
| **Total** | **43** | **27** |

---

## PnC — Permutations & Combinations

**SVG** (11): `fig-01` product-rule tree · `fig-02` decision tree · `fig-03`
circular permutations · `fig-04` Pascal's triangle · `fig-05` hockey stick ·
`fig-06` stars and bars · `fig-07` two-set inclusion–exclusion Venn ·
`fig-08` pigeonhole · `fig-09` domino tiling, two cases · `fig-10` reflection
principle on a grid · `fig-11` Young-diagram conjugation.

**Mermaid** (12): product rule · circular permutations · Pascal & hockey stick ·
stars and bars · lattice paths & reflection · Young diagrams · Burnside necklace
counting · inclusion–exclusion sieve · plus the generating-function, Catalan and
cycle-lemma flowcharts.

---

## Complex Numbers

**SVG** (4): `fig-01` complex plane loci · `fig-02` $z=a+bi \leftrightarrow (a,b)$ ·
`fig-03` multiplication by $i$ = $90°$ rotation · `fig-04` fourth roots of 16 as a
square on the circle of radius 2.

**Mermaid** (3): complex plane loci · multiplication as rotation · roots of unity
as a regular $n$-gon.

---

## Conic Sections

**SVG** (1): `fig-01` the conic family from focus–directrix eccentricity.

**Mermaid** (6): conic family by $e$ · parabola anatomy · ellipse as squashed
circle · hyperbola asymptotes · unified $S=0$ conic · parabola reflection.

---

## Applications of Derivatives

**SVG** (2): `fig-01` related-rates chain · `fig-02` curve sketching.

**Mermaid** (2): word problem → rates chain · domain + intercepts → sketch.

---

## Binomial Theorem

**SVG** (1): `fig-01` $(a+b)^3$ expansion.

**Mermaid** (3): pick-lists census · substitution engines $f(x)=(1+x)^n$ ·
negative binomial $(1-x)^{-k}=\sum\binom{n+k-1}{k-1}x^n$.

---

## Differential Equations

**SVG** (2): `fig-01` slope field · `fig-02` solution family.

**Mermaid** (1): variables separable $y'=f(x)g(y)$.

---

## The remaining twelve modules

Each carries two SVG figures (`fig-01`, `fig-02`) drawn from its core machinery:

| Module | Figures |
|---|---|
| 3D-Geometry | coordinate axes in space; the plane from point + normal |
| Coordinate Geometry — Lines & Circles | locus/distance; the circle and its chord geometry |
| Differentiation & Methods | the derivative as a limit of secants; the chain rule |
| Inequalities | the wavy curve; the mean family on a number line |
| Integration | Riemann sums → the definite integral; area under a curve |
| Limits & Continuity | the $\varepsilon$-$\delta$ neighbourhood; continuity at a point |
| Matrices & Determinants | matrix multiplication; the cofactor expansion |
| Probability | the sample space; Bayes' tree |
| Quadratic Equations | the parabola and the discriminant; location of roots |
| Sequences & Series | partial sums; the AGP telescoping |
| Trigonometry | the unit circle; compound-angle construction |
| Vectors | the two products; the line and the plane |

---

## How Diagrams Are Used in Markdown

1. **SVG** — Exact figure from HTML, preserved for offline use:
   ```md
   ![Fig 1.1 — Product rule tree](assets/fig-02.svg)
   ```

2. **Mermaid** — Added for GitHub native rendering, same concept but interactive:
   ````md
   ```mermaid
   flowchart TD
       Start --> Red
   ```
   ````

3. **Both** — Every major concept has SVG + Mermaid, so notes work offline (SVG) and online (Mermaid) — dual redundancy.

---

## Maintaining this catalog

When you add or remove a figure, update this table. `python3 tools/verify-md.py`
already fails the build if an image link does not resolve, so the catalog can
never drift from the notes without CI noticing — but it will not notice a figure
that exists on disk yet is never referenced. To find those:

```bash
python3 - <<'EOF'
import io, glob, os
for d in sorted(glob.glob("notes/*")):
    if not os.path.isdir(d):
        continue
    ad = os.path.join(d, "assets")
    if not os.path.isdir(ad):
        continue
    body = "".join(io.open(os.path.join(d, f), encoding="utf-8").read()
                   for f in os.listdir(d) if f.endswith(".md"))
    for f in sorted(os.listdir(ad)):
        if f.endswith(".svg") and f not in body:
            print("ORPHAN", os.path.basename(d), f)
EOF
```

Thirteen byte-identical duplicate figures (PnC `fig-12`…`fig-21`, Complex-Numbers
`fig-05`…`fig-07`) were removed on that basis — each was an exact copy of a
figure that was already referenced.

---

*All figures are stored as `notes/<Module>/assets/fig-XX.svg`; see [FORMATTING-GUIDE.md](FORMATTING-GUIDE.md) for how they are referenced.*

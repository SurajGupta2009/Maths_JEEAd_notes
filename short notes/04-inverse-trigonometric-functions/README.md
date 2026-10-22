# Chapter 4 — Inverse Trigonometric Functions

Handwritten-style revision sheets for JEE Advanced, built from `content/*.md`
by the shared `_engine` renderer (`scripts/render.py`).

## Layout

- **Part I — JEE (Main + Advanced): `JEE/`** — 13 sheets.
  Motivation and the six principal values; graphs with domains and ranges;
  standard values; the composition formulas (`sin⁻¹(sin x)` and companions,
  `2tan⁻¹x` in all three faces) with their piecewise branch conditions;
  trig-of-an-inverse expressions; the `tan⁻¹` addition formulas *with case
  conditions*; the `sin⁻¹`/`cos⁻¹` addition formulas derived from the addition
  laws; a worked canonical set (identities, equations, extrema, piecewise
  functions, `tan⁻¹x = cos⁻¹x`); equations/inequalities/parameters solved
  domain-first; a full recap toolkit; and the forward map to where the toolkit
  reappears (calculus, complex numbers, coordinate geometry).
- **Part II — Olympiad extensions: `Olympiad/`** — 6 sheets.
  The complete piecewise master `f(x) = sin⁻¹(sin x) + cos⁻¹(cos x)` (with
  arcs/triangles/peaks construction and range 0 to π); telescoping arctan
  series (three standard splits, limits, products, closed forms); and the
  hidden-structure identities (`x+y+z = xyz ⇒ sum = π`, `xy+yz+zx = 1 ⇒ sum = π/2`)
  with proofs, degenerate-face analysis, min-max under constraints, and
  parameterised equations.

Every sheet carries its part label (JEE PART I / OLYMPIAD PART II) and page
number in the footer. Coverage sets the page count — nothing was trimmed to
hit a target.

## Files

| Path | What |
|---|---|
| `content/*.md` | editable source (9 files) |
| `scripts/render.py` | PNG renderer (wrapper over `_engine`) |
| `scripts/export.py` | ZIP + PDF export |
| `scripts/check.py` | reproducible checks (geometry, glyphs, footers) |
| `scripts/math_checks.py` | numeric verification of every exact claim |
| `exports/` | the deliverables (3 ZIPs + 3 PDFs) |
| `index.html` | gallery (combined, then Part I, then Part II) |
| `SCOPE.md` | what is in/out and why |
| `SOURCE-AUDIT.md` | source review, corrections, assumptions |
| `PRINTING.txt` | print instructions |

## Rebuild

```bash
python3 scripts/render.py && python3 scripts/export.py && python3 scripts/check.py
python3 scripts/math_checks.py
```

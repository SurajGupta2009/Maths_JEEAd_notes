# Chapter 5 — Complex Numbers and Quadratic Equations (Complex Numbers strand)

Handwritten-style revision sheets for JEE Advanced, built from `content/*.md`
by the shared `_engine` renderer (`scripts/render.py`).

## Layout

- **Part I — JEE (Main + Advanced): `JEE/`** — 18 sheets.
  Why `i` exists and what it forces; conjugate/division/field facts; `z` and
  `z̄` as two coordinates; modulus and argument (all four quadrant
  conventions, the |Arg| ≤ π convention); the two languages (polar =
  stretch × rotate) and De Moivre/Euler; n-th roots (exactly n, regular
  polygons, the ± square-root formula); the ω toolkit, vanishing sums and
  roots-of-unity filters; the products `∏(1−ζₖ) = n` and `∏sin(πk/n)`;
  loci (circles, disks and their ranges, arcs and ellipses from argument
  conditions); equations in `z` and `z̄`; optimization (triangle inequality
  with equality conditions, chords, ranges); a recap toolkit.
- **Part II — Olympiad extensions: `Olympiad/`** — 11 sheets.
  The rotation engine (equilateral condition and tests, areas,
  circumcenters, the 4-unit-sum-0 rectangle fact); Ptolemy from one complex
  identity plus distance theorems by expansion (British flag, Van Aubel,
  Napoleon); Leibniz sums; unit-circle configurations (`z̄ = 1/z`);
  the Joukowski map `w = z + 1/z`; the quadratic Gauss sum `G(n)` with its
  closed form and evaluation mechanism; Gauss–Lucas and Marden's theorem
  (with worked critical points); Pompeiu's theorem.

Every sheet carries its part label (JEE PART I / OLYMPIAD PART II) and page
number in the footer. Coverage sets the page count — nothing was trimmed to
hit a target.

## Files

| Path | What |
|---|---|
| `content/*.md` | editable source (17 files) |
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

# Chapter 7 — Sequences & Series

Handwritten-style revision sheets for JEE Advanced, built from `content/*.md`
by the shared `_engine` renderer (`scripts/render.py`).

## Layout

- **Part I — JEE (Main + Advanced): `JEE/`** — 5 sheets.
  Arithmetic progressions (formulas derived by pairing, symmetric
  parametrisations, means); geometric progressions (shift-and-subtract
  proof, finite and infinite sums, means); AM–GM with attainable-equality
  discipline and the syllabus power sums $\sum k$, $\sum k^{2}$, $\sum k^{3}$
  (derived by telescoping $(k+1)^{m+1} - k^{m+1}$); the two summation
  engines — AGP shift-and-subtract and the method of differences — labelled
  as derivable applications of the GP formula; mixed problem shapes and
  the recap toolkit.
- **Part II — Olympiad extensions: `Olympiad/`** — 3 sheets.
  Harmonic progressions and $A \geq G \geq H$ with $G^{2} = AH$ (HP is not
  in the official JEE Advanced syllabus — flagged as such); recurrences,
  characteristic equations and generating functions (Fibonacci $F(x)$ to
  Binet); telescoping products, Wallis's product, Stolz–Cesàro, and
  asymptotics ($a_{n+1} = a_{n} + 1/a_{n} \sim \sqrt{2n}$).

Every sheet carries its part label and page number in the footer. Coverage
sets the page count — nothing was trimmed to hit a target.

## Files

| Path | What |
|---|---|
| `content/*.md` | editable source (8 files) |
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

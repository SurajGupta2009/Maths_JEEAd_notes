# Chapter 6 — Quadratic Equations

Handwritten-style revision sheets for JEE Advanced, built from `content/*.md`
by the shared `_engine` renderer (`scripts/render.py`).

## Layout

- **Part I — JEE (Main + Advanced): `JEE/`** — 8 sheets.
  The discriminant and quadratic formula (derived by completing the square);
  rational/irrational/conjugate root pairs; Vieta's relations and the full
  symmetric-function toolkit; the quadratic expression (vertex, sign, range,
  always-positive conditions); location of roots (the three-ingredient
  toolkit: D, a·f(k), vertex); equations reducible to quadratics
  (substitution + admissibility + verification); common roots and
  transformed equations; parameter problem shapes, the discriminant method
  for ranges, recap and the ten-mistake checklist.
- **Part II — Olympiad extensions: `Olympiad/`** — 3 sheets.
  Newton's power sums and the Fibonacci–Lucas machine from $x^{2}-x-1$;
  the discriminant as $a^{2}(\alpha-\beta)^{2}$, rational-root criteria, and
  Lagrange's resolvent (cubics solved by quadratics); Vieta jumping with
  IMO 1988/6.

Every sheet carries its part label and page number in the footer. Coverage
sets the page count — nothing was trimmed to hit a target.

## Files

| Path | What |
|---|---|
| `content/*.md` | editable source (10 files) |
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

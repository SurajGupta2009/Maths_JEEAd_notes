# Chapter 9 — Binomial Theorem

Handwritten-style revision sheets for JEE Advanced, built from `content/*.md`
by the shared `_engine` renderer (`scripts/render.py`).

## Layout

- **Part I — JEE (Main + Advanced): `JEE/`** — 4 sheets.
  The theorem as a census of bracket choices; the general term
  $T_{k+1} = \binom{n}{k}a^{n-k}b^{k}$ and the exponent equation for
  coefficients/constant terms; middle terms and equal coefficients;
  multinomial coefficients and the number-of-terms trap; greatest
  coefficients and terms (ratio walk); three identity engines
  (substitution, calculus, coefficient extraction) with Vandermonde and
  hockey-stick; truncation inequalities (Bernoulli, $(1+1/n)^{n}$ between
  2 and 3); remainders/last digits and conjugate-surd integer parts.
- **Part II — Olympiad extensions: `Olympiad/`** — 2 sheets.
  The general binomial series for real index (negative/fractional indices,
  validity $\left|x\right| < 1$, factoring discipline, approximations with
  error budgets, series recognition); divisibility: prime rows, the
  Freshman's dream, Lucas's theorem, Kummer (statement), finite
  differences.

Every sheet carries its part label and page number in the footer. Coverage
sets the page count — nothing was trimmed to hit a target.

## Files

| Path | What |
|---|---|
| `content/*.md` | editable source (6 files) |
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

## Reading order

Follow the `LESSON n / total` ribbons; read down the left column, then down the right column, and continue to the next sheet. This sequence follows the chapter’s prerequisite path.

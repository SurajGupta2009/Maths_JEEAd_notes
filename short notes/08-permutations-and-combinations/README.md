# Chapter 8 — Permutations & Combinations

Handwritten-style revision sheets for JEE Advanced, built from `content/*.md`
by the shared `_engine` renderer (`scripts/render.py`).

## Layout

- **Part I — JEE (Main + Advanced): `JEE/`** — 7 sheets.
  Product/sum/complement rules with exact hypotheses and the bijection
  mindset; permutations $P(n,r)$, identical objects (label–count–divide with
  the exact-symmetry condition); circular permutations; bundle/gap/relative
  -order restriction methods; combinations, Pascal, hockey-stick, restricted
  selections; stars and bars, compositions, multisets, bounded distributions;
  inclusion–exclusion and derangements; pigeonhole and recurrence counting;
  recap and checklist.
- **Part II — Olympiad extensions: `Olympiad/`** — 3 sheets.
  Lattice paths, reflection principle, Catalan numbers, ballot theorem;
  Burnside's lemma and necklace/bracelet enumeration; integer partitions
  (Euler distinct = odd, pentagonal recurrence), Stirling/Bell numbers,
  Sperner and Erdős–Ko–Rado.

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

## Reading order

Follow the `LESSON n / total` ribbons; read down the left column, then down the right column, and continue to the next sheet. This sequence follows the chapter’s prerequisite path.

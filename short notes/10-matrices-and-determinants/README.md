# Chapter 10 — Matrices & Determinants

Explanatory handwritten-style notes, generated from the editable sources in
`content/` with the shared renderer. **Part I (JEE): 4 sheets; Part II
(Olympiad extensions): 2 sheets.**

## Coverage

- **Part I — JEE Main + Advanced:** matrix order/operations and linear-map
  intuition; transpose and matrix families; determinants through order 3,
  cofactor signs and row operations; determinant identities and singularity;
  minors, cofactors, adjoint and inverse; $AX=B$, inverse method, Cramer's
  rule (2 and 3 variables), homogeneous systems and consistency; symmetric,
  skew-symmetric, orthogonal, idempotent, involutory and nilpotent matrices.
- **Part II — Olympiad/specialised extensions:** characteristic polynomial,
  eigenvalues, Cayley–Hamilton and power reduction; similarity invariants;
  Hadamard, rank-one determinant lemma and Vandermonde; trace cyclicity,
  rank–nullity, block determinants and Schur complement.

The official JEE scope is narrower than the source module's full linear-algebra
frontier; extensions are clearly separated, not implied to be explicit syllabus
requirements.

## Files

- `JEE/`, `Olympiad/` — independently numbered portrait PNG sheets.
- `exports/` — three PNG ZIPs and three bookmarked A4 PDFs (combined PDF puts
  JEE first).
- `index.html` — gallery; `manifest.json` — render manifest.
- `content/*.md` — editable content; `scripts/` — render, export, layout and
  numeric checks.
- `SCOPE.md`, `SOURCE-AUDIT.md`, `PRINTING.txt` — boundaries, source review,
  and printer setup.

## Rebuild

```bash
python3 scripts/render.py && python3 scripts/export.py && python3 scripts/check.py
python3 scripts/math_checks.py
```

## Reading order

Follow the `LESSON n / total` ribbons; read down the left column, then down the right column, and continue to the next sheet. This sequence follows the chapter’s prerequisite path.

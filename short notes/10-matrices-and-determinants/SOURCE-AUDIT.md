# Source Audit — Chapter 10: Matrices & Determinants

## Sources reviewed

- `notes/Matrices-and-Determinants/Matrices-and-Determinants.md` — all 856
  lines reviewed before authoring, including its six chapters and appendix.
  Its exposition ranges from basic operations through rank/special matrices
  to Cayley–Hamilton, determinant bounds and Vandermonde.
- `notes/Matrices-and-Determinants/Matrices-and-Determinants — Paper.md` and
  `… — Solutions.md` are identified as companion material; the sheets are
  based on the theory module, not a transcription of the paper.
- Official JEE Advanced syllabus scope: matrices/determinants through order 3,
  adjoint and inverse, and Cramer's rule for 2/3 variables.

## Independent verification performed

`scripts/math_checks.py`: **341 assertions** (after the final content update;
see script output), including direct products $AB$ and $BA$, transpose,
2×2/3×3 determinants, determinant product identity on seeded integer matrices
of orders 1–3, scalar homogeneity, row swaps/additions, transpose invariance,
$A\operatorname{adj}A=(\det A)I$ examples, both Cramer examples, orthogonal
matrices, symmetric/skew decomposition, idempotence, Cayley–Hamilton and a
power reduction, Hadamard inequalities, rank-one update determinant, the
Vandermonde value, and trace cyclicity. These are targeted independent checks,
not a formal proof of every theorem.

The renderer's matrix environments were also exercised in inline formulas,
standalone 2×2 and 3×3 matrices, determinants, and matrices embedded between
ordinary math text. `matrix`, `pmatrix`, `bmatrix`, and `vmatrix` rendering and
cell-level math parsing are handled by the shared engine extension in
`short notes/_engine/core.py`.

## Corrections and assumptions

No source numeric error was identified among the statements and examples
reproduced. The notes do make two scope/precision improvements explicit:

- Distinct eigenvalues imply diagonalisation over a field containing them;
  for a real matrix this may require complex scalars.
- The determinant lemma and Schur-complement formulas state their invertibility
  hypotheses; Hadamard's equality includes the zero-column case.

The source module includes material beyond official JEE scope. Such material is
kept in Part II rather than presented as an explicit JEE requirement.

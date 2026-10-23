# Chapters 1–11 — completeness and reading-order review

**Review pass:** 2026-10-23. This report records a second-pass cross-check of
all eleven existing short-note sets against the official JEE Advanced 2026
syllabus items assigned to these chapters, their chapter `SCOPE.md` /
`SOURCE-AUDIT.md`, source-note coverage, and the rendered page order. The Part I
sheets are labelled for JEE Main + Advanced, but this pass is not a separate,
exhaustive item-by-item crosswalk of the official JEE Main syllabus; use the
chapter scope maps for topic detail and consult NTA's current syllabus directly
for Main-specific changes.

## Findings: JEE Advanced coverage

| Ch. | Review result | Required coverage checked / action |
|---|---|---|
| 1 Sets, Relations & Functions | Mapped coverage present | Set algebra and finite-family De Morgan; products, relations/equivalence, functions, domain/range, special functions, one-one/onto/inverse/composition. Existing scope map is retained. |
| 2 Exponents & Logarithms | Mapped coverage present | Logarithm definition/properties and domain/base conditions; exponents and exponential function are explicitly identified as prerequisite machinery, not a separate syllabus bullet. |
| 3 Trigonometry | Mapped coverage present | Ratios/unit circle, standard values, identities, transformations, equations and interval filtering. Triangle properties / heights-and-distances are not misclassified as JEE core. |
| 4 Inverse Trigonometric Functions | Mapped coverage present | Principal branches and ranges, compositions, standard values, addition formulas with branch conditions, equations/inequalities. Branch conventions remain explicit. |
| 5 Complex Numbers | **One omission found and corrected** | The scope listed the Fundamental Theorem of Algebra, but the theorem statement was missing from the rendered JEE material. Added a statement-only box to JEE-07, with the nonconstant-polynomial hypothesis and roots counted with multiplicity. |
| 6 Quadratic Equations | Mapped coverage present | Real-coefficient quadratics, discriminant/nature, Vieta, sign/range, location of roots, reducible/common-root and parameter problems. |
| 7 Sequences & Series | Mapped coverage present | AP, GP, AM–GM, and the named sums through cubes. Harmonic progressions remain Part II; they are not described as official JEE syllabus content. |
| 8 Permutations & Combinations | Mapped coverage present | Fundamental counting, permutations, combinations, restrictions, distributions, inclusion–exclusion and standard applications. The two source arithmetic/counting errors are already recorded and corrected in its audit. |
| 9 Binomial Theorem | Mapped coverage present | Positive-integral-index theorem, terms/coefficient work and standard derivable applications. General/negative index remains clearly Part II. |
| 10 Matrices & Determinants | Mapped coverage present | Matrix algebra, determinants through order 3, adjoint/inverse, and Cramer's rule for 2/3 unknowns. Matrix-array rendering was tested. |
| 11 Probability & Statistics | Mapped coverage present; statistics source gap remains disclosed | Probability/Bayes/random-variable mean and variance plus grouped/ungrouped mean, median, mode, mean deviation, variance and SD. The repository has no dedicated descriptive-statistics source chapter; the authored treatment and grouped-data estimation assumptions are disclosed. |

“Mapped coverage present” means the stated official chapter bullets have
corresponding authored material and were checked against the chapter scope map;
it is not a claim that every possible examination question or every proof has
been exhaustively verified. The existing per-chapter math checks are targeted
numerical checks, not proof verification.

## IOQM / RMO boundary

The Part II material in these eleven JEE chapters supplies topic-linked
Olympiad extensions (for example, functional equations/floor tools, trig
identities, complex geometry, Vieta jumping, recurrences, Catalan/Burnside,
Lucas/Kummer, determinant structure and probability recurrences). It is **not a
complete IOQM course**: the first eleven JEE chapters do not include dedicated
number theory or Euclidean-geometry chapters, and IOQM problems are not bounded
by this repository's chapter list. No extension is claimed to be impossible
in JEE. A future IOQM-completeness pass must span the remaining syllabus areas
and include a separate number-theory/geometry coverage map.

## Reading-order redesign applied to all 11

The authored concept order in the source files already follows the prerequisite
chain shown in each chapter's scope; where the audit identified a syllabus
omission, it was added rather than hiding the gap. The rendered sheets were
hard to navigate because the reader had no explicit column order and adjacent
source lessons could meet without a visible boundary. The shared renderer now:

1. prints a plain-language reading instruction on **every page**: read down
   the left column, then down the right, then continue to the next sheet;
2. inserts a numbered **LESSON n / total** ribbon at every editable lesson
   boundary, retaining the authored prerequisite order;
3. uses compact, numbered lesson markers so source boundaries are visible
   without repeating long lesson titles; and
4. preserves the existing section-heading / worked-example / derivation / trap
   order and keeps a section heading with the block it introduces.

This is a navigational and page-flow redesign, not a claim that the mathematical
content has been rewritten from scratch. Per-chapter source audits remain the
record of source review, corrections, and assumptions. All 11 sets are
re-rendered and their manifests, galleries, ZIPs and PDFs regenerated from the
editable content after this redesign.

## Syllabus references

- JEE Advanced 2026 Mathematics syllabus (official):
  <https://jeeadv.ac.in/documents/jee-advanced-2026-syllabus.pdf>
- JEE Main 2026 official syllabus landing page (NTA):
  <https://jeemain.nta.nic.in/document/syllabus-2026/>

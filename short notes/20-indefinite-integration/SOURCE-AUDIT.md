# Source Audit — Chapter 20: Indefinite Integration

## Sources reviewed

- `notes/Integration/Integration.md` — the 798-line canonical module covering S1–S19, P1–P18, antiderivative techniques, definite integration and the frontier appendix.
- `notes/Integration/Integration — Paper.md` and `Integration — Solutions.md` — all **46 question/answer pairs** were inspected to partition indefinite techniques from definite evaluation and to check conventions and corrections.
- `notes/Integration/assets/fig-01.svg` and `fig-02.svg` — the Riemann-sum and Fundamental Theorem assets were inspected. Both belong to Chapter 21; the new Chapter 20 figures are editable slope/domain diagrams rather than static area screenshots.
- `notes/Differentiation-and-Methods/Differentiation-and-Methods.md` — the preceding derivative-methods boundary was checked. Chapter 20 uses differentiation as its verification tool.
- Official JEE Advanced 2026 Mathematics syllabus, Integral Calculus: <https://jeeadv.ac.in/documents/jee-advanced-2026-syllabus.pdf>. The official/extension and Chapter 21 boundaries are mapped in `SCOPE.md`.

## Coverage map

The new lessons are a reorganized teaching edition, not a verbatim copy. Every canonical **indefinite** S/P method and every fully indefinite paper question is included. Definite questions are explicitly assigned to Chapter 21 rather than being silently dropped or duplicated.

| Source material | New location |
|---|---|
| Chapter 1, S1–S2, P1–P2, Q1–Q4: antiderivatives, library and constants | `jee-01.md` |
| Chapter 2, S3–S4, Q5–Q6: reverse-chain substitution | `jee-02.md` |
| P4, Q7: $e^{x^2}$ antiderivative stage; definite evaluation reserved | `jee-02.md` |
| P3, Q8: tangent and logarithmic substitution; Q4 scaled logarithm | `jee-03.md` |
| Q9 and trigonometric-power preparation; antiderivatives behind P10/Q24/Q36 | `jee-04.md` |
| S5, Q13: completing the square and arctangent; P5/Q10–Q12 antiderivative stages | `jee-05.md` |
| Q21 and radical standard forms | `jee-06.md` |
| Chapter 3, S6–S7, P6, Q14–Q16: by parts and repeated parts | `jee-07.md` |
| P7, Q18: cyclic by parts; Q17 antiderivative stage | `jee-08.md` |
| Chapter 4, S8, Q19: distinct linear factors; Q20 antiderivative stage | `jee-09.md` |
| P8: irreducible quadratic and corrected logarithm-only answer | `jee-10.md` |
| S13, Q35: universal half-angle method and branch; definite value reserved | `jee-11.md` |
| Appendix A/B theory and the indefinite mistake checklist | redistributed through `jee-01.md`–`jee-12.md` |
| S15, S19, Q30, Q43: Wallis/reduction foundation without definite limits | `olympiad-02.md` |
| S14, P13–P14, Q28–Q29: parameter-differentiated antiderivatives; endpoint limits reserved | `olympiad-03.md` |
| S16, Q32–Q33, Q37, Q46: non-elementary-antiderivative boundary; exact definite values reserved | `olympiad-04.md` |
| P7/Q18 generalisation to damped sine and cosine | `olympiad-05.md` |

### Complete question partition

- **Fully covered in Chapter 20:** **Q1–Q6, Q8–Q9, Q13–Q16, Q18–Q19 and Q21** — all 15 questions whose requested result is an indefinite antiderivative.
- **Reserved for full evaluation in Chapter 21:** **Q7, Q10–Q12, Q17, Q20 and Q22–Q46**. Their definite limits, FTC properties, improper convergence or frontier values are outside this chapter.
- Several reserved questions have their indefinite foundation deliberately prepared here: Q7, Q10–Q12, Q17, Q20, Q23–Q24, Q28–Q30, Q32–Q33, Q35–Q37, Q43 and Q46. This is method linkage, not a claim that their definite answers have already been derived.
- Chapter 21 also retains S9–S12, S16–S18 and the definite parts of S13–S15/S19, together with P4–P5, P9–P18 and the two source SVG area/FTC figures. No source material is lost in the two-chapter partition.

The six-page visual lab uses additional exact models rather than embedding the source's definite-area figures. It reinforces slope verification and domains without introducing the Fundamental Theorem or area evaluation.

## Scope decisions

Part I contains the complete indefinite JEE toolkit and close derivable applications. Part II generalises substitution, recurrence, parameter differentiation, non-elementary representation and complexification. Placement in Part II is organizational, not a claim that an elementary special case is outside JEE.

## Corrections and necessary clarifications to source wording

- **P8 — incorrect extra arctangent term:** for
  $$
  I=\int\frac{x+1}{x^2+2x+2}dx,
  $$
  the numerator satisfies $x+1=\frac12(2x+2)$ exactly. The correct answer is only
  $$
  I=\frac12\ln(x^2+2x+2)+C.
  $$
  The source's added $\frac12\tan^{-1}(x+1)$ has nonzero derivative $1/(2(x^2+2x+2))$ and therefore makes the answer wrong. Its displayed split with an additional $1/2$ remainder is also algebraically inconsistent. Both the corrected and incorrect candidates are independently differentiated in `math_checks.py`.
- **Standard-form hypotheses:** the arctangent, arcsine and difference-of-squares formulas require appropriate $a>0$ and domain restrictions. The new notes state these explicitly rather than treating the formula table as domain-free.
- **Constants on disconnected domains:** $\ln|x|+C$ is used on one interval at a time. The visual lab makes the negative and positive branches distinct and permits independent constants.
- **Half-angle branches:** $t=\tan(x/2)$ fails at odd multiples of $\pi$. The new lesson does not treat its arctangent output as an automatically continuous antiderivative across those points.
- **Non-elementary language:** failure of the elementary toolkit does not imply nonexistence of an antiderivative or failure of every definite-integral method. Extension IV states the precise distinction.

### Deferred-source issues flagged for Chapter 21

These do not affect Chapter 20, but are recorded now because the same canonical module will be reused:

- **Solutions Q36:** the phrase “the integrand is $1/2$” is wrong; the integrand simplifies to $\sin^2x$. The final definite value $\pi/4$ is correct.
- **Canonical Gamma duplication discussion at $z=1/2$:** the substitution is mishandled. Since $\Gamma(1)=1$ and $2^{1-2z}=1$ at $z=1/2$, the formula reduces to $\Gamma(1/2)\Gamma(1)=\sqrt\pi\,\Gamma(1)$, not the printed $\Gamma(1/2)^2=2\sqrt\pi\,\Gamma(1)$ or $\pi=2\sqrt\pi$. The separate $z=1/4$ result $\Gamma(1/4)\Gamma(3/4)=\pi\sqrt2$ is correct.

## Independent verification

`scripts/math_checks.py` contains **631 exact/rational, numerical, visual-lab and editable-figure checks**. It independently differentiates every printed antiderivative family, checks exact partial-fraction and Euler identities, solves undetermined-coefficient systems, iterates reduction recurrences, and reads the actual JSON diagram specifications.

Fourth-order central differences provide a numerical derivative oracle. Exact `Fraction` arithmetic checks rational decompositions. Recursive antiderivatives are compared with displayed closed forms. The `erf` derivative is tested directly, and an independently summed power series checks the derivative and normalisation of `Si`. The suite explicitly rejects the incorrect P8 candidate and a cyclic by-parts answer missing its factor $1/2$.

Selected independently confirmed results include:

- The source's basic power, exponential, logarithmic and trigonometric antiderivatives all differentiate to their integrands on valid intervals.
- The corrected P8 has no arctangent remainder; the extra source term is measured and rejected.
- The half-angle antiderivative of $1/(2+\cos x)$ has the expected derivative and satisfies $F(\pi/2)=\pi/(3\sqrt3)$ on its branch.
- The sixth sine-power reduction, exponential and logarithmic recurrences, and both parameter-differentiated logarithmic formulas agree with independent closed forms.
- All 25 editable figures have valid structure; all 10 graphs have their actual curve derivatives, point anchors and tangent slopes checked.
- The six visual-lab models verify parallel slopes, negative/positive logarithm branches, by-parts slopes, partial-fraction values, exact vertical shifts and the half-angle branch.

These are targeted reproducible checks, not automated proof verification. Native-size visual inspection supplements them, including label placement, continuation-page flow, safe margins and the distinction between an integrand's height and an antiderivative's slope.

## IOQM boundary

Part II provides integration-linked Olympiad and specialised extensions only. It is not a complete IOQM/RMO syllabus. Numerical derivative checks are independent evidence for exact formulas, never replacements for the printed derivations.

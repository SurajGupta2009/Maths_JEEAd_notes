# Source Audit — Chapter 21: Definite Integration & Areas

## Sources reviewed

- `notes/Integration/Integration.md` — the canonical module, including S9–S19, P4–P5 and P9–P18, the definite/frontier theory and the mistake checklist.
- `notes/Integration/Integration — Paper.md` and `Integration — Solutions.md` — all 46 question/answer pairs were rechecked. Chapter 20 covers the 15 indefinite questions; this chapter fully evaluates the remaining 31.
- `notes/Integration/assets/fig-01.svg` and `fig-02.svg` — the Riemann-sum and FTC concepts were inspected and recreated as editable JSON graphs.
- `short notes/20-indefinite-integration/SOURCE-AUDIT.md` — the previous chapter's question partition and deferred-source corrections were used as the starting boundary, then checked again against the canonical paper.
- Official JEE Advanced 2026 Mathematics syllabus, Integral Calculus: <https://jeeadv.ac.in/documents/jee-advanced-2026-syllabus.pdf>. Official and extension boundaries are recorded in `SCOPE.md`.

## Canonical S/P and figure coverage

The lessons are a reorganised teaching edition, not a verbatim copy. No definite S/P item is silently omitted.

| Source material | New location |
|---|---|
| S9, S10: FTC evaluation and accumulation derivative | `jee-02.md` |
| P4, P5: definite exponential and completed-square substitutions | `jee-03.md` |
| S13: half-angle definite integral | `jee-04.md` |
| S11, P11: odd-function symmetry | `jee-05.md` |
| S12, P10: King reflection and sine squared | `jee-06.md` |
| P9: sine-arch area | `jee-10.md` |
| P12: exponential improper integral | `jee-07.md` |
| P13, P14: logarithmic singular endpoints | `jee-08.md` |
| S14: $x\ln x$ by parts and by Feynman differentiation | `jee-08.md`, `olympiad-05.md` |
| P15: logarithmic inversion on $(0,\infty)$ | `jee-09.md` |
| S15: Wallis reduction for $\sin^6x$ | `olympiad-01.md` |
| S18: $B(1/2,1/2)$ and $\sqrt{\sin x\cos x}$; S19: Beta–Wallis | `olympiad-02.md` |
| P18: duplication at $z=1/4$ | `olympiad-02.md` |
| S16, P16: Gaussian and scaled Gaussian | `olympiad-03.md` |
| S17, P17: exponential Frullani integrals | `olympiad-04.md` |
| Riemann-sum source figure `fig-01.svg` | `jee-01.md`, especially `jee-visual-01.md` |
| FTC source figure `fig-02.svg` | `jee-02.md`, especially `jee-visual-02.md` |
| Definite/frontier appendix theory and mistake checklist | redistributed through the relevant core and extension lessons |

## Complete deferred-question coverage

Chapter 20 previously covered Q1–Q6, Q8–Q9, Q13–Q16, Q18–Q19 and Q21. The remaining **Q7, Q10–Q12, Q17, Q20 and Q22–Q46** are evaluated here:

| Question | Exact result or statement | New location |
|---|---|---|
| Q7 | $\int_0^1 2xe^{x^2}dx=e-1$ | `jee-03.md` |
| Q10 | $\int_0^1 dx/(1+x^2)=\pi/4$ | `jee-03.md` |
| Q11 | $\tan^{-1}2-\pi/4$ | `jee-03.md` |
| Q12 | $\int_0^1 dx/\sqrt{4-x^2}=\pi/6$ | `jee-03.md` |
| Q17 | $\int_0^\pi x\sin x\,dx=\pi$ | `jee-04.md` |
| Q20 | $\ln(4/3)$ | `jee-04.md` |
| Q22 | $A'(x)=x^3$ | `jee-02.md` |
| Q23 | $\int_0^1x^3dx=1/4$ | `jee-02.md` |
| Q24 | $\int_0^{\pi/2}\sin^2x\,dx=\pi/4$ | `jee-06.md` |
| Q25 | $\int_{-1}^1x^3dx=0$ | `jee-05.md` |
| Q26 | $\int_0^{\pi/2}dx/(1+\tan x)=\pi/4$ | `jee-06.md` |
| Q27 | $\int_0^\infty e^{-x}dx=1$ | `jee-07.md` |
| Q28 | $\int_0^1x\ln x\,dx=-1/4$ | `jee-08.md`, `olympiad-05.md` |
| Q29 | $\int_0^1(\ln x)^2dx=2$ | `jee-08.md`, `olympiad-05.md` |
| Q30 | $\int_0^{\pi/2}\sin^6x\,dx=5\pi/32$ | `olympiad-01.md` |
| Q31 | $\int_0^\infty\ln x/(1+x^2)dx=0$ | `jee-09.md` |
| Q32 | $\int_0^\infty e^{-x^2}dx=\sqrt\pi/2$ | `olympiad-03.md` |
| Q33 | $\int_{-\infty}^\infty e^{-2x^2}dx=\sqrt{\pi/2}$ | `olympiad-03.md` |
| Q34 | exponential Frullani value $\ln2$ | `olympiad-04.md` |
| Q35 | $\int_0^{\pi/2}dx/(2+\cos x)=\pi/(3\sqrt3)$ | `jee-04.md` |
| Q36 | corrected integrand and value $\pi/4$ | `jee-06.md` |
| Q37 | Dirichlet integral $\pi/2$, conditionally convergent | `olympiad-06.md` |
| Q38 | exponential Frullani value $\ln(5/3)$ | `olympiad-04.md` |
| Q39 | $B(1/2,1/2)=\pi$ | `olympiad-02.md` |
| Q40 | $\frac{1}{\sqrt2}\frac{\sqrt\pi}{2}\frac{\Gamma(3/4)}{\Gamma(5/4)}\approx0.8472130848$ | `olympiad-02.md` |
| Q41 | $\Gamma(1/4)\Gamma(3/4)=\pi\sqrt2$ | `olympiad-02.md` |
| Q42 | $\Gamma(z)\Gamma(1-z)=\pi/\sin(\pi z)$ | `olympiad-02.md` |
| Q43 | Beta evaluation of $\int_0^{\pi/2}\sin^6x\,dx=5\pi/32$ | `olympiad-02.md` |
| Q44 | $\Gamma(z)\Gamma(z+1/2)=2^{1-2z}\sqrt\pi\,\Gamma(2z)$ | `olympiad-02.md` |
| Q45 | $\int_0^1(x^3-1)/\ln x\,dx=\ln4$ | `olympiad-05.md` |
| Q46 | $\int_{-\infty}^{\infty}e^{-ax^2+bx}dx=\sqrt{\pi/a}\,e^{b^2/(4a)}$, $a>0$ | `olympiad-03.md` |

Additional cosine-Frullani, cosine-transform, rational-tail and logarithmic-trigonometric examples are labelled as extensions; they are not substituted for any canonical question.

## Corrections and necessary clarifications to source wording

- **Solutions Q36 — contradictory prose:** the simplified integrand is $\sin^2x$, not $1/2$. The final answer $\pi/4$ is correct. `jee-06.md` states the correction, and the check suite verifies both the identity and the rejection of the constant-$1/2$ claim.
- **Gamma duplication at $z=1/2$:** the source substitution is mishandled. Q44's identity reduces to $\Gamma(1/2)\Gamma(1)=\sqrt\pi\,\Gamma(1)$, equivalently $\Gamma(1/2)=\sqrt\pi$; it does not imply $\Gamma(1/2)^2=2\sqrt\pi$ or $\pi=2\sqrt\pi$. The separate P18/Q41 value at $z=1/4$ is $\pi\sqrt2$ and is confirmed independently by reflection.
- **Solutions Q45 — wrong parameter-integral lower limit:** for $x>0$, $x\ne1$,
  $$
  \int_0^a x^t dt=\frac{x^a-1}{\ln x},\qquad
  \int_1^a x^t dt=\frac{x^a-x}{\ln x}.
  $$
  The intended representation therefore needs lower limit **0**, not 1. The final Q45 value $\ln4$ remains correct. Both forms are tested and the printed representation is explicitly rejected.
- **Canonical Frullani warning — nonexistence of $f(\infty)$ is not a divergence proof:** the finite-limit theorem simply does not apply directly. For $a,b>0$, the additional sine-difference integral converges conditionally to $0$; the cosine difference converges conditionally to $\ln(b/a)$. `olympiad-04.md` derives both through damping, Dirichlet convergence and Abel continuity instead of repeating the source's divergence claim.
- **Dirichlet convergence class and damping limit:** $\int_0^\infty\sin x/x\,dx=\pi/2$ is conditionally, not absolutely, convergent. `olympiad-06.md` proves convergence, gives a harmonic lower-bound argument for nonabsolute convergence, derives the damped family for positive parameter, and only then applies Abel continuity.
- **Q40 substitution detail:** the lesson writes the full $u=2x$ calculation, including the factor $1/2$ and symmetry on $[0,\pi]$, before applying Beta. This makes the source's compressed but correct final expression reproducible.

## Independent verification

`scripts/math_checks.py` contains **417 exact/rational, numerical, visual-lab and editable-figure checks**. It uses exact `Fraction` arithmetic, fourth-order finite differences, composite Simpson quadrature, finite-part plus exact-tail calculations, transformed improper integrals, recursive Wallis identities and an accelerated sum of Dirichlet arches.

The suite checks every deferred question with its canonical numbering, including direct quadratures for Q33, Q34, Q38, Q40 and Q46. It tests additional parameter values for Beta/Gamma, reflection, duplication, Gaussian and damped Frullani families. The source's incorrect Q36, duplication and Q45 candidates are explicitly rejected. The sine-Frullani correction is tested by its damped limit, and Dirichlet's exact value is independently approximated while a harmonic estimate confirms nonabsolute convergence.

All 24 editable diagrams are parsed from the Markdown. The suite checks 11 graphs, 6 workflows and 7 tables; actual rectangle heights and area, curve derivatives, fill expressions, intersections, point anchors and graph values are included. Six further visual-lab assertions are registered in `_engine/visual_math_checks.py`.

These are targeted reproducible checks, not automated proof verification. All 42 pages were reviewed in contact sheets, with dense formula, table, graph and continuation pages also inspected at native size. Safe-border and running-header checks remain mandatory delivery gates.

## IOQM boundary

Part II provides integration-linked Olympiad and specialised extensions only. It is not a complete IOQM/RMO, real-analysis or special-functions syllabus. Numerical evidence supplements, but never replaces, the printed exact derivations.

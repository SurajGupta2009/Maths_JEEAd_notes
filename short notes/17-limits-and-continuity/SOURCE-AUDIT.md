# Source Audit — Chapter 17: Limits & Continuity

## Sources reviewed

- `notes/Limits-and-Continuity/Limits-and-Continuity.md` — the 845-line canonical module covering limits, computation, continuity, labelled Olympiad techniques and synthesis.
- `notes/Limits-and-Continuity/Limits-and-Continuity — Paper.md` and `Limits-and-Continuity — Solutions.md` — the 220-line paper and 235-line solutions. All 39 companion question/answer pairs were inspected for method coverage, conventions and independent checks.
- `notes/Limits-and-Continuity/assets/fig-01.svg` — the existing δ/ε-band construction was inspected. The new notes use an editable JSON graph with the same mathematical band idea rather than embedding a screenshot.
- Official JEE Advanced 2026 Mathematics syllabus, Differential Calculus: <https://jeeadv.ac.in/documents/jee-advanced-2026-syllabus.pdf>. The official/extension boundary is mapped in `SCOPE.md`.

## Coverage map

The new lessons are a reorganized teaching edition, not a verbatim copy. Every source section and companion-question technique is either included or explicitly assigned to a later chapter.

| Source material | New location |
|---|---|
| S1–S2, P3, Q1–Q3: direct limits, factoring and rationalisation | `jee-02.md` |
| P1–P2, one-sided and greatest-integer limits | `jee-01.md`, `jee-07.md` |
| S3–S5, P4–P7, Q5–Q16: squeeze, standard limits, exponentials and L'Hôpital | `jee-03.md`–`jee-06.md` |
| S6, P8–P10, Q17–Q23: continuity, piecewise joins, IVT and fixed points | `jee-07.md`–`jee-09.md` |
| P12, Q27–Q28: horizontal and vertical asymptotes | `jee-05.md` |
| S7, P11, Q26: derivative-from-definition and tangent calculations | **Chapter 18 boundary**, not silently dropped |
| S8, Q4: sequential criteria and oscillatory nonexistence | `olympiad-01.md` |
| S9, S11, P14, P18, Q29, Q31, Q36: Stolz–Cesàro and recurrences | `olympiad-02.md` |
| S10, S13–S14, P15, Q30, Q33–Q34, Q39: Riemann-sum limits | `olympiad-03.md`, explicitly as an extension/Chapter 21 bridge |
| P16–P17: Stirling and Euler–Mascheroni | `olympiad-04.md` |
| S12, Q35: logarithmic bounds for the product limit | `olympiad-03.md` |
| P19: $(1+1/n)^n/n$ | `jee-04.md`, using only the $e$-limit and quotient law |
| P20, Q38: continuous exponential and Jensen functional equations | `olympiad-05.md` |
| S15, Q24–Q25, Q37: half-shift and antipodal IVT constructions | `olympiad-05.md` |
| S16, Q32: second-order convergence rate | `olympiad-04.md` |

The six-page visual lab uses additional exact models rather than duplicating the source's single static asset. It reinforces, but does not replace, the derivations.

## Scope decisions

Part I contains the complete limit/continuity core and directly supporting techniques. Sequential criteria, Stolz–Cesàro, recursive sequences, Riemann-sum limits, Stirling/Euler–Mascheroni, convergence rates and functional equations are explicitly separated into Part II.

Derivative-from-definition calculations and tangent methods belong to Chapter 18. The continuity/differentiability relationship is mentioned only as a boundary, not used to teach derivative rules. Riemann sums are a labelled sequence-limit extension and forward bridge to Chapter 21, not core definite-integration instruction.

## Corrections and necessary clarifications to source wording

- **S8, the nonanalytic-smooth-function remark:** the formula $e^{-1/x^2}$ is initially undefined at $0$. The notes explicitly assign $f(0)=0$ before claiming continuity there. No unsupported claim about analyticity is needed for the limit proof.
- **P19, suggested Stolz method:** since $(1+1/n)^n\to e$ and $1/n\to0$, the quotient laws immediately give $(1+1/n)^n/n\to0$. Stolz–Cesàro is unnecessary; the new solution says so.
- **P20, continuous exponential functional equation:** the zero solution must be excluded using $f(1)=a>0$. The proof then establishes $f(0)=1$ and strict positivity before deriving $f(q)=a^q$ on rationals and extending by continuity. Writing $f(x)=a^x$ without these steps would be incomplete.
- **Q24, antipodal temperatures:** the IVT argument proves existence of **some** equal-temperature antipodal pair. It does not prove that every attained temperature occurs at antipodal pairs. The notes state the narrower correct conclusion.
- **S11 and recursive models generally:** solving $L=f(L)$ does not itself prove convergence. The nested-radical and Heron examples establish monotonicity and bounds first; sign/range information then selects the fixed point.
- **Riemann-sum wording:** a right-endpoint sum includes the mesh $1/n$ and sampled point $k/n$. These are displayed explicitly so that an unweighted sum is not mistaken for a Riemann sum.

## Independent verification

`scripts/math_checks.py` contains **356 exact/rational, numerical, visual-lab and editable-figure checks**. It recomputes the displayed identities and numerical models, tests theorem hypotheses and degenerate cases, performs bisection independently, and reads the actual JSON diagram specifications. Every plotted curve is evaluated inside its own sampled segment; all marked Heine, recurrence and Riemann points are checked mathematically.

Selected independently confirmed values include:

- $x^3+x-1=0$ has its unique root in $(0,1)$ at approximately $0.6823278038$; the first bisection signs are $f(1/2)=-3/8$ and $f(3/4)=11/64$.
- $\cos x=x$ has the Dottie root approximately $0.7390851332$.
- $\prod_{k=1}^{n}(1+k/n^2)\to\sqrt e$; the full logarithmic two-sided error bound is printed.
- $n[(1+1/n)^n-e]\to-e/2\approx-1.3591409142$; independent scaled errors at $n=100$ and $n=1000$ are $-1.3467999038$ and $-1.3578962232$.
- $\binom{2n}{n}/4^n\sim1/\sqrt{\pi n}$; at $n=10$, the ratio to the asymptotic expression is approximately $0.9875829288$.
- The nested-radical recurrence has $a_6\approx1.998929175$. The oscillation figure's unit-height markers use $y_n=1/(\pi/2+2n\pi)$ exactly, rather than merely lying near the drawn curve.

These are targeted reproducible checks, not automated proof verification. Native-size visual inspection supplements them, including label placement, open/closed-point visibility, safe margins and continuation-page flow.

## IOQM boundary

Part II provides limit/sequence/continuity Olympiad and specialised extensions only. It is not a complete IOQM/RMO syllabus. Numerical checks are used as independent evidence for exact formulas, never as replacements for the printed proofs.

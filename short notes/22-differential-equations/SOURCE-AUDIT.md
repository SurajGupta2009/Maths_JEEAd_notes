# Source Audit — Chapter 22: Differential Equations

## Sources reviewed

- `notes/Differential-Equations/Differential-Equations.md` — canonical theory, S1–S21, P1–P16, appendix and mistake checklist.
- `notes/Differential-Equations/Differential-Equations — Paper.md` — all 41 questions, Q1–Q41.
- `notes/Differential-Equations/Differential-Equations — Solutions.md` — every supplied derivation and numerical answer, independently rechecked rather than copied.
- `notes/Differential-Equations/assets/fig-01.svg` and `fig-02.svg` — the slope-field/solution-branch and orthogonal-trajectory concepts, inspected and rebuilt as editable JSON graphs.
- Official JEE Advanced 2026 Mathematics syllabus, Integral Calculus: <https://jeeadv.ac.in/documents/jee-advanced-2026-syllabus.pdf>. Official and organisational extension boundaries are recorded in `SCOPE.md`.

The lessons are a reorganised teaching edition, not a verbatim copy. No canonical S/P/Q item is silently omitted.

## Canonical S/P and figure coverage

| Source material | New location |
|---|---|
| S1, P1: verification, order and degree | `jee-01.md` |
| S2, P2: formation from one-parameter families | `jee-02.md` |
| S3, S4, P3, P4: separable equations | `jee-03.md` |
| S5, P5: homogeneous first-order equations | `jee-04.md` |
| S6, S7, P6: linear first-order equations | `jee-05.md` |
| S8: Bernoulli equation | `jee-06.md` |
| S9, P7: exact differential forms | `jee-07.md` |
| S10, P8: orthogonal trajectories | `jee-08.md`, especially `jee-visual-03.md` |
| S11, S12, P9: constant-coefficient second order | `jee-09.md` |
| S13, P12: Cauchy–Euler equations | `jee-10.md` |
| S14, P10: cooling and growth; S16: autonomous reduction | `jee-11.md` |
| S21, P16: damping regimes | `jee-12.md`, especially `jee-visual-04.md` |
| S17, P13: reduction of order and independence | `olympiad-01.md` |
| S15, P11: Clairaut equations and singular envelopes | `olympiad-02.md`, especially `jee-visual-06.md` |
| S18, P14: non-uniqueness and delayed solutions | `olympiad-03.md`, especially `jee-visual-05.md` |
| S19: Lagrange equation | `olympiad-04.md` |
| S20, P15: Riccati equations | `olympiad-05.md` |
| Source `fig-01.svg`: $y'=x/y$, $y^2-x^2=C$, $(0,1)$ | `jee-03.md`, especially `jee-visual-01.md` |
| Source `fig-02.svg`: $y=cx^2$ and $x^2+2y^2=C$ | `jee-08.md`, especially `jee-visual-03.md` |
| Appendix theory and mistake checklist | redistributed through the relevant core/extension lessons |

## Complete Q1–Q41 coverage

| Question | Verified result or statement | New location |
|---|---|---|
| Q1 | Order $3$, degree $1$ | `jee-01.md` |
| Q2 | $y=e^{2x}$ satisfies $y'-2y=0$ on $(-\infty,\infty)$ | `jee-01.md` |
| Q3 | $y=xy'+(y')^2$ | `jee-02.md` |
| Q4 | $2xyy'=y^2-x^2$ | `jee-02.md` |
| Q5 | $y=\sqrt{x^2+1}$, $y(1)=\sqrt2$ | `jee-03.md`, `jee-visual-01.md` |
| Q6 | $y=e^x$, $y(1)=e$ | `jee-03.md` |
| Q7 | $y=3e^{x^2}$, $y(1)=3e$ | `jee-03.md` |
| Q8 | $y=x$ | `jee-03.md` |
| Q9 | $y=x\ln x$ on $x>0$, $y(e)=e$ | `jee-04.md` |
| Q10 | $y=x/(1-\ln x)$ on $(0,e)$, $y(2)=2/(1-\ln2)$ | `jee-04.md` |
| Q11 | $y=x\sqrt{2\ln x+1}$ on $(e^{-1/2},\infty)$, $y(e)=e\sqrt3$ | `jee-04.md` |
| Q12 | $y=\sinh x$, $y(1)=\sinh1$ | `jee-05.md`, `jee-visual-02.md` |
| Q13 | $y=2x-1+2e^{-2x}$, $y(1)=1+2e^{-2}$ | `jee-05.md` |
| Q14 | $y=x^2/3-1/(3x)$ on $x>0$, $y(2)=7/6$ | `jee-05.md` |
| Q15 | $y=1/(x+1)$ on $(-1,\infty)$, $y(1)=1/2$ | `jee-06.md` |
| Q16 | $y=e^{-x}$ | `jee-05.md` |
| Q17 | $x^2+xy+y^2=1$; the explicit branch and finite-slope interval are stated | `jee-07.md` |
| Q18 | $x^3+x^2y+y^2=1$ | `jee-07.md` |
| Q19 | $x^2+2y^2=C$, $C>0$ for nondegenerate ellipses | `jee-08.md`, `jee-visual-03.md` |
| Q20 | $y=Cx$ **and** $x=0$: all nondegenerate radial lines | `jee-08.md` |
| Q21 | $y=\sin x$ | `jee-09.md` |
| Q22 | $y=e^{2x}-e^x$, $y(1)=e^2-e$ | `jee-09.md` |
| Q23 | $y=(1+2x)e^{-2x}$, $y(1)=3e^{-2}$ | `jee-09.md` |
| Q24 | $y=(x-1/x)/2$ on $x>0$, $y(2)=3/4$ | `jee-10.md` |
| Q25 | $y=x^2$, $y(3)=9$ | `jee-10.md` |
| Q26 | $T(20)=40^\circ\mathrm{C}$ | `jee-11.md` |
| Q27 | $P(10)=1000e$ under the continuous $10\%$ relative-rate convention | `jee-11.md` |
| Q28 | $y=(\sin x-\cos x+e^{-x})/2$, $y(\pi/2)=(1+e^{-\pi/2})/2$ | `jee-06.md` |
| Q29 | $y=e^{-x}\sin2x$, under-damped, $y(1)\approx0.3345118292$ | `jee-12.md`, `jee-visual-04.md` |
| Q30 | $y=e^{-x}-e^{-2x}$, over-damped, $y(1)\approx0.2325441579$ | `jee-12.md` |
| Q31 | $y=e^x$; constant solutions of the general equation are also audited | `jee-11.md` |
| Q32 | $y=Cx+C^2$ and singular solution $y=-x^2/4$ | `olympiad-02.md`, `jee-visual-06.md` |
| Q33 | $y=Cx-C^2$ and singular solution $y=x^2/4$ | `olympiad-02.md` |
| Q34 | $C_1\sin x+C_2\cos x$; with $y_2=-\cos x$, $W=+1$ | `olympiad-01.md` |
| Q35 | $y=Ax^2+Bx$ on an interval not containing $0$ | `olympiad-01.md` |
| Q36 | Zero solution and immediate/delayed $(x-a)^2/4$ departures; Lipschitz hypothesis fails | `olympiad-03.md`, `jee-visual-05.md` |
| Q37 | Zero through $x=1$, then $[2(x-1)/3]^{3/2}$; joining derivative checked | `olympiad-03.md` |
| Q38 | Parametric family plus the separate solutions $y=1$ and $y=x+1$ | `olympiad-04.md` |
| Q39 | $y=1/(1+Ce^x)$ away from poles, **plus** $y=0$ | `olympiad-05.md` |
| Q40 | $y=1+1/(Ce^{-x^2}-1/2)$ away from poles, **plus** $y=1$; $y=-1$ is the $C=0$ equilibrium | `olympiad-05.md` |
| Q41 | $y''-y=0$ | `jee-02.md` |

Extension VI is additional nonhomogeneous-second-order enrichment; it does not replace or renumber any canonical item.

## Corrections and necessary clarifications to source wording

- **Q20/P8 — omitted vertical trajectory:** separation gives $y=Cx$ only on finite-slope half-plane intervals. The geometric family is all lines through the origin, so $x=0$ must be included. `jee-08.md` states and verifies this explicitly.
- **Q34/S17 — Wronskian sign:** with the convention $W=y_1y_2'-y_1'y_2$, $y_1=\sin x$ and $y_2=-\cos x$, the value is $+1$, not $-1$. Choosing $\cos x$ as the second representative reverses the sign but not independence.
- **Q38/S19 — erroneous differentiation and incomplete branch list:** differentiating $y=xp^2+1$ with $p=dy/dx$ gives $p=p^2+2xp(dp/dx)$. Equivalently, with $x=x(p)$,
  $$
  p\frac{dx}{dp}=p^2\frac{dx}{dp}+2xp
  \quad\Longrightarrow\quad
  (1-p)\frac{dx}{dp}=2x
  $$
  away from discarded branches. The quoted parametric family is valid for $C\ne0$ on appropriate $p$-intervals, but the constant-slope solutions $y=1$ and $y=x+1$ must also be listed. The source's displayed $p=2xp+xp^2p'$ is explicitly rejected numerically.
- **Q39/S20 — omitted equilibrium:** $1/(1+Ce^x)$ never equals zero for finite $C$. The solution $y=0$ is separate; taking $C\to\infty$ is only a limiting motivation. Negative-$C$ denominator zeros restrict the interval.
- **Q40/P15 — omitted equilibrium and poles:** $y=1$ is not attained by the displayed family for finite $C$ and is listed separately. The other equilibrium $y=-1$ corresponds to $C=0$. Every branch avoids zeros of $Ce^{-x^2}-1/2$; their exact locations are stated.
- **Q29/S21 — damping is not periodic:** for $y=e^{-x}\sin2x$, zeros occur at $x=n\pi/2$, so consecutive zeros are $\pi/2$ apart. Corresponding sine phases recur after $\pi$, the oscillation or quasi-period, but $y(x+\pi)=e^{-\pi}y(x)$. Thus $\pi$ is not a true period of the damped solution.
- **Q27/P10 — growth convention:** the source answer $1000e$ assumes $P'/P=0.1$ continuously. Annual discrete compounding instead gives $1000(1.1)^{10}$. Both values are printed so the modelling assumption cannot be hidden.
- **Domain and branch qualifications:** Q10 has maximal IVP interval $(0,e)$; Q11 has $(e^{-1/2},\infty)$; Q15 has $(-1,\infty)$; Q17's explicit finite-slope branch has $-2/\sqrt3<x<2/\sqrt3$. Q31's constant solutions, Bernoulli's zero equilibrium and the Riccati equilibria are checked before or after divisions rather than silently discarded.
- **Source `fig-01.svg`:** it contains no actual slope-field strokes and its lower branch lies outside the declared viewBox. Visual Lab 1 computes genuine line elements from $x/y$, omits the undefined $y=0$ row and shows both $\pm\sqrt{x^2+1}$ branches plus the source's $\sqrt{x^2-1}$ concept.
- **Source `fig-02.svg`:** the concept is rebuilt from explicit parabola and ellipse branches. The marked intersection satisfies $u=x^2=4\sqrt3-4$, and the plotted slopes are checked to multiply to $-1$.

## Independent verification

`scripts/math_checks.py` contains **711 exact, numerical, source-correction, domain and editable-figure checks**. It uses pure-Python scalar and second-order RK4 integration, fourth-order finite differences, exact parametric residuals, Wronskians, pole/domain calculations and joining-limit scaling. Every Q1–Q41 receives at least one targeted assertion; visible destinations for every S1–S21 and P1–P16 are also checked.

All 24 editable diagrams are parsed from the Markdown: 8 graphs, 8 workflows and 8 tables. The suite evaluates actual curve and slope-field expressions, branch constants, damping envelopes, delayed departures, Riccati residuals, tangent contacts and the exact orthogonality marker. The three slope-field specifications are genuine $f(x,y)$ fields, not decorative strokes. All eight tables render with `strict_fit: true` and `min_fontsize: 9`, so cell overflow is a build failure.

These are targeted reproducible checks, not automated proof verification. All 42 pages were reviewed in contact sheets; dense tables, visual labs, correction pages and continuations were also inspected at native size. Safe-border and running-header checks remain mandatory delivery gates.

## IOQM boundary

Part II provides differential-equation-linked Olympiad and specialised extensions only. It is not a complete IOQM/RMO, dynamical-systems or existence-theory syllabus. Numerical evidence supplements, but never replaces, the printed exact derivations.

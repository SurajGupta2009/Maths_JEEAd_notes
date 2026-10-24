# Source Audit — Chapter 19: Applications of Derivatives

## Sources reviewed

- `notes/Applications-of-Derivatives/Applications-of-Derivatives.md` — the 890-line canonical module covering S1–S20, P1–P18, six theory chapters, the optimisation frontier and the appendix.
- `notes/Applications-of-Derivatives/Applications-of-Derivatives — Paper.md` and `Applications-of-Derivatives — Solutions.md` — all **46 question/answer pairs** and their checks were inspected for method coverage, conventions and independent verification.
- `notes/Applications-of-Derivatives/assets/fig-01.svg` and `fig-02.svg` — the existing cubic-extrema and cubic-inflection assets were inspected. The new notes use editable JSON figures rather than embedding static screenshots.
- `notes/Differentiation-and-Methods/Differentiation-and-Methods.md` — the preceding derivative-methods boundary was checked to avoid duplicating Chapter 18.
- Official JEE Advanced 2026 Mathematics syllabus, Differential Calculus: <https://jeeadv.ac.in/documents/jee-advanced-2026-syllabus.pdf>. The official/extension boundaries are mapped in `SCOPE.md`.

## Coverage map

The new lessons are a reorganized teaching edition, not a verbatim copy. Every canonical S/P example and every companion Q1–Q46 is included.

| Source material | New location |
|---|---|
| Chapter 1, S1–S2, P1–P2, Q1–Q4: rates and related rates | `jee-01.md` |
| Chapter 2, S3–S4, Q5–Q7, Q9: tangents, normals, angles and chords | `jee-02.md` |
| P3, Q8: subtangent and subnormal; tangent/normal lengths | `jee-03.md` |
| S5, P4, Q10–Q12: differentials and linear approximation | `jee-03.md` |
| Chapter 3, S6, P5–P6, Q13–Q14, Q16: monotonicity and inequalities | `jee-04.md` |
| S7, Q15: exactly three roots of $x^3-3x+1$ | `jee-05.md` |
| Chapter 4, S8–S9, P7, Q17–Q19: local extrema | `jee-06.md` |
| S10, S15, Q20–Q22, Q31: absolute and global extrema | `jee-07.md` |
| Chapter 5, S11, P8, Q23–Q24: convexity and cubic inflection | `jee-08.md` |
| P9, Q25–Q26: quartic turning points, inflection and sketching | `jee-08.md`, `jee-09.md` |
| S12, P10–P11, Q27–Q28, Q32: fencing, products, box and perimeter | `jee-10.md` |
| S13, Q29: maximum of $xyz$ with $x+y+z=1$ | `jee-10.md`, `olympiad-05.md` |
| P13, Q30: maximum rectangle area in an ellipse | `jee-11.md` |
| P14: rectangle-with-semicircle window | `jee-11.md`, visual lab sheet 6 |
| S16, Q33: supporting line of $x^2$ at $a=3$ | `jee-08.md`, `olympiad-01.md` |
| P12, Q34: exponential Jensen | `olympiad-01.md` |
| S14: $\cos x\geq1-x^2/2$ | `olympiad-01.md` |
| P16, Q36, Q38–Q40: Young, AM–GM, signed square and Cauchy | `olympiad-02.md` |
| Q35: constrained sum of squares and Lagrange multipliers | `olympiad-04.md` |
| Q37, S18, Q41: envelope, parabola contact and directrix | `olympiad-03.md` |
| P17, S19, Q42–Q43: ellipse and circle director circles | `olympiad-04.md` |
| P15, S20, P18, Q44–Q46: symmetric optimisation and sum of squares | `olympiad-05.md` |
| Appendix theory, formulas and mistake checklist | redistributed through the matching core/extension lessons above |

The six-page visual lab uses additional exact models rather than duplicating the two static assets. It reinforces, but does not replace, the derivations. The shorter interval $[0,2]$ in visual sheet 5 is deliberately contrasted with the source's $[-2,2]$ absolute-extremum question in `jee-07.md`.

## Scope decisions

Part I contains the complete applications core and the source's JEE Advanced tagged constrained-product and supporting-line questions. Part II generalises these ideas through Jensen, Young, AM–GM, envelopes, director circles, Lagrange multipliers and symmetric optimisation. Placement of a specialised method in Part II is organizational, not a claim that every elementary special case lies outside JEE.

## Corrections and necessary clarifications to source wording

- **Q26, Paper and Solutions — incorrect inflection points:** for $f(x)=x^4-4x^2$, $f''(x)=12x^2-8$. The printed $(\pm1/\sqrt3,-11/9)$ satisfy $f''=-4$, not zero. The correct inflection points are
  $$
  \left(\pm\sqrt{\frac23},-\frac{20}{9}\right).
  $$
  Both sign changes and both ordinates are independently checked.
- **P14, window model — algebra and feasibility:** the perimeter is $2h+2r+\pi r=10$ and the area is
  $$
  A=10r-\left(2+\frac{\pi}{2}\right)r^2,
  \qquad 0\leq r\leq\frac{10}{2+\pi}.
  $$
  The source incorrectly cancels the semicircle term, obtains $r=2.5$, and declares the optimum infeasible. In fact $r=h=10/(4+\pi)$ is feasible and gives $A_{\max}=50/(4+\pi)$. Numerically, $r\approx1.4002479$ and $A_{\max}\approx7.0012394$. At the zero-height endpoint, the semicircle still has positive area $\pi r_{\max}^2/2\approx5.9418891$; it is not a zero-area endpoint.
- **S17, signed-square identity:** the displayed alternative containing $\sqrt{a^2b^2}$ uses $|ab|$, not $ab$, and fails when $ab<0$. The valid proof for all real $a,b$ is $a^2+b^2-2ab=(a-b)^2\geq0$, with equality iff $a=b$.
- **S5, square-root numerical value:** $\sqrt{25.4}=5.0398412673\ldots$, not $5.03968\ldots$. The differential estimate $5.04$ and error approximately $1.5873\times10^{-4}$ are consistent.
- **Solutions Q19, intermediate typo:** the quartic minima satisfy $f(\pm\sqrt2)=-4$, not $\pm4$. The final printed answer already has the correct value.
- **Solutions Q34, numerical check:** at $(1,2,3)$, $(e+e^2+e^3)/3\approx10.0643$, not $10.71$. The right side is $e^2\approx7.3891$; the Jensen conclusion is unchanged.
- **Solutions Q45, numerical check:** at $(0.1,5.9)$, $x^3+y^3=0.001+205.379=205.38$, not $205.8$. The value remains below the supremum $216$.
- **Q45/P18, open-boundary language:** for $x,y>0$ with $x+y=6$, the minimum is $54$ at $x=y=3$. The supremum is $216$ as an endpoint is approached; there is **no attained maximum** on the positive domain, not merely no interior stationary maximum.
- **S8, derivative-sign presentation:** the source initially reverses the sign at $x=-1$ and then corrects itself in the same paragraph. The new lesson gives only the clean sign chart: $+\to-$ at $-1$ and $-\to+$ at $1$.
- **Appendix D, monotonicity inequality:** $g'\geq0$ and $g(x_0)=0$ imply $g\geq0$ only on the forward side $x\geq x_0$ (with the analogous backward conclusion reversed). The unqualified displayed statement is false, as $g(x)=x$ at $x_0=0$ shows. The new monotonicity proofs state the interval direction explicitly through MVT.

## Independent verification

`scripts/math_checks.py` contains **469 exact/rational, numerical, visual-lab and editable-figure checks**. It recomputes displayed identities and numerical models, tests theorem hypotheses and degenerate cases, solves the root-counting cubic independently, and reads the actual JSON diagram specifications. Every plotted curve is evaluated inside its own sampled segment.

Independent bisection and NumPy's polynomial-root algorithm confirm three real roots of $x^3-3x+1$ in three separate monotone branches. Numerical grids independently locate the fencing optimum. Exact rational arithmetic checks tangent lengths, candidate values, inflection ordinates and completed squares. Direct numerical evaluation checks every printed approximation and the corrected source values.

Selected independently confirmed results include:

- The ladder rate is $-5/24$ m/s; the balloon rate is $1/(4\pi)$ cm/s.
- The tangent and normal to $x^3-3x$ at $x=2$ are $y=9x-16$ and $x+9y=20$.
- The three linear estimates are $5.04$, $1.1$ and $0.02$, with direct values and error signs checked.
- The absolute extrema of $x^3-3x$ on $[-2,2]$ are $\pm2$, with all attaining points identified.
- The corrected quartic inflection points are $(\pm\sqrt{2/3},-20/9)$.
- The window optimum is feasible and satisfies $h=r=10/(4+\pi)$; its completed-square identity proves the global maximum.
- The supporting line $y=6x-9$, exponential Jensen, Young's equality example, envelope contacts, director-circle distances and symmetric-optimisation equality cases all have direct checks.
- The editable window figure places both the feasible maximum and the positive-area $h=0$ endpoint on the actual area curve; the symmetric-cubic figure uses hollow markers for unattained endpoints.

These are targeted reproducible checks, not automated proof verification. Native-size visual inspection supplements them, including label placement, open/closed-point visibility, safe margins and continuation-page flow.

## IOQM boundary

Part II provides derivative-linked Olympiad and specialised extensions only. It is not a complete IOQM/RMO syllabus. Numerical checks are used as independent evidence for exact formulas, never as replacements for the printed proofs.

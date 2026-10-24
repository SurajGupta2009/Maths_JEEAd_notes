# Source Audit — Chapter 18: Differentiability & Methods

## Sources reviewed

- `notes/Differentiation-and-Methods/Differentiation-and-Methods.md` — the 703-line canonical module covering first principles, derivative rules, methods, higher derivatives, functional equations, Darboux and the MVT frontier.
- `notes/Differentiation-and-Methods/Differentiation-and-Methods — Paper.md` and `Differentiation-and-Methods — Solutions.md` — the companion paper and solutions. All **38 question/answer pairs** were inspected for method coverage, conventions and independent checks.
- `notes/Differentiation-and-Methods/assets/fig-01.svg` — the existing secant-to-tangent construction was inspected. The new notes use editable JSON secant/tangent graphs rather than embedding a screenshot.
- `notes/Applications-of-Derivatives/Applications-of-Derivatives.md` — headings were inspected to keep systematic applications in Chapter 19.
- Official JEE Advanced 2026 Mathematics syllabus, Differential Calculus: <https://jeeadv.ac.in/documents/jee-advanced-2026-syllabus.pdf>. The official/extension and Chapter 19 boundaries are mapped in `SCOPE.md`.

## Coverage map

The new lessons are a reorganized teaching edition, not a verbatim copy. Every source section and companion-question technique is included or explicitly assigned to a later chapter.

| Source material | New location |
|---|---|
| Chapter 1, S1–S2, P1–P2, Q1–Q4: definition, reciprocal, absolute value and $x|x|$ | `jee-01.md`, `jee-02.md` |
| Chapter 2, S3, P3–P4, Q5–Q10: product, quotient and power rules | `jee-03.md` |
| Chapter 3, S4–S5, P5–P6, Q11–Q16: chain rule and inverse trigonometry | `jee-04.md`, `jee-05.md` |
| S6–S7, P7–P9, Q17–Q23: implicit, logarithmic, parametric and basic higher derivatives | `jee-06.md`–`jee-09.md` |
| P11: recognize the logarithmic difference quotient | `jee-01.md` |
| Q26–Q28: basic tangent, normal and piecewise parameters | `jee-01.md`, `jee-09.md`, `jee-02.md` |
| S8, P12, Q24, Q32: Leibniz's rule for $x^2e^x$ and $x^2\cos x$ | `olympiad-01.md` |
| P10, Q25, Q34: reciprocal $n$th derivatives | `olympiad-02.md` |
| S11: $D^n\ln(x^2-1)$ on both real components | `olympiad-02.md` |
| S12, Q33: $x^2e^x$ and the exponential-cosine phase formula | `olympiad-01.md`, `olympiad-02.md` |
| P15: $y=\sqrt{1-x^2}$, its second derivative and differential identity | `olympiad-02.md` |
| S9, S13, Q31, Q35: exponential and additive functional equations | `olympiad-03.md` |
| Section 6.5 product-argument table: $f(xy)=f(x)+f(y)$ | `olympiad-03.md` |
| S14, Q36: discontinuous derivative and Darboux | `olympiad-04.md` |
| Q29–Q30: MVT for $x^2$ and Rolle for $x^3-x$ | `olympiad-05.md` |
| S10, P13–P14, Q37–Q38: sine, exponential and logarithmic derivative inequalities | `olympiad-05.md` |
| Appendix theory and quick formula sheet | redistributed through the matching core/extension lessons above |

The six-page visual lab uses additional exact models rather than duplicating the source's single static asset. It reinforces, but does not replace, the derivations. The source's motivational remark about differentiating an exponential defined by a series or limit was reviewed: this chapter does not silently assume termwise or limit differentiation. The exponential is characterized rigorously through the differentiable functional equation instead; series convergence theory is not smuggled into the method core.

## Scope decisions

Part I contains the complete differentiation-methods core, including the source's basic tangent, normal and piecewise-parameter questions. Higher-order closed forms, functional equations, Darboux and MVT inequalities are explicitly separated into Part II. Rolle/MVT retain their source placement in the synthesis stream; this is not a syllabus exclusion.

Advanced tangent/normal problems, related rates, monotonicity, extrema, convexity, optimization and curve sketching belong to **Chapter 19 — Applications of Derivatives**. The MVT inequalities here are a labelled forward bridge, not the start of that applications chapter.

## Corrections and necessary clarifications to source wording

- **S5, inverse-trigonometric simplification:** $\arctan(\tan(x/2))=x/2$ only for $-\pi<x<\pi$. On $((2k-1)\pi,(2k+1)\pi)$, the value is $x/2-k\pi$, with derivative $1/2$. Odd multiples of $\pi$ are excluded by $1+\cos x=0$; the figure shows the resulting branch jumps.
- **S11, real logarithm domain:** $y=\ln(x^2-1)$ has domain $|x|>1$. Writing $\ln(x-1)+\ln(x+1)$ is not real-valued on the negative component. The new derivation first obtains $y'=1/(x-1)+1/(x+1)$ as a rational identity and differentiates that on either component.
- **Section 6.4, general phase:** an unqualified $\theta=\arctan(b/a)$ does not determine a quadrant for all $a,b$. The notes require $(a,b)\ne(0,0)$ and choose $\phi$ through $\cos\phi=a/r$ and $\sin\phi=b/r$.
- **General power formulas:** for $(ax+b)^m$, factorial form is stated for nonnegative integer $m$ and $0\leq n\leq m$; higher derivatives vanish. General real powers use a falling-factorial product and a valid positive-base domain.
- **Exponential functional equation:** $f(0)=f(0)^2$ alone also permits the identically zero solution. The new proof explicitly excludes that solution, then proves $f(0)=1$ and strict positivity before deriving $f(x)=e^{cx}$. In the source case $f'(0)=2$, the answer is $e^{2x}$.
- **Section 6.5 product-argument formula:** for $f(xy)=f(x)+f(y)$ on positive reals, differentiate in $y$ and set $y=1$ to obtain $xf'(x)=f'(1)=a$, hence $f'(x)=a/x$. The source's malformed displayed differentiation formula is not reused.
- **P8/Q21 and parametric second derivatives:** for $x=t^2$, $y=t^3$, the first derivative is $3t/2$ where $dx/dt\ne0$, and the second is $3/(4t)$. The second derivative is not $y''(t)/x''(t)$.
- **P15, radical identity:** $y'=-x/y$ and $y''=-1/y^3$ give $(1-x^2)y''-xy'=-y$. The printed intermediate line was independently corrected during visual review to $-1/y+x^2/y=(x^2-1)/y$.
- **Piecewise differentiability:** matching $a=2$ alone is insufficient. Continuity gives $a+b=1$, so the complete answer is $a=2$, $b=-1$.
- **Darboux versus continuity:** the oscillatory example proves that $f'$ can exist everywhere without being continuous. Darboux's theorem still prohibits simple jump discontinuities of a genuine derivative; it does not prohibit oscillation.

## Independent verification

`scripts/math_checks.py` contains **402 exact/rational, numerical, visual-lab and editable-figure checks**. It recomputes displayed identities and numerical models, tests theorem hypotheses and degenerate cases, solves the implicit cubic independently, and reads the actual JSON diagram specifications. Every plotted curve is evaluated inside its own sampled segment.

Higher-order formulas are checked independently using trapezoidal Cauchy-integral differentiation, rather than by repeatedly evaluating the same printed formula. The checks cover both real components of $\ln(x^2-1)$, Leibniz products, real and integer powers, reciprocals and the exponential-cosine phase formula.

Selected independently confirmed values include:

- The piecewise parameters are $a=2$, $b=-1$; both one-sided slopes at $1$ are $2$.
- For $x=t^2$, $y=t^3$, $dy/dx=3t/2$ and $d^2y/dx^2=3/(4t)$, giving $3/4$ at $t=1$.
- $D^n(x^2e^x)=e^x[x^2+2nx+n(n-1)]$ and $D^n(e^x\cos x)=2^{n/2}e^x\cos(x+n\pi/4)$ agree with independent Cauchy-integral values through the tested orders.
- For $x^x$, the plotted tangent at $(1,1)$ has slope $1$. The ellipse example gives the same slope $-1/2$ by implicit and parametric methods.
- The oscillatory derivative takes the exact values $-1$ at $1/(2n\pi)$ and $1$ at $1/((2n+1)\pi)$, while its difference quotient at $0$ satisfies $|Q_h|\leq|h|$.
- Rolle gives $c=\pm1/\sqrt3$ for $x^3-x$ on $[-1,1]$; MVT gives $c=2$ for $x^2$ on $[1,3]$. Numerical samples verify the strict inequality cases and equality points for $e^x\geq1+x$ and $\ln x\leq x-1$.

These are targeted reproducible checks, not automated proof verification. Native-size visual inspection supplements them, including label placement, open/closed-point visibility, safe margins and continuation-page flow.

## IOQM boundary

Part II provides differentiation-linked Olympiad and specialised extensions only. It is not a complete IOQM/RMO syllabus. Numerical checks are used as independent evidence for exact formulas, never as replacements for the printed proofs.

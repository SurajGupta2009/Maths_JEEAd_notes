# Scope — Chapter 18: Differentiability & Methods

**Official JEE Advanced 2026 anchor (Differential Calculus):** derivative of a function; derivative algebra and the chain rule; derivatives of standard and inverse-trigonometric functions; implicit differentiation; derivatives up to order two; geometrical interpretation through tangents and normals; Rolle's theorem and Lagrange's Mean Value Theorem. The source's logarithmic and parametric methods are included as directly supporting computational techniques.

Official syllabus PDF: <https://jeeadv.ac.in/documents/jee-advanced-2026-syllabus.pdf>.

## Part I — JEE core and close applications

- Finite difference quotients, derivative from first principles, differentiability implying continuity, and the basic tangent to $y=x^2$.
- One-sided derivatives, corners and cusps, smooth piecewise joins, and the parameters $a=2$, $b=-1$ for the source's quadratic/linear junction.
- Linearity, product, quotient and power rules, including domain preservation after algebraic simplification.
- A rigorous chain-rule account and standard derivatives of trigonometric, exponential and logarithmic functions.
- Inverse-function differentiation, principal inverse-trigonometric derivatives and branch-safe simplification of $\arctan(\tan(x/2))$.
- Implicit, logarithmic and parametric differentiation, including first and second parametric derivatives and the condition $dx/dt\ne0$ for the displayed ratios.
- Higher derivatives through basic cycles and exponentials, the normal to $y=x^3$ at $(1,1)$, finite-difference diagnostics and method selection.
- Six visual-method sheets joining exact calculations to secants, smooth joins, local slopes, an ellipse, $x^x$ and the semicubical parabola.

## Part II — Olympiad / specialised extensions

- Leibniz's rule, polynomial termination, and closed forms for $x^2e^x$ and $x^2\cos x$.
- Falling-factorial power formulas, reciprocal and logarithmic $n$th derivatives, exponential-trigonometric phase formulas and the radical differential identity.
- Exponential, additive and product-argument functional equations under differentiability, with zero solutions and real domains handled first.
- An everywhere-existing but discontinuous derivative and Darboux's intermediate value property.
- Rolle's theorem, the Mean Value Theorem, sine and exponential bounds, and $\ln x\leq x-1$ as a forward bridge to derivative applications.

These are explicitly labelled topic-linked extensions, not a complete IOQM/RMO course. Placement of Rolle/MVT in the source's synthesis stream is organizational; it is not a claim that those theorems lie outside JEE. No extension is blended into the core without a label.

## Chapter boundaries

- **Chapter 17:** limit laws and general continuity theory remain with Limits & Continuity. This chapter uses only the limits needed to define and compute derivatives.
- **Chapter 19:** systematic monotonicity, extrema, convexity, optimization, related rates, curve sketching and advanced tangent/normal applications remain with Applications of Derivatives. Only the source's basic tangent/normal and the labelled MVT bridge appear here.
- **Later calculus chapters:** antiderivatives and differential-equation solution methods are not introduced merely because a derivative equation can be written. The zero-derivative consequence used in functional equations is proved through MVT in Extension V.

## Conventions and hypotheses

- Ordinary differentiability requires a finite two-sided derivative; at a one-sided domain point, the corresponding one-sided notion is used. Continuity alone does not imply differentiability.
- Piecewise branch formulas are used only after the function value and continuity at the junction are secured.
- Real logarithms and real variable powers require their stated domains. In particular, $u(x)^{v(x)}$ is differentiated logarithmically on $u(x)>0$.
- $\arctan(\tan u)=u$ holds only on the principal interval. On $((2k-1)\pi,(2k+1)\pi)$, the source expression simplifies to $x/2-k\pi$, not globally to $x/2$.
- For $y=\ln(x^2-1)$, the real domain is $|x|>1$. The derivative is decomposed as a rational identity on both components; the original logarithm is not split into non-real logs on the negative component.
- Parametric formulas require $dx/dt\ne0$ at the substitution point. A second derivative differentiates $dy/dx$ with respect to $t$ and divides by $dx/dt$ again.
- General real-power $n$th derivatives use a falling factorial and a valid positive-base domain. Nonnegative integer powers terminate after their degree.
- Functional-equation differentiation requires regularity. The nonzero exponential case excludes the identically zero solution before deriving $f(0)=1$ and positivity.
- A derivative need not be continuous, but it has the Darboux intermediate value property. Rolle/MVT conclusions require continuity on the closed interval and differentiability in its interior.

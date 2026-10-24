---
id: jee-01
part: jee
title: "Terminology, Verification and Solution Intervals"
---

## Read a differential equation before solving it

A differential equation relates an unknown function to its derivatives. Its **order** is the highest derivative present. Its **degree** is the power of that highest derivative after the equation has been written as a polynomial in the derivatives, with no radical or transcendental operation applied to a derivative.

A solution is a function satisfying the equation on a stated **interval**. An initial-value problem, or IVP, also prescribes values such as $y(x_0)=y_0$. A general solution contains arbitrary constants; a particular solution results from determining them. Constants do not remove the need to state the domain.

:::diagram
{
  "type": "table",
  "strict_fit": true,
  "min_fontsize": 9,
  "title": "The first four checks prevent most notation errors",
  "columns": ["Check", "Ask", "Trap"],
  "col_widths": [0.18, 0.40, 0.42],
  "rows": [
    ["Order", "Highest derivative?", "Largest power instead"],
    ["Degree", "Power of that derivative?", "Ignoring radicals"],
    ["Solution", "Identity after substitution?", "One-point check only"],
    ["Interval", "Where is it defined?", "Crossing a pole or domain edge"]
  ],
  "caption": "Verification is an identity on an interval, not a numerical coincidence at a single x-value."
}
:::

:::example title="S1 and Q2: verify rather than solve"
For $y=e^{2x}$,
$$
\frac{dy}{dx}=2e^{2x}=2y,
\qquad \frac{dy}{dx}-2y=0.
$$
The equality holds for every real $x$, so $e^{2x}$ is a solution on $(-\infty,\infty)$. More generally, $y=Ce^{2x}$ solves the same equation; the initial condition $y(0)=1$ selects $C=1$.
:::

:::example title="P1 and Q1: order is not the largest visible power"
In
$$
\frac{d^3y}{dx^3}+\left(\frac{dy}{dx}\right)^4+y=0,
$$
the highest derivative is $y'''$, so the order is $3$. Its exponent is $1$, so the degree is $1$. The exponent $4$ belongs to the lower derivative $y'$ and does not determine either answer.
:::

## Two practical habits

- **Verify by differentiation:** compute the required derivatives, substitute, and simplify to zero or to the prescribed right-hand side.
- **Carry the interval:** formulas containing $\ln x$, $1/x$, or a denominator may represent different solution branches on different intervals.

:::warn title="A formula can solve an equation without containing every solution"
A finite choice of an arbitrary constant cannot always recover an equilibrium or singular solution. Keep track of every division by a quantity that might be zero; the Bernoulli, Lagrange and Riccati lessons apply this audit explicitly.
:::

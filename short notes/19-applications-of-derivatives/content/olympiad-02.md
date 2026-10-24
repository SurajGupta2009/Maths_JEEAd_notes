---
id: olympiad-02
part: olympiad
title: "Extension II — Young, Cauchy and AM–GM"
---

## Young's inequality is weighted AM–GM in exponential form

For $a,b\geq0$ and conjugate exponents $p,q>1$ with $1/p+1/q=1$,
$$
ab\leq\frac{a^p}{p}+\frac{b^q}{q}.
$$
For positive $a,b$, weighted AM–GM with weights $1/p$ and $1/q$ gives
$$
\frac{a^p}{p}+\frac{b^q}{q}
\geq(a^p)^{1/p}(b^q)^{1/q}=ab.
$$
Equality holds exactly when $a^p=b^q$, equivalently $a^{p-1}=b$; the boundary equality cases are checked directly.

:::example title="Young with p=q=2 proves two-variable AM–GM"
For $a,b>0$, apply Young to $\sqrt{a}$ and $\sqrt{b}$:
$$
\sqrt{ab}\leq\frac{(\sqrt{a})^2+(\sqrt{b})^2}{2}
=\frac{a+b}{2}.
$$
Equality holds exactly when $\sqrt{a}=\sqrt{b}$, hence when $a=b$.
:::

## AM–GM for three positive numbers from concavity

Since $(\ln x)''=-1/x^2<0$, Jensen for the concave logarithm reverses the inequality:
$$
\frac{\ln x+\ln y+\ln z}{3}
\leq\ln\left(\frac{x+y+z}{3}\right).
$$
Exponentiating gives
$$
\sqrt[3]{xyz}\leq\frac{x+y+z}{3},
$$
with equality exactly when $x=y=z$. This proves Q36. The same concave-log Jensen argument with weights $1/p$ and $1/q$ proves the weighted AM–GM step used above.

## Cauchy–Schwarz starts with a direct square

For all real $a,b$,
$$
a^2+b^2-2ab=(a-b)^2\geq0,
$$
so $a^2+b^2\geq2ab$, with equality exactly when $a=b$. The source's alternative expression containing $\sqrt{a^2b^2}$ equals $|ab|$, not $ab$; it is invalid when $ab<0$. The displayed square is valid for all real numbers.

Summing the two-variable inequality with suitable normalisation leads to Cauchy–Schwarz. In Engel form, for real $a_i$ and positive $x_i$,
$$
\left(\sum_{i=1}^n a_i\right)^2
=\left(\sum_{i=1}^n\frac{a_i}{\sqrt{x_i}}\sqrt{x_i}\right)^2
\leq\left(\sum_{i=1}^n\frac{a_i^2}{x_i}\right)
 \left(\sum_{i=1}^n x_i\right).
$$
Thus $\sum a_i^2/x_i\geq(\sum a_i)^2/\sum x_i$.

:::diagram
{
  "type": "table",
  "title": "The inequality family has distinct hypotheses and equality cases",
  "columns": ["Result", "Main hypotheses", "Equality"],
  "rows": [
    ["Young", "1/p+1/q=1", "a^p=b^q"],
    ["2-variable AM-GM", "a,b>0", "a=b"],
    ["3-variable AM-GM", "x,y,z>0", "x=y=z"],
    ["Square bound", "a,b real", "a=b"],
    ["Cauchy Engel", "x_i>0", "a_i proportional to x_i"]
  ],
  "col_widths": [0.28, 0.38, 0.34],
  "caption": "Use the signed square for all real a,b. Use positive variables when logarithms, geometric means or Engel denominators require them."
}
:::

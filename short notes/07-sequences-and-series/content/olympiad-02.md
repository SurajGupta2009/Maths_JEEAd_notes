---
id: olympiad-02
part: olympiad
title: "Extension — Recurrences, Characteristic Equations, and Generating Functions"
---

:::assume title="STATUS — olympiad/specialised extension (IOQM/RMO-flavoured)"
Linear recurrences and generating functions sit outside the official AP/GP syllabus lines; they are the standard Olympiad machinery for sequences defined inductively.
:::

## First- and second-order recurrences

:::derive title="Fixed-point shift for aₙ = p·aₙ₋₁ + q"
Seek $L$ with $L = pL + q$, i.e. $L = \frac{q}{1 - p}$ ($p \neq 1$). Then $a_{n} - L = p(a_{n - 1} - L)$: a GP in disguise, so $a_{n} = L + (a_{1} - L)p^{n - 1}$. Worked: $a_{n} = 2a_{n - 1} + 1$, $a_{1} = 1$: $L = -1$, $a_{n} = 2^{n} - 1$ ✓ ($1, 3, 7, 15, \ldots$). If $p = 1$ it is an AP instead.
:::

:::key title="Characteristic equation for aₙ = p·aₙ₋₁ + q·aₙ₋₂"
Try $a_{n} = r^{n}$: the **characteristic equation** is $r^{2} - pr - q = 0$. Distinct roots $r_{1} \neq r_{2}$: $a_{n} = A r_{1}^{n} + B r_{2}^{n}$; repeated root $r$: $a_{n} = (A + Bn)r^{n}$. Constants from two initial values. Always verify the closed form against the first computed terms.
:::

## Generating functions

:::key title="The clothesline: operations on G(x) are operations on the sequence"
$G(x) = \sum_{n \geq 0} a_{n}x^{n}$. Multiply by $x$: shift right. Multiply by $\frac{1}{1 - x}$: replace $a_{n}$ by its partial sums. Differentiate: multiply $a_{n}$ by $n$. $G(-x)$: alternate signs. Recurrences become algebraic equations for $G(x)$; solving and expanding reads off $a_{n}$.
:::

:::derive title="Fibonacci: G(x) to Binet in three moves"
With $F_{0} = 0$, $F_{1} = 1$, $F_{n} = F_{n - 1} + F_{n - 2}$: comparing coefficients of $x^{n}$ ($n \geq 2$) in $F(x)$ and $xF(x) + x^{2}F(x) + x$ gives

$$F(x) = \frac{x}{1 - x - x^{2}} = \frac{x}{(1 - \varphi x)(1 - \psi x)}, \qquad \varphi, \psi = \frac{1 \pm \sqrt{5}}{2}$$

Partial fractions: $F(x) = \frac{1}{\sqrt{5}}\left(\frac{1}{1 - \varphi x} - \frac{1}{1 - \psi x}\right)$; expanding both geometric series,

$$F_{n} = \frac{\varphi^{n} - \psi^{n}}{\sqrt{5}}$$

Checks: $F_{1} = \frac{2.236068}{2.236068} = 1$ ✓; $F_{7} = 13$ ✓; $F_{10} = 55$ ✓. This is Binet with no induction — pure algebra (and it matches the quadratic route of chapter 6, Olympiad sheet 01).
:::

:::warn title="Common traps — recurrences and generating functions"
- Characteristic equation sign: for $a_{n} = pa_{n - 1} + qa_{n - 2}$ it is $r^{2} - pr - q = 0$, not $r^{2} + pr + q$.
- Repeated-root case forgotten: $(A + Bn)r^{n}$, not $Ar^{n}$.
- Closed form not checked at $n = 1, 2$: index-shift errors are invisible otherwise.
- Generating-function manipulations treated as convergent series: for coefficient extraction they are formal power series; convergence is a separate question.
:::

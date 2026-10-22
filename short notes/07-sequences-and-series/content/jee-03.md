---
id: jee-03
part: jee
title: "AM–GM and the Special Sums Σk, Σk², Σk³ — The Syllabus Power Sums"
---

## The means and the master inequality

:::key title="AM ≥ GM, with equality condition"
For positive reals, $\frac{a + b}{2} \geq \sqrt{ab}$, equality iff $a = b$; for $n$ positive numbers, $\frac{a_{1} + \cdots + a_{n}}{n} \geq \left(a_{1} \cdots a_{n}\right)^{1/n}$, equality iff all are equal. The hypothesis **positive** is not decoration: AM–GM is false for negative numbers.
:::

:::example title="Worked — AM–GM as an optimiser"
Least value of $x + \frac{4}{x}$ for $x > 0$: AM–GM gives $\geq 2\sqrt{x \cdot \frac{4}{x}} = 4$, attained when $x = \frac{4}{x}$, i.e. $x = 2$ ✓. The recipe: force the product to be constant, apply AM–GM, then **check the equality case is attainable** in the domain. If equality needs $x = 2$ but the domain is $x \geq 3$, the bound is not the minimum — the function is increasing there and the answer is at $x = 3$ (value $\frac{13}{3}$). Unattainable equality is the classic trap.
:::

## The special sums (official syllabus)

:::derive title="Where the power sums come from — one telescoping identity"
$(k + 1)^{m + 1} - k^{m + 1}$ expands with leading terms $(m + 1)k^{m} + \cdots$; summing over $k = 1..n$ telescopes the left side to $(n + 1)^{m + 1} - 1$ and yields $\sum k^{m}$ in terms of lower sums. With $m = 1$: $(k+1)^{2} - k^{2} = 2k + 1$ gives $\sum k = \frac{n(n + 1)}{2}$; iterating gives the rest. You can re-derive any of them in the exam if forgotten.
:::

:::key title="Memorise these three (the fourth is a bonus)"
$$\sum_{k=1}^{n} k = \frac{n(n + 1)}{2}, \qquad \sum_{k=1}^{n} k^{2} = \frac{n(n + 1)(2n + 1)}{6}$$

$$\sum_{k=1}^{n} k^{3} = \left(\frac{n(n + 1)}{2}\right)^{2}$$

The cube sum is the **square** of the first sum — remember it as a picture, not a formula. (Bonus, beyond the syllabus list: $\sum k^{4} = \frac{n(n + 1)(2n + 1)(3n^{2} + 3n - 1)}{30}$.)
:::

:::example title="Worked — special sums"
$\sum_{1}^{10} k^{2} = \frac{10 \cdot 11 \cdot 21}{6} = 385$; $\sum_{1}^{10} k^{3} = 55^{2} = 3025$. Mixed: $\sum_{k=1}^{n} (3k^{2} - 2k) = 3 \cdot \frac{n(n + 1)(2n + 1)}{6} - 2 \cdot \frac{n(n + 1)}{2} = \frac{n(n + 1)(2n + 1)}{2} - n(n + 1)$; at $n = 10$: $1155 - 110 = 1045$ (direct check by script in math_checks). Sums of odd/even terms: first $n$ odd numbers sum to $n^{2}$ (AP or $2\sum k - n$).
:::

:::warn title="Common traps — means and sums"
- AM–GM applied to quantities that can be negative, or with equality case outside the domain.
- "$n$-term AM–GM" confused with repeated two-term AM–GM giving a weaker bound whose equality case is inconsistent.
- $\sum k^{3}$ written as $\frac{n(n+1)}{2}$ (forgotten square).
- Sums indexed from $k = 0$ or shifted ranges substituted into formulas built for $k = 1..n$: adjust by subtracting the missing head.
:::

:::intuition title="Reading a sum before computing it"
Ask: is the general term a polynomial in $k$? Then split into power sums. A product of polynomial × exponential? AGP (sheet 04). A rational function with AP-spaced factors in the denominator? Telescope (sheet 04). Anything else, suspect a disguised difference $f(k) - f(k + 1)$.
:::

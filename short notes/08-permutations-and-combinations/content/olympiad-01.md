---
id: olympiad-01
part: olympiad
title: "Extension — Lattice Paths, Reflection, Catalan Numbers, and the Ballot Theorem"
---

:::assume title="STATUS — olympiad/specialised extension (IOQM/RMO-flavoured)"
Lattice-path methods, Catalan numbers and reflection arguments are beyond the official P&C syllabus lines; they are the standard Olympiad continuation of $\binom{n}{r}$ as a path count.
:::

:::key title="Paths are binomial coefficients"
Monotone paths from $(0, 0)$ to $(a, b)$ (steps right/up): choose which steps are up: $\binom{a + b}{b}$. Paths that never rise above the diagonal $y = x$ to $(n, n)$: the **Catalan number**

$$C_{n} = \binom{2n}{n} - \binom{2n}{n + 1} = \frac{1}{n + 1}\binom{2n}{n} = 1, 1, 2, 5, 14, 42, \ldots$$

**Reflection principle:** a "bad" path first touching $y = x + 1$, reflected up to that point, bijects with all paths from $(-1, 1)$ to $(n, n)$ — $\binom{2n}{n - 1}$ of them. Subtract. Paths to $(4, 4)$ staying weakly below the diagonal: $C_{4} = 70 - 56 = 14$.
:::

:::key title="Ballot theorem"
Votes $p$ for A, $q$ for B, $p > q$: counting orders where A is **strictly ahead throughout**: $\frac{p - q}{p + q}\binom{p + q}{q}$. For $p = 5$, $q = 3$: $\frac{2}{8} \cdot 56 = 14$. The same reflection gives paths to $(a, b)$, $a \geq b$, never above the diagonal: $\frac{a - b + 1}{a + 1}\binom{a + b}{b}$.
:::

:::intuition title="Why Catalan counts everything"
Dyck paths, balanced parentheses, full binary trees, polygon triangulations, non-crossing matchings share one decomposition: *first return splits the object into inside × outside*, giving $C_{n + 1} = \sum_{i=0}^{n} C_{i} C_{n - i}$. Recognising the convolution shape is the solution; the closed form follows. Brute-force checks: Dyck paths of semilength $n \leq 7$ counted by enumeration in math_checks.
:::

:::warn title="Common traps — path counts"
- "Never above" vs "never below" and weak vs strict inequalities change which line to reflect in ($y = x + 1$ vs $y = x - 1$): draw the first forbidden point.
- Ballot needs $p > q$ strictly; ties throughout (weakly ahead) is the Catalan-style variant with a different formula.
:::

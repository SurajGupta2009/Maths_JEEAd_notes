---
id: oly-03
part: olympiad
title: "Extension — Hidden-Structure Identities and Constraint Problems"
---

:::assume title="STATUS — olympiad/specialised extension (IOQM/RMO + coaching classics)"
These are "prove/evaluate with structure" problems: symmetric conditions on $x, y, z$ forcing angle sums, nested-inverse expressions, and range problems where the *branch constraints* are the hidden system of inequalities. All are derivable from Part I; the added value is problem-recognition. No claim is made that such items "can never appear" in JEE Advanced — they are simply the harder end of the same toolkit.
:::

## The classic: x + y + z = xyz forces A + B + C = π

:::key title="Theorem (with its hypothesis)"
If $x, y, z > 0$ and $x + y + z = xyz$, then

$$\tan^{-1}x + \tan^{-1}y + \tan^{-1}z = \pi.$$

More symmetrically: with $A = \tan^{-1}x$ etc. all in $(0, \frac{\pi}{2})$, the condition $x + y + z = xyz$ is exactly $\tan(A + B + C) = 0$ — and the range bookkeeping ($A + B + C \in (0, \frac{3\pi}{2})$) pins $A + B + C = \pi$ (it cannot be $0$: each angle is positive).
:::

:::derive title="Proof — expand $\tan(A+B+C)$"
With $A = \tan^{-1}x, B = \tan^{-1}y, C = \tan^{-1}z$:

$$\tan(A + B + C) = \frac{x + y + z - xyz}{1 - (xy + yz + zx)}.$$

Hypothesis: the numerator vanishes. So either the denominator is nonzero and $\tan(A+B+C) = 0$, giving $A+B+C = k\pi$; since $A+B+C \in (0, \frac{3\pi}{2})$ the only candidate is $\pi$. Or the denominator vanishes too ($xy + yz + zx = 1$): then $A + B + C \in \{\frac{\pi}{2}, \frac{3\pi}{2}\}$ — one checks directly that $x,y,z > 0$ with $x+y+z = xyz$ forces $xy + yz + zx > 1$, so this degenerate case cannot occur (e.g. by AM–GM: $xyz = x+y+z \geq 3\sqrt[3]{xyz}$ gives $xyz \geq 3\sqrt{3}$, while $xy + yz + zx \geq 3(xyz)^{2/3} \geq 9 > 1$). ∎

Sanity: $x = y = z = \sqrt{3}$: sum $= 3\sqrt{3}$, product $= 3\sqrt{3}$ ✓, and $3\tan^{-1}\sqrt{3} = 3\cdot\frac{\pi}{3} = \pi$ ✓.
:::

:::example title="Companion identity — $xy + yz + zx = 1$ forces the sum to $\frac{\pi}{2}$"
If $x, y > 0$ and $xy < 1$ then $\tan^{-1}x + \tan^{-1}y = \tan^{-1}\frac{x + y}{1 - xy}$; with $x, y, z > 0$ and $xy + yz + zx = 1$, pairwise: $\tan^{-1}x + \tan^{-1}y = \tan^{-1}\frac{x+y}{1-xy}$ and $1 - xy = z(x + y)$, so $\frac{x+y}{1-xy} = \frac{1}{z}$ and $\tan^{-1}x + \tan^{-1}y = \tan^{-1}\frac{1}{z} = \frac{\pi}{2} - \tan^{-1}z$ (complementary pair!). Hence

$$\tan^{-1}x + \tan^{-1}y + \tan^{-1}z = \frac{\pi}{2}$$

$$\text{whenever } x,y,z > 0,\ xy + yz + zx = 1.$$

(Condition $xy < 1$ is automatic: $xy < xy + yz + zx = 1$ ✓.) Example: $x = y = \frac{1}{2}$, then $z = \frac{1 - 1/4}{1} = \frac{3}{4}$... check: $xy + yz + zx = \frac{1}{4} + \frac{3}{8} + \frac{3}{8} = 1$ ✓ and $2\tan^{-1}\frac{1}{2} + \tan^{-1}\frac{3}{4} \approx 0.9273 + 0.6435 = 1.5708 = \frac{\pi}{2}$ ✓.
:::

## Nested and mixed constraint problems

:::app title="Pattern 1 — nested arctans: $\tan^{-1}\left(\frac{1}{2}\right) + \tan^{-1}\left(\frac{1}{5}\right) + \tan^{-1}\left(\frac{1}{8}\right)$-style chains"
Add two at a time with the $xy < 1$ face (small positive arguments keep you in the plain case): $\tan^{-1}\frac{1}{2} + \tan^{-1}\frac{1}{5} = \tan^{-1}\frac{7}{9}$ (since $\frac{1/2 + 1/5}{1 - 1/10} = \frac{7/10}{9/10}$); then $+ \tan^{-1}\frac{1}{8}$: $\tan^{-1}\frac{7}{9} + \tan^{-1}\frac{1}{8} = \tan^{-1}\frac{65/72}{65/72} = \tan^{-1}1 = \frac{\pi}{4}$. So the chain sums to $\frac{\pi}{4}$ exactly. The discipline: after each addition, re-check the $xy$ condition with the *new* combined argument.
:::

:::app title="Pattern 2 — the branch constraints as a system: solve $\sin^{-1}x + \sin^{-1}y = \frac{\pi}{2}$ given $x + y = 1$"
Take the sine of both sides: $x\sqrt{1 - y^{2}} + y\sqrt{1 - x^{2}} = 1$. With $y = 1 - x$ this becomes $x\sqrt{2x - x^{2}} + (1 - x)\sqrt{2x - x^{2}} = \sqrt{2x - x^{2}} = 1$, so $2x - x^{2} = 1$, $(x - 1)^{2} = 0$, $x = 1, y = 0$. Check: $\sin^{-1}1 + \sin^{-1}0 = \frac{\pi}{2}$ ✓. Alternatively read the equation itself: $\sin^{-1}y = \frac{\pi}{2} - \sin^{-1}x = \cos^{-1}x = \sin^{-1}\sqrt{1 - x^{2}}$ needs $y = \sqrt{1 - x^{2}}$ (branch: $y \geq 0$) — together with $x + y = 1$: $x + \sqrt{1 - x^{2}} = 1$ gives $x \in \{0, 1\}$, and both $(1, 0)$ and $(0, 1)$ work by symmetry. **Two solutions** — a squaring route may lose one; the branch route sees both.
:::

:::app title="Pattern 3 — bounding an arctan sum without computing it"
For positive $a_i$, $\tan^{-1}$ is increasing and concave on $\mathbb{R}^{+}$, but the exam-legitimate bound is cruder: $\tan^{-1}x < \frac{\pi}{2}$ and $\tan^{-1}x \leq x$ for $x \geq 0$ (from the graph: tangent line at $0$ is $y = x$, curve below it). So e.g. $\sum_{k=1}^{100} \tan^{-1}\frac{1}{k^{2}} < \sum_{k=1}^{100} \frac{1}{k^{2}} < \frac{\pi^{2}}{6} < 2$, and since also each term $> 0$ the sum is trapped in $(0, 2)$; sharper telescoping (oly-02) gives its exact value when the shape allows. Bounds + exact-when-possible is the olympiad habit.
:::

:::warn title="Traps — structure problems"
- $x + y + z = xyz \Rightarrow$ sum $=\pi$ **requires positivity** ($x, y, z$ of mixed signs can give $0$ or $-\pi$; e.g. $x = y = z = 0$ satisfies the equation with sum $0$).
- $xy + yz + zx = 1$ identity uses the complementary pair $\tan^{-1}\frac{1}{z} = \frac{\pi}{2} - \tan^{-1}z$ — true because $\frac{1}{z} > 0$; for $z < 0$ it fails (both sides off by $\pi$-jumps).
- In constraint systems, the *range of each inverse* is a real inequality: $\sin^{-1}x + \sin^{-1}y = \frac{\pi}{2}$ already forces $x, y \geq 0$ (LHS $\geq -\pi$, but for the sum to reach $\frac{\pi}{2}$ with both terms $\leq \frac{\pi}{2}$ and $\geq -\frac{\pi}{2}$ you need... precisely: $x = \sin A, y = \sin B$ with $A + B = \frac{\pi}{2}$, $A, B \in [-\frac{\pi}{2}, \frac{\pi}{2}]$ forces $A, B \in [0, \frac{\pi}{2}]$, so $x, y \geq 0$ and $y = \cos A = \sqrt{1 - x^{2}}$: the solution set is exactly the quarter circle $x^{2} + y^{2} = 1$, $x, y \geq 0$ — the constraint $x + y = 1$ then intersects it in $\{(1,0), (0,1)\}$ as computed).
- Two-step telescopes and nested arctans: re-check the addition-formula condition after **every** combination; a chain is only as safe as its last link.
:::

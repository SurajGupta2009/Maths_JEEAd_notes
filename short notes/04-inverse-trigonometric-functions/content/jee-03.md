---
id: jee-03
part: jee
title: "tan⁻¹ Addition Formulas — With Their Branch Conditions"
---

## The master formula and why conditions are unavoidable

Take tangents of $\tan^{-1}x \pm \tan^{-1}y$ using the compound-angle formula. The *tangent* of the answer is never the issue — the issue is which **branch of $\tan^{-1}$** the sum lands in. Since each of $\tan^{-1}x, \tan^{-1}y \in (-\pi/2, \pi/2)$, their sum lies in $(-\pi, \pi)$; and $\tan^{-1}$ returns values only in $(-\pi/2, \pi/2)$. Whenever the true sum exits that window, a $\pm\pi$ correction is mandatory.

:::key title="Addition and subtraction — statement with corrections"
For all real $x, y$:

$$\tan^{-1}x + \tan^{-1}y = \tan^{-1}\frac{x+y}{1-xy} \quad \text{if } xy < 1$$

$$\tan^{-1}x + \tan^{-1}y = \pi + \tan^{-1}\frac{x+y}{1-xy}$$

$$\text{if } xy > 1 \text{ and } x > 0$$

$$\tan^{-1}x + \tan^{-1}y = -\pi + \tan^{-1}\frac{x+y}{1-xy}$$

$$\text{if } xy > 1 \text{ and } x < 0$$

$$\tan^{-1}x - \tan^{-1}y = \tan^{-1}\frac{x-y}{1+xy} \quad \text{if } xy > -1$$

with the analogous $\pm\pi$ corrections when $xy < -1$ (sign chosen so the final answer lies in $(-\pi,\pi)$, matching the true sum).

**Domain wall:** the fraction is undefined at $xy = 1$ (sum $= \pm\pi/2$) and $xy = -1$ (difference $= \pm\pi/2$) — those are boundary cases, handled by direct branch arithmetic, not by the formula.
:::

:::derive title="Derivation of the corrections — sign of the cosine decides"
Let $A = \tan^{-1}x$, $B = \tan^{-1}y$, $S = A + B \in (-\pi, \pi)$. First, $\tan S = \frac{x + y}{1 - xy}$ (compound angle), so $S = \tan^{-1}\frac{x+y}{1-xy} + k\pi$ for some integer $k \in \{-1, 0, 1\}$. Which $k$? Ask where $S$ sits on $(-\pi, \pi)$ via its cosine:

$$\cos S = \cos A \cos B\,(1 - \tan A \tan B)$$

$$\cos A \cos B\,(1 - xy)$$

and $\cos A, \cos B > 0$ strictly (both branches inside $(-\pi/2, \pi/2)$), so $\operatorname{sign}(\cos S) = \operatorname{sign}(1 - xy)$:

- $xy < 1$: $\cos S > 0$ forces $S \in (-\pi/2, \pi/2)$ — the branch itself: $k = 0$.
- $xy > 1$, $x > 0$ (then $y > 0$): $S \in (\pi/2, \pi)$: $k = +1$.
- $xy > 1$, $x < 0$ (then $y < 0$): $S \in (-\pi, -\pi/2)$: $k = -1$.
- $xy = 1$: $\cos S = 0$ and $S = \pm\pi/2$ — compute directly, the fraction is void.

∎ (Every line of the table is machine-checked at adversarial points in `math_checks.py`.)
:::

:::example title="Worked — $\tan^{-1}2 + \tan^{-1}3$ and the sign trap"
$x = 2, y = 3$: $xy = 6 > 1$ and $x > 0$, so the correction fires:

$$\tan^{-1}2 + \tan^{-1}3 = \pi + \tan^{-1}\frac{5}{1-6} = \pi + \tan^{-1}(-1)$$

$$\pi - \frac{\pi}{4} = \frac{3\pi}{4}.$$

Without the correction you would answer $-\pi/4$ — wrong quadrant. Sanity: $\tan^{-1}2 \approx 1.107$, $\tan^{-1}3 \approx 1.249$, sum $\approx 2.356 = \frac{3\pi}{4}$ ✓.

By contrast $\tan^{-1}\frac{1}{2} + \tan^{-1}\frac{1}{3}$: $xy = \frac{1}{6} < 1$, no correction:

$$\tan^{-1}\frac{1}{2} + \tan^{-1}\frac{1}{3}$$

$$ = \tan^{-1}\left(\frac{\frac{1}{2} + \frac{1}{3}}{1 - \frac{1}{6}}\right)$$

$$ = \tan^{-1}1 = \frac{\pi}{4}.$$
:::

## The 2tan⁻¹x chain — three faces, three conditions

Set $y = x$ in the addition formula, and separately take $\sin$/$\cos$ of $2\tan^{-1}x$ via the triangle of sheet 02. All three forms are JEE staples:

:::key title="$2\tan^{-1}x$ in three forms (conditions are part of the formula)"
$$2\tan^{-1}x = \tan^{-1}\frac{2x}{1-x^{2}} \quad |x| < 1$$

$$2\tan^{-1}x = \pi + \tan^{-1}\frac{2x}{1-x^{2}} \quad x > 1;$$

$$= -\pi + \tan^{-1}\frac{2x}{1-x^{2}} \quad x < -1$$

$$2\tan^{-1}x = \sin^{-1}\frac{2x}{1+x^{2}} \quad |x| \leq 1$$

$$2\tan^{-1}x = \pi - \sin^{-1}\frac{2x}{1+x^{2}} \quad x > 1;$$

$$= -\pi - \sin^{-1}\frac{2x}{1+x^{2}} \quad x < -1$$

$$2\tan^{-1}x = \cos^{-1}\frac{1-x^{2}}{1+x^{2}} \quad x \geq 0;$$

$$= -\cos^{-1}\frac{1-x^{2}}{1+x^{2}} \quad x < 0$$
:::

:::derive title="Where the $\sin^{-1}$ face comes from"
Let $\theta = \tan^{-1}x$, so $\tan\theta = x$. Then $\sin 2\theta = \frac{2\tan\theta}{1 + \tan^{2}\theta} = \frac{2x}{1 + x^{2}}$. Now branch-check: for $|x| \leq 1$, $2\theta \in [-\pi/2, \pi/2]$ and $\sin^{-1}(\sin 2\theta) = 2\theta$ ✓. For $x > 1$, $2\theta \in (\pi/2, \pi)$, so $2\theta = \pi - \sin^{-1}(\sin 2\theta)$ ✓ (mirror-angle read of sheet 02). The $\cos^{-1}$ face: $\cos 2\theta = \frac{1 - x^{2}}{1 + x^{2}}$, and $2\theta \in [0,\pi]$ exactly when $\theta \geq 0$, i.e. $x \geq 0$ ✓. Same computation, three branch bookkeepings.
:::

:::app title="Standard applications — simplification and telescoping"
1. **Simplify a sum of two arctans**: check $xy$ against $1$ first, then apply the table. E.g. $\tan^{-1}\frac{1}{7} + \tan^{-1}\frac{1}{8}$: $xy = \frac{1}{56} < 1$ → $\tan^{-1}\frac{\frac{1}{7}+\frac{1}{8}}{1 - \frac{1}{56}} = \tan^{-1}\frac{15/56}{55/56} = \tan^{-1}\frac{3}{11}$.

2. **Sums that telescope**: recognise $\tan^{-1}\frac{a - b}{1 + ab} = \tan^{-1}a - \tan^{-1}b$ (when $ab > -1$). E.g.

$$\sum_{k=1}^{n} \tan^{-1}\frac{1}{1 + k + k^{2}} = \sum_{k=1}^{n}[\tan^{-1}(k+1) - \tan^{-1}k]$$

$$\tan^{-1}(n+1) - \frac{\pi}{4}.$$

because $1 + k + k^{2} = 1 + k(k+1)$ and $\frac{(k+1) - k}{1 + k(k+1)} = \frac{1}{1 + k + k^{2}}$ ✓. (Olympiad sheets push this hard; the exam-visible core is the identity itself.)

3. **Equations**: $2\tan^{-1}x = \sin^{-1}x$-style problems: convert both sides to one inverse via the chain, then use **injectivity of the outer inverse**, never of $x \mapsto$ expression.
:::

:::warn title="Common traps — the addition formulas"
- Forgetting the $\pm\pi$: $\tan^{-1}2 + \tan^{-1}3 = \frac{3\pi}{4}$, not $-\frac{\pi}{4}$. Rule of thumb: two positive arctans of numbers $> 1$ each... more precisely if $x, y > 0$ and $xy > 1$ the sum exceeds $\frac{\pi}{2}$ and needs $+\pi$.
- Writing $\tan^{-1}x + \tan^{-1}y = \tan^{-1}\frac{x+y}{1-xy}$ with **no condition at all** — the identity is false at e.g. $x = y = 2$ as written.
- $xy = 1$ and $xy = -1$ are boundary cases: the fraction $\frac{x+y}{1-xy}$ explodes while the true sum is $\pm\frac{\pi}{2}$ or $\pm\frac{\pi}{2} \mp \pi$ — compute from the branch directly: if $x = y = 1$, $\tan^{-1}1 + \tan^{-1}1 = \frac{\pi}{2}$ ✓.
- $2\tan^{-1}x = \sin^{-1}\frac{2x}{1+x^{2}}$ fails for $x > 1$: e.g. $x = 2$: LHS $= 2\tan^{-1}2 \approx 2.214$, but $\sin^{-1}\frac{4}{5} \approx 0.927$ — the $\pi -$ face is the true one ($\pi - 0.927 \approx 2.214$ ✓).
- In telescoping, check $ab > -1$ before using $\tan^{-1}\frac{a-b}{1+ab} = \tan^{-1}a - \tan^{-1}b$; for positive $a,b$ it always holds.
:::

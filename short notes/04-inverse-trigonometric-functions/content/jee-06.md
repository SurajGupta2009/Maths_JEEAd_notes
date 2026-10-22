---
id: jee-06
part: jee
title: "Recap Toolkit — Every Formula of the Chapter on One Page"
---

## The one-page register

:::key title="Definitions and branches (the non-negotiable core)"
$$\sin^{-1} : [-1,1] \to [-\frac{\pi}{2}, \frac{\pi}{2}], \quad \cos^{-1} : [-1,1] \to [0, \pi],$$

$$\tan^{-1} : \mathbb{R} \to (-\frac{\pi}{2}, \frac{\pi}{2})$$

$$\cot^{-1} : \mathbb{R} \to (0, \pi), \quad \sec^{-1} : |x| \geq 1 \to [0,\pi] \setminus \{\frac{\pi}{2}\},$$

$$\csc^{-1} : |x| \geq 1 \to [-\frac{\pi}{2}, \frac{\pi}{2}] \setminus \{0\}$$

Complementary pairs: $\sin^{-1}x + \cos^{-1}x = \frac{\pi}{2}$, $\tan^{-1}x + \cot^{-1}x = \frac{\pi}{2}$, $\sec^{-1}x + \csc^{-1}x = \frac{\pi}{2}$ (on their shared domains).
:::

:::key title="Composition reads (sheet 02 in one line each)"
$$\sin^{-1}(\sin x) = x \ (x \in [-\frac{\pi}{2}, \frac{\pi}{2}]),$$

$$= \pi - x \ (x \in [\frac{\pi}{2}, \frac{3\pi}{2}])$$

$$\cos^{-1}(\cos x) = x \ (x \in [0, \pi]),$$

$$= 2\pi - x \ (x \in [\pi, 2\pi])$$

$$\tan^{-1}(\tan x) = x \ (x \in (-\frac{\pi}{2}, \frac{\pi}{2})),$$

$$= x - \pi k \text{ with output forced into } (-\frac{\pi}{2}, \frac{\pi}{2})$$

Outside these windows: reduce mod the period first (sine/cosine: $2\pi$; tangent/cotangent: $\pi$), then read the branch.
:::

:::key title="Addition formulas (sheets 03–04, conditions included)"
$$\tan^{-1}x + \tan^{-1}y = \tan^{-1}\frac{x+y}{1-xy} \ (xy < 1);$$

$$= \pi + \tan^{-1}\frac{x+y}{1-xy} \ (xy > 1,\ x > 0)$$

$$= -\pi + \tan^{-1}\frac{x+y}{1-xy} \ (xy > 1,\ x < 0);$$

$$\tan^{-1}x - \tan^{-1}y = \tan^{-1}\frac{x-y}{1+xy} \ (xy > -1)$$

$$2\tan^{-1}x = \sin^{-1}\frac{2x}{1+x^{2}} \ (|x| \leq 1),$$

$$= \cos^{-1}\frac{1-x^{2}}{1+x^{2}} \ (x \geq 0)$$

$$\sin^{-1}x + \sin^{-1}y$$

$$\sin^{-1}(x\sqrt{1-y^{2}} + y\sqrt{1-x^{2}}) \ (xy \leq 0 \text{ or } x^{2}+y^{2} \leq 1)$$

(with the $\pi - (\cdot)$ / $-\pi - (\cdot)$ corrections when both positive / both negative and $x^{2}+y^{2} > 1$.)
:::

:::key title="Trig of an inverse — the triangle, not a table"
$$\sin(\tan^{-1}x) = \frac{x}{\sqrt{1+x^{2}}}, \quad \cos(\tan^{-1}x) = \frac{1}{\sqrt{1+x^{2}}},$$

$$\sin(\cos^{-1}x) = \sqrt{1 - x^{2}}$$

$$\cos(\sin^{-1}x) = \sqrt{1 - x^{2}},$$

$$\tan(\sin^{-1}x) = \frac{x}{\sqrt{1 - x^{2}}} \ (|x| < 1)$$

Signs fixed by the branches: $\cos(\sin^{-1}x) \geq 0$, $\sin(\cos^{-1}x) \geq 0$, always.
:::

## Strategy card — the order of operations that avoids every trap

:::app title="Five steps, in order"
1. **Domain**: write the legal input set first (and parameter conditions).
2. **Reduce**: any $\sin^{-1}(\sin(\cdot))$-shaped pieces — reduce mod period, read branch (sheet 02).
3. **Collapse**: complementary pairs ($\sin^{-1}x + \cos^{-1}x = \frac{\pi}{2}$) before any arithmetic.
4. **Combine**: addition formulas — check the condition ($xy$ vs $1$, $x^{2}+y^{2}$ vs $1$) *before* writing the formula.
5. **Verify**: substitute back into the original equation (kills both ghost species) and check the answer lies in the output range of the original left-hand side.
:::

## Where this toolkit reappears (forward map, not spoilers)

- **Calculus**: $\frac{d}{dx}\sin^{-1}x = \frac{1}{\sqrt{1 - x^{2}}}$-type derivatives are proved from these branches (the sign of $\sqrt{1-x^{2}}$ *is* the branch fact); $\int \frac{dx}{1 + x^{2}} = \tan^{-1}x + C$ uses the principal branch; definite integrals like $\int_{0}^{1} \sin^{-1}x\, dx$ need the range for bounds.
- **Complex numbers (chapter 5)**: $\arg z$ is a multi-valued cousin of $\tan^{-1}$; $\operatorname{Arg} z$ = principal argument in $(-\pi, \pi]$ is this same "pick a branch" discipline, extended to a $2\pi$-window; $\tan^{-1}\frac{y}{x}$ recovers the quadrant-corrected angle only after a quadrant check.
- **Coordinate geometry**: angles between lines $\tan^{-1}\left|\frac{m_{1} - m_{2}}{1 + m_{1}m_{2}}\right|$ are exactly the sheet-03 formula with a branch read for the acute angle.

:::assume title="Conventions register (locked for the whole series)"
- $\sin^{-1}x$ = inverse of sine = arcsine, never $(\sin x)^{-1}$; radians everywhere; principal ranges as in the first box; $\cot^{-1}$ range $(0, \pi)$.
- All "$=$" between an inverse-trig expression and an angle assert equality of *real numbers*, i.e. the angle on the stated branch.
- $\sqrt{\cdot}$ denotes the non-negative root of a non-negative real.
:::

:::warn title="Final trap sweep (self-test before the exam)"
1. $\sin^{-1}(\sin 3)$ — did you reduce $3 - 2\pi$ or read $\pi - 3$? ($3 \in (\pi/2, 3\pi/2)$: answer $\pi - 3 \approx 0.1416$ ✓)
2. $\tan^{-1}2 + \tan^{-1}3$ — did you add $\pi$? (answer $3\pi/4$)
3. $2\tan^{-1}2 = \sin^{-1}\frac{4}{5}$? — no: $x > 1$ needs the $\pi -$ face.
4. $\cos^{-1}(-x)$ vs $-\cos^{-1}x$ — the first is $\pi - \cos^{-1}x$, the second is negative; never equal for $x > 0$.
5. $\sin^{-1}x + \cos^{-1}y = \frac{\pi}{2}$ — only when $x = y$.
6. $\tan^{-1}x = \sin^{-1}x$ has the single solution $x = 0$ (branches coincide only there: both sides $0$); $\sin^{-1}x = \cos^{-1}x$ has $x = \frac{1}{\sqrt{2}}$; $\tan^{-1}x = \cos^{-1}x$ needs $x > 0$ and gives $x = \sqrt{\frac{\sqrt{5} - 1}{2}}$... unless you solved it yourself — different inverse equations give genuinely different answers; never pattern-match across them.
:::

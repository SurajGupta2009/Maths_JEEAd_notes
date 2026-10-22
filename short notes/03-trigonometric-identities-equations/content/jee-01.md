---
id: jee-01
part: jee
title: "Trigonometry — Ratios, the Unit Circle, Fundamental Identities"
---

## Where the six ratios come from

For a right triangle with angle $\theta$ (acute), opposite $O$, adjacent $A$, hypotenuse $H > 0$:

$$\sin\theta = \dfrac{O}{H}, \quad \cos\theta = \dfrac{A}{H}, \quad \tan\theta = \dfrac{O}{A}$$

$$\csc\theta = \dfrac{H}{O}, \quad \sec\theta = \dfrac{H}{A}, \quad \cot\theta = \dfrac{A}{O}.$$

**Radian convention (the default).** An angle is the arc length it cuts on the unit circle: full turn $= 2\pi$ radians $= 360^{\circ}$, so $180^{\circ} = \pi$ rad, $90^{\circ} = \pi/2$, $60^{\circ} = \pi/3$, $45^{\circ} = \pi/4$, $30^{\circ} = \pi/6$. **Never mix degrees and radians in one computation** — pick one system per problem and convert at the boundaries.

## The unit circle definition (all angles, not just acute)

The point at angle $\theta$ from the positive $x$-axis on the unit circle is $P = (\cos\theta, \sin\theta)$. This defines $\sin$ and $\cos$ for **all** real $\theta$ (negative, $> 2\pi$, whatever), makes them periodic with period $2\pi$, and gives the fundamental identity as the equation of the circle.

:::diagram
{"type": "unitcircle", "angle_deg": 38, "title": "The unit circle: P = (cos θ, sin θ) — the definition of all six ratios"}
:::

$\sin^{2}\theta + \cos^{2}\theta = 1 \qquad \text{(every point of the unit circle)}$

**Reciprocal and quotient identities** (valid wherever both sides are defined):

$$\sin\theta \csc\theta = 1, \quad \cos\theta \sec\theta = 1, \quad \tan\theta \cot\theta = 1$$

$$\tan\theta = \dfrac{\sin\theta}{\cos\theta}, \quad \cot\theta = \dfrac{\cos\theta}{\sin\theta}.$$

Dividing $\sin^{2} + \cos^{2} = 1$ by $\cos^{2}$ or $\sin^{2}$ gives the other two Pythagorean forms:

$$1 + \tan^{2}\theta = \sec^{2}\theta, \qquad 1 + \cot^{2}\theta = \csc^{2}\theta.$$

:::derive title="Deriving $1 + \tan^{2} = \sec^{2}$ — the pattern that generates all three"
Divide $\sin^{2}\theta + \cos^{2}\theta = 1$ by $\cos^{2}\theta$ (legal when $\cos\theta \ne 0$): $\tan^{2}\theta + 1 = \sec^{2}\theta$. Divide by $\sin^{2}\theta$ (when $\sin\theta \ne 0$): $1 + \cot^{2}\theta = \csc^{2}\theta$. Each Pythagorean identity is one *constraint between two coordinates* read in a different ratio basis — never memorise three formulas, memorise one and the two divisions.
:::

:::assume
Angle variable $\theta$ (or $x$) is real; all identities are **identities of functions**, true at every angle where both sides are defined. Points of definition: $\tan, \sec$ undefined at $\frac{\pi}{2} + k\pi$ (cosine zero); $\cot, \csc$ undefined at $k\pi$ (sine zero), $k \in \mathbb{Z}$. $\sin, \cos$ have domain $\mathbb{R}$, range $[-1, 1]$; $\tan, \cot$ have range $\mathbb{R}$. Units: radians unless a problem states degrees.
:::

:::key
**Ranges and the inequality toolkit.** $-1 \leq \sin\theta, \cos\theta \leq 1$ for all $\theta$; so $|\sin\theta| \leq 1$, $|\cos\theta| \leq 1$, and expressions like $3\sin\theta - 4\cos\theta$ are bounded ($|a\sin\theta + b\cos\theta| \leq \sqrt{a^{2} + b^{2}}$ — proved in sheet 3 via compound angles). The reciprocal ratios are unbounded near their poles: $|\sec| \geq 1$, $|\csc| \geq 1$.
:::

:::warn title="Common traps — foundations"
- $\sin^{2}\theta + \cos^{2}\theta = 1$ does **not** mean $\sin\theta + \cos\theta = 1$; also $(\sin\theta + \cos\theta)^{2} = 1 + 2\sin\theta\cos\theta = 1 + \sin 2\theta$.
- $\sqrt{\sin^{2}\theta} = |\sin\theta|$, not $\sin\theta$.
- $\tan\theta = \frac{\sin\theta}{\cos\theta}$ is undefined wherever $\cos\theta = 0$ — never cancel a $\cos$ without stating the domain.
- $\sin(\theta)^{-1} \ne \sin^{-1}\theta$: the first is $\csc\theta$; the second is the *inverse function* (chapter 4). Write $\csc$ and $\arcsin$ to stay unambiguous.
:::

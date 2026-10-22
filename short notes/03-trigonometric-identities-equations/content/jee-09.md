---
id: jee-09
part: jee
title: "Chapter Recap — Identities & Equations Toolkit"
---

## The whole toolkit on one sheet

**Definitions.** Unit circle: $P = (\cos\theta, \sin\theta)$; $\tan = \sin/\cos$; $\sin^{2} + \cos^{2} = 1$; $1 + \tan^{2} = \sec^{2}$; $1 + \cot^{2} = \csc^{2}$ (divide the master identity). Radians default: $\pi = 180^{\circ}$. Ranges: $\sin, \cos \in [-1, 1]$; periods: $\sin, \cos$ are $2\pi$, $\tan, \cot$ are $\pi$.

**Signs & allied angles.** Quadrant signs (ASTC); odd multiples of $\frac{\pi}{2}$ swap $\sin \leftrightarrow \cos$ with quadrant signs, even multiples only sign; $\sin(\pi - \theta) = \sin\theta$, $\cos(\pi - \theta) = -\cos\theta$.

**Compound angles.** $\sin(A \pm B) = \sin A \cos B \pm \cos A \sin B$; $\cos(A \pm B) = \cos A \cos B \mp \sin A \sin B$ (flip!); $\tan(A \pm B) = \frac{\tan A \pm \tan B}{1 \mp \tan A \tan B}$. Derived bound: $|a \sin x + b \cos x| \leq \sqrt{a^{2} + b^{2}}$.

**Multiple/submultiple.** $\sin 2A = 2 \sin A \cos A$; $\cos 2A$ three forms; power reduction $\sin^{2} = \frac{1 - \cos 2A}{2}$, $\cos^{2} = \frac{1 + \cos 2A}{2}$; $\sin 3A = 3 \sin A - 4 \sin^{3} A$, $\cos 3A = 4 \cos^{3} A - 3 \cos A$; half-angle radicals with $\pm$ from the quadrant of $\frac{A}{2}$; $\tan\frac{A}{2} = \frac{1 - \cos A}{\sin A} = \frac{\sin A}{1 + \cos A}$ (no radical form needed).

**Transformations.** $2 \sin A \cos B = \sin(A+B) + \sin(A-B)$ etc. (4 formulas); sum-to-product with the minus sign in $\cos C - \cos D = -2 \sin\frac{C+D}{2} \sin\frac{C-D}{2}$.

**Equations.** Master general solutions: $\sin\theta = \sin\alpha \Rightarrow \theta = n\pi + (-1)^{n}\alpha$; $\cos\theta = \cos\alpha \Rightarrow \theta = 2n\pi \pm \alpha$; $\tan\theta = \tan\alpha \Rightarrow \theta = n\pi + \alpha$. Methods: factorise (never divide), harmonic form $R \sin(x + \varphi)$ with compatibility $|c| \leq R$, polynomial in one ratio with range clip, squaring + filtering, interval counting by ranging $n$.

**Conditional ($A + B + C = \pi$).** $\tan A + \tan B + \tan C = \tan A \tan B \tan C$; $\sin 2A + \sin 2B + \sin 2C = 4 \sin A \sin B \sin C$; half-angle product sum $= 1$.

:::key
**Five questions to ask any trig problem.** (1) Degrees or radians? (2) Which quadrant is the angle in (signs)? (3) Am I allowed to divide/cancel (any factor that can vanish)? (4) After any squaring/substitution, which solutions are ghosts? (5) Does a hidden constraint ($A + B + C = \pi$, complementary angles) trigger a conditional identity?
:::

:::assume
All angles real; radians unless stated; identities hold wherever both sides are defined; general solutions are over $n \in \mathbb{Z}$; square roots in half-angle formulas carry the sign of the quadrant of $\frac{A}{2}$; "solve generally" means the general solution, "solve in $[a, b)$" means filter with integer $n$.
:::

:::app
**Where this reappears.** Compound-angle machinery powers the calculus of $\sin/\cos$ (derivatives), vectors (angles, projections), 2D/3D geometry (direction angles), complex numbers (de Moivre), and periodic modelling. Equation discipline (domain, factorise, filter) is exactly the discipline of solving with substitutions in calculus and of Diophantine angle problems in olympiads (Part II).
:::

:::warn title="Final trap sweep"
- $\cos(A - B) = \cos A \cos B + \sin A \sin B$ — plus sign, every time.
- $\theta = n\pi + (-1)^{n}\alpha$ for sine (not $n\pi + \alpha$).
- Divide by $\cos x$? Don't. Factor instead.
- $\sqrt{\sin^{2} x} = |\sin x|$; half-angle radicals need the quadrant of $\frac{A}{2}$.
- $\sin 2x = \sin 2y \Rightarrow x = y + k\pi$ **or** $x = \frac{\pi}{2} - y + k\pi$ — the $2$-periodicity doubles the families. Reduce to one function first.
:::

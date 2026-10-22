---
id: olympiad-01
part: olympiad
title: "Extension — Newton's Sums, Power Sums, and the Fibonacci–Lucas Machine"
---

:::assume title="STATUS — olympiad/specialised extension (IOQM/RMO-flavoured)"
Beyond the official syllabus sentence (quadratics with real coefficients), power-sum recurrences and closed forms for $\alpha^{n} + \beta^{n}$ are extension theory. Nothing here is needed for Part I; the *habit* — never solve for roots when a symmetric combination is asked — is the transferable skill.
:::

## Power sums from coefficients alone

:::derive title="Newton's recurrence for two roots"
$\alpha, \beta$ satisfy $ax^{2} + bx + c = 0$. Multiply the equation for $\alpha$ by $\alpha^{n-2}$, the one for $\beta$ by $\beta^{n-2}$, and add. With $S_{n} = \alpha^{n} + \beta^{n}$:

$$aS_{n} + bS_{n-1} + cS_{n-2} = 0, \qquad S_{0} = 2, \quad S_{1} = -\frac{b}{a}$$

So $S_{n} = \frac{-bS_{n-1} - cS_{n-2}}{a}$ generates every power sum from the coefficients — no radicals, ever. Start at $S_{0} = 2$, not $S_{1}$ (checklist item).
:::

:::example title="Worked — Newton's sums"
$x^{2} - 5x + 3 = 0$: $S_{0} = 2$, $S_{1} = 5$; $S_{2} = 5 \cdot 5 - 3 \cdot 2 = 19$; $S_{3} = 5 \cdot 19 - 3 \cdot 5 = 80$. Matches $S^{2} - 2P = 19$ and $S^{3} - 3PS = 125 - 45 = 80$ ✓ (and numerically $\alpha \approx 4.3028, \beta \approx 0.6972$ give $\alpha^{3} + \beta^{3} \approx 80.00$ ✓).
:::

:::key title="The golden quadratic generates Fibonacci and Lucas"
For $x^{2} - x - 1 = 0$ with roots $\varphi = \frac{1 + \sqrt{5}}{2}$, $\psi = \frac{1 - \sqrt{5}}{2}$: induction on $\alpha^{2} = \alpha + 1$ gives

$$\alpha^{n} = F_{n}\alpha + F_{n-1} \qquad (F_{0} = 0, F_{1} = 1)$$

for both roots. Adding the two identities: $S_{n} = \varphi^{n} + \psi^{n} = F_{n} + 2F_{n-1} = F_{n+1} + F_{n-1} = L_{n}$, the **Lucas numbers** $2, 1, 3, 4, 7, 11, 18, 29, 47, \ldots$ Subtracting and dividing by $\sqrt{5} = \varphi - \psi$ gives **Binet**: $F_{n} = \frac{\varphi^{n} - \psi^{n}}{\sqrt{5}}$. Worked check: $F_{10} = 55$, and $55\varphi + 34 \approx 122.9918 \approx \varphi^{10}$ ✓.
:::

:::app title="Standard applications"
Integer-valuedness: if $S, P$ are integers, every $S_{n}$ is an integer (recurrence), so $\varphi^{n} + \psi^{n} \in \mathbb{Z}$ despite the radicals — the standard trick for proving $\lfloor \varphi^{2n} \rfloor$-type results, using $\left|\psi\right| < 1$ so $\psi^{n} \to 0$ and the integer $L_{n}$ sits within 1 of $\varphi^{n}$.
:::

:::warn title="Common traps — power sums"
- Recurrence sign: $aS_{n} + bS_{n-1} + cS_{n-2} = 0$ — move terms carefully.
- $S_{0} = 2$ (two roots), including when a root is repeated.
- Binet needs $\varphi - \psi = \sqrt{5}$ in the denominator, not $2\sqrt{5}$.
:::

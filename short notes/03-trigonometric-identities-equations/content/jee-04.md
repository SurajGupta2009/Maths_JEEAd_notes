---
id: jee-04
part: jee
title: "Multiple & Submultiple Angles — Double, Triple, Half, Power Reduction"
---

## Double angles (set $B = A$ in the compound formulae)

$$\sin 2A = 2 \sin A \cos A$$

$$\cos 2A = \cos^{2} A - \sin^{2} A = 2\cos^{2} A - 1 = 1 - 2\sin^{2} A$$

$$\tan 2A = \dfrac{2 \tan A}{1 - \tan^{2} A}.$$

The three forms of $\cos 2A$ are one identity seen through $\sin^{2} + \cos^{2} = 1$; each is the natural form for a different substitution (in terms of $\cos$ alone, $\sin$ alone, or mixed).

**Power reduction (inverse reading — used constantly):**

$$\sin^{2} A = \dfrac{1 - \cos 2A}{2}, \qquad \cos^{2} A = \dfrac{1 + \cos 2A}{2}$$

$$\sin A \cos A = \dfrac{\sin 2A}{2}$$

## Triple angles (set $B = 2A$, expand)

$$\sin 3A = 3 \sin A - 4 \sin^{3} A$$

$$\cos 3A = 4 \cos^{3} A - 3 \cos A.$$

:::derive title="Derivation — ten seconds, no memorising"
$\sin 3A = \sin(2A + A) = \sin 2A \cos A + \cos 2A \sin A = 2 \sin A \cos^{2} A + (1 - 2 \sin^{2} A) \sin A = 2\sin A(1 - \sin^{2} A) + \sin A - 2 \sin^{3} A = 3 \sin A - 4 \sin^{3} A$ ✓. The cosine version is the same computation with the cosine formulae. Inverting them: $3 \sin A - 4 \sin^{3} A = \sin 3A$ solves cubics of that shape — the standard move behind $\sin 18^{\circ}$-style values (Part II).
:::

## Half angles (solve the double-angle forms for $A/2$)

$$\sin\dfrac{A}{2} = \pm\sqrt{\dfrac{1 - \cos A}{2}}, \qquad \cos\dfrac{A}{2} = \pm\sqrt{\dfrac{1 + \cos A}{2}}$$

$$\tan\dfrac{A}{2} = \dfrac{1 - \cos A}{\sin A} = \dfrac{\sin A}{1 + \cos A} = \pm\sqrt{\dfrac{1 - \cos A}{1 + \cos A}}.$$

The two rational forms of $\tan\frac{A}{2}$ carry **no square root** — prefer them whenever $\tan$ is all you need. The $\pm$ in the radical forms is resolved from the **quadrant of $\frac{A}{2}$**, not of $A$.

:::diagram
{"type": "graph", "ratio": 0.5, "xrange": [-2, 8.3], "yrange": [-1.6, 1.6], "xticks": [0, 1.5708, 3.1416, 4.7124, 6.2832], "xticklabels": ["0", "$\\pi/2$", "$\\pi$", "$3\\pi/2$", "$2\\pi$"], "yticks": [-1, 0, 1], "title": "sin A vs sin 2A: the double-angle curve oscillates twice as fast", "curves": [{"expr": "sin(x)", "color": "#0F766E", "label": "sin A", "labpos": 0.06}, {"expr": "sin(2*x)", "color": "#B91C1C", "label": "sin 2A = 2 sin A cos A", "labpos": 0.31}], "hlines": [{"y": 0, "label": ""}]}
:::

:::key
**Forms to convert between, fluently:** $\sin 2A = 2\sin A \cos A$; $\cos 2A = 1 - 2\sin^{2} A = 2 \cos^{2} A - 1$; power reduction $\sin^{2}, \cos^{2} \leftrightarrow \cos 2A$; products $\sin A \cos A \leftrightarrow \sin 2A$. Converting an equation into $\sin 2A$-language often halves its degree — that is the point of the machinery.
:::

:::example title="Worked. If $\cos A = \frac{3}{5}$, $A$ acute, find $\cos 2A$, $\sin 2A$, $\tan\frac{A}{2}$"
$\sin A = \frac{4}{5}$ (acute $\Rightarrow +$). $\cos 2A = 2 \cdot \frac{9}{25} - 1 = -\frac{7}{25}$ ✓. $\sin 2A = 2 \cdot \frac{4}{5} \cdot \frac{3}{5} = \frac{24}{25}$ ✓ (check: $(-\frac{7}{25})^{2} + (\frac{24}{25})^{2} = \frac{49 + 576}{625} = 1$ ✓). $\tan\frac{A}{2} = \frac{1 - \cos A}{\sin A} = \frac{2/5}{4/5} = \frac{1}{2}$ ✓ (positive: $A/2$ acute).
:::

:::warn title="Common traps — multiple angles"
- Half-angle $\pm$: for $A = 60^{\circ}$, $\frac{A}{2} = 30^{\circ}$ (QI) $\Rightarrow +$; for $A = 420^{\circ}$, $\frac{A}{2} = 210^{\circ}$ (QIII) $\Rightarrow$ sine root negative. Decide from $\frac{A}{2}$'s quadrant.
- $\cos 2A = 1 - 2\sin^{2} A$ solved for $\sin A$ gives **two** roots ($\pm$); the quadrant of $A$ selects.
- $\tan 2A$ is undefined when $1 - \tan^{2} A = 0$, i.e. $A = \frac{\pi}{4} + k\frac{\pi}{2}$ — consistent with $\tan 2A$ blowing up at $2A = \frac{\pi}{2} + k\pi$.
- $(\sin A \pm \cos A)^{2} = 1 \pm \sin 2A$ — remember the middle term.
:::

---
id: olympiad-01
part: olympiad
title: "Extension — Harmonic Progressions and the A ≥ G ≥ H Chain"
---

:::assume title="STATUS — olympiad/specialised extension (IOQM/RMO-flavoured)"
Harmonic progressions are **not** in the official JEE Advanced syllabus (which lists AP, GP, AM/GM and the power sums only). They appear in IOQM/RMO-style material and older JEE Main contexts. The technique — reciprocate, solve the AP, reciprocate back — is the transferable part.
:::

## HP via reciprocals

:::key title="Definitions and the only method"
A **harmonic progression** is a sequence whose reciprocals form an AP. There is no closed formula for its $n$-th term or sum comparable to AP/GP: every HP problem is routed through the reciprocal AP.

The **harmonic mean** of $a, b > 0$ is $H = \frac{2ab}{a + b} = \frac{2}{\frac{1}{a} + \frac{1}{b}}$ — defined by $\frac{1}{a}, \frac{1}{H}, \frac{1}{b}$ in AP. For $n$ numbers, $H = \frac{n}{\sum 1/a_{i}}$.
:::

:::example title="Worked — HP basics"
HM of 2 and 4: $H = \frac{2 \cdot 2 \cdot 4}{6} = \frac{8}{3}$. The HP $1, \frac{1}{2}, \frac{1}{3}, \ldots$ has reciprocals $1, 2, 3, \ldots$ (an AP), so its $4$-th term is $\frac{1}{4}$. General HP term: if the reciprocal AP has first term $\frac{1}{a}$ and difference $d'$, the $n$-th HP term is $\frac{1}{\frac{1}{a} + (n - 1)d'}$.
:::

:::key title="The chain A ≥ G ≥ H and the identity G² = AH"
For two positive numbers, $A = \frac{a + b}{2}$, $G = \sqrt{ab}$, $H = \frac{2ab}{a + b}$ satisfy $A \geq G \geq H$, and moreover

$$G^{2} = AH$$

since $\frac{a + b}{2} \cdot \frac{2ab}{a + b} = ab$. So $A, G, H$ are in GP. Equality throughout iff $a = b$. For $n$ positives, $A \geq G \geq H$ still holds (apply AM–GM to the numbers and to their reciprocals).
:::

:::app title="Standard applications"
Average speed over equal distances at speeds $u, v$ is the **harmonic** mean $\frac{2uv}{u + v}$, not the arithmetic mean — the canonical HP-in-disguise. Work-rate and parallel-resistance formulas are the same shape: whenever the *reciprocals* add, $H$ appears.
:::

:::warn title="Common traps — HP"
- Inventing an "$S_{n}$ formula" for HP by analogy with AP/GP: none exists in elementary closed form; sums route through $H_{n} = \sum \frac{1}{k}$ estimates only.
- $H$ for numbers of mixed sign: the mean framework assumes positives.
- Confusing "insert harmonic means" (reciprocate, insert AMs, reciprocate back) with inserting AMs directly.
:::

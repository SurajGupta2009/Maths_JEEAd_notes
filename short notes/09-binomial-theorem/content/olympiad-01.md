---
id: olympiad-01
part: olympiad
title: "Extension — The General Binomial Series: Negative and Fractional Indices, Validity, Approximation"
---

:::assume title="STATUS — olympiad/specialised extension (IOQM/RMO-flavoured)"
The official JEE Advanced syllabus specifies the binomial theorem for **positive integral index only**. The general series below is extension material (it underlies JEE Main-style approximation questions historically, and all of analysis).
:::

:::key title="The generalised coefficient and Euler's series"
For any real $r$, $\binom{r}{k} = \frac{r(r - 1)\cdots(r - k + 1)}{k!}$ (with $\binom{r}{0} = 1$), and

$$(1 + x)^{r} = \sum_{k=0}^{\infty} \binom{r}{k} x^{k} \qquad \text{for } \left|x\right| < 1$$

The extension is forced: it is the unique choice keeping $\frac{d}{dx}(1 + x)^{r} = r(1 + x)^{r - 1}$ term-by-term. Families to own: $(1 - x)^{-n} = \sum_{k} \binom{n + k - 1}{k} x^{k}$ (stars-and-bars counts — coefficients of $(1 - x)^{-3}$ are $\binom{k + 2}{2}$: $x^{2}$ coefficient $6$); $(1 - x)^{-1/2} = \sum_{k} \frac{\binom{2k}{k}}{4^{k}} x^{k}$ ($x^{5}$: $\frac{252}{1024} = \frac{63}{256}$); $(1 + x)^{1/2} = 1 + \frac{x}{2} - \frac{x^{2}}{8} + \frac{x^{3}}{16} - \cdots$
:::

:::key title="Validity is part of the answer"
Factor so the bracket is $1 + u$ with $\left|u\right| < 1$. $(3 + 2x)^{-2} = \frac{1}{9}\left(1 + \frac{2x}{3}\right)^{-2} = \frac{1}{9} - \frac{4x}{27} + \cdots$ valid for $\left|x\right| < \frac{3}{2}$; in *descending* powers factor $2x$ instead, valid for $\left|x\right| > \frac{3}{2}$. $(4 + 3x)^{-1/2} = \frac{1}{2} - \frac{3x}{16} + \cdots$ for $\left|x\right| < \frac{4}{3}$. Coefficient of $x^{6}$ in $(1 + 3x)^{-2}$: $(-1)^{6} \cdot 7 \cdot 3^{6} = 5103$, valid $\left|x\right| < \frac{1}{3}$.
:::

:::example title="Worked — approximation with an error budget"
$\sqrt[3]{26} = 3\left(1 - \frac{1}{27}\right)^{1/3} \approx 3\left(1 - \frac{1}{81} - \frac{1}{6561}\right) = 2.96250$; the first dropped term is $< 10^{-4}$ in the final value, certifying $2.96$. $\sqrt{1.02} \approx 1 + 0.01 - 0.00005 + 0.0000005 = 1.0099505$ with first dropped term $< 10^{-8}$. Series recognition in reverse: $\sum_{k} (k + 1)(0.9)^{k} = \frac{1}{(1 - 0.9)^{2}} = 100$, and $\sum_{k} \frac{\binom{2k}{k}}{8^{k}} = \left(1 - \frac{4}{8}\right)^{-1/2} = \sqrt{2}$.
:::

:::warn title="Common traps — general series"
- Writing an expansion without its validity range: zero marks, even with correct coefficients.
- The radius is the ratio inside the bracket, never automatically 1.
- Boundary $x = \pm 1$ is delicate (convergence depends on $r$); JEE-level questions test $\left|x\right| < 1$ only — do not evaluate at endpoints without Abel-type justification.
:::

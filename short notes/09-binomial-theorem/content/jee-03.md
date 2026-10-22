---
id: jee-03
part: jee
title: "Three Identity Engines — Substitution, Calculus, and Coefficient Extraction"
---

## One master polynomial, three engines

Everything runs on $f(x) = (1 + x)^{n} = \sum_{k} \binom{n}{k} x^{k}$. **Engine 1 (substitute):** $f(1) = 2^{n}$; $f(-1) = 0$ (even/odd halves $2^{n - 1}$ each); $f(2) = 3^{n}$, i.e. $\sum \binom{n}{k} 2^{k} = 59049$ at $n = 10$. **Engine 2 (differentiate/integrate):** the operator $x\frac{d}{dx}$ stamps $k$ onto each term:

$$\sum k \binom{n}{k} = n 2^{n - 1}, \qquad \sum k(k - 1)\binom{n}{k} = n(n - 1)2^{n - 2}$$

$$\sum k^{2}\binom{n}{k} = n(n + 1)2^{n - 2}$$

($k^{2} = k(k - 1) + k$; at $n = 8$: $8 \cdot 9 \cdot 2^{6} = 4608$.) Divide-by-$(k + 1)$ is the integral's fingerprint: $\sum \frac{\binom{n}{k}}{k + 1} = \int_{0}^{1} (1 + x)^{n} dx = \frac{2^{n + 1} - 1}{n + 1}$, and $\sum \frac{(-1)^{k}}{k + 1}\binom{n}{k} = \frac{1}{n + 1}$.

:::intuition title="Every identity is also a counting story"
$\sum k\binom{n}{k} = n2^{n - 1}$ counts committees with a chair: choose the chair ($n$), then any subset of the rest ($2^{n - 1}$). Engines and stories are two proofs of one fact — quote whichever the question rewards.
:::

:::key title="Engine 3: products of coefficients are one coefficient"
**Vandermonde:** $\sum_{k} \binom{r}{k}\binom{s}{m - k} = \binom{r + s}{m}$ — the $x^{m}$ coefficient of $(1 + x)^{r}(1 + x)^{s}$, or committees from two groups. Specialisations: $\sum \binom{n}{k}^{2} = \binom{2n}{n}$ (at $n = 10$: $184756$; at $n = 6$ via $\binom{6}{k}\binom{6}{6 - k}$: $\binom{12}{6} = 924$); $\sum \binom{n}{k}\binom{n}{k + 1} = \binom{2n}{n + 1}$; alternating squares $\sum (-1)^{k}\binom{n}{k}^{2}$ is the $x^{n}$ coefficient of $(1 - x^{2})^{n}$: $0$ for odd $n$, $(-1)^{n/2}\binom{n}{n/2}$ for even $n$. **Hockey-stick:** $\sum_{i=r}^{m} \binom{i}{r} = \binom{m + 1}{r + 1}$ (telescope Pascal), e.g. $\binom{4}{4} + \binom{5}{4} + \binom{6}{4} + \binom{7}{4} = \binom{8}{5} = 56$.
:::

:::warn title="Common traps — identities"
- Differentiating then evaluating at the wrong point, or dropping the outer $x$ in $xf'(x)$ (a factor-$x$ error away from $x = 1$: $\sum k\binom{n}{k}2^{k} = 2n \cdot 3^{n - 1}$).
- Reaching for memorised identities when the engine derives them in one line — engines survive twists, lists do not.
- Vandermonde index mismatch: the second factor must be $\binom{s}{m - k}$ with the *same* $k$; check the target slot first.
:::

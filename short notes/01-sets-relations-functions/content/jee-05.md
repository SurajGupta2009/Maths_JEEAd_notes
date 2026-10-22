---
id: jee-05
part: jee
title: "Functions — Definition, Domain, Range, Image & Preimage"
---

## A function is a relation with two guarantees

$f : A \to B$ is a relation $f \subseteq A \times B$ such that every $a \in A$ has **exactly one** $b \in B$ with $(a,b) \in f$. The two halves — *existence* (at least one image) and *uniqueness* (at most one) — are checked separately on exam questions. $A$ is the **domain** (declared; it is part of the definition), $B$ the **codomain**, and $f(A) = \{f(a) : a \in A\} \subseteq B$ the **range** (image).

- Arrow-diagram test: every element of $A$ sends exactly one arrow out of $B$ (an element of $B$ may receive many or none).
- Graph test on $\mathbb{R}$: vertical line test (every vertical line hits the curve at most once) plus domain coverage.

Notation: $y = f(x)$; $f : x \mapsto x^2 - 1$; $f$ and $g$ are equal ($f = g$) iff same domain, same codomain and same values everywhere.

:::assume
Statements like "find the domain of $f$" assume the **maximal** real domain unless a domain is specified: all real $x$ for which the formula makes sense. Range is always inside the declared codomain; when a question says $f : \mathbb{R} \to \mathbb{R}$ and asks whether $f$ is onto, the codomain being all of $\mathbb{R}$ is part of the data. Writing $f : A \to B$ with $A$ the natural domain and $B$ chosen larger than the range makes $f$ "into" but not onto — same formula, different function.
:::

## Finding domains (the rule stack)

:::key
Apply every restriction simultaneously, then intersect:
1. Polynomial: all of $\mathbb{R}$. 2. Rational $p(x)/q(x)$: $q(x) \ne 0$. 3. Even root $\sqrt[n]{g(x)}$ ($n$ even): $g(x) \geq 0$. 4. Logarithm $\log_b g(x)$: $g(x) > 0$, base $b > 0, b \ne 1$. 5. $\tan g(x)$: $g(x) \ne \frac{\pi}{2} + k\pi$. 6. $1/g(x)$: additionally $g(x) \ne 0$. 7. Composite $g \circ f$: $x \in \operatorname{dom} f$ **and** $f(x) \in \operatorname{dom} g$. 8. Real powers $g^{p/q}$ in lowest terms: if $q$ even, need $g \geq 0$.
:::

:::example
**Worked (domain).** $f(x) = \sqrt{x - 1} + \dfrac{\sqrt{5 - x}}{x - 3}$. Conditions: $x - 1 \geq 0 \Rightarrow x \geq 1$; $5 - x \geq 0 \Rightarrow x \leq 5$; $x - 3 \ne 0 \Rightarrow x \ne 3$. Domain $= [1,3) \cup (3,5]$. **Boundary checks:** $x = 1$: $f(1) = 0 + \frac{2}{-2} = -1$ — defined, so the bracket at 1 is closed. $x = 5$: $f(5) = 2 + 0$ — defined, closed. $x = 3$: division by zero — deleted even though both roots are fine there. Endpoint testing is not optional: open vs closed brackets are where partial marks live.
:::

## Finding ranges (the four techniques)

- **Complete the square:** $x^2 - 4x + 7 = (x-2)^2 + 3 \geq 3$, so range on $\mathbb{R}$ is $[3,\infty)$; the vertex $(2,3)$ is the only point where the bound is met.
- **Monotone pieces:** a strictly decreasing $f$ maps $[a,b]$ onto $[f(b), f(a)]$ (order flips!). On $[0,1]$, $x^2 - 4x + 7$ decreases from $7$ to $4$: range $[4,7]$.
- **Solve for $x$:** write $y = f(x)$, solve for $x = g(y)$, and require a real solution: for $y = \dfrac{x^2 + 1}{x^2 - 1}$ with $x^2 \ne 1$... cleaner classic below.
- **Sign / bound analysis:** $|f|$, $e^x > 0$, $\sqrt{\cdot} \geq 0$ give one-sided bounds; combine with continuity (the image of an interval is an interval).

:::example
**Worked (range by discriminant).** $f(x) = \dfrac{x^2}{x^2 + 1}$ on $\mathbb{R}$. Solve $y = \frac{x^2}{x^2+1}$ for $x$: $y(x^2 + 1) = x^2 \Rightarrow x^2 (1 - y) = y \Rightarrow x^2 = \frac{y}{1-y}$. Real $x$ exists iff $\frac{y}{1-y} \geq 0$, i.e. $0 \leq y < 1$ (note $y = 1$ is impossible: $1 - y = 0$ gives $0 = 1$). Range $= [0, 1)$. **Check:** $f(0) = 0$ attained; $f(x) \to 1$ as $|x| \to \infty$ but never equals 1 — the range is half-open exactly as the algebra says.
:::

:::warn
- $\sqrt{x^2} = |x|$, not $x$ — the root output is never negative.
- $e^{\ln x} = x$ only for $x > 0$; $\ln(e^{x}) = x$ for all real $x$. Swapping them silently changes domains.
- Range of a formula **changes with the domain**: $x^2$ on $\mathbb{R}$ has range $[0,\infty)$; on $[-1,2]$ it has range $[0,4]$.
- $f(A) \cap f(B) \supseteq f(A \cap B)$ always, but equality can fail (e.g. $f(x) = x^2$, $A = \{-2\}$, $B = \{2\}$): $f(A \cap B) = \varnothing$ while $f(A) \cap f(B) = \{4\}$. The similar-looking $f(A \setminus B)$ vs $f(A) \setminus f(B)$ is even more fragile — draw arrows before trusting algebra.
:::

## Image and preimage (defined for every function)

For $S \subseteq A$ the **image** is $f(S) = \{f(x) : x \in S\}$. For $T \subseteq B$ the **preimage** is $f^{-1}(T) = \{x \in A : f(x) \in T\}$. The superscript $-1$ here does **not** require invertibility — $f^{-1}(T)$ is a set of inputs, and it can be empty ($f^{-1}(\{-5\}) = \varnothing$ for $f(x) = x^2$).

:::key
$f^{-1}$ used as a **function** exists only for bijections (see the composition & inverse sheet). $f^{-1}(T)$ used as a **set** is always defined. Identities that always hold: $f(f^{-1}(T)) \subseteq T$; $f^{-1}(f(S)) \supseteq S$; $f^{-1}(T_1 \cap T_2) = f^{-1}(T_1) \cap f^{-1}(T_2)$ (both directions); $f(S_1 \cup S_2) = f(S_1) \cup f(S_2)$.
:::

---
id: jee-08
part: jee
title: "Composition & Inverse Functions — and the Chapter Recap"
---

## Composition: $g \circ f$

$(g \circ f)(x) = g(f(x))$ — apply $f$ **first**, then $g$.

:::key
Domain of $g \circ f$: $\{x \in \operatorname{dom} f : f(x) \in \operatorname{dom} g\}$. Order matters: $g \circ f \ne f \circ g$ in general. Composition is associative ($(h \circ g) \circ f = h \circ (g \circ f)$) because both sides equal $h(g(f(x)))$. If $f : A \to B$ and $g : B \to C$ then $g \circ f : A \to C$ and $f(A) \subseteq B$ must land inside $g$'s domain — if $f$'s range escapes $\operatorname{dom} g$, shrink $f$'s domain until it does not.
:::

:::diagram
{
  "type": "compose",
  "Aname": "A", "Bname": "B", "Cname": "C",
  "f": "f", "g": "g", "comp": "g o f : A to C"
}
:::

:::example
**Worked.** $f(x) = \sqrt{x}$ (domain $[0,\infty)$), $g(x) = x - 3$ (domain $\mathbb{R}$). Then $(g \circ f)(x) = \sqrt{x} - 3$ with domain $[0,\infty)$ — every output of $f$ is fine for $g$. But $(f \circ g)(x) = \sqrt{x - 3}$ has domain $[3,\infty)$ — $g$ must not leave $f$'s domain. **Check:** $x = 0$: $g(f(0)) = -3$ defined; $f(g(0)) = \sqrt{-3}$ undefined. The *same two functions* give different composite domains; the direction of composition is the whole question.
:::

## Inverse functions

$f : A \to B$ has an **inverse** $f^{-1} : B \to A$ iff $f$ is bijective; then $f^{-1}(f(x)) = x$ for $x \in A$ and $f(f^{-1}(y)) = y$ for $y \in B$. Recipe: write $y = f(x)$, solve for $x = g(y)$, swap letters: $f^{-1}(x) = g(x)$. The domain of $f^{-1}$ is the **range** of $f$ and vice versa.

:::derive title="(g o f) inverse rule"
$(g \circ f)^{-1} = f^{-1} \circ g^{-1}$ — the socks-and-shoes law: undo $g$ first, then $f$. Check: $(f^{-1} \circ g^{-1}) \circ (g \circ f) = f^{-1} \circ (g^{-1} \circ g) \circ f = f^{-1} \circ \operatorname{id} \circ f = \operatorname{id}$ ✓, and symmetrically on the other side (needed since $g \circ f$ bijective implies each of $f, g$ suitably bijective between the right sets).
:::

Graphically $y = f^{-1}(x)$ is the reflection of $y = f(x)$ in the line $y = x$ (points $(a,b) \mapsto (b,a)$). If $f$ is one-one but not onto, restrict the codomain to the range; if onto but not one-one, restrict the domain (e.g. $x^{2}$ on $[0,\infty)$ has inverse $\sqrt{x}$).

:::example
**Worked.** $f(x) = \frac{2x + 3}{x - 1}$, $x \ne 1$. Solve $y = \frac{2x+3}{x-1}$: $y(x - 1) = 2x + 3 \Rightarrow x(y - 2) = y + 3 \Rightarrow x = \frac{y + 3}{y - 2}$. So $f^{-1}(x) = \frac{x + 3}{x - 2}$, domain $x \ne 2$ = range of $f$. Vertical asymptote $x = 1$, horizontal asymptote $y = 2$ of $f$ become the horizontal $y = 1$ and vertical $x = 2$ of $f^{-1}$ — asymptotes swap roles under reflection in $y = x$, exactly like domain and range. **Check:** $f(f^{-1}(3)) = f(6) = \frac{15}{5} = 3$ ✓; $f^{-1}(f(2)) = f^{-1}(7) = \frac{10}{5} = 2$ ✓.
:::

:::warn
- $f^{-1}$ as an inverse **function** needs bijection; writing $f^{-1}$ before checking one-one + onto is the commonest Chapter-1 error.
- $(f \circ g)^{-1} \ne f^{-1} \circ g^{-1}$ (order flips!). The square bracket notation $f^{-1}(x) \ne \frac{1}{f(x)}$ — the $-1$ superscript means inverse function (or preimage set), never reciprocal, except the (rare) $\sin^{-1}$ convention confusion: $\sin^{-1}x$ is the inverse sine, while $(\sin x)^{-1} = \csc x$.
- $f \circ g = g \circ f$ happens only in special cases (e.g. $f = g$; or both powers $x^{a}, x^{b}$; or $f = g^{-1}$ giving identity) — never assume it.
:::

## Chapter recap — the whole sheet in one place

:::key
Sets: $|\mathcal{P}(A)| = 2^{n}$; equal $=$ double inclusion; $\varnothing, \{0\}, \{\varnothing\}$ distinct. Operations: De Morgan $(A \cup B)' = A' \cap B'$; $A \setminus B = A \cap B'$; $A \,\Delta\, B = (A \cup B) \setminus (A \cap B)$; $n(A \cup B) = n(A) + n(B) - n(A \cap B)$; three-set version with alternating signs. Products & relations: $n(A \times B) = n(A)n(B)$; relations on $n$-set $= 2^{n^{2}}$; reflexive $= 2^{n^{2}-n}$; symmetric $= 2^{n(n+1)/2}$; reflexive+symmetric $= 2^{n(n-1)/2}$; equivalence $=$ partitions $= B_n$. Functions: $|B|^{|A|}$ total; injections $P(|B|,|A|)$; bijections $n!$; domain rule stack; $\operatorname{dom}(g \circ f)$ careful; $f$ invertible iff bijective; $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$; even/odd need symmetric domain; periods scale as $1/|a|$.
:::

:::app
**How JEE asks this chapter.** (i) Domain/range of built formulas with roots, logs, floors — always test endpoints. (ii) Counting: number of relations/functions with axiom constraints. (iii) Equivalence classes: partition a concrete set, name classes. (iv) Function classification: one-one/onto/even/odd/periodic verdicts on a given formula. (v) Composite domains and inverse formulas with parameter conditions. Each is a two-line application of the boxes above — the marks go to boundary discipline, not to new algebra.
:::

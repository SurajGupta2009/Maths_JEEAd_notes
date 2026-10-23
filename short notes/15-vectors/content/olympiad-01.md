---
id: olympiad-01
part: olympiad
title: "Extension I — Vector Triple Products and Jacobi"
---

## The vector triple product returns to a plane

The **BAC–CAB** identity is
$$
\mathbf{a}\times(\mathbf{b}\times\mathbf{c})
=\mathbf{b}(\mathbf{a}\cdot\mathbf{c})-\mathbf{c}(\mathbf{a}\cdot\mathbf{b}).
$$
The result is a linear combination of $\mathbf{b},\mathbf{c}$, as it must be: a vector perpendicular to $\mathbf{b}\times\mathbf{c}$ lies in their span. The identity can be proved by linearity and checking basis vectors, or by expanding components once.

The other grouping gives
$$
(\mathbf{a}\times\mathbf{b})\times\mathbf{c}
=\mathbf{b}(\mathbf{a}\cdot\mathbf{c})-\mathbf{a}(\mathbf{b}\cdot\mathbf{c}).
$$
The two expressions are different in general. Cross products need parentheses.

:::example title="Two groupings, two different answers"
For $\mathbf{a}=(7,8,9)$, $\mathbf{b}=(1,2,3)$ and $\mathbf{c}=(4,5,6)$,
$$
\mathbf{a}\cdot\mathbf{c}=122,\qquad \mathbf{a}\cdot\mathbf{b}=50,\qquad \mathbf{b}\cdot\mathbf{c}=32.
$$
Hence
$$
\mathbf{a}\times(\mathbf{b}\times\mathbf{c})
=122\mathbf{b}-50\mathbf{c}=(-78,-6,66),
$$
whereas
$$
(\mathbf{a}\times\mathbf{b})\times\mathbf{c}
=122\mathbf{b}-32\mathbf{a}=(-102,-12,78).
$$
They are unequal, but each expansion agrees with direct cross-product computation.
:::

:::warn title="Not associative does not mean never equal"
The two groupings may coincide for special dependent or orthogonal vectors. “Not associative” means no universal equality is available. Prove a special case if you want to remove parentheses; never remove them by habit.
:::

## Jacobi's identity is three expansions cancelling

For every $\mathbf{a},\mathbf{b},\mathbf{c}$,
$$
\mathbf{a}\times(\mathbf{b}\times\mathbf{c})
+\mathbf{b}\times(\mathbf{c}\times\mathbf{a})
+\mathbf{c}\times(\mathbf{a}\times\mathbf{b})=\mathbf{0}.
$$

:::derive title="Cancellation by cyclic terms"
Apply BAC–CAB to each term:
$$
\mathbf{b}(\mathbf{a}\cdot\mathbf{c})-\mathbf{c}(\mathbf{a}\cdot\mathbf{b})
+\mathbf{c}(\mathbf{b}\cdot\mathbf{a})-\mathbf{a}(\mathbf{b}\cdot\mathbf{c})
+\mathbf{a}(\mathbf{c}\cdot\mathbf{b})-\mathbf{b}(\mathbf{c}\cdot\mathbf{a}).
$$
Commutativity of the dot product makes corresponding vector coefficients cancel in pairs. The numerical example above therefore gives a zero cyclic sum even though neither individual triple product is zero.
:::

## A scalar quadruple product generalizes Lagrange

Another useful identity is
$$
(\mathbf{a}\times\mathbf{b})\cdot(\mathbf{c}\times\mathbf{d})
=(\mathbf{a}\cdot\mathbf{c})(\mathbf{b}\cdot\mathbf{d})
-(\mathbf{a}\cdot\mathbf{d})(\mathbf{b}\cdot\mathbf{c}).
$$
Setting $\mathbf{c}=\mathbf{a}$ and $\mathbf{d}=\mathbf{b}$ recovers Lagrange's identity. This form is valuable when two planes or two oriented areas must be compared without computing every cross component separately.

:::diagram
{
  "type": "table",
  "title": "Keep the triple-product shapes distinct",
  "columns": ["Expression", "Type", "Main interpretation"],
  "rows": [
    ["a·(b×c)", "scalar", "signed volume / dependence"],
    ["a×(b×c)", "vector", "BAC–CAB in span(b,c)"],
    ["(a×b)·(c×d)", "scalar", "dot of two oriented normals"],
    ["cyclic Jacobi sum", "zero vector", "three expansions cancel"]
  ],
  "col_widths": [0.30, 0.18, 0.52],
  "caption": "First identify whether the answer is a scalar or a vector. That simple type check rejects many incorrect identities immediately."
}
:::

:::example title="A quick scalar-quadruple check"
Let $\mathbf{a}=\mathbf{i}$, $\mathbf{b}=\mathbf{j}$, $\mathbf{c}=\mathbf{i}+\mathbf{j}$ and $\mathbf{d}=\mathbf{j}+\mathbf{k}$. Then
$$
(\mathbf{a}\times\mathbf{b})\cdot(\mathbf{c}\times\mathbf{d})
=\mathbf{k}\cdot(\mathbf{i}-\mathbf{j}+\mathbf{k})=1.
$$
The right side is $(\mathbf{a}\cdot\mathbf{c})(\mathbf{b}\cdot\mathbf{d})-(\mathbf{a}\cdot\mathbf{d})(\mathbf{b}\cdot\mathbf{c})=1\cdot1-0\cdot1=1$.
:::

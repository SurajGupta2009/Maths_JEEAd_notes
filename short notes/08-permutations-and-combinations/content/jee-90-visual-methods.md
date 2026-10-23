---
id: jee-90
part: jee
title: "Visual Counting Lab — Decisions, Paths, Distributions and Overlap"
---

## Multiply along a path, add across disjoint paths

The product rule counts a sequence of independent decisions; the sum rule counts disjoint cases. A tree makes the distinction visible: each root-to-leaf path is one outcome, while the leaves are partitioned by their first decision.

:::diagram
{
  "type": "tree",
  "title": "A two-stage decision tree has 2 x 3 = 6 leaves",
  "ratio": 0.66, "node_width": 1.7,
  "nodes": [
    {"id": "start", "at": [0, 3], "label": "start"},
    {"id": "a", "at": [-2, 1.7], "label": "option A"}, {"id": "b", "at": [2, 1.7], "label": "option B"},
    {"id": "a1", "at": [-3.2, 0], "label": "A1"}, {"id": "a2", "at": [-2, 0], "label": "A2"}, {"id": "a3", "at": [-0.8, 0], "label": "A3"},
    {"id": "b1", "at": [0.8, 0], "label": "B1"}, {"id": "b2", "at": [2, 0], "label": "B2"}, {"id": "b3", "at": [3.2, 0], "label": "B3"}
  ],
  "edges": [
    {"from": "start", "to": "a", "label": "A"}, {"from": "start", "to": "b", "label": "B"},
    {"from": "a", "to": "a1"}, {"from": "a", "to": "a2"}, {"from": "a", "to": "a3"},
    {"from": "b", "to": "b1"}, {"from": "b", "to": "b2"}, {"from": "b", "to": "b3"}
  ],
  "caption": "The first stage has two alternatives and the second has three for each alternative. There are six root-to-leaf paths, not 2 + 3 = 5."
}
:::

If the second-stage number of choices changes with the first decision, do not multiply a single pair of numbers. Count each branch separately and then add the branch totals.

<!-- pagebreak -->
## Lattice paths encode a word with identical letters

A shortest path from $(0,0)$ to $(4,3)$ using only right and up steps contains four R's and three U's. Every arrangement of the seven-letter word RRRRUUU gives exactly one path, so the count is $\binom{7}{3}=35$.

:::diagram
{
  "type": "geometry",
  "title": "One shortest path represented by R R U R U R U",
  "xrange": [-0.5, 4.5], "yrange": [-0.5, 3.5], "grid": true,
  "elements": [
    {"kind": "segment", "a": [0, 0], "b": [1, 0]}, {"kind": "segment", "a": [1, 0], "b": [2, 0]},
    {"kind": "segment", "a": [2, 0], "b": [2, 1]}, {"kind": "segment", "a": [2, 1], "b": [3, 1]},
    {"kind": "segment", "a": [3, 1], "b": [3, 2]}, {"kind": "segment", "a": [3, 2], "b": [4, 2]},
    {"kind": "segment", "a": [4, 2], "b": [4, 3]},
    {"kind": "point", "at": [0, 0], "label": "start", "dy": -0.4},
    {"kind": "point", "at": [4, 3], "label": "end (4, 3)", "dx": -1.2, "dy": 0.2}
  ],
  "caption": "Exactly seven unit steps occur. Choosing which three of the seven positions are U determines all four R positions, giving C(7,3) = C(7,4) = 35."
}
:::

If diagonal or left/down steps are allowed, this binomial count no longer applies. The step restrictions are part of the model, not a minor detail.

<!-- pagebreak -->
## Stars and bars count nonnegative distributions

The number of nonnegative integer solutions of $x_1+x_2+x_3=9$ is $\binom{9+3-1}{3-1}=\binom{11}{2}=55$. Arrange nine stars and two bars; the bars split the stars into three groups.

:::diagram
{
  "type": "geometry",
  "title": "The arrangement ** | *** | **** represents (2, 3, 4)",
  "xrange": [-0.5, 11], "yrange": [-1, 2], "axes": false, "equal": false,
  "elements": [
    {"kind": "point", "at": [0, 0], "label": "star", "dy": 0.3}, {"kind": "point", "at": [1, 0], "label": "star", "dy": 0.3},
    {"kind": "segment", "a": [2, -0.6], "b": [2, 0.8], "label": "bar 1", "label_pos": 0.8, "dx": 0.15, "color": "#B91C1C"},
    {"kind": "point", "at": [3, 0], "label": "star", "dy": 0.3}, {"kind": "point", "at": [4, 0], "label": "star", "dy": 0.3}, {"kind": "point", "at": [5, 0], "label": "star", "dy": 0.3},
    {"kind": "segment", "a": [6, -0.6], "b": [6, 0.8], "label": "bar 2", "label_pos": 0.8, "dx": 0.15, "color": "#B91C1C"},
    {"kind": "point", "at": [7, 0], "label": "star", "dy": 0.3}, {"kind": "point", "at": [8, 0], "label": "star", "dy": 0.3}, {"kind": "point", "at": [9, 0], "label": "star", "dy": 0.3}, {"kind": "point", "at": [10, 0], "label": "star", "dy": 0.3}
  ],
  "caption": "Nine stars and two dividers occupy eleven positions. Choosing the two bar positions determines the nonnegative group sizes. Empty groups are allowed."
}
:::

For positive solutions, set $y_i=x_i-1$ first. The transformed equation has a smaller right-hand side; forgetting that shift is the most common stars-and-bars error.

<!-- pagebreak -->
## Inclusion–exclusion repairs double counting

For two sets, $|A\cup B|=|A|+|B|-|A\cap B|$. The intersection was counted once in $|A|$ and again in $|B|$, so subtract it once. For three sets, pairwise intersections are subtracted and the triple intersection is added back.

:::diagram
{
  "type": "venn3",
  "title": "Three-set overlap regions must be counted with the correct multiplicity",
  "labels": {"Aonly": "A only", "Bonly": "B only", "Conly": "C only", "ABn": "AB", "ACn": "AC", "BCn": "BC", "ABC": "ABC"},
  "caption": "The centre ABC occurs in all three set counts, all three pairwise counts and the triple count. Its net coefficient is 3 - 3 + 1 = 1."
}
:::

:::example title="None of the bad events"
If $A_i$ is the event that condition $i$ fails, then “no failure” has count $N-|A_1\cup\cdots\cup A_m|$. Inclusion–exclusion is often used on the bad events and then subtracted from the total, rather than applied directly to the desired region.
:::

<!-- pagebreak -->
## A counting workflow

:::diagram
{
  "type": "flow",
  "title": "Choose the model before choosing a formula",
  "steps": [
    {"title": "Define one outcome precisely", "detail": "Decide whether order matters, whether objects are identical, and whether repetition is allowed."},
    {"title": "Draw the decision or region structure", "detail": "Use a tree for sequential choices, a path for step words, stars and bars for distributions, or regions for overlap."},
    {"title": "Count without hidden duplication", "detail": "Multiply along a path, add disjoint cases, divide only for proven symmetry, and use inclusion-exclusion for overlap."},
    {"title": "Test a small case", "detail": "Enumerate a reduced instance and compare it with the formula before generalising."}
  ],
  "caption": "Most counting errors are model errors: a correct permutation or combination formula applied to the wrong definition of an outcome."
}
:::

:::key title="Complement is a counting method"
When “at least one” or “none” creates many cases, count the complementary event. For example, at least one success in $n$ independent trials has probability $1-(1-p)^n$; the same complement idea works in ordinary enumeration.
:::

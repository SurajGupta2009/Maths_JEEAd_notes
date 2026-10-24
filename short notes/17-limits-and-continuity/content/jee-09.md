---
id: jee-09
part: jee
title: "Mixed Limit and Continuity Strategy"
---

## Split at every definition change

Absolute values, greatest-integer functions, fractional parts and piecewise formulas require one-sided analysis at their breakpoints. For example,
$$
\lim_{x\to0^-}\frac{|x|}{x}=-1,
\qquad
\lim_{x\to0^+}\frac{|x|}{x}=1,
$$
so the two-sided limit does not exist. The fractional part $\{x\}=x-\lfloor x\rfloor$ has left limit $1$ and right limit $0$ at every integer.

:::example title="Two standard limits and a value determine two parameters"
Suppose a function is defined by
$$
\frac{\sin(ax)}{x}\quad(x<0),\qquad b\quad(x=0),\qquad \frac{e^{2x}-1}{x}\quad(x>0).
$$
Its left limit is $a$, its right limit is $2$, and its value is $b$. Continuity at $0$ requires all three to agree, hence
$$
a=2,\qquad b=2.
$$
Checking only $a=2$ would make the two-sided limit exist but would not ensure continuity unless $b=2$ as well.
:::

## Choose the smallest sufficient method

:::diagram
{
  "type": "table",
  "title": "Match the expression to a reliable limit tool",
  "columns": ["Observation", "Method", "Essential check"],
  "rows": [
    ["Finite substitution", "Direct limit laws", "denominator limit nonzero"],
    ["Polynomial or radical 0/0", "Factor or conjugate", "cancel only off the target"],
    ["Bounded oscillation", "Squeeze", "both bounds share a limit"],
    ["sin, exp or log standard", "Match small argument", "same argument and coefficient"],
    ["0/0 or infinity/infinity", "L'Hopital", "hypotheses after every step"],
    ["1^infinity or other power", "Take logarithms", "positive base; exponentiate last"],
    ["Piecewise continuity", "Match left, right and value", "all three quantities agree"],
    ["Root or intermediate value", "Build an auxiliary function", "continuity on the whole interval"]
  ],
  "col_widths": [0.30, 0.31, 0.39],
  "caption": "The form suggests a method, but the hypotheses decide whether that method is valid."
}
:::

:::diagram
{
  "type": "flow",
  "title": "A repeatable limit-and-continuity workflow",
  "steps": [
    {"title": "Read the approach and domain", "detail": "Record approach, domain and definition changes."},
    {"title": "Classify before transforming", "detail": "Choose direct arithmetic, a limit form or a theorem."},
    {"title": "Keep an exact chain", "detail": "Transform exactly and check every hypothesis."},
    {"title": "Answer the actual question", "detail": "Verify the requested limit, value or existence claim."}
  ],
  "caption": "Most errors come from answering a different question from the one asked, not from the final arithmetic."
}
:::

:::key title="Final limit-and-continuity self-check"
Did I preserve excluded points and one-sided restrictions? Did every cancellation occur only off the target? Did I normalize the correct small argument or highest power? Did every L'Hôpital step remain a permitted form? For continuity, do left limit, right limit and value all agree? For IVT, is the function continuous on the entire closed interval, and am I claiming existence rather than unsupported uniqueness?
:::

---
title: "Formatting Guide — Obsidian Vault"
aliases: ["Formatting Guide", "Conventions"]
module: "docs"
type: guide
tags: [formatting, conventions]
created: 2026-09-27
---

# Formatting Guide — the Obsidian vault

The notes are **authored directly in Markdown** inside an Obsidian vault. This
document is the formatting reference: frontmatter, callouts, math, links,
collapsible answers, diagrams, and the quality gates.

## Frontmatter (every note)

```yaml
---
title: "Chapter 2 — Permutations"
aliases: ["Permutations", "Ch 2 — Permutations"]
module: "PnC"
module_title: "PnC"
chapter: 2
level: machinery
tags: [pnc, chapter, machinery]
created: 2026-09-27
---
```

- `level` ∈ `foundations | machinery | core | applications | frontier | synthesis`.
- Module notes (`<Module>.md`) use `type: index`; the reference/paper/solutions
  notes use `type: reference | paper | solutions`.

## Math

- **Inline**: `$…$`. **Display**: `$$…$$`. Rendered by Obsidian's built-in
  MathJax (same LaTeX as GitHub).
- Real math only — never fake prose math with Unicode glyphs (`x²`, `√`, `≤`).
- Example:
  ```md
  The binomial coefficient is $\binom{n}{k} = \frac{n!}{k!(n-k)!}$

  $$\sum_{k=0}^n \binom{n}{k} = 2^n$$
  ```

## Callouts (fixed Obsidian types)

Body lines of a callout are `>`-prefixed lines under the `> [!type] Title` line.

```md
> [!abstract] First Principles — why the product rule is true
> Count choice-sequences $(c_1,\dots,c_k)$. Fix $c_1$: the rest is
> $n_2\cdots n_k$ ways; $n_1$ disjoint families → $n_1(n_2\cdots n_k)$.

> [!tip] Key Idea — the rule of roles
> Labeled roles make different paths automatically different outcomes.

> [!warning] Common Trap — "3 choices, then 3 choices" is not always 9
> Fails when different paths land on the same object (overcounting).

> [!example] Olympiad Extension — counting twice is a proof technique
> …

> [!info] Formula box
> $\binom{n+k-1}{k-1}$ — stars and bars.

> [!quote] Vandermonde's identity
> $\sum_k \binom{r}{k}\binom{s}{n-k} = \binom{r+s}{n}$.
```

Type map: First Principles → `[!abstract]`, Key Idea → `[!tip]`, Common Trap →
`[!warning]`, Olympiad Extension → `[!example]`, formula box → `[!info]`, named
result/identity → `[!quote]`, checklist → `[!success]`, bridge → `[!info]`.
The CSS snippet `.obsidian/snippets/maths-vault.css` tints these.

## Links & navigation

- Internal links are `[[Wikilinks]]`. Every chapter note carries a navigation
  callout at the top:
  ```md
  > [!info] Navigation
  > 📖 [[PnC|PnC]] · ⬅ [[01-counting-basics|Chapter 1]] · [[03-combinations|Chapter 3]] ➡ · 📝 [[PnC — Paper|Olympiad Paper]] · ✅ [[PnC — Solutions|Solutions]]
  ```
- Note names are globally unique, so bare `[[note-name]]` resolves.

## Collapsible answers

```md
<details>
<summary>Answer + Reasoning</summary>

Solution & reasoning…

**Answer: 112** ✓

</details>
```

Keep `<details>`/`<summary>` pairs balanced (the gate checks this).

## Diagrams

- **SVG** in the module's `assets/`, referenced as
  `![caption](assets/fig-XX.svg)` (renders inline on GitHub and in Obsidian).
- **Mermaid** flowcharts for key ideas (native in both):
  ````md
  ```mermaid
  flowchart TD
    A[Product rule] --> B[leaves = n1·n2·…·nk]
  ```
  ````

## Tables

GitHub Flavored Markdown tables.

## File organization

```
notes/<Module>/
├── <Module>.md            # complete notes: course map + 6 chapters + theory appendix
├── <Module> — Paper.md    # Olympiad paper (A–G / A–H / A–I)
├── <Module> — Solutions.md
└── assets/fig-XX.svg
```

## Dataview dashboards

`[[Home]]` lists the modules (there is one complete note per module):

```dataview
LIST
FROM "notes"
WHERE type = "notes"
SORT file.name ASC
```

Requires the **Dataview** community plugin.

## Quality gates

```bash
python3 tools/verify-md.py          # frontmatter, math balance, blocks, image links
python3 tools/verify-structure.py   # 3 notes/module, 6 chapters + appendix, paper<->solutions
```

---

*This is the vault formatting standard. See [CONTRIBUTING.md](../CONTRIBUTING.md) for the full authoring rules and [DIAGRAMS.md](DIAGRAMS.md) for the diagram catalog.*

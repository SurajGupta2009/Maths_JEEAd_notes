---
title: "Home — JEE Advanced + Olympiad Maths"
aliases:
  - "Vault Home"
  - "Start Here"
type: home
tags:
  - home
  - index
created: 2026-09-27
---

# 🧮 JEE Advanced + Olympiad Maths — Obsidian Vault

Hand-crafted, first-principles maths notes that climb one ladder:
**board basics → JEE Main → JEE Advanced → Olympiad frontier.** Every formula
is *derived*, never memorised; every paper answer is *numerically verified*.

> [!tip] How to use this vault
> - **One note per chapter.** Each `NN-slug.md` is a complete chapter; the six
>   chapters of a module are numbered `01`…`06` (foundations → machinery → core
>   → applications → frontier → synthesis).
> - **Navigate with Wikilinks** — every note has a `Navigation` callout at the
>   top (module home · prev · next · paper · solutions). Use the **Graph view**
>   (left ribbon) to see the whole course.
> - **Callouts** carry the pedagogy: ⛁/abstract = First Principles, tip = Key
>   Idea, warning = Common Trap, example = Olympiad Extension, note/info/quote
>   = formulas & named results.
> - **Math is real LaTeX** — `$…$` inline, `$$…$$` display (renders via
>   Obsidian's built-in MathJax).
> - **Dataview** powers the dashboards below (install the *Dataview* community
>   plugin if the tables are empty — see [[README]]).

## 📚 Modules

| Module | Folder | Chapters | Start |
|---|---|---|---|
| **PnC** — Permutations & Combinations | `notes/PnC` | 6 | [[PnC]] |
| **Complex Numbers** | `notes/Complex-Numbers` | 6 | [[Complex-Numbers]] |
| **Binomial Theorem** | `notes/Binomial-Theorem` | 6 | [[Binomial-Theorem]] |
| **Conic Sections** | `notes/Conic-Sections` | 6 | [[Conic-Sections]] |
| **Limits & Continuity** | `notes/Limits-and-Continuity` | 6 | [[Limits-and-Continuity]] |
| **Differentiation & Methods** | `notes/Differentiation-and-Methods` | 6 | [[Differentiation-and-Methods]] |
| **Applications of Derivatives** | `notes/Applications-of-Derivatives` | 6 | [[Applications-of-Derivatives]] |

Jump to any module's [[PnC — Paper|Olympiad papers]] and
[[PnC — Solutions|solution keys]].

## 📖 Modules in this vault (Dataview)

```dataview
TABLE module AS "Module"
FROM "notes"
WHERE type = "notes"
SORT file.name ASC
```

Each module is one complete-notes note (six chapters + theory appendix), plus its
[[PnC — Paper|Olympiad paper]] and [[PnC — Solutions|solutions]].

## 🎯 What's next

See [[ROADMAP]] for the full module list and how many chapters remain to reach
Olympiad coverage. To add a new module, follow [[CONTRIBUTING]] and the
skeletons in `templates/markdown/`.

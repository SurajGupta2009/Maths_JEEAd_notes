---
title: "{{MODULE TITLE}} — Course Notes"
aliases: ["{{MODULE TITLE}}", "{{MODULE}}"]
module: "{{MODULE}}"
type: index
tags: [{{module-slug}}, module, index]
created: {{date:YYYY-MM-DD}}
---

> [!info] Navigation
> 📖 [[Home|Vault home]] · 🧪 [[{{MODULE}} — Paper|Olympiad Paper]] · ✅ [[{{MODULE}} — Solutions|Solutions]] · 📘 [[{{MODULE}} — Theory|Theory Reference]]

# {{MODULE TITLE}}

> **JEE Advanced → Olympiad ladder**

<One to two sentences: what this module is and what it builds, from first
principles to the Olympiad frontier.>

`6 chapters` `~{{N}} worked & practice questions` `SVG diagrams` `{{Q}}-question Olympiad paper + full solutions`

### ★ How to use these notes

**Read in order — do not skip the "why" boxes.** Each chapter is built in
layers: *concept → first-principles reasoning → JEE theory → Olympiad
extension*.

- **Callouts** — `[!abstract]` First Principles = the actual reasoning;
  `[!tip]` Key Idea = the takeaway technique; `[!warning]` Common Trap = the
  classic mistake; `[!example]` Olympiad Extension = the frontier version.
- **Questions are placed in context** — a solved example right after the
  technique that solves it, plus practice sets with difficulty tags:
  `[JEE Main] [JEE Adv] [Olympiad]`.
- **The Olympiad paper** ({{Q}} questions) is the exam: attempt it after
  Chapter 6, without solutions. The [[{{MODULE}} — Solutions|solution key]] is
  separate and complete.
- **Small-case habit** — whenever you get an answer, *list all cases for a tiny
  instance* and check.

### ▣ The roadmap

| Ch | Title | Note |
|---|---|---|
| 1 | {{Chapter 1 title}} | [[01-{{slug}}]] |
| 2 | {{Chapter 2 title}} | [[02-{{slug}}]] |
| 3 | {{Chapter 3 title}} | [[03-{{slug}}]] |
| 4 | {{Chapter 4 title}} | [[04-{{slug}}]] |
| 5 | {{Chapter 5 title}} | [[05-{{slug}}]] |
| 6 | {{Chapter 6 title}} | [[06-{{slug}}]] |

> The theory is **well-ordered**: board-level basics → JEE Main → JEE Advanced
> → Olympiad. Dependencies are respected — nothing is used before it is
> established.

## Chapters

```dataview
TABLE chapter AS "Ch", level AS "Level"
FROM "notes/{{MODULE}}"
WHERE chapter
SORT chapter ASC
```

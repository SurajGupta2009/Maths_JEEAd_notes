---
title: "New-Module Checklist"
aliases: ["Checklist", "New Module"]
module: "templates"
type: checklist
tags: [templates, checklist, process]
created: 2026-09-27
---

# New-Module Checklist (Obsidian vault)

The exact ordered procedure for adding a module. Notes are authored **directly in
Markdown** inside the vault — one note per chapter under `notes/<Module-Slug>/`.
Content conventions live in [`CONTRIBUTING.md`](../CONTRIBUTING.md); this file
only fixes the order. Skeletons are in [`markdown/`](markdown/) and configured as
the Templater folder (`.obsidian/plugins/templates/data.json`).

1. **Create the module folder.** Kebab-case slug under `notes/`:
   `notes/Quadratic-Equations/`, plus an empty `assets/` directory.
   ```bash
   mkdir -p notes/Quadratic-Equations/assets
   ```

2. **Write the module index** `notes/Quadratic-Equations/Quadratic-Equations.md`
   from `templates/markdown/module-index.md`: frontmatter, pitch, how-to-use,
   callout legend, roadmap table linking the six chapter notes, Dataview block.

3. **Create one note per chapter**, named after the chapter
   (`01-counting-basics.md`, `02-permutations.md`, …), and write each chapter's
   full content in it from `templates/markdown/chapter.md` — frontmatter, a
   `Navigation` callout, sections, First-Principles boxes, worked examples
   (`S#`) and practice (`P#`) woven **between** theory sections.

4. **Number practice questions P1…Pn continuously across the whole module**
   (unique across all six chapter notes; worked examples S1…Sn likewise). Check:
   ```bash
   grep -rhoE '#### \*\*[PS][0-9]+\*\*' notes/Quadratic-Equations/ | sort -V | uniq -d
   ```
   → empty.

5. **Write the paper** `notes/Quadratic-Equations/Quadratic-Equations — Paper.md`
   from `templates/markdown/paper.md`: 30+ questions (aim 38–40), lettered
   sections A–H, difficulty ramping Main → Advanced → Olympiad, every question
   with a short `**Answer:**` line. **Before writing solutions, verify every
   answer numerically with a pure-Python script** (stdlib only — no numpy, no
   sympy). Do not proceed with a wrong answer. Keep the throwaway script out of
   the repo; paste its verdict into the PR description.

6. **Write full solutions** `Quadratic-Equations — Solutions.md` from
   `templates/markdown/solutions.md`: same Q-ids verbatim, every solution =
   method name first → full derivation → check; give **both** standard methods
   wherever two exist.

7. **Write the one-page reference** `Quadratic-Equations — Theory.md` from
   `templates/markdown/theory.md`: definition → statement → proof idea →
   small-case habit for every topic, plus the formula sheet.

8. **Add diagrams**: inline SVG files in `assets/fig-XX.svg`, referenced as
   `![caption](assets/fig-XX.svg)`; add Mermaid flowcharts for key ideas where
   they help.

9. **Run the gates** and fix anything that fails:
   ```bash
   python3 tools/verify-md.py          # frontmatter, math, blocks, image links
   python3 tools/verify-structure.py   # 6 chapters/module, unique names, P/S numbering
   ```

10. **Update the indexes and open a PR** (do not push to `main`): add the module
    to [[Home]], [README.md](../README.md) and
    [docs/ROADMAP.md](../docs/ROADMAP.md) (flip its status to ✅), then open one
    branch/PR for the module. Paste the verifier outputs and the pure-Python
    answer-verification verdict into the PR description.

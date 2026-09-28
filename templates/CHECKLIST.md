---
title: "New-Module Checklist"
aliases: ["Checklist", "New Module"]
module: "templates"
type: checklist
tags: [templates, checklist, process]
created: 2026-09-27
---

# New-Module Checklist (Obsidian vault)

The exact ordered procedure for adding a module. Each module is **three notes**:
one **complete-notes** file (course map + all six chapters + theory appendix),
plus the **paper** and the **solutions**. Content conventions live in
[`CONTRIBUTING.md`](../CONTRIBUTING.md); skeletons are in [`markdown/`](markdown/)
and configured as the Templater folder (`.obsidian/plugins/templates/data.json`).

1. **Create the module folder.** Kebab-case slug under `notes/` + an empty
   `assets/` directory.
   ```bash
   mkdir -p notes/Quadratic-Equations/assets
   ```

2. **Write the complete notes** `notes/Quadratic-Equations/Quadratic-Equations.md`
   from `templates/markdown/complete.md`: frontmatter, a `Navigation` callout,
   the course map, then the six chapters inline
   (**foundations → machinery → core → applications → frontier → synthesis**),
   and the theory appendix. All of a chapter's content lives in this one file.

3. **Number questions continuously per module.** Practice `P1…Pn` and worked
   examples `S1…Sn` are unique across the whole file, woven **between** theory
   sections. Check for duplicates:
   ```bash
   grep -rhoE '#### \*\*[PS][0-9]+\*\*' notes/Quadratic-Equations/Quadratic-Equations.md | sort -V | uniq -d
   ```
   → empty.

4. **Write the paper** `Quadratic-Equations — Paper.md` from
   `templates/markdown/paper.md`: 34+ questions (aim 38–50), lettered sections
   A–G / A–H / A–I, difficulty ramping Main → Advanced → Olympiad, every question
   with a
   short `**Answer:**` line. **Before writing solutions, verify every answer
   numerically with a pure-Python script** (stdlib only — no numpy, no sympy).
   Do not proceed with a wrong answer. Keep the throwaway script out of the repo;
   paste its verdict into the PR description.

5. **Write full solutions** `Quadratic-Equations — Solutions.md` from
   `templates/markdown/solutions.md`: same Q-ids verbatim, every solution =
   method name first → full derivation → check; give **both** standard methods
   wherever two exist.

6. **Add diagrams**: inline SVG in `assets/fig-XX.svg`, referenced as
   `![caption](assets/fig-XX.svg)`; Mermaid flowcharts for key ideas where they
   help.

7. **Run the gates** and fix anything that fails:
   ```bash
   python3 tools/verify-md.py          # frontmatter, math, blocks, image links
   python3 tools/verify-structure.py   # 3 notes/module, 6 chapters + appendix, paper↔solutions
   ```

8. **Update the indexes and open a PR** (do not push to `main`): add the module
   to [[Home]], [README.md](../README.md) and
   [docs/ROADMAP.md](../docs/ROADMAP.md) (flip its status to ✅), then open one
   branch/PR. Paste the verifier outputs and the pure-Python answer-verification
   verdict into the PR description.

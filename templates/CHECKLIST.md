# New-Module Checklist (Markdown-first)

The exact ordered procedure for adding a module. **Notes are authored
directly in Markdown** — one folder per chapter under `notes/<Module-Slug>/`.
The standalone HTML mindmaps in `published/` are a legacy distribution
artifact: the four existing modules keep them, and a new module may get one
later if ever needed, but HTML authoring is no longer part of the workflow.

Rules and content conventions live in
[`CONTRIBUTING.md`](../CONTRIBUTING.md) (the notes standard) — this file only
fixes the order. Skeletons are in [`markdown/`](markdown/).

1. **Create the module folder.**
   Kebab-case slug under `notes/`: `notes/Quadratic-Equations/`, plus an
   empty `assets/` directory (diagrams land there as `fig-XX.svg`).
   ```bash
   mkdir -p notes/Quadratic-Equations/assets
   ```

2. **Write the module index** `notes/Quadratic-Equations/README.md` from
   `templates/markdown/module-index.md`: pitch, how-to-use, box legend,
   roadmap table linking the six chapter folders.

3. **Create one folder per chapter**, named after the chapter
   (`01-counting-basics/`, `02-permutations/`, …), and write each chapter's
   full content in **`<folder>/README.md`** from
   `templates/markdown/chapter.md` — sections, first-principles boxes,
   worked examples (`S#`), practice questions (`P#`) woven **between**
   theory sections. All of a chapter's content lives in its folder.

4. **Number practice questions P1…Pn continuously across the whole module**
   (unique across all six chapter folders; worked examples S1…Sn likewise).
   Check:
   ```bash
   grep -rhoE '#### \*\*[PS][0-9]+\*\*' notes/Quadratic-Equations/ | sort -V | uniq -d
   ```
   → empty.

5. **Write the paper** `notes/Quadratic-Equations/olympiad-paper.md` from
   `templates/markdown/olympiad-paper.md`: 30+ questions (aim 38–40),
   lettered sections A–H, difficulty ramping Main → Advanced → Olympiad,
   every question with a short `**Answer:**` line.
   **Before writing the solutions file, verify every answer numerically with
   a pure-Python script** (stdlib only — no numpy, no sympy). Do not proceed
   with a wrong answer. Keep the throwaway script out of the repo; paste its
   verdict into the PR description.

6. **Write full solutions** `olympiad-paper-solutions.md` from
   `templates/markdown/olympiad-paper-solutions.md`: same Q-ids verbatim,
   every solution = method name first → full derivation → check; give **both
   standard methods** wherever two exist.

7. **Write the one-page reference** `00-WELL-ORDERED-THEORY.md` from
   `templates/markdown/00-WELL-ORDERED-THEORY.md`: definition → statement →
   proof idea → small-case habit for every topic, plus the formula sheet.

8. **Add diagrams**: inline SVG files in `assets/fig-XX.svg`, referenced as
   `![caption](assets/fig-XX.svg)` from module-level files and
   `![caption](../assets/fig-XX.svg)` from chapter folders; add Mermaid
   flowcharts for the key ideas where they help.

9. **Build the single-file snapshot and run the gates:**
   ```bash
   python3 tools/build-complete.py Quadratic-Equations   # writes <slug>-complete.md
   python3 tools/verify-md.py                            # every *.md must PASS
   python3 tools/verify-math.py && python3 tools/verify-mindmap.py all   # published/ unchanged
   git diff -- notes/Quadratic-Equations/*-complete.md   # snapshot must be stable
   ```

10. **Update `README.md` and open a PR** (do not push to `main`): add the
    module row (chapter count, P/Q counts, links) to the root modules table
    and to `notes/README.md`, then open one branch/PR for the module. Paste
    the verifier outputs and the pure-Python answer-verification verdict into
    the PR description.

# New-Module Checklist

The exact ordered procedure for adding a module. Work top to bottom; each step
has a command or an acceptance test. Rules and markup patterns live in
[`AGENTS.md`](../AGENTS.md) / [`CONTRIBUTING.md`](../CONTRIBUTING.md) — this file
only fixes the order. `templates/` holds every skeleton you need.

1. **Create the folder + stylesheet.**
   New modules are kebab-case-ish capitalized slugs: `Quadratic-Equations/`
   (the existing `Complex Numbers/` folder with its space stays as-is — don't "fix" it).
   ```bash
   mkdir Quadratic-Equations
   mkdir Quadratic-Equations/assets
   cp PnC/assets/notes.css Quadratic-Equations/assets/notes.css
   ```

2. **Build `index.html` from `templates/module-index.html`.**
   Fill the banner, chips, roadmap SVG, chapter cards. The mind map card can link
   `quadratic-equations-mindmap.html` now — the file appears in step 7.

3. **Write the chapters `01-…` … `06-…` from `templates/chapter.html`.**
   One single large HTML file per chapter — never bifurcate a chapter into
   multiple HTMLs. Each chapter: intro card, theory cards with `div.box`
   callouts, worked examples (`S#`), practice questions woven **between**
   theory sections.

4. **Number practice questions P1…Pn continuously across the whole module**
   (unique across all six chapter files; worked examples S1…Sn likewise).
   Check: `grep -h 'class="q-id">P' Quadratic-Equations/0*.html | sort | uniq -d` → empty.

5. **Write the paper** `olympiad-paper.html` from `templates/olympiad-paper.html`:
   30+ questions (aim 38–40), lettered sections A–H, difficulty ramping
   Main → Advanced → Olympiad, every question with a short `p.answer-pill`.
   **Before writing the solutions file, verify every answer numerically with a
   pure-Python script** (stdlib only — no numpy, no sympy). Do not proceed with
   a wrong answer pill.

6. **Write full solutions** `olympiad-paper-solutions.html` from
   `templates/olympiad-paper-solutions.html`: same structure as the paper;
   every solution = method name first, full derivation, check; give **both
   standard methods** wherever two exist.

7. **Generate the mind map** (never hand-write it):
   ```bash
   python3 tools/build-mindmap.py Quadratic-Equations
   ```
   Output name is `<folder-slug>-mindmap.html` (e.g.
   `quadratic-equations-mindmap.html`); re-running after any content change
   keeps it in sync. Pin fancier labels via `tools/mindmap-overrides.json` if wanted.

8. **Run the verifiers on every file of the module:**
   ```bash
   python3 tools/verify-math.py Quadratic-Equations/*.html      # every line must end PASS
   python3 tools/verify-mindmap.py Quadratic-Equations          # must end PASS
   ```
   (CI runs both repo-wide, plus a mind-map freshness check.)

9. **Update `README.md`:** add the module row to the modules table — chapters /
   practice Qs / paper Qs counts and links.

10. **Open a PR** (do not push to `main`): one module = one branch
    `add-<module>` → PR. Paste the two verifier outputs into the PR description.
